# routes.py
from flask import render_template, request, redirect, url_for
from . import app

# временное хранилище в памяти (на время запуска)
people = []

@app.route("/", methods=["GET", "POST"])
def index():
  if request.method == "POST":
    name = (request.form.get("name") or "").strip()
    age_raw = request.form.get("age")
    city = (request.form.get("city") or "").strip()
    hobby = (request.form.get("hobby") or "").strip()

    # простая серверная валидация
    errors = []
    try:
      age = int(age_raw) if age_raw is not None else None
    except ValueError:
      errors.append("Возраст должен быть числом.")

    if not name:
      errors.append("Имя обязательно.")
    if age is None or not (0 <= age <= 120):
      errors.append("Возраст должен быть в диапазоне 0–120.")
    if not city:
      errors.append("Город обязателен.")
    if not hobby:
      errors.append("Хобби обязательно.")

    if errors:
      # Перерисовываем шаблон с ошибками и уже введёнными данными
      return render_template("form.html", people=people, errors=errors,
                             values={"name": name, "age": age_raw, "city": city, "hobby": hobby})

    # добавляем запись и делаем PRG (Post/Redirect/Get)
    people.append({"name": name, "age": age, "city": city, "hobby": hobby})
    return redirect(url_for("index"))

  # GET — отрисовка страницы
  return render_template("form.html", people=people)
