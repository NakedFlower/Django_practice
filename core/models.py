from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    capacity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# "__str__" 메서드는 관리자 페이지 등에서 객체 이름이 예쁘게 보이도록 도와줌
# "auto now add=True"는 생성 시간을 자동으로 저장해줌
