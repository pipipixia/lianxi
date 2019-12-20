from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
import redis
black_ips = ['192.168.1.2']

r=redis.Redis(host='127.0.0.1',port=6379, db=14)

# 中间件的配置顺序特别重要 请求按照中间件的配置顺序执行，响应按照中间件的倒序执行

class Firstmiddleware(MiddlewareMixin):

    def process_request(self, request):  # 接受到请求，但未解析到视图函数
        ip = request.META.get('REMOTE_ADDR')  # 获取档期那发送请求的ip地址
        print('Firstmiddleware process_request...发送当前请求的客户端ip是:' + ip)
        if ip in black_ips:
            return HttpResponse("<h3 style='color:red'>回去把，你已被假如黑名单</h3>")

    def process_response(self, request, response):
        print('Firstmiddleware process_response... 返回响应给：' + request.META.get('REMOTE_ADDR'))
        return response


class Secondmiddleware(MiddlewareMixin):

    def process_request(self, request):
        print('Seconmiddleware process_request()...')

    def process_response(self, request, response):
        print('Seconmiddleware process_response...')
        return response


class LimitMiddleware(MiddlewareMixin):

    def process_request(self, request):
        ip = request.META.get('REMOTE_ADDR')
        key = 'limit:'+ip  # 发送请求的客户端IP作为redis的key
        is_ok = r.set(key, 1, ex=60, nx=True)  # 设置当前key的过期时间为60，当只要key不存在（未过期）时才能设置成功
        if is_ok or r.incr(key) <= 5:  # 如果是第一次设置（key-1）对应的value设置为1，或1分钟之间访问的次数小于五次则通过
            request.visit_count = r.get(key).decode('utf-8')  # 将当前IP的访问次数获取，并设置到请求对象中。
        else:
            return HttpResponse("<h3 style='color:red'>您访过太过频繁</h3>")

