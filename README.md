# WineStorage

Run server:

```bash
DATABASE_URL="mysql+mysqlconnector://root:pass@mariadb-wine-storage/wine_storage"
```

restart

docker-compose rm -fs
docker-compose up --build

new migration:

from root directory:

```
cd WineStorage/
FLASK_APP="wsgi.py" flask db revision --autogenerate --message "${message:-No message}" --directory "src/migrations"
```

run server
python run_dev.py
uwsgi uwsgi.ini --set-placeholder port=$PORT

import dummy data

INSERT INTO wine (winery, variety, attribute, sugar, year) VALUES
('Šilinek', 'Solaris', 'Pozdní sběr', 'Suché', '2019'),
('Šilinek', 'Hibernal', 'Pozdní sběr', 'Polosuché', '2019'),
('Šilinek', 'Souvignier gris', 'Pozdní sběr', 'Suché', '2019'),
('Šilinek', 'Sylvánské zelené', 'Pozdní sběr', 'Suché', '2018'),
('Šilinek', 'Ryzlink vlašský', 'Pozdní sběr', 'Suché', '2019'),
('Šilinek', 'Pálava', 'Pozdní sběr', 'Polosuché', '2018'),
('Šilinek', 'Pálava', 'Pozdní sběr', 'Suché', '2019'),
('Šilinek', 'Ryzlink rýnský', 'Pozdní sběr', 'Suché', '2019'),
('Šilinek', 'Tramín červený', 'Pozdní sběr', 'Suché', '2018'),
('Šilinek', 'Sauvignon', 'Pozdní sběr', 'Suché', '2018'),
('Šilinek', 'Irsai Oliver', 'Pozdní sběr', 'Suché', '2019'),
('Paulus', 'Souvignier gris', 'Pozdní sběr', 'Suché', '2019'),
('Paulus', 'Pálava', 'Výběr z hroznů', 'Polosuché', '2019'),
('Antoš', 'Chardonnay', 'Zemské víno', 'Polosuché', '2019'),
('Vinium V.P.', 'Sauvignon', 'Pozdní sběr', 'Polosuché', '2019'),
('Vinium V.P.', 'Tramín červený', 'Pozdní sběr', 'Polosuché', '2019'),
('Vinium V.P.', 'Hibernal', 'Pozdní sběr', 'Polosuché', '2019'),
('Břeclav', 'Ryzlink rýnský', 'Pozdní sběr', 'Polosuché', '2018'),
('Šilinek', 'Solaris', 'Pozdní sběr', 'Suché', '2020'),
('Šilinek', 'Ryzlink vlašský', 'Pozdní sběr', 'Suché', '2020'),
('Šilinek', 'Irsai Oliver', 'Pozdní sběr', 'Suché', '2020'),
('Šilinek', 'Tramín červený', 'Výběr z hroznů', 'Polosuché', '2019'),
('Šilinek', 'Ryzlink vlašský', 'Jakostní', 'Suché', '2020'),
('Šilinek', 'Pálava', 'Výběr z hroznů', 'Polosuché', '2020'),
('Šilinek', 'Muškát moravský', 'Pozdní sběr', 'Polosuché', '2019'),
('Šilinek', 'Veltlínské zelené', 'Pozdní sběr', 'Polosuché', '2019'),
('Šilinek', 'Veltlínské zelené', 'Jakostní', 'Polosuché', '2019'),
('Šilinek', 'Cabernet Sauvignon', 'Pozdní sběr', 'Suché', '2017'),
('Šilinek', 'Dornfelder', 'Pozdní sběr', 'Suché', '2019'),
('Šilinek', 'Ryzlink rýnský', 'Pozdní sběr', 'Suché', '2020');
