# 4- https://www.hackerrank.com/challenges/finding-the-percentage/problem

n = int(input())            # 
student_marks = {}
for _ in range(n):
    name, *line = input().split()   # girdi: "Ali 70 80 90"     ->  ["Ali", "70", "80", "90"]   ->  name = "Ali"  line = ["70", "80", "90"]
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
scores = student_marks[query_name]
average = sum(scores) / len(scores)
print(f"{average:.2f}")  # 2 ondalık basamak göstermek için


#Girdi Alır:

#İlk olarak kaç öğrenci olduğunu (n) alır.
#Ardından her bir öğrenci için isim ve notları girdi olarak alır.
#Sözlük Oluşturur:

#Her öğrencinin ismini bir anahtar (key), notlarını ise bir liste olarak student_marks sözlüğüne ekler.
#Sorgu Çalıştırır:

#Kullanıcıdan sorgulamak istediği öğrencinin adını alır ve o öğrencinin notlarını bulur.
#Ortalama Hesaplar ve Yazdırır:

#Notların ortalamasını hesaplar ve sonucu yazdırır.


#1- Öğrencileri ve notlarını toplama:
# student_marks[name] = scores
# Bu işlem for döngüsü içinde olur ve her öğrencinin adı (name) ile notları (scores) sözlüğe eklenir.

#2- Kullanıcının sorgulaması:
# query_name = input()
# scores = student_marks[query_name]

# Kullanıcıdan bir isim (örneğin "Ali") alırız ve bu ismi kullanarak sözlükten ilgili notlara ulaşırız.

numbers = ["1", "2", "3", "4"]

# map fonksiyonu kullanılır
result = map(int, numbers)

print(result)  # Bu bir map object: <map object at 0x...>

# Listeye çevrildiğinde elemanları görürüz
print(list(result))  # [1, 2, 3, 4]
