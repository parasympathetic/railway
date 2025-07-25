# 🚀 Розгортання Telegram бота на Railway (БЕЗКОШТОВНО 24/7)

## ✅ Переваги Railway:
- **24/7 робота** - бот працює постійно без сну
- **500 годин/місяць** безкоштовно (достатньо для 24/7)
- **Простий деплой** - один клік з GitHub
- **Автоматичні оновлення** - при push в репозиторій
- **Логи в реальному часі** - легко відстежувати роботу

## 📁 Файли для Railway:

Використовуйте ці файли:
- `main_railway.py` - оптимізований код бота
- `requirements_railway.txt` - залежності
- `runtime.txt` - версія Python
- `Procfile` - команда запуску
- `.env_railway` - змінні середовища

## Крок 1: Підготовка GitHub репозиторію

1. **Створіть новий репозиторій** на GitHub
2. **Завантажте файли**:
   - `main_railway.py`
   - `requirements_railway.txt` (перейменуйте в `requirements.txt`)
   - `runtime.txt`
   - `Procfile`
   - `.env_railway` (перейменуйте в `.env` і додайте в `.gitignore`)

3. **Створіть `.gitignore`**:
   ```
   .env
   __pycache__/
   *.pyc
   .DS_Store
   ```

4. **Push в GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Initial bot setup for Railway"
   git branch -M main
   git remote add origin https://github.com/yourusername/telegram-bot.git
   git push -u origin main
   ```

## Крок 2: Реєстрація на Railway

1. Перейдіть на **railway.app**
2. **Зареєструйтеся** через GitHub
3. **Підтвердіть email** (якщо потрібно)

## Крок 3: Деплой бота

1. **Натисніть "New Project"**
2. **Виберіть "Deploy from GitHub repo"**
3. **Оберіть ваш репозиторій** з ботом
4. Railway автоматично:
   - Виявить Python проект
   - Встановить залежності з `requirements.txt`
   - Використає версію Python з `runtime.txt`
   - Запустить команду з `Procfile`

## Крок 4: Налаштування змінних середовища

1. **Перейдіть в проект** на Railway
2. **Відкрийте вкладку "Variables"**
3. **Додайте змінну**:
   - **Name**: `TELEGRAM_BOT_TOKEN`
   - **Value**: `ваш_токен_бота`
4. **Збережіть** зміни

## Крок 5: Перевірка роботи

1. **Перейдіть у вкладку "Deployments"**
2. **Перевірте логи** - повинно бути "Бот запущено на Railway - 24/7 режим"
3. **Надішліть `/start`** вашому боту в Telegram
4. **Переконайтеся**, що бот відповідає і надсилає статті

## 🔧 Моніторинг та логи

### Перегляд логів:
1. Відкрийте проект на Railway
2. Перейдіть у вкладку "Deployments"
3. Натисніть на активний деплой
4. Переглядайте логи в реальному часі

### Перезапуск бота:
1. Перейдіть у "Deployments"
2. Натисніть "Redeploy"
3. Або зробіть новий commit в GitHub

## 📊 Використання ресурсів

**Безкоштовний план Railway:**
- **500 годин/місяць** виконання
- **1GB RAM** максимум
- **1GB диск** простору
- **Необмежений трафік**

**Для 24/7 роботи:**
- 24 години × 30 днів = 720 годин
- Потрібно оптимізувати або перейти на платний план ($5/місяць)

## 🚨 Важливі примітки

⚠️ **Безпека:**
- Ніколи не додавайте `.env` файл в Git
- Використовуйте змінні середовища Railway
- Регулярно оновлюйте токен бота

💡 **Оптимізація:**
- Бот оптимізований для мінімального використання ресурсів
- Логування допомагає відстежувати роботу
- Автоматична обробка помилок

## 🆘 Вирішення проблем

**Бот не запускається:**
1. Перевірте логи в Railway
2. Переконайтеся, що токен правильний
3. Перевірте, чи всі файли в репозиторії

**Бот не відповідає:**
1. Перевірте статус деплою
2. Подивіться логи на помилки
3. Перезапустіть деплой

**Вичерпано години:**
1. Перевірте використання в Dashboard
2. Оптимізуйте код
3. Розгляньте платний план

## 🎉 Готово!

Ваш бот тепер працює **24/7 безкоштовно** на Railway! 

**Переваги над іншими платформами:**
- ✅ Справжня 24/7 робота (не засинає)
- ✅ Простий деплой з GitHub
- ✅ Автоматичні оновлення
- ✅ Якісні логи та моніторинг
- ✅ Швидка підтримка
