from .models import Shortener, Access, Shortener_Access


class ShortenerQuery:

    def __init__(self):
        self.shortener = Shortener

    def all(self):
        return self.shortener.objects.all()

    def byId(self, id=1):
        return self.shortener.objects.filter(id=id).first()

    def byShort(self, short='a'):
        return self.shortener.objects.filter(short_url=short).first()

    def getAcessos(self, short='a'):
        id = self.byShort(short).id
        return AccessQuery().access.objects.filter(shortener_access__fk_shortener_id=id)


class AccessQuery:

    def __init__(self):
        self.access = Access

    def all(self):
        return self.access.objects.all()

    def byId(self, id=1):
        return self.access.objects.filter(id=id)

    def byIP(self, ip='127.0.0.1'):
        return self.access.objects.filter(ip=ip)
