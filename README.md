# Movie Watchlist

İstifadəçilərə öz filmlərini əlavə etmək, redaktə etmək, silmək və status/janra görə filtrləmək imkanı verən Django tətbiqi.

## Başlatmaq

Python 3.10+ və Django tələb olunur. Layihə SQLite istifadə edir.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Brauzerdə `http://127.0.0.1:8000/` ünvanını açın və **Qeydiyyat** vasitəsilə hesab yaradın. İdarəetmə paneli üçün əvvəlcə `python manage.py createsuperuser` işlədin; panel `http://127.0.0.1:8000/admin/` ünvanındadır.

## Əsas funksiyalar

- Film adı, janr, buraxılış ili, status, 1–10 arası şəxsi qiymət, əlavə olunma tarixi və sahib.
- ModelForm ilə əlavə etmə və redaktə formaları.
- Giriş və qeydiyyat; siyahı yalnız daxil olmuş istifadəçiyə görünür.
- Redaktə/silmə sorğuları sahibin filmləri ilə məhdudlaşır. Başqa istifadəçinin film ID-si 404 qaytarır.
- Janr və status filtrləri, 10 film üzrə səhifələmə.
- Bootstrap 5 ilə mobilə uyğun sadə interfeys.

## Django REST Framework API

API giriş tələb edir. Django session authentication browsable API-dən istifadə etməyə, Basic authentication isə API klientlərindən sorğu göndərməyə imkan verir. İstehsal mühitində Basic authentication-i yalnız HTTPS üzərindən istifadə edin.

| Metod | Endpoint | Təsvir |
|---|---|---|
| `GET` | `/api/movies/` | Öz filmlərinin siyahısı |
| `POST` | `/api/movies/` | Öz siyahısına film əlavə et |
| `GET` | `/api/movies/<id>/` | Öz filminə bax |
| `PUT`, `PATCH` | `/api/movies/<id>/` | Öz filmini redaktə et |
| `DELETE` | `/api/movies/<id>/` | Öz filmini sil |

Siyahını statusa və janra görə filtrləmək olar: `/api/movies/?status=watched&genre=Drama`. Dəstəklənən statuslar: `want`, `watching`, `watched`. Nəticələr 10 film olmaqla səhifələnir (`?page=2`).

Film yaratma sorğusunun JSON nümunəsi:

```json
{
  "title": "Interstellar",
  "genre": "Elmi fantastika",
  "release_year": 2014,
  "status": "watched",
  "rating": 10
}
```

`owner`, `id` və `created_at` server tərəfindən idarə olunur; sahib həmişə autentifikasiya olunmuş istifadəçidən götürülür. Başqa istifadəçinin film ID-si siyahıda görünmür və detail endpoint-lərdə 404 qaytarır.

## Təhlükəsizlik qeydi

İstehsal mühitində `DJANGO_SECRET_KEY`, `DJANGO_DEBUG=0` və `DJANGO_ALLOWED_HOSTS` mühit dəyişənlərini təyin edin; HTTPS və təhlükəsiz cookie parametrlərini deploy mühitinizə uyğun aktiv edin.
