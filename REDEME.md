> 自动生成ORM
```cmd
pip install flask-sqlacodegen

flask-sqlacodegen 'mysql://root:000000@192.168.159.145/food_db' --table user --outfile "common/models/user.py" --flask

```