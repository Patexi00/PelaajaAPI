Tämä on käynnistysohje, PelaajaAPI:n käynnistämiseen käyttäen visual studio code:a windows käyttöjärjestelmässä.

- Avaa visual studio codella PelaajaAPI kansio
- Luo virtuaaliympäristö
- Avaa VScode terminaali ja syötä sinne seuraavat komennot
    - pip install fastapi
    - pip install uvicorn

- Käynnistä kirjoittamalla terminaaliin 
    - uvicorn main:app --reload