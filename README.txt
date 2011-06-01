README FILE
--------------



South commands

To set your reference point (Important: You should run this command before making any changes to your Model):
python manage.py schemamigration <app_name> blank --empty

After you make your changes:
python manage.py schemamigration <app_name> --auto
python manage.py migrate <app_name>

If ever syncdb has not even created your app tables, run:
python manage.py schemamigration <app_name> --initial
python manage.py migrate <app_name>