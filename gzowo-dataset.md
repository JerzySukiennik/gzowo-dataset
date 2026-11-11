# Gzowo Dataset

> Jedno miejsce z całą wiedzą o działce Gzowo 34 nad Narwią: miejsce, historia, ludzie, zwierzęta, sprzęt, rytuały, powiedzonka, wspomnienia, marki (Gzowo Labs, GSP) i media. Zrobione głównie pod grę o Gzowie (planszową albo komputerową), ale ma służyć każdemu projektowi, który potrzebuje prawdziwego Gzowa.

Wersja 1.2, 2026-11-11. Język: polski. Autor: Jurek (Jerzy) Sukiennik, spisane i uporządkowane z Claude.

## Jak z tego korzystać (dla AI)

- Ten plik zawiera **cały tekst** datasetu. Adres: https://dataset.gzowo.fun/gzowo-dataset.md
- To samo w JSON: https://dataset.gzowo.fun/data/all.json (albo osobne pliki w https://dataset.gzowo.fun/data/).
- Zdjęcia i filmy: https://dataset.gzowo.fun/data/media.json ma każdy plik z opisem, kto, gdzie, kiedy i co widać. Obrazy możesz otwierać i oglądać sam.
- Masz terminal? `git clone https://github.com/JerzySukiennik/gzowo-dataset` daje wszystko lokalnie. Jeśli twoje narzędzie do stron streszcza treść, pobierz pliki przez `curl -L`.
- Filmów nie musisz oglądać: każdy ma kadry w `media/klatki/<id>/` i opis.

**Zasada prawdy:** Wszystko tutaj ma być prawdziwe. Każdy fakt ma źródło (pole source) i pewność (confidence). Rzeczy niepewne są oznaczone, niczego nie dopisano dla ozdoby. Jedyny dział z pomysłami zamiast faktów to game_kit i jest tak podpisany.

Źródła:
- `jurek-2026-11-10`: Odpowiedzi Jurka na pytania, rozmowa z 10.11.2026 (najświeższe i najważniejsze źródło).
- `jurek-2026-11-11`: Opisy zdjęć i filmów oraz notatka, które Jurek wpisał 11.11.2026 na stronie do opisywania mediów.
- `galeria`: Podpisy i tytuły z Galerii Gzowo (prezent Jurka dla taty na Dzień Ojca, czerwiec 2026). Pisał je Jurek.
- `notatki`: Notatki projektowe Jurka z lat 2025-2026 (opisy jego gier i projektów osadzonych w Gzowie).
- `gra-narew`: Gra Rysia 'NAREW, posesja nad jeziorem' (narew.html). Świat gry jest wzorowany na działce, ale to fikcja.
- `gzowo.fun`: Dane ze strony Gzowo Labs (gzowo.fun).
- `geodane`: Numeryczny model terenu i ortofotomapa z Geoportalu oraz OpenStreetMap, pobrane w lipcu 2026.
- `obserwacja`: Opis tego, co widać na zdjęciu albo filmie (opisał Claude).
- `wniosek`: Wniosek Claude'a z kilku źródeł. Niepotwierdzony przez rodzinę.

Pewność:
- `pewne`: Powiedziane wprost przez Jurka albo widoczne w materiale.
- `prawdopodobne`: Wynika ze źródeł, ale nikt tego wprost nie potwierdził.
- `niepewne`: Jurek sam zaznaczył niepewność ("chyba", "najprawdopodobniej") albo źródła się różnią.

## 1. Miejsce

**Gzowo 34** (Gzowo, Ośrodek, Ośrodek Gzowo, działka, posesja nad Narwią). Rodzinna działka Sukienników nad Narwią, dawny ośrodek FSO (Fabryki Samochodów Osobowych). Na starej tablicy stoi "Ośrodek Wędkarski w Gzowie", na tabliczce domku "Ośrodek Wypoczynkowy". Od niej pochodzą wszystkie marki z 'Gzowo' w nazwie.

- Adres: Gzowo 34, wieś Gzowo, gmina Pokrzywnica, powiat pułtuski, województwo mazowieckie, Polska
- Współrzędne: 52.612806, 21.116
- Ok. 45 km w linii prostej na północ od centrum Warszawy (wyliczone ze współrzędnych). Rodzina mieszka w Warszawie i przyjeżdża na działkę.

**Narew.** "Serce Gzowa - Narew!" (podpis z galerii). Działka schodzi do samej wody. Rzeka jest tu szeroka i spokojna, wygląda jak jezioro. W rodzinnych podpisach bywa nazywana jeziorem ("łabędź na jeziorze"), gra Rysia ma podtytuł "posesja nad jeziorem". W dolinie są rozlewiska, starorzecze i piaszczyste łachy. Poziom wody ok. 79.3 m n.p.m. Co się na niej robi: kąpiel i brodzenie, SUP, kajaki, motorówka, kopanie w piasku na plaży, wędkowanie (wędkarze z okolicy), zimą chodzenie po lodzie.

**Teren.** Działka leży na samej krawędzi skarpy nadnarwiańskiej. Jest góra i dół: na górze terasa z polami, sadami i zabudową wsi, na dole dolina z rzeką, mokrymi łąkami i piaskiem. Skarpa biegnie z północy na południe, ok. 20 m różnicy wysokości na krótkim dystansie. W kwadracie 1 x 1 km wysokości od 79.1 do 104.1 m n.p.m. (różnica 25.0 m), sama działka ok. 87.2 m. Drzewa: Sosny (na działce rośnie kępa wysokich sosen), brzozy, dęby, przy wodzie wierzby i olchy. W kwadracie 1 x 1 km wokół działki OpenStreetMap ma ok. 300 budynków, Aleję Lipową, plażę, mokradło, starorzecze i rowy melioracyjne.

Pokrycie terenu w kwadracie 1 x 1 km: pola uprawne 32.4%, łąka 21.1%, woda 17.4%, siedliska i ogrody 16.1%, las 7.3%, budynki 1.8%, drogi 2.5%, piach 1.3%.

**Widok z góry.** Na zdjęciu lotniczym (media/geo/ortofoto-dzialka-zblizenie.jpg, żółte kółko = Gzowo 34): w środku działki ciemna kępa sosen, dookoła jasny piasek, od północnego wschodu i wschodu szeroka woda Narwi, na wschodzie mała zatoczka i zalesiony cypel, od południa i zachodu domy sąsiadów, dojazd drogą od południowego zachodu.

## 2. Historia i oś czasu

- **przed 2021**: Na tym terenie działał ośrodek FSO (Fabryki Samochodów Osobowych). Stara czerwona tablica mówi "Ośrodek Wędkarski w Gzowie", tabliczka na domku "Ośrodek Wypoczynkowy". Stało tu 10 domków i wiata, był też budynek łazienek. _(źródło: jurek-2026-11-10, jurek-2026-11-11, obserwacja; pewne)_
- **nieznane, dawniej**: Na skarpie, na górze działki, pod ziemią jest najprawdopodobniej stary skład bomb i broni. _(źródło: jurek-2026-11-10; niepewne)_
- **po wojnie i do dziś**: To tereny powojenne. Na działce trafiają się niewypały i przyjeżdżają do nich saperzy. _(źródło: jurek-2026-11-10; pewne)_
- **2020-11-30**: Jurek i Rysio wygłupiają się przed kamerką komputera w Warszawie (filmik 'Movie on 30-11-2020'). Jeszcze przed Gzowem. _(źródło: obserwacja, jurek-2026-11-10; pewne)_
- **2021-05-17**: Zdjęcie papierowej mapy geodezyjnej okolicy, zrobione w Warszawie miesiąc przed tym, jak działka trafiła do Sukienników. _(źródło: jurek-2026-11-11; pewne)_
- **2021-06**: Od tego miesiąca Sukiennicy mają działkę Gzowo 34. _(źródło: jurek-2026-11-10; pewne)_
- **2021-06-13**: Jedno z pierwszych zdjęć z działki: Domek nr 1, ciemny drewniany domek z czerwonymi drzwiami i tabliczką "Ośrodek Wypoczynkowy". W tle siedzi Rysio. _(źródło: jurek-2026-11-11; pewne)_
- **2021-07-10**: Rysio stoi o zachodzie słońca na Cyplu i rzuca coś do Narwi. _(źródło: jurek-2026-11-11; pewne)_
- **2021-10-23**: Zdjęcie starej czerwonej tablicy "Fabryka Samochodów Osobowych, Ośrodek Wędkarski w Gzowie". _(źródło: jurek-2026-11-11; pewne)_
- **po 2021**: Z 10 domków zostały 3. Powstał dom (bryłą nawiązuje do dawnych łazienek ośrodka), drewniany taras z desek i panele słoneczne. Wiata została. _(źródło: jurek-2026-11-10; pewne)_
- **jedne święta, rok nieznany**: Boże Narodzenie w Gzowie z kozą przywiezioną na chwilę z Warszawy. Dom jest jeszcze w surowym stanie, są Jurek, Rysio, Zofia i tata. _(źródło: jurek-2026-11-11; pewne)_
- **2022-09-06**: Na skarpie stoi granatowy helikopter SP-MMM. Waldek pozuje przy nim z nogą na płozie, pod helikopterem stoi jego pies Kropka. _(źródło: jurek-2026-11-11; pewne)_
- **ok. zimy 2022/2023**: Czas Dropsika, małego czarno-karmelowego psa. Film DANCE z nim został zmontowany 28.01.2023. Niedługo po tym, jak się pojawił, został porwany. _(źródło: jurek-2026-11-10, obserwacja; prawdopodobne)_
- **2023-06-07**: Zdjęcie logo Gzowa 34: biała ośmiornica na czarnym tle. _(źródło: jurek-2026-11-11; pewne)_
- **2023-07-08**: Zofia stoi o zmierzchu na Cyplu, cała oświetlona na czerwono, i patrzy na Narew. _(źródło: jurek-2026-11-11; pewne)_
- **2023-07-15**: Szamborski wisi helikopterem nisko nad Narwią przy Cyplu, na brzegu są Rysio i Zofia. _(źródło: jurek-2026-11-11; pewne)_
- **2023-08-29**: Jurek jako KALAKASANYT nagrywa w Warszawie reakcję na '200 memes in 1 song'. _(źródło: obserwacja, jurek-2026-11-10; pewne)_
- **2025-05-25**: Ktoś w zielonej bluzie z kapturem maluje na ziemi przed domkiem wielkie kolorowe płótno szczotką na długim kiju (film z sali 3C Galerii). _(źródło: obserwacja; pewne)_
- **2025, lato albo jesień**: Powstaje Gzowo Space Program (GSP), rakiety modelarskie Jurka i taty. Notatki mówią o lecie 2025, strona o jesieni 2025. _(źródło: notatki, gzowo.fun; niepewne)_
- **2025-10-18 i 19**: Zielona rakieta taty 'Architektoniczny wieżowiec' wydrukowana w 3D i starty z szutrowej drogi i z pola pod Gzowem. _(źródło: galeria, obserwacja; pewne)_
- **2025-11-01**: Kolejne starty rakiet z łąki o zmierzchu. _(źródło: obserwacja; pewne)_
- **2025-11-29**: Start czerwono-czarnej rakiety The Orange Beauty z oszronionej łąki (nagrany też kamerą Insta360). Spadochron się nie otworzył. Strona gzowo.fun podaje datę lotu 22.02.2026, ale nazwy plików z WhatsAppa wskazują 29.11.2025. _(źródło: obserwacja, gzowo.fun; niepewne)_
- **2026-03-21**: Pierwszy lot rakiety Gzofajfus Classic Mk II. Spadochron otworzył się za pierwszym razem. _(źródło: gzowo.fun; pewne)_
- **2026-06-23**: Dzień Ojca: Jurek daje tacie Galerię Gzowo, galerię 3D ze zdjęciami z działki ("Dla Taty. Historia Gzowa zebrana w interaktywną i jedyną w swoim rodzaju formę"). _(źródło: notatki, galeria; pewne)_
- **2026-07 i 08**: Jurek spędza lato w Gzowie (do ok. 10 sierpnia). Nagrywa dom od środka i z zewnątrz (28.07) i fotografuje plażę (08.08). _(źródło: notatki, obserwacja; pewne)_
- **2026-10-29**: Strona gzowo.fun staje się pulpitem Windows 98 nad pikselową mapą działki. _(źródło: notatki; pewne)_
- **2026-11-05**: Gzowo Labs dostaje logo Wschód: dwa splecione ogniwa (dwóch braci) nad horyzontem. _(źródło: notatki; pewne)_
- **2026-11-10**: GSP jest już scalone z Gzowo Labs, miejsce startów nazywa się GL Launch Site. Powstaje ten dataset. _(źródło: jurek-2026-11-10; pewne)_

## 3. Ludzie

### Rodzina

**Jurek Sukiennik (Jerzy Sukiennik)**. Starszy syn. Autor tego datasetu, twórca Gzowo Labs, konstruktor rakiet. _(źródło: notatki, jurek-2026-11-10, gzowo.fun, obserwacja; pewne)_
- Rocznik 2012, mieszka w Warszawie, w roku szkolnym 2026/27 chodzi do 8 klasy.
- Pasje: rakiety modelarskie, druk 3D, AI i własne modele, gry przeglądarkowe, design, pianino i fortepian (poziom zaawansowany), Michael Jackson.
- Minimalista. Ulubiona marka aut to Tesla.
- Dawny nick w internecie: KALAKASANYT (Kalakasan yt).
- W Gzowo Space Program ma tytuł CEO.
- Na stronie gzowo.fun przedstawia się hasłem: "I build things that fly. And a few that don't crash."
- Wygląd: Ok. 173 cm, szczupły, jasna skóra, oczy zielono-piwne, włosy średni brąz, potargane. Typowy strój: czarna bluza z kapturem Nike x RTFKT (żółty znaczek), czarne dresy, zielone Crocsy. Na starszych zdjęciach z działki: czerwona kurtka i żółta albo zielona czapka.
- W grach: W grze Ośrodek Daje to on jest sprawcą dziur w ziemi (eksperyment GSP), chodzi z telefonem w ręku. Na gzowo.fun jest pikselowym i trójwymiarowym awatarem, który wiosłuje kajakiem, łowi ryby i jeździ na łyżwach po zamarzniętej Narwi.

**Rysio Sukiennik (Ryszard Sukiennik)**, inaczej: Ryś, Rysio. Młodszy brat Jurka. _(źródło: notatki, galeria, gzowo.fun, obserwacja; pewne)_
- Autor gry 'NAREW, posesja nad jeziorem', w której chodzi się po działce.
- Na zdjęciach: pływa na desce SUP w kapoku, łapie wiatr na motorówce, pozuje w okrągłych okularach ("Rysio lubi Old School"), zimą trzyma wielką taflę lodu ("Zimowy obiad Rysia") i staje w pozie Supermana w świetle reflektora ("Strike a pose!").
- Jedno z dwóch ogniw w logo Gzowo Labs (ogniwa to dwaj bracia).
- W czerwcu 2021 siedzi w tle zdjęcia Domku nr 1, w lipcu 2021 rzuca coś do Narwi o zachodzie słońca na Cyplu.
- Wygląd: Ok. 145 cm, jasne, płaskie blond włosy. Znak rozpoznawczy: puchata czerwona bluza Spider-Man z czarną maską, niebieskie jeansy. Charakter: nakręcony młodszy brat.
- W grach: W Ośrodek Daje stoi z rękami w górze w czerwonej bluzie.

**Jan Sukiennik**, inaczej: Tata, KS, Kierownik Ośrodka. Tata. Zabawowo i śmiesznie: KS, czyli Kierownik Ośrodka (bo działka to dawny ośrodek). _(źródło: jurek-2026-11-10, notatki, galeria, gra-narew, gzowo.fun; pewne)_
- Jego złota myśl i zasada nr 1: "Ośrodek daje, Ośrodek daje" (od "Bóg daje, Bóg zabiera").
- Jak mówi i jaki jest (wg Jurka): siup do przodu, nie uważa, wyluzowany, kocha lustra, wizjoner, prosty, elegancki.
- Pilotuje drona DJI Avata (zdjęcie "Pilot Jan": stoi nad Narwią z kontrolerem w rękach).
- Maluje światłem przy ognisku (zdjęcie "Malowanie Światłem").
- W GSP ma tytuł Founding Partner. Jego rakieta to zielony 'Architektoniczny wieżowiec'.
- Czyta dzieciom książki na działce ("Letnia lektura"), konsultował budowę tarasu.
- Prowadzi firmę R&D Studio (rd.studio).
- To dla niego powstała Galeria Gzowo (Dzień Ojca 2026).
- Jest ilustracja "Jan Sukiennik z kozą nad Narwią": w białym futrze i czarnej czapce prowadzi kozę na smyczy o złotym świcie.
- Wygląd: Ok. 185 cm, szczupły, ok. 45 lat, grube granatowe okulary (zawsze), jasnobrązowe włosy (w jednym opisie długie do ramion, w drugim zaczesane do tyłu). Stroje-legendy: białe kudłate futro do kolan, kozaki z krokodyla (ciemna skóra z łuską, jest też wersja limonkowa), czerwona czapka z daszkiem, kowbojskie buty, żółta kurtka, cytrynowe japonki z flagą Brazylii, szlafrok granatowo-fioletowy.
- W grach: W Ośrodek Daje jest KS w białym futrze i butach z krokodyla. W grze Rysia stoi w Narwi i klawiszem R wystrzeliwuje gracza w górę, a potem siedzi na kanapie w domu.

**Zofia**, inaczej: Mama. Mama Jurka i Rysia. _(źródło: jurek-2026-11-11; pewne)_
- 08.07.2023 stoi o zmierzchu na Cyplu w długim stroju, cała oświetlona na czerwono, i patrzy na Narew.
- 15.07.2023 jest z Rysiem na Cyplu, kiedy Szamborski wisi helikopterem nad wodą.
- Jest na filmie ze świąt w Gzowie z kozą.

### Przyjaciele i goście

**Waldek (Waldemar Otton)**. Pracownik i pomocnik w Gzowie, ale też bardzo przyjaciel. _(źródło: jurek-2026-11-10, galeria, gra-narew; pewne)_
- To głównie on pracuje koparką i kopie na działce.
- Ma swój dom w okolicy (miejsce "dom Waldka").
- Dropsik był bardziej jego psem niż Sukienników.
- W Galerii ma własny pokój "Ottonowie. Wierni członkowie Gzowa" z portretem z żoną Bożeną, zatytułowanym "Dziadkowie".
- Na zdjęciu z 06.09.2022 pozuje przy helikopterze na skarpie: żółta czapka, zielona wzorzysta marynarka, noga na płozie.
- Miał psa Kropkę (zmarła ok. 2024).
- W grach: W grze Rysia Waldek przyjeżdża konno, kiedy wpisze się poprawny kod na ścianie ("Waldek jeździ tu konno, odkąd pamiętam"), jest też "zakład z Waldkiem" o kopanie.

**Bożena Otton**. Żona Waldka. Razem z nim na portrecie "Dziadkowie" w cieniu drzew. _(źródło: galeria; pewne)_

**Ciszewscy**. Zaprzyjaźniona rodzina, stali goście Gzowa: Bartek, Ola Kluzek "Clu", Ignacy i Helena. _(źródło: jurek-2026-11-10, galeria, gra-narew, wniosek; pewne)_
- W Galerii mają pokój "Ciszewscy x Sukiennicy" z hasłem "Herbata nie wyklucza kawy".
- Ola "Clu" odpoczywa w hamaku wśród sosen.
- Ignacy i Helena to dzieci (wniosek ze zdjęć): "Modlitwa przy drzewie", wspólne czytanie z Janem, Jurkiem i Rysiem.
- Ignacy z Rysiem przedzierali się przez trawy do stacji Moya ("Ciężka droga do stacji Moya").
- Helena chodziła zimą po zamarzniętej Narwi.
- W grach: W grze Rysia po czterech minutach wjeżdżają autem przez bramę, parkują przed domem, wysiada czworo i od tej pory chodzą po posesji.

**Czupryńscy**. Znajomi rodziny. Właściciele kota Beethovena. _(źródło: jurek-2026-11-10, galeria; pewne)_
- Zdjęcie "Razem o zachodzie": przytuleni nad wodą w złotym świetle.

**Janek Kunstler**. Kolega Jurka. Był w Gzowie podczas wielkiej burzy z gradem. _(źródło: jurek-2026-11-10; pewne)_

**Szamborski**. Czasem przylatuje do Gzowa helikopterem. _(źródło: jurek-2026-11-10, wniosek; pewne)_
- 15.07.2023 wisiał helikopterem nisko nad Narwią przy Cyplu (film).
- Granatowy helikopter Airbus z rejestracją SP-MMM stał na skarpie 06.09.2022. To najpewniej jego maszyna (wniosek).
- Pusty pokój "Heli" w Galerii Gzowo najpewniej czeka na zdjęcia jego helikoptera (wniosek, niepotwierdzony).

### Okolica

**Arek**. Śp. "Gzowiański somsiad", wędkarz znad Narwi. Imię niepewne (Jurek: "chyba Arek"). _(źródło: jurek-2026-11-10, galeria; niepewne)_
- Zdjęcie "Letni odpoczynek" z Janem na brzegu: "Piwko, Narew, wspólny czas. Czego by tu chcieć więcej!".

**Benny**. Lokalna postać, lubiana przez rodzinę. _(źródło: jurek-2026-11-10; pewne)_
- Znany z tego, że często chodzi z puszką piwa, nawet w deszczu.

**Ekipa stacji Moya**. Bardzo miłe panie, które pracują na stacji Moya, i pan, który często tam przychodzi. _(źródło: jurek-2026-11-10; pewne)_

**Major**. Łowi ryby, ale też robi u Sukienników wycinki drzew. _(źródło: jurek-2026-11-10; pewne)_
- Nie wiadomo, czy Major to ksywka, stopień czy nazwisko.

**Paweł**. Łysy gość z kanału obok Kociej Wyspy. _(źródło: jurek-2026-11-10; pewne)_
- Jurek opisał go jako "jakiś łysy gość", więcej o nim nie wiadomo.

**Wójt**. Wójt, czyli szef gminy. Jurek wymienił go jako postać Gzowa, bez szczegółów. _(źródło: jurek-2026-11-10; pewne)_

### Postacie zmyślone (z gier i projektów)

- **Edward Warchocki** (gra Rysia NAREW): Postać z gry: chodzi w kółko po posesji i zagaduje. Jego kwestie: "dziki znowu zryły łąkę za płotem", "szopy tańczą przy ognisku, sam zobacz", "Waldek jeździ tu konno, odkąd pamiętam", "woda w Narwi dziś czysta, można nalać". Ma też własne rolki na telefonie w grze (@edward.warchocki).
- **Michael Jackson** (gra Rysia NAREW): Tancerz w domu, sunie moonwalkiem tam i z powrotem. Jurek jest fanem MJ.
- **Narek** (Narew Labs (projekt Jurka)): Celowo dziwna maskotka 3D: pień-ciało w kolorze #E8A93A, nogi-patyki, jedno oko większe, jedna długa makaronowa ręka i jeden kikut, antenka z żarówką. W planowanym filmiku pisze kredą na ścianie domu "Gzowo Jest Najlepsze <3" i przytula dom. Render: media/postacie/narek/narek_hero.png.
- **Mieszkańcy Żabiego raju** (Galeria Gzowo): Ukryty pokój-łąka ze stawem ("Nasze małe zoo"): żaby, pies, ośmiornica, koza i osioł, które można głaskać i karmić, a ośmiornicę posadzić sobie na głowie.

## 4. Zwierzęta

**Dropsik** (pies, nie ma go już w Gzowie) _(źródło: jurek-2026-11-10, galeria, notatki, obserwacja; pewne)_
- Mały, młody, czarno-karmelowy, bardzo energiczny i "mega zabawny".
- Bardziej pies Waldka niż Sukienników.
- Został porwany niedługo po tym, jak się pojawił. W Galerii podpisany jako "śp. Dropsik".
- Jurek go kochał (zdjęcie "Jurek z Dropsikiem. Letnie przytulanie psa").
- Film DANCE: szczeniak bawi się na liściach i na śniegu przy wiacie i stercie kamieni.
- W grach: W Ośrodek Daje jest pomocnikiem Jurka: jedno ucho stojące, drugie klapnięte, język na wierzchu, czerwona obroża (model zrobiony z opisu, bez zdjęcia).

**Beethoven** (kot, kot Czupryńskich) _(źródło: jurek-2026-11-10, galeria; pewne)_
- Biały, głuchy, "mega fajny".
- "Beethoven nie boi się Jurka (podejrzane)": siedzi spokojnie przed Jurkiem na plaży.
- "Kontemplujący Beethoven": siedzi tyłem na trawie i wita słońce nad zamgloną Narwią.

**Koza** (koza, gość na jedne święta) _(źródło: jurek-2026-11-11; pewne)_
- Była w Gzowie przez jedne święta Bożego Narodzenia, rodzina przywiozła ją na chwilę z Warszawy.
- Brązowo-biała, z czerwoną obrożą. Na filmie ze świąt stoi przy beli siana i przytula się do niej chłopiec.
- Jest też na ilustracji z Janem Sukiennikiem w białym futrze nad Narwią.

**Kropka** (pies, pies Waldka, zmarła ok. 2024) _(źródło: jurek-2026-11-11; pewne)_
- Pies Waldka. Zmarła mniej więcej dwa lata przed listopadem 2026.
- Na zdjęciu z 06.09.2022 stoi pod helikopterem na skarpie.

**Szopy pracze** (dzikie, ważne dla Gzowa) _(źródło: jurek-2026-11-10, gra-narew; pewne)_
- Jurek zaznaczył je jako ważne.
- W grze Rysia pięć szopów tańczy w kręgu wokół ogniska, szybciej, gdy ogień płonie.

**Koty i małe kotki** (dzikie i półdzikie, ważne dla Gzowa) _(źródło: jurek-2026-11-10; pewne)_
- Kręcą się po działce, także kocięta. Jurek zaznaczył je jako ważne.

**Łosie** (dzikie, spotykane) _(źródło: jurek-2026-11-10; pewne)_

**Kuny** (dzikie, spotykane) _(źródło: jurek-2026-11-10; pewne)_

**Lisy** (dzikie, spotykane) _(źródło: jurek-2026-11-10; pewne)_

**Łabędzie** (ptaki, na Narwi) _(źródło: galeria; pewne)_
- Na zdjęciu "Nad wodą" łabędź płynie tuż obok kopiących w piasku dzieci.

**Klucze ptaków** (ptaki, wiosną) _(źródło: galeria; pewne)_
- Zdjęcie "Klucz Ptaków": ptaki wracające w szyku V na wiosennym niebie.

**Dziki** (dzikie, tylko w grze Rysia) _(źródło: gra-narew; niepewne)_
- W grze Rysia: "dziki znowu zryły łąkę za płotem", "trzeci raz w tym tygodniu". Jurek ich nie wymienił.

**Ośmiornica** (symbol, logo Gzowa 34) _(źródło: jurek-2026-11-10, notatki; pewne)_
- Logo Gzowa 34 to ośmiornica.
- Pojawia się w Żabim raju w Galerii (można ją posadzić sobie na głowie) i w pomyśle na Gzowo Car (znak: ośmiornica + napis Car).

## 5. Miejsca na działce i w okolicy

**Dom** (kloc (w grze Rysia)), na działce, wbudowany w skarpę, wśród sosen _(źródło: jurek-2026-11-10, notatki, obserwacja; pewne)_
- Zwykły graniastosłup. Bryłą nawiązuje do dawnych łazienek ośrodka FSO.
- Z zewnątrz (film z 28.07.2026): niska bryła wsunięta w skarpę, na dole otwarty garaż albo schowek, na górze przeszklony prostopadłościan, dookoła sosny i łąka.
- W środku jeden open space ok. 12 x 8 m: ściana z płyt OSB, marmurowa podłoga, sufit ze sklejki na czarnych szynach, przeszklenie na całą wysokość z widokiem na taras, trawę, sosny i Narew.
- Wyposażenie: czarny kominek-koza z rurą, pianino cyfrowe na stojaku, telewizor (LG OLED bez internetu), długa czarna wisząca półka z konsolą PlayStation, modelem z klocków i kulą śnieżną, szafa z lustrem, czarna sofa, duży stół ze sklejki na limonkowych kozłach, kuchnia ze stali nierdzewnej z boomboxem, lampa podłogowa, zasłona, podświetlany pas onyksu przy podłodze.
- Przy dużym stole rodzina prawie zawsze je rano śniadania.
- Na filmie ze świąt, gdy dom był jeszcze surowy: na ścianie z OSB świeci niebieska ośmiokątna lampa, nad biurkiem wisi duży kolorowy obraz, stoi choinka.

**Taras**, przy domu _(źródło: jurek-2026-11-10, galeria; pewne)_
- Drewniany, z desek, duży.
- Zdjęcie "Praca nad tarasem. Konsultacja tarasu": Jan z pracownikiem na piasku budowy.

**Trzy domki**, na działce _(źródło: jurek-2026-11-10, obserwacja; pewne)_
- Zostały 3 z 10 domków dawnego ośrodka FSO.
- Na filmie z 2025 widać jeden: ciemny, drewniany, z czerwonymi drzwiami, obok drewno na opał.
- Domki mają numery. Domek nr 1 (zdjęcie z 13.06.2021): ciemne deski, czerwone drzwi, okno w czerwonej ramie, betonowe bloczki, biała tabliczka "Ośrodek Wypoczynkowy".

**Wiata**, na działce _(źródło: jurek-2026-11-10, galeria, gra-narew, obserwacja; pewne)_
- Stoi od czasów ośrodka.
- Pod nią pasiasty fotel i drewno na opał. Tu powstały zdjęcia "Wspólny czas" i "Krowi chłopiec".
- W grze Rysia przy wiacie stoją koparka, łopata oparta o słup i palenisko.

**Panele słoneczne**, na działce _(źródło: jurek-2026-11-10; pewne)_
- Stoją tam, gdzie kiedyś były domki.

**Ognisko**, na działce _(źródło: jurek-2026-11-10, galeria; pewne)_
- "Ogień + Gzowo to niepokonane combo!"
- Miejsce malowania światłem po zmroku.

**Hamak**, między sosnami _(źródło: jurek-2026-11-10, galeria; pewne)_
- "Odpoczynek wśród sosen", w tle prześwituje woda.

**Plaża** (Plaża Gzowo 34), na dole, nad Narwią _(źródło: jurek-2026-11-10, galeria, obserwacja; pewne)_
- Trawiasto-piaszczysty stok schodzący do płytkiej wody, trzciny, łódki leżące dnem do góry.
- Dojazd piaszczystą drogą wzdłuż muru z gabionów (kosze z kamieniem).
- Tu się kopie w piasku i woduje SUP-a, kajaki i motorówkę.
- Na zdjęciach z 08.08.2026 cumuje żółty skuter wodny, ale nie jest Sukienników.

**Skarpa i stary skład**, górna część działki _(źródło: jurek-2026-11-10, geodane; niepewne)_
- Stroma skarpa nadnarwiańska.
- Pod ziemią najprawdopodobniej stary skład bomb i broni.
- W ziemi na działce trafiają się niewypały z czasów wojny.
- Na skarpie ląduje helikopter (zdjęcie z 06.09.2022).

**Kępa sosen**, środek działki _(źródło: obserwacja; pewne)_
- Wysokie sosny widać na prawie każdym zdjęciu i na zdjęciu lotniczym.

**Cypel**, nad Narwią przy działce _(źródło: jurek-2026-11-10, wniosek; prawdopodobne)_
- Jurek wymienił Cypel jako osobne miejsce i podpisał nim cztery nagrania i ilustrację.
- Miejsce na zachody słońca nad samą wodą: Rysio rzuca coś do Narwi (2021), Zofia stoi o zmierzchu w czerwonym świetle (2023).
- Jest tu palenisko i czerwone krzesła. 15.07.2023 tuż przy brzegu wisiał nad wodą helikopter Szamborskiego.
- Na zdjęciu lotniczym na wschód od działki widać małą zatoczkę i zalesiony język lądu wchodzący w wodę. To najpewniej Cypel (wniosek, do potwierdzenia).

**Kocia Wyspa**, w okolicy, obok kanału _(źródło: jurek-2026-11-10, wniosek; prawdopodobne)_
- Wyspa znana rodzinie, obok niej jest kanał, przy którym bywa Paweł.
- Skąd nazwa i gdzie dokładnie leży, jeszcze nie wiadomo. Koty są w Gzowie ważne, więc nazwa pewnie nie jest przypadkowa (wniosek).

**Kanał**, obok Kociej Wyspy _(źródło: jurek-2026-11-10; pewne)_
- Stąd jest Paweł.

**GL Launch Site** (GSP Launch Site (stara nazwa)), pola, łąki i szutrowa droga w okolicy Gzowa _(źródło: jurek-2026-11-10, galeria, obserwacja; pewne)_
- Miejsce startów rakiet. Nazwa GL, bo GSP jest już scalone z Gzowo Labs.
- Na filmach: wyrzutnia na statywie, start z szutrowej drogi, z brzegu zaoranego pola i z łąki.

**Dom Waldka**, w okolicy _(źródło: jurek-2026-11-10, galeria; pewne)_
- Zdjęcie "Słońce nad polem" (Jurek doświadcza zachodu słońca) zrobiono w okolicach domu Waldka.

**Stacja Moya**, stacja benzynowa obok Gzowa _(źródło: jurek-2026-11-10, galeria; pewne)_
- Bardzo ważna dla rodziny. Często chodzi się tam na lody i napoje.
- Pracują tam bardzo miłe panie, często przychodzi też pewien pan.
- Idzie się na przełaj: "Ciężka droga do stacji Moya. Przedzieranie się przez trawy".

**Sklep**, "w Nieporęcie" (nazwa z dyktowania, niepewna) _(źródło: jurek-2026-11-10; niepewne)_
- Sklep, do którego rodzina często chodzi. Jurek podyktował "w Nieporęcie", a Nieporęt leży ok. 30 km od Gzowa, więc nazwa miejscowości wymaga potwierdzenia.

## 6. Sprzęt i rzeczy

- **Koparka** (nasze): Koparka na kółkach, własna. Pomaga na działce. Pracuje nią głównie Waldek. W grze Rysia stoi przy wiacie, a "łyżka bierze pół metra naraz". _(źródło: jurek-2026-11-10, gra-narew)_
- **Tesla** (nasze): Rodzinne auto elektryczne. Tesla to ulubiona marka Jurka (za minimalizm). W grze Rysia można nią jeździć po posesji, światła zapalają się o zmroku. _(źródło: jurek-2026-11-10, notatki, gra-narew)_
- **Motorówka** (nasze): Szara łódź motorowa. "Rysio łapie wiatr na motorówce". _(źródło: jurek-2026-11-10, galeria)_
- **Kajaki** (nasze): Leżą na brzegu Narwi. Na pikselowej mapie gzowo.fun są dwa: pomarańczowy i turkusowy. _(źródło: jurek-2026-11-10, gzowo.fun, gra-narew)_
- **Deska SUP** (nasze): "Rysio na SUPie świetnie się bawi!" _(źródło: jurek-2026-11-10, galeria)_
- **Dron DJI Avata** (nasze): Pilotuje tata. Zdjęcie "Dron w chmurach. Lecąca AVATA". _(źródło: jurek-2026-11-10, galeria)_
- **Rakiety modelarskie** (nasze): Flota Gzowo Space Program, patrz dział Rakiety. _(źródło: gzowo.fun)_
- **Pianino cyfrowe** (nasze): Stoi w domu. Jurek gra na zaawansowanym poziomie. _(źródło: notatki)_
- **Duży stół na limonkowych kozłach** (nasze): Blat ze sklejki. Miejsce porannych śniadań. _(źródło: jurek-2026-11-10, notatki)_
- **Pasiasty fotel pod wiatą** (nasze): Mieści tatę i trójkę dzieci naraz ("Wspólny czas na fotelu"). _(źródło: galeria, obserwacja)_
- **Białe futro i buty z krokodyla** (nasze): Strój KS-a. "Alligator included" w podpisie zdjęcia "Krowi chłopiec" to najpewniej te buty. _(źródło: notatki, galeria, wniosek)_
- **Żółty skuter wodny** (NIE nasze): Widać go na zdjęciach plaży, ale NIE jest Sukienników. W grze Rysia można nim pływać i robić fale. _(źródło: jurek-2026-11-10, obserwacja, gra-narew)_
- **Czerwone VW Polo** (NIE nasze): Stoi na zdjęciu z Beethovenem, ale NIE jest Sukienników. _(źródło: jurek-2026-11-10, obserwacja)_
- **Helikopter Szamborskiego** (NIE nasze): Czasem ląduje w Gzowie, przylatuje nim Szamborski. Granatowy Airbus, rejestracja SP-MMM. Stał na skarpie (2022) i wisiał nad Narwią przy Cyplu (2023). _(źródło: jurek-2026-11-10)_
- **Stara tablica ośrodka FSO** (nasze): Czerwona, pordzewiała blacha z białym napisem: FABRYKA SAMOCHODÓW OSOBOWYCH, OŚRODEK WĘDKARSKI W GZOWIE. Pamiątka po dawnym ośrodku. _(źródło: jurek-2026-11-11)_
- **Mapa geodezyjna** (nasze): Papierowa mapa z działkami, budynkami i drogami okolicy, z czerwonymi pieczątkami. Sfotografowana w maju 2021. _(źródło: jurek-2026-11-11)_

## 7. Rytuały

- **Śniadanie przy dużym stole**: Prawie zawsze rano, przy dużym stole w domu. _(źródło: jurek-2026-11-10)_
- **Wyprawa na stację Moya**: Spacer na lody i napoje, czasem na przełaj przez wysokie trawy. _(źródło: jurek-2026-11-10, galeria)_
- **Ognisko**: Wieczorem ogień, czasem malowanie światłem na długim czasie naświetlania. _(źródło: galeria)_
- **Starty rakiet**: Wyjście na GL Launch Site, czekanie aż ucichnie wiatr, odliczanie, szukanie rakiety po lądowaniu. _(źródło: gzowo.fun, obserwacja)_
- **Narew latem**: SUP, motorówka, kajaki, kopanie w piasku, hamak, leżenie nad wodą. _(źródło: galeria)_
- **Narew zimą**: Chodzenie po zamarzniętej rzece i "zimowy obiad", czyli gryzienie tafli lodu ("Mmm, yummy!"). _(źródło: galeria)_
- **Wspólne czytanie**: Tata czyta dzieciom na dworze, leniwe dni na kanapie w domu. _(źródło: galeria)_
- **Zachody słońca**: Złota godzina nad wodą, osobny pokój w Galerii ("Sunsety"). _(źródło: galeria)_
- **Latanie dronem**: Tata z kontrolerem nad brzegiem, Avata w chmurach. _(źródło: galeria)_

## 8. Powiedzonka i słownik

- "Ośrodek daje, Ośrodek daje." (KS (tata)). Zasada nr 1, od "Bóg daje, Bóg zabiera". Od niej nazwa gry Ośrodek Daje. _(źródło: notatki; pewne)_
- "Herbata nie wyklucza kawy." (Ciszewscy x Sukiennicy). Hasło pokoju Ciszewskich w Galerii. _(źródło: galeria; pewne)_
- "Tak to czasem w życiu bywa, pies się topi, ła..." (rodzinne powiedzonko). Tak podyktował Jurek, końcówka się urwała. Znane przysłowie brzmi: "Tak to czasem w życiu bywa: pies się topi, łańcuch pływa". Pełne brzmienie do potwierdzenia. _(źródło: jurek-2026-11-10; niepewne)_
- "Serce Gzowa - Narew!" (Jurek). Podpis pokoju "Nasza Narew". _(źródło: galeria; pewne)_
- "Ogień + Gzowo to niepokonane combo!" (Jurek). Podpis pokoju "Fire". _(źródło: galeria; pewne)_
- "Pan Senek musi poczekać." (Jurek). Tytuł pokoju z nocnymi, cichymi momentami. _(źródło: galeria; pewne)_
- "Piwko, Narew, wspólny czas. Czego by tu chcieć więcej!" (Jurek). Podpis zdjęcia "Letni odpoczynek". _(źródło: galeria; pewne)_
- "Gzowo Jest Najlepsze <3" (Jurek). Napis kredą, który maskotka Narek ma pisać na ścianie domu. _(źródło: notatki; pewne)_
- "Mmm, yummy!" (Jurek). O jedzeniu lodu z Narwi. _(źródło: galeria; pewne)_

- **Ośrodek**: Działka Gzowo 34, bo to dawny ośrodek FSO (wędkarski i wypoczynkowy).
- **KS**: Kierownik Ośrodka, czyli tata.
- **Gzowiański**: Przymiotnik od Gzowa: Gzowiański somsiad, Gzowiańskie momenty, Gzowiańskie klasyki.
- **somsiad**: Sąsiad, żartobliwie.
- **Aminalsy**: Zwierzaki ("Nasi mali mieszkańcy Gzowa!").
- **Sunsety**: Zachody słońca nad Narwią.
- **Gzofajfus**: Nazwa serii rakiet Jurka (Gzofajfus Mini, Gzofajfus Classic) i jednej z walut na gzowo.fun (GZF).
- **kloc**: Dom, tak nazywa go gra Rysia.
- **GL Launch Site**: Miejsce startów rakiet (GL = Gzowo Labs).
- **szyszki**: Waluta na stronie gzowo.fun.
- **KALAKASANYT**: Dawny internetowy nick Jurka.
- **A1, 2B, 3C**: Nazwy trzech sal kinowych w Galerii Gzowo. Zawsze dokładnie tak, nigdy 1A.

## 9. Historie i wspomnienia

- **Burza z gradem**: Kiedyś nad Gzowem przeszła burza z gradem wielkości małych kostek lodu. Był wtedy w Gzowie Janek Kunstler. _(źródło: jurek-2026-11-10; pewne)_
- **Porwanie Dropsika**: Dropsik, młody i zabawny pies (bardziej Waldka niż Sukienników), został porwany niedługo po tym, jak się pojawił. _(źródło: jurek-2026-11-10; pewne)_
- **Skład pod skarpą**: Na górze działki, pod ziemią w skarpie, ma być stary skład bomb i broni. _(źródło: jurek-2026-11-10; niepewne)_
- **Niewypały i saperzy**: Gzowo leży na terenach powojennych. Na działce znajdowano niewypały i przyjeżdżali do nich saperzy. Jurek chce tego w grze jako motywu (niewypał i przyjazd saperów), nie jako postaci. _(źródło: jurek-2026-11-10; pewne)_
- **Helikopter nad Gzowem**: Szamborski czasem przylatuje do Gzowa helikopterem. Granatowy Airbus SP-MMM stał w 2022 na skarpie (pozował przy nim Waldek, pod spodem stała Kropka), a w lipcu 2023 wisiał nisko nad Narwią przy Cyplu. _(źródło: jurek-2026-11-10; pewne)_
- **Wycinka Majora**: Major, który na co dzień łowi ryby, robi na działce wycinki drzew. _(źródło: jurek-2026-11-10; pewne)_
- **Święta z kozą**: Na jedne święta Bożego Narodzenia rodzina przywiozła do Gzowa kozę z Warszawy. Dom był jeszcze surowy: kominek, choinka, bela siana i świąteczny stół ze świeczkami. _(źródło: jurek-2026-11-11; pewne)_
- **Czerwona postać na Cyplu**: Lipcowy zmierzch 2023: Zofia stoi w trawie nad Narwią, cała oświetlona na czerwono, i patrzy na wodę. _(źródło: jurek-2026-11-11; pewne)_
- **Dziesięć domków FSO**: Działka była ośrodkiem FSO z dziesięcioma domkami (na starej tablicy: Ośrodek Wędkarski w Gzowie). Zostały trzy, a nowy dom wziął kształt od dawnych łazienek. _(źródło: jurek-2026-11-10; pewne)_
- **Lot The Orange Beauty**: Start udany i najlepiej nagrany w całej flocie, ale spadochron się nie otworzył. _(źródło: gzowo.fun, obserwacja; pewne)_
- **Pierwszy spadochron**: Gzofajfus Classic Mk II: spadochron otworzył się już w pierwszym locie (21.03.2026). _(źródło: gzowo.fun; pewne)_
- **Mk IV po wielkim sukcesie**: Zdjęcie: rakieta Gzofajfus Classic Mk IV leży na trawie po locie, obok niebieski spadochron. _(źródło: galeria; pewne)_
- **Okładka Beatlesów**: Zielona rakieta taty stoi sama na środku szutrowej drogi pod wielkim niebem: "Idealna okładka dla nowego albumu Beatlesów". _(źródło: galeria; pewne)_
- **Ciężka droga do stacji Moya**: Rysio z Ignacym przedzierają się przez trawy wyższe od nich, żeby dojść do stacji. _(źródło: galeria; pewne)_
- **Zimowy obiad**: Jurek i Rysio jedzą tafle lodu wyłamane z Narwi. _(źródło: galeria; pewne)_
- **Malowanie światłem**: Tata rysuje w powietrzu świetlisty łuk przy ognisku, zdjęcie na długim czasie. _(źródło: galeria; pewne)_
- **Wielki obraz przed domkiem**: Maj 2025: ktoś w zielonej bluzie maluje na ziemi ogromne kolorowe płótno szczotką na kiju. Nie wiadomo jeszcze kto i po co. _(źródło: obserwacja; prawdopodobne)_

## 10. Rakiety

Gzowo Space Program (GSP) to rakiety modelarskie budowane ręcznie i drukowane w 3D, odpalane z pól pod Gzowem, z kamerami pokładowymi, spadochronami i czekaniem, aż ucichnie wiatr. Od listopada 2026 GSP jest scalone z Gzowo Labs. Zespół: Jerzy Sukiennik (CEO), Jan Sukiennik (Founding Partner).

- **Architektoniczny wieżowiec** (tata, latała): Ciemnozielona, wydrukowana w 3D, ostre stateczniki, "architektoniczna budowa oraz wygląd". Starty 18-19.10.2025 z szutrowej drogi. _(źródło: galeria, obserwacja)_
- **Gzofajfus Mini Mk I** (Jurek, latała): Pierwsza rakieta serii Mini, miniaturowa platforma eksperymentalna o bardzo małej masie. Lot udany. _(źródło: gzowo.fun)_
- **Gzofajfus Classic Mk II** (Jurek, latała): Pierwsza pełnowymiarowa z serii Classic. Lot 21.03.2026, spadochron otworzył się za pierwszym razem. _(źródło: gzowo.fun)_
- **Gzofajfus Classic Mk III** (Jurek, latała): Silnik F35-4 TSP. W nosie ma komorę na AirTaga, żeby dało się ją znaleźć po lądowaniu. _(źródło: gzowo.fun)_
- **Gzofajfus Classic Mk IV** (Jurek, latała): Zdjęcie "po wielkim sukcesie": leży na trawie z niebieskim spadochronem. _(źródło: galeria)_
- **The Orange Beauty** (Jurek, latała): Jedyna taka we flocie: czerwono-pomarańczowy dół, czarny czubek. Najlepsze nagrania startu. Lot udany, spadochron się nie otworzył. Najpierw powstał jej render w Blenderze ("Pomarańczowa piękność"). _(źródło: gzowo.fun, galeria, obserwacja)_
- **TBH Mk I (The Black Hawks)** (Jurek, planowana): Pierwsza z całkiem czarnych rakiet. Jedyna misja: bezpiecznie wylądować na spadochronie. Silnik TSP F35-4. _(źródło: gzowo.fun)_
- **Gzofajfus 4** (Jurek, w budowie): Drukowana rakieta o średnicy 60 mm na silnik F41-5W, cała z PLA, projekt w OpenSCAD i OpenRocket. Wydrukowana sekcja nosa. _(źródło: notatki)_

## 11. Marki i logo

### Gzowo 34 (Ośrodek)

Sama działka. Jej logo to ośmiornica.

- Uwaga: Jest zdjęcie logo: biała ośmiornica z długimi, wygiętymi mackami na czarnym tle (media/photos/archiwum/2023-06-07_logo-gzowo-34.jpg). Czystego pliku wektorowego jeszcze nie ma.
- Media: https://dataset.gzowo.fun/media/photos/archiwum/2023-06-07_logo-gzowo-34.jpg

### Gzowo Labs

Marka i portfolio Jurka: rakiety, druk 3D, gry i software z AI, wszystko w jednym miejscu. Od listopada 2026 obejmuje też GSP. Strona: https://gzowo.fun

- Hasło: I build things that fly. And a few that don't crash.
- Podpis strony: Jerzy Sukiennik's Official Home Page ~ Gzowo 34, Poland ~ Est. 2025
- Strona: Strona gzowo.fun to pulpit Windows 98 nad żywą pikselową mapą działki. Budynki na mapie to działy: wyrzutnia = Rockets, warsztat = 3D Printing, Arcade = Games, Lab = Software and AI. Na mapie są też: znak Gzowo 34, skrzynka na listy (księga gości), ogródek do sadzenia, pomost do łowienia ryb, dwa kajaki na Narwi, hangar z flotą rakiet, nieskończony mur do malowania, pulpit startowy z licznikiem startów. Celowo w klimacie GeoCities 1998.
- Ekonomia na stronie: Waluta: szyszki. Dwie krypto-zabawki: Gzowium (GZM) i Gzofajfus (GZF), na "Gzowo Street".
- Płonący GIF: Stary tytuł strony: płonący napis GZOWO LABS (media/brand/gzowo-labs/strona/gzowo-labs-fire.gif). Dalej żyje na stronie i w zakończeniach rolek.
- Działy: Rockets ("Real ones. They really fly."); 3D Printing ("Things made of plastic and stubbornness."); Games ("Play in your browser. No download."); Software and AI ("Apps, experiments and models trained from scratch.")
- Logo "Wschód": Dwa splecione ogniwa (dwóch braci) wschodzą zza horyzontu. Pod linią ich odbicie w paskach, jak w Narwi. Linia niesie napis GZOWO LABS, pod nią podpis ROCKETS · GAMES · 3D PRINTS · AI.
- Kolory: Atrament #141414, Zapłon #FF6A13 (tylko prawe ogniwo), biel #FFFFFF
- Kroje: napis Unbounded Bold, podpis Space Mono Bold
- Wersje: poziome, poziome bez podpisu, pionowe, sam napis (na korpus rakiety), znak, mały znak (favicon). Każda w 4 wariantach: kolor, ciemne tło, czarne, białe. SVG i PNG.
- Zasady: Pole ochronne równe promieniowi ogniwa. Minimum: poziome 140 px albo 35 mm, znak od 32 px, mały znak od 16 px.
- Pliki: media/brand/gzowo-labs/svg/, png/, favicon/, naklejki/ (naklejki na korpus i statecznik rakiety), awatar/, filmy/ (animacje logo MP4)
- Najważniejsze pliki: https://dataset.gzowo.fun/media/brand/gzowo-labs/svg/gzowo-labs-poziome-kolor.svg , https://dataset.gzowo.fun/media/brand/gzowo-labs/svg/gzowo-labs-znak-kolor.svg , https://dataset.gzowo.fun/media/brand/gzowo-labs/png/gzowo-labs-poziome-kolor.png

### GSP, Gzowo Space Program

Rakietowa marka Jurka i taty, założona w 2025. Od listopada 2026 scalona z Gzowo Labs. Styl: czarne tło, kroje Bebas Neue, Space Mono i DM Sans, kosmiczny brutalistyczny minimalizm. Strona: https://gspaerospace.pl

- Pliki: media/brand/gsp/ (logo PNG, gify, zakończenia filmów, awatary)

### Gzowo Industries

Strona sprzętowa Gzowo Labs: inteligentne okulary Gzowo Glass i drukowany pies-robot Smendiłendi.


### Narew Labs

Parasol nad własnymi modelami AI Jurka z rodziny G (G-Micro, G-Mini i kolejne). Maskotka: Narek.


### Gzowo TV

Własny system telewizyjny Jurka dla domu w Gzowie (MacBook przy telewizorze, iPhone jako pilot).


### KALAKASANYT

Dawny nick Jurka z czasów nagrywania filmików z kamerką (ramka "Kalakasan yt").


### Projekty Gzowo Labs (65)

- **Apogee** (Web app, 2026, live): A Mac browser that blocks every ad, cleans up YouTube and answers your questions on a drawn board. apogee.gzowo.fun
- **Wire Choir** (Experiment, 2026, live): Type a line and glowing heads sing it, every tongue and jaw movement driven by a real model of the human throat. choir.gzowo.fun
- **Gzowo StarNet** (Web app, 2026, live): Every project on this site hangs in one net. Pick what you like and everything that does not fit drops out. starnet.gzowo.fun
- **Beam** (Game, 2026, live): Projection mapping as a game: trace the frames and shelves on your wall, then run and jump across them in neon. beam.gzowo.fun
- **Odd Herd** (Game, 2026, building): A pixel art co-op platformer for 1 to 4 players online: pick one of ten animals and get the whole herd through the door. odd-herd.gzowo.fun
- **Ghostbusters** (Game, 2026, live): Suit up at the Ecto-1 with up to three friends, blast a greedy ghost, wrangle it together and drag it into a trap. ghostbusters.gzowo.fun
- **Instalator** (Game, 2026, live): Kit out real houses with real smart home gear: the TV shows a dollhouse, your phones are the tools. instalator.gzowo.fun
- **Rybna Wyspa** (Game, 2026, live): Build a fish farm with friends on a small island in the Narew: pumps, belts, flumes, machines and a riverside fish fry. rybna-wyspa.gzowo.fun
- **Stillvale** (Game, 2026, live): A quiet walk through an alpine valley: tall grass, a still lake and birdsong. Keep an eye on the timer. stillvale.gzowo.fun
- **Robotea** (Game, 2026, live): Your webcam turns your hands into a robot's hands: high-five another robot, or make finger guns and hit the range. robotea.gzowo.fun
- **Ghostframe** (Experiment, 2026, live): Pose see-through ghosts of Tesla Optimus around a stage and watch it walk and jump through every in-between frame. ghostframe.gzowo.fun
- **Rug Rush** (Game, 2026, live): Unload rug trucks, read the care labels and wash every rug in a co-op warehouse without ruining the silk. rugs.gzowo.fun
- **Fabrics** (Experiment, 2026, live): Pull curtains, fly flags, drape robes and scrunch rugs, then cut, burn, dye and blow on real-time cloth. fabrics.gzowo.fun
- **Roadster Jump** (Game, 2026, live): Suction the Roadster up a giant curled ramp, hang from the ceiling, then kickflip off the lip on cold-gas jets. roadster-jump.gzowo.fun
- **Spillway** (Game, 2026, live): Draw gutters with a limited marker and pump your colour of water into its cup, alone or with up to three friends online. spillway.gzowo.fun
- **Mirage** (Game, 2026, live): Put on smart glasses, call drones down from orbit and project a dragon, a whale or outer space over Venice. mirage.gzowo.fun
- **Timeblock** (Experiment, 2026, live): Drop in a video and it turns into a block of time cast in sanded resin, where every frame is a slice. timeblock.gzowo.fun
- **Speak & Groove** (Experiment, 2026, live): Type a letter and a robot voice spells it through a big reverb, then a techno band joins in behind you. speak-groove.gzowo.fun
- **Toot Tube** (Game, 2026, live): Up to three animals hang on to one inflatable ring and steer it down a spiky river the only way they can: by farting. toot.gzowo.fun
- **Cutlery** (Game, 2026, live): Fork, Knife and Butter find their way back to the breakfast table, each one a tool the others need. cutlery.gzowo.fun
- **Kindling** (Game, 2026, live): Stick monsters crawl out of a cornfield. Cut them apart with a laser, jump the iron wall and feed the fire. kindling.gzowo.fun
- **Campfire** (Experiment, 2026, live): Sit by a campfire in a dark forest: stack logs, stir the embers, toast a marshmallow or put it all out. campfire.gzowo.fun
- **Cube Breakers** (Game, 2026, live): Shoot balls that bounce forever into a giant cube of blocks, together with everyone who is online. cubes.gzowo.fun
- **Roadster 88** (Game, 2026, live): Drive, boost and fly the 2026 Tesla Roadster on ten cold-gas thrusters, then hit 88 mph and jump through time. roadster.gzowo.fun
- **Wolisz?!** (Game, 2026, live): A 2D online sandbox where every would-you-rather question gives your avatar a power, and the powers pile up. wolisz.gzowo.fun
- **Make Your Own Game, I'm Lazy** (Game, 2026, live): Draw a tree, a hero and a gun, say what game you want, and an AI writes it around your drawings. make-your-own-game-im-lazy.gzowo.fun
- **Foamwalker** (Game, 2026, live): A hunched purple alien with a human face crawls through a foam-block maze. foamwalker.gzowo.fun
- **iPhone Duo** (Experiment, 2026, archive): A semi-realistic virtual clone of the iPhone Duo iphone-duo.gzowo.fun
- **Wordshader** (Game, 2026, live): Type a line of words and watch a glowing 3D blob and its soundtrack appear letter by letter, then export the loop as a video. wordshader.gzowo.fun
- **Timberline Express** (Game, 2026, building): Survive an endless mountain forest by turning a hand-pumped rail cart into a steam-powered, house-sized train. 
- **Haystack Inc.** (Game, 2026, building): Somewhere in a stack of a million straws there is one needle. Dig by hand, then build the machines that dig for you. 
- **Hello Miner** (Game, 2026, building): Program mining drones in a tiny Python-like language and automate a floating quarry together with friends in real time. hello-miner.gzowo.fun
- **Gzowo Glass** (Hardware, 2026, building): Home-built smart glasses with a see-through HUD and a voice assistant that talks back in Polish. 
- **Squish** (Game, 2026, live): A silent paper-white void full of squishies and fidget toys you can actually squeeze, crack and stretch. squish.gzowo.fun
- **Doodle Run** (Game, 2026, building): A 2D runner where you draw every single thing in it first, then rig your scribbles so they walk, flap and chase you. doodlerun.gzowo.fun
- **Smendilendi Bureau** (Game, 2026, building): Run a tiny architecture practice with your friends, draw the walls, take the client's notes, then walk the finished building thirty years later. https://bureau.gzowo.fun/
- **Mark Zero** (Game, 2026, building): Fly a powered armor suit at the speed of sound, six degrees of freedom, no rails, no limits. https://markzero.gzowo.fun/
- **Noclip** (Game, 2026, live): A found-footage Backrooms experience, you fall in, something tall follows, and the tape keeps rolling. https://noclip.gzowo.fun/
- **Voidworks** (Game, 2026, live): A factory hanging in white nothing. Droppers, belts, upgraders, and a hard cap on how much can be moving at once. https://voidworks.gzowo.fun/
- **Ducks** (Game, 2026, live): Feed rubber ducks to a hungry pit, then build the machines that do it for you. https://ducks.gzowo.fun/
- **G-Doodle** (AI model, 2026, live): A transformer that draws. Type what you want in Polish and it sketches it stroke by stroke. ai.gzowo.fun
- **Hollowtree** (Game, 2026, live): One to three players, each of them a queen bee, sharing one hive inside a hollow tree. https://hollowtree.gzowo.fun/
- **Narew Labs** (Web app, 2026, live): Chat with a language model trained from scratch, running on a MacBook, reached from anywhere. https://g-micro-web.web.app/
- **SKI Together** (Game, 2026, live): A day at a ski resort for two to five people, on snow that remembers every turn you carved. https://ski.gzowo.fun/
- **Smendiłendi** (Hardware, 2026, building): A printed robot dog on four servos and an ESP32, the first project here whose output is a physical object. 
- **Gzowo Builders** (Game, 2026, live): Build a vehicle out of blocks, wheels and pistons, then drive it until something snaps off. https://jerzysukiennik.github.io/gzowo-builders/
- **G-Mini** (AI model, 2026, building): The second rung of the ladder: 178 million parameters, warm-started from G-Micro, trained in one week of free GPU time. 
- **Gzowo TV** (Experiment, 2026, building): An Apple TV for the family plot, every streaming service in one launcher, on a Mac plugged into the television. 
- **Airwave** (Experiment, 2026, live): An instrument you play with your hands in the air, in front of a webcam. No hardware. https://jerzysukiennik.github.io/airwave/
- **Voxel Demolition** (Game, 2026, building): A destruction sandbox with twenty-five tools and co-op for four. Runs on a server at home. 
- **G-Images** (AI model, 2026, building): A diffusion model for editing photos, trained from scratch, small enough to run on a laptop. 
- **G-Micro** (AI model, 2026, building): A 117-million-parameter language model in Polish, trained from scratch, tokenizer, corpus and training loop included. 
- **MJJ Archives** (Game, 2026, live): Watch Billie Jean at Motown 25 rebuilt in 3D, together, with the television cuts replayed shot for shot. https://jerzysukiennik.github.io/mjj-archives/
- **Untitled Civ Game** (Game, 2026, building): One to three gods share a single city and take down a rival built by the machine. 
- **Gargantua** (Game, 2026, live): Co-op zero-gravity spacewalk next to a black hole. Push off carefully; there is no brake. https://jerzysukiennik.github.io/Gargantua/
- **Cruise Control** (Game, 2026, live): A precision driving game with retro pixel post-processing, moving hazards and a shop. https://jerzysukiennik.github.io/cruise-control/
- **Untitled Pogo Game** (Game, 2026, live): Fifteen levels of pogo-stick parkour, playable together, installable as an app. https://untitled-pogo-game.web.app/
- **Backrooms** (Game, 2026, live): Yellow rooms, buzzing lights, and a maze that does not care whether you get out. https://jerzysukiennik.github.io/backrooms-labirynth/
- **Gzowo AI** (Web app, 2026, live): A voice assistant for the house in Gzowo, speak to it in Polish and it answers in real time. https://gzowoai.gzowo.fun/
- **GSP Brand Kit** (Experiment, 2026, building): The visual identity behind GSP, logo, colours and type, in one page you can download from. 
- **Gzowo Bowling** (Game, 2026, live): Bowling on a laptop, thrown with a phone. Scan the code and your phone becomes the ball. https://jerzysukiennik.github.io/gzowo-bowling/
- **Modular** (Game, 2026, live): Drop sixteen kinds of building on a plot and watch a town assemble itself around them. https://jerzysukiennik.github.io/modular/
- **Galeria Gzowo** (Web app, 2026, live): A gallery for the place the rest of this site is named after. https://galeria-gzowo.netlify.app/
- **Narew** (Game, 2026, live): One real property by the Narew: paddle it, dig it, ride a jet ski through it, or watch TV indoors. https://rysiosukiennik.github.io/backrooms-game/narew.html
- **Spider-Man: New York** (Game, 2026, building): None 

## 12. Gry i projekty osadzone w Gzowie

- **NAREW, posesja nad jeziorem** (Rysio): Spacer 3D po działce: kopanie łopatą i koparką, Tesla, kajaki, skuter wodny, telewizor z własnym Narewflixem, szopy tańczące przy ognisku, wiewiórki do głaskania, tata wystrzeliwujący gracza z Narwi. https://rysiosukiennik.github.io/backrooms-game/narew.html
- **Galeria Gzowo** (Jurek): Galeria 3D zdjęć z działki, prezent na Dzień Ojca 2026. Pokoje tematyczne, kino z salami A1, 2B i 3C, ukryty Żabi raj. https://galeria-gzowo.netlify.app
- **Ośrodek Daje** (Jurek): Kanapowy co-op: dziury w ziemi sterowane telefonami połykają senny ośrodek nad Narwią. Postacie: KS, Jurek, Ryś, Dropsik. Poziomy: Piknik, Ognisko, Pomost. https://osrodek-daje.gzowo.fun
- **Rybna Wyspa** (Jurek): Farma ryb z Narwi na małej wyspie. Sekretne gatunki: Rakieta GSP, Ognista, Wydrukowana, G-Micro, Złoty Sum z Gzowa, Potwór z Narwi. https://rybna-wyspa.gzowo.fun
- **Gzowo Meadow** (Jurek): Wierna rekonstrukcja prawdziwego Gzowa 1 x 1 km z prawdziwą pogodą, słońcem i gwiazdami. Stąd pochodzą dane terenu w tym datasecie. 
- **Gzowo ASCII** (Jurek): Spacer po prawdziwym Gzowie narysowanym znakami ASCII. https://gzowo-ascii.gzowo.fun
- **gzowo.fun** (Jurek): Pikselowa mapa działki z życiem: łowienie ryb z pomostu, kajaki, ogródek, starty rakiety, zimą łyżwy na Narwi. https://gzowo.fun
- **Instalator** (Jurek): Gra dla taty o zakładaniu smart home. Jeden z czterech budynków to domek w Gzowie nad Narwią. https://instalator.gzowo.fun

## 13. Zdjęcia

Pokoje Galerii Gzowo to gotowy podział tematyczny wspomnień. Puste pokoje (Heli, Taras, The New Era) czekają na zdjęcia.

Pokoje Galerii: The Early Days ("Gdzie wszystko się zaczęło"); Ciszewscy x Sukiennicy ("Herbata nie wyklucza kawy"); Nasza Narew ("Serce Gzowa - Narew!"); Zima ("Mróz, lód i śnieg oraz zimowe przygody!"); Aminalsy ("Nasi mali mieszkańcy Gzowa!"); Black n' White ("Kolekcja Gzowiańskich czarno-białych klasyków"); Sunsety ("Złota godzina nad wodą - ciepłe światło na koniec dnia."); Gzowo Space Program ("Drony, rakiety i postęp technologiczny Gzowa"); Fire ("Ogień + Gzowo to niepokonane combo!"); Pan Senek musi poczekać ("Wszystkie ciche Gzowiańskie momenty"); Ottonowie ("Wierni członkowie Gzowa"); Wiosna! ("Wiosenne!"); Heli ("Wkrótce"); Taras ("Wkrótce"); The New Era ("Wkrótce"); Hol ("Hol kinowy - Polecam popcorn!"); Sala A1 ("Gzowo Space Program History — wielki ekran i rakiety w locie. Usiądź (G), kliknij ekran i oglądaj."); Sala 2B ("The Early Days of Gzowo — usiądź (G), kliknij ekran i oglądaj."); Sala 3C ("Wkrótce — nowy seans w przygotowaniu. Usiądź (G) i zaczekaj."); Żabi raj ("Nasze małe zoo")

### archiwum

Zdjęcia dosłane przez Jurka 11.11.2026. Tytuł, opis, kto i gdzie wpisał Jurek, data i GPS pochodzą z pliku.

- **Mapa geodezyjna działki**. "Papierowa mapa geodezyjna z działkami, budynkami i drogami, rozłożona na stole, z czerwonymi pieczątkami w rogu. Zdjęcie zrobione w Warszawie, miesiąc przed tym, jak działka była Sukienników." Gdzie: Warszawa. Data: 2021-05-17. GPS z pliku: 46 km od Gzowa. Plik: https://dataset.gzowo.fun/media/photos/archiwum/2021-05-17_mapa-geodezyjna-dzialki.jpg
- **Domek nr 1**. "Ciemny drewniany domek z czerwonymi drzwiami i oknem w czerwonej ramie, na betonowych bloczkach, pod sosnami. Na ścianie biała tabliczka z napisem OŚRODEK WYPOCZYNKOWY. W tle po lewej siedzi Rysio Sukiennik. Domek nr. 1" Kto: Rysio. Gdzie: Domki. Data: 2021-06-13. GPS z pliku: Gzowo 34. Plik: https://dataset.gzowo.fun/media/photos/archiwum/2021-06-13_domek-nr-1.jpg
- **Stara tablica ośrodka FSO**. "Stara, czerwona, pordzewiała blaszana tablica z białym napisem: FABRYKA SAMOCHODÓW OSOBOWYCH, OŚRODEK WĘDKARSKI W GZOWIE. Zdjęcie zrobione poza Gzowem (GPS z okolic Warszawy)." Gdzie: Dom. Data: 2021-10-23. GPS z pliku: 47 km od Gzowa. Plik: https://dataset.gzowo.fun/media/photos/archiwum/2021-10-23_stara-tablica-osrodka-fso.jpg
- **Waldek pozuje z helikopterem**. "Granatowy helikopter Airbus z rejestracją SP-MMM stoi na trawie pod drzewami. Waldek w żółtej czapce i zielonej wzorzystej marynarce pozuje z nogą na płozie, pod helikopterem stoi pies Kropka." Kto: Waldek, Kropka. Gdzie: Skarpa. Data: 2022-09-06. GPS z pliku: Gzowo 34. Plik: https://dataset.gzowo.fun/media/photos/archiwum/2022-09-06_waldek-pozuje-z-helikopterem.jpg
- **Logo Gzowo 34**. "Biała ośmiornica z długimi, wygiętymi mackami na czarnym tle, czarno-białe zdjęcie. Logo Gzowo 34" Gdzie: Dom. Data: 2023-06-07. GPS z pliku: 46 km od Gzowa. Plik: https://dataset.gzowo.fun/media/photos/archiwum/2023-06-07_logo-gzowo-34.jpg
- **Jan Sukiennik z kozą nad Narwią**. "Ilustracja w malarskim stylu: Jan Sukiennik w białym kudłatym futrze i czarnej czapce stoi tyłem nad zamgloną rzeką o złotym świcie i trzyma na smyczy brązowo-białą kozę z czerwoną obrożą. Na trawie jesienne liście." Kto: Tata, Koza. Gdzie: Cypel. Plik: https://dataset.gzowo.fun/media/photos/archiwum/bez-daty_jan-sukiennik-z-koza-nad-narwia.jpg

### galeria

Zdjęcia z Galerii Gzowo. Tytuły, podpisy, kto i gdzie pochodzą od Jurka (czerwiec 2026). Daty zdjęć z iPhone'a nie zachowały się.

- **Architektoniczny wieżowiec**. "Rakieta z architektoniczną budową oraz wyglądem" Kto: Rakieta Taty. Gdzie: Gzowo 34, Polska. Data: 2025-10-19. Pokoje: aerospace. Widać: Dłoń trzyma ciemnozieloną rakietę wydrukowaną w 3D, z ostrymi statecznikami. W tle drzewa, piaszczysta ziemia i woda. Plik: https://dataset.gzowo.fun/media/photos/galeria/IMG-20251019-WA0000_architektoniczny-wiezowiec.jpg
- **Architektoniczny wieżowiec gotów do startu**. "Gotów do startu w 100%. Idealna okładka dla nowego albumu Beatlesów" Kto: Rakieta Taty. Gdzie: Okolice GSP Launch Site. Data: 2025-10-19. Pokoje: aerospace. Widać: Mała zielona rakieta stoi sama na środku szerokiej szutrowej drogi, nad nią wielkie niebieskie niebo z chmurami. Plik: https://dataset.gzowo.fun/media/photos/galeria/IMG-20251019-WA0001_architektoniczny-wiezowiec-gotow-do-startu.jpg
- **Architektoniczny wieżowiec gotów do startu V2**. "Gotów do startu w 100%" Kto: Jerzy Sukiennik oraz Rakieta Taty. Gdzie: Okolice GSP Launch Site. Data: 2025-10-19. Pokoje: aerospace. Widać: Jurek w czerwonej kurtce i żółtej czapce kuca na szutrowej drodze i ustawia zieloną rakietę do startu. Plik: https://dataset.gzowo.fun/media/photos/galeria/IMG-20251019-WA0003_architektoniczny-wiezowiec-gotow-do-startu-v2.jpg
- **Render rakiety "The Orange Beauty" w Blenderze**. "Pomarańczowa piękność" Kto: Rakieta Jurka. Gdzie: Blender. Data: 2025-11-26. Pokoje: aerospace. Widać: Render z Blendera: rakieta The Orange Beauty leci ukośnie na czarnym tle, za nią jasna poświata. Plik: https://dataset.gzowo.fun/media/photos/galeria/IMG-20251126-WA00021_render-rakiety-the-orange-beauty-w-blenderze.jpg
- **"The Orange Beauty" w pełnej okazałości**. "Zdjęcie 0,5x rakiety "The Orange Beauty"" Kto: Rakieta Jurka. Gdzie: GSP Launch Site. Data: 2025-11-29. Pokoje: aerospace. Widać: Ujęcie od dołu, szerokim kątem: czerwone stateczniki i czarny czubek rakiety The Orange Beauty na tle szarego nieba. Plik: https://dataset.gzowo.fun/media/photos/galeria/IMG-20251129-WA0001_the-orange-beauty-w-pelnej-okazalosci.jpg
- **Rakieta Gzofajfus Classic Mk IV po wielkim sukcesie**. "Rakieta Gzofajfus Classic Mk IV po wielkim sukcesie leży na ziemi." Kto: Rakieta Jurka. Gdzie: GSP Launch Site. Pokoje: aerospace. Widać: Rakieta leży na trawie po lądowaniu, obok niebieski spadochron na zielonych linkach. Płaska łąka, niskie słońce. Plik: https://dataset.gzowo.fun/media/photos/galeria/IMG_3054_rakieta-gzofajfus-classic-mk-iv-po-wielkim-sukce.jpg
- **Pilot Jan**. "Z kontrolerem w ręce w naturze" Kto: Jan Sukiennik (tata). Gdzie: Narew - Gzowo 34, Polska. Pokoje: aerospace. Widać: Tata stoi na trawiastym brzegu z kontrolerem drona w rękach i goglami na czole. Za nim szeroka, gładka Narew i drzewa na drugim brzegu. Plik: https://dataset.gzowo.fun/media/photos/galeria/IMG_4297_pilot-jan.jpg
- **Dron w chmurach**. "Lecąca AVATA" Kto: DJI Avata. Gdzie: Gzowo 34, Polska. Pokoje: aerospace. Widać: Mały dron w locie na tle nieba pokrytego drobnymi chmurami. Plik: https://dataset.gzowo.fun/media/photos/galeria/IMG_4299_dron-w-chmurach.jpg
- **Beethoven&Jurek**. "Beethoven nie boi się Jurka (podejrzane)" Kto: Kot Beethoven oraz Jerzy Sukiennik. Gdzie: Plaża Gzowo 34, Polska. Pokoje: aminals. Widać: Jurek stoi przed czerwonym VW Polo i białym busem, przed nim na trawie siedzi biały kot Beethoven. Plik: https://dataset.gzowo.fun/media/photos/galeria/IMG_2872_beethoven-jurek.jpg
- **Jurek z Dropsikiem**. "Letnie przytulanie psa" Kto: Śp. Dropsik oraz Jerzy Sukiennik. Gdzie: Gzowo 34, Polska. Pokoje: aminals, the-early-days. Widać: Jurek w kolorowej zimowej czapce leży na macie i przytula leżącego psa o czarno-brązowej sierści. W tle żółty kontener i stoliki z krzesłami pod sosnami. Plik: https://dataset.gzowo.fun/media/photos/galeria/IMG_3748_jurek-z-dropsikiem.jpg
- **Kontemplujący Beethoven**. "Beethoven wita słońce" Kto: Kot Beethoven. Gdzie: Narew - Gzowo 34, Polska. Pokoje: aminals, sunset. Widać: Biały kot siedzi tyłem na trawie i patrzy na słońce wiszące nisko nad zamgloną Narwią. Plik: https://dataset.gzowo.fun/media/photos/galeria/IMG_4288_kontemplujacy-beethoven.jpg
- **Rysio Na desce SUP**. "Rysio na SUPie świetnie się bawi!" Kto: Ryszard Sukiennik. Gdzie: Narew - Gzowo, Polska. Pokoje: black-n-white, narew. Widać: Czarno-białe. Rysio w kapoku i czapce z daszkiem siedzi na desce SUP z wiosłem w rękach, uśmiechnięty. Plik: https://dataset.gzowo.fun/media/photos/galeria/IMG_1997_rysio-na-desce-sup.jpg
- **Rysio lubi Old School**. "Rysio w okularach" Kto: Ryszard Sukiennik. Gdzie: Gzowo 34, Polska. Pokoje: black-n-white, the-early-days. Widać: Czarno-białe. Mały Rysio bez koszulki, w okrągłych okularach przeciwsłonecznych, stoi na trawie. Plik: https://dataset.gzowo.fun/media/photos/galeria/IMG_2487_rysio-lubi-old-school.jpg
- **Nad wodą**. "Kopanie w piasku i łabędź na jeziorze." Kto: Ryszard, Jerzy oraz Jan. Gdzie: Narew - Gzowo 34, Polska. Pokoje: black-n-white, narew, the-early-days. Widać: Czarno-białe, z góry. Na piaszczystym brzegu dzieci i dorosły kopią w piasku, obok wiaderka. Po wodzie tuż przy brzegu płynie łabędź. Plik: https://dataset.gzowo.fun/media/photos/galeria/IMG_2850_nad-woda.jpg
- **Clu na hamaku**. "Odpoczynek wśród sosen." Kto: Ola Kluzek. Gdzie: Gzowo 34, Polska. Pokoje: ciszewscy. Widać: Ola "Clu" w okularach leży w hamaku rozwieszonym między sosnami, w tle prześwituje woda. Plik: https://dataset.gzowo.fun/media/photos/galeria/IMG_1458_clu-na-hamaku.jpg
- **Modlitwa przy drzewie**. Kto: Ignacy oraz Helena. Gdzie: Gzowo, Polska. Pokoje: ciszewscy. Widać: Dwoje dzieci stoi przy asfaltowej ścieżce pod bezlistnym drzewem ogrodzonym białym płotkiem z kolorowymi chorągiewkami. Plik: https://dataset.gzowo.fun/media/photos/galeria/IMG_3765_modlitwa-przy-drzewie.jpg
- **Letnia lektura**. "Wspólne letnie czytanie" Kto: Jerzy, Ignacy, Ryszard oraz Jan. Gdzie: Gzowo 34, Polska. Pokoje: ciszewscy, the-early-days. Widać: Tata w czapce z daszkiem i okularach czyta dużą książkę z obrazkami trzem chłopcom, którzy się do niego tulą. W tle piasek i skarpa. Plik: https://dataset.gzowo.fun/media/photos/galeria/IMG_3771_letnia-lektura.jpg
- **Ciężka droga do stacji Moya**. "Przedzieranie się przez trawy" Kto: Ryszard oraz Ignacy. Gdzie: Okolice stacji Moya w Gzowie. Pokoje: ciszewscy. Widać: Dwoje dzieci brodzi przez zielone zboże wyższe od nich, jedno w różowej czapce z daszkiem. W tle dom z ciemnym dachem i błękitne niebo. Plik: https://dataset.gzowo.fun/media/photos/galeria/IMG_4503_ciezka-droga-do-stacji-moya.jpg
- **Wspólny czas**. "Wspólny czas na fotelu" Kto: Jerzy, Ryszard, Ignacy oraz Jan. Gdzie: Gzowo 34, Polska. Pokoje: ciszewscy, the-early-days. Widać: Tata w czapce i okularach siedzi z trójką chłopców na szerokim pasiastym fotelu pod wiatą. Obok ułożone drewno na opał, na piasku buty. Plik: https://dataset.gzowo.fun/media/photos/galeria/IMG_8205_wspolny-czas.jpg
- **Zimowe chodzenie po lodzie**. "Zimowy spacer po zamarzniętej Narwi" Kto: Helena. Gdzie: Narew - Gzowo 34, Polska. Pokoje: ciszewscy, zima. Widać: Dziecko w zimowym ubraniu stoi z rozłożonymi rękami na zamarzniętej Narwi. Na pierwszym planie popękana kra, w tle linia drzew. Plik: https://dataset.gzowo.fun/media/photos/galeria/IMG_8213_zimowe-chodzenie-po-lodzie.jpg
- **Malowanie Światłem**. "Malowanie Światłem przy ognisku" Kto: Jan Sukiennik (tata). Gdzie: Narew - Gzowo 34, Polska. Pokoje: fire. Widać: Noc, długi czas naświetlania. Postać stoi w trawie, a nad nią świeci pomarańczowy łuk namalowany światłem. Granatowo-fioletowe niebo. Plik: https://dataset.gzowo.fun/media/photos/galeria/IMG_3663_malowanie-swiatlem.jpg
- **Luna**. "Cicha noc i samotny księżyc." Kto: Luna. Gdzie: Okolice Gzowa. Pokoje: midnight. Widać: Prawie czarny kadr: mały księżyc na niebie i fragment drogi oświetlony reflektorami. Plik: https://dataset.gzowo.fun/media/photos/galeria/IMG_8933_luna.jpg
- **Motorówka&Rysio**. "Rysio łapie wiatr na motorówce" Kto: Ryszard Sukiennik. Gdzie: Narew - Gzowo 34, Polska. Pokoje: narew. Widać: Ujęcie z góry. Rysio w kapeluszu wychyla się z szarej motorówki przy brzegu, w wodzie odbijają się chmury i drzewa. Plik: https://dataset.gzowo.fun/media/photos/galeria/IMG_2110_motorowka-rysio.jpg
- **Letni odpoczynek**. "Piwko, Narew, wspólny czas - Czego by tu chcieć więcej!" Kto: Jan Sukiennik oraz śp. Gzowiański somsiad. Gdzie: Narew - Gzowo 34, Polska. Pokoje: narew, the-early-days. Widać: Dwóch mężczyzn siedzi na krzesłach na piaszczystym brzegu pod zielenią, obaj na luzie, boso. Plik: https://dataset.gzowo.fun/media/photos/galeria/IMG_2387_letni-odpoczynek.jpg
- **Razem o zachodzie**. "Przytuleni nad wodą w złotym świetle." Kto: Czupryńscy. Gdzie: Narew - Gzowo 34, Polska. Pokoje: sunset. Widać: Para stoi tyłem, przytulona, na brzegu i patrzy na zachód słońca nad szeroką wodą. Plik: https://dataset.gzowo.fun/media/photos/galeria/IMG_7545_razem-o-zachodzie.jpg
- **Słońce nad polem**. "Jurek doświadcza zachodu słońca" Kto: Jerzy Sukiennik. Gdzie: Okolice domu Waldka. Pokoje: sunset. Widać: Zachód słońca nad ciemnym, płaskim polem. Słońce nisko, częściowo za chmurami. Plik: https://dataset.gzowo.fun/media/photos/galeria/IMG_9197_slonce-nad-polem.jpg
- **Krowi chłopiec**. "Wspólny odpoczynek na podwórku (Alligator included)" Kto: Jerzy, Ryszard oraz Jan. Gdzie: Gzowo 34, Polska. Pokoje: the-early-days. Widać: Tata w czerwonej czapce z daszkiem i kowbojskich butach siedzi na krześle pod wiatą z tabletem, po bokach Jurek i Rysio. Na pierwszym planie pasiasty fotel. Plik: https://dataset.gzowo.fun/media/photos/galeria/IMG_2802_krowi-chlopiec.jpg
- **Czytanie w Domu**. "Leniwy dzień na kanapie" Kto: Jerzy Sukiennik oraz Ryszard Sukiennik. Gdzie: Gzowo 34, Polska. Pokoje: the-early-days. Widać: Wnętrze domu w trakcie wykańczania: czarna sofa na tle szklanej ściany, leżą na niej dwie osoby w kurtkach, podłoga pod folią. Za szybą sosny i Narew. Plik: https://dataset.gzowo.fun/media/photos/galeria/IMG_7131_czytanie-w-domu.jpg
- **Praca nad tarasem**. "Konsultacja tarasu" Kto: Jan Sukiennik oraz Pracownik. Gdzie: Gzowo 34, Polska. Pokoje: the-early-days. Widać: Dwóch mężczyzn rozmawia na jasnym piasku budowy pod sosnami, obok ciemna bryła budynku i deski. Jeden w żółtej kurtce. Plik: https://dataset.gzowo.fun/media/photos/galeria/IMG_9191_praca-nad-tarasem.jpg
- **Dziadkowie**. "Portret w cieniu drzew." Kto: Waldemar oraz Bożena Ottonowie. Gdzie: Narew - Gzowo 34, Polska. Pokoje: waldek. Widać: Czarno-białe. Starsza para w ogrodzie w cieniu drzew: mężczyzna w koszuli w kratę siedzi na krześle, kobieta w jasnej sukience siedzi obok. Plik: https://dataset.gzowo.fun/media/photos/galeria/IMG_7546_dziadkowie.jpg
- **Klucz Ptaków**. "Ptaki wracające na wiosennym niebie." Kto: Ptaki!. Gdzie: Narew - Gzowo 34, Polska. Pokoje: wiosna. Widać: Klucz ptaków w kształcie litery V na szaroniebieskim wieczornym niebie. Plik: https://dataset.gzowo.fun/media/photos/galeria/IMG_8221_klucz-ptakow.jpg
- **Zimowy Obiad Jurka**. "Mmm, yummy!" Kto: Jerzy Sukiennik. Gdzie: Narew - Gzowo 34, Polska. Pokoje: zima. Widać: Jurek w czerwonej puchowej kurtce z kapturem gryzie dużą taflę lodu. W tle śnieg i trzciny. Plik: https://dataset.gzowo.fun/media/photos/galeria/IMG_6684_zimowy-obiad-jurka.jpg
- **Zimowy Obiad Rysia**. "Mmm, yummy!" Kto: Ryszard Sukiennik. Gdzie: Narew - Gzowo 34, Polska. Pokoje: zima. Widać: Rysio stoi na śniegu między drzewami i trzyma przed sobą wielką taflę lodu. Plik: https://dataset.gzowo.fun/media/photos/galeria/IMG_6746_zimowy-obiad-rysia.jpg
- **Strike a pose!**. "Mały Superman w świetle reflektorów!" Kto: Ryszard Sukiennik. Gdzie: Narew - Gzowo 34, Polska. Pokoje: zima. Widać: Zimowa noc. Rysio w niebieskiej kurtce stoi w rozkroku z rękami na biodrach na betonowej płycie przy wodzie, oświetlony mocnym reflektorem. Plik: https://dataset.gzowo.fun/media/photos/galeria/IMG_8094_strike-a-pose.jpg

### rakiety

Zdjęcia z folderu Rakietomania (WhatsApp, jesień 2025), których nie było w Galerii.

- **Rakieta na wyrzutni**. Data: 2025-11-02. Widać: Rakieta stoi na wyrzutni ze statywu i długiego pręta pośrodku płaskiej łąki, pochmurne niebo. Plik: https://dataset.gzowo.fun/media/photos/rakiety/IMG-20251102-WA0000.jpg
- **Druk rakiety**. Data: 2025-10-19. Widać: Drukarka 3D Bambu Lab w trakcie druku ciemnozielonej części rakiety. Plik: https://dataset.gzowo.fun/media/photos/rakiety/IMG-20251019-WA0002.jpg
- **Dwie rakiety na tle próbek**. Data: 2025-10-18. Widać: Dwie wydrukowane rakiety, ciemnozielona i jasnozielona, stoją na tle regału z próbkami materiałów. Plik: https://dataset.gzowo.fun/media/photos/rakiety/IMG-20251018-WA0001.jpg
- **Warsztat rakietowy**. Data: 2025-10-19. Widać: Biurko z perforowaną tablicą na ścianie: zielone rakiety i części w trakcie składania. Plik: https://dataset.gzowo.fun/media/photos/rakiety/IMG-20251019-WA0004.jpg

### plaza

Seria 23 zdjęć plaży z 08.08.2026, zrobiona przez Jurka jako dokumentacja miejsca do odwzorowania w 3D. Bez ludzi.

- Gdzie: Plaża Gzowo 34. Data: 2026-08-08. Widać: Gęste trzciny i zarośla przy brzegu, z boku słupek ogrodzenia. Plik: https://dataset.gzowo.fun/media/photos/plaza/IMG_1139.jpg
- Gdzie: Plaża Gzowo 34. Data: 2026-08-08. Widać: Trawiasty brzeg schodzący do wody, przy wodzie leży łódka dnem do góry. Plik: https://dataset.gzowo.fun/media/photos/plaza/IMG_1140.jpg
- Gdzie: Plaża Gzowo 34. Data: 2026-08-08. Widać: Skoszona trawa na stoku, krzewy, w tle łódka dnem do góry. Plik: https://dataset.gzowo.fun/media/photos/plaza/IMG_1141.jpg
- Gdzie: Plaża Gzowo 34. Data: 2026-08-08. Widać: Piaszczysta ścieżka w górę stoku, na górze zaparkowany srebrny minivan. Plik: https://dataset.gzowo.fun/media/photos/plaza/IMG_1142.jpg
- Gdzie: Plaża Gzowo 34. Data: 2026-08-08. Widać: Linia brzegu: płytka woda, pas piasku i wyrzucone trzciny. Plik: https://dataset.gzowo.fun/media/photos/plaza/IMG_1143.jpg
- Gdzie: Plaża Gzowo 34. Data: 2026-08-08. Widać: Beżowy kadłub łódki leży w wysokiej trawie. Plik: https://dataset.gzowo.fun/media/photos/plaza/IMG_1144.jpg
- Gdzie: Plaża Gzowo 34. Data: 2026-08-08. Widać: Trzciny w płytkiej wodzie, biała łódka przy brzegu, dalej szeroka Narew. Plik: https://dataset.gzowo.fun/media/photos/plaza/IMG_1145.jpg
- Gdzie: Plaża Gzowo 34. Data: 2026-08-08. Widać: Kępy trzcin w wodzie, niebieskie niebo, drugi brzeg daleko. Plik: https://dataset.gzowo.fun/media/photos/plaza/IMG_1146.jpg
- Gdzie: Plaża Gzowo 34. Data: 2026-08-08. Widać: Żółto-czarny skuter wodny zacumowany na linie w płytkiej wodzie. Plik: https://dataset.gzowo.fun/media/photos/plaza/IMG_1147.jpg
- Gdzie: Plaża Gzowo 34. Data: 2026-08-08. Widać: Skuter wodny z bliska, widać piaszczyste dno. Plik: https://dataset.gzowo.fun/media/photos/plaza/IMG_1148.jpg
- Gdzie: Plaża Gzowo 34. Data: 2026-08-08. Widać: Piaszczysto-trawiasty stok plaży w stronę wody, w tle łódki. Plik: https://dataset.gzowo.fun/media/photos/plaza/IMG_1149.jpg
- Gdzie: Plaża Gzowo 34. Data: 2026-08-08. Widać: Ten sam stok z innego miejsca, piasek z patykami na pierwszym planie. Plik: https://dataset.gzowo.fun/media/photos/plaza/IMG_1150.jpg
- Gdzie: Plaża Gzowo 34. Data: 2026-08-08. Widać: Stok plaży w cieniu drzew, na piasku ślady. Plik: https://dataset.gzowo.fun/media/photos/plaza/IMG_1151.jpg
- Gdzie: Plaża Gzowo 34. Data: 2026-08-08. Widać: Widok w górę stoku pod słońce, na górze auto. Plik: https://dataset.gzowo.fun/media/photos/plaza/IMG_1152.jpg
- Gdzie: Plaża Gzowo 34. Data: 2026-08-08. Widać: Trawa pocięta śladami kół, słupek, na górze auto. Plik: https://dataset.gzowo.fun/media/photos/plaza/IMG_1153.jpg
- Gdzie: Plaża Gzowo 34. Data: 2026-08-08. Widać: Trawiasty stok ze słupkiem, w tle auto i zarośla. Plik: https://dataset.gzowo.fun/media/photos/plaza/IMG_1154.jpg
- Gdzie: Plaża Gzowo 34. Data: 2026-08-08. Widać: Długi mur z gabionów (stalowe kosze z kamieniem) wzdłuż piaszczystej drogi. Plik: https://dataset.gzowo.fun/media/photos/plaza/IMG_1155.jpg
- Gdzie: Plaża Gzowo 34. Data: 2026-08-08. Widać: Narożnik gabionowego muru, przy nim żółte kwiaty i wysoka trawa. Plik: https://dataset.gzowo.fun/media/photos/plaza/IMG_1156.jpg
- Gdzie: Plaża Gzowo 34. Data: 2026-08-08. Widać: Zarośla i młode drzewa przy ścieżce. Plik: https://dataset.gzowo.fun/media/photos/plaza/IMG_1157.jpg
- Gdzie: Plaża Gzowo 34. Data: 2026-08-08. Widać: Piaszczysta droga ze śladami opon, kępy trawy. Plik: https://dataset.gzowo.fun/media/photos/plaza/IMG_1158.jpg
- Gdzie: Plaża Gzowo 34. Data: 2026-08-08. Widać: Droga dojazdowa między murem z gabionów a zielenią, latarnia. Plik: https://dataset.gzowo.fun/media/photos/plaza/IMG_1159.jpg
- Gdzie: Plaża Gzowo 34. Data: 2026-08-08. Widać: Ta sama droga, z prawej wystaje bok auta. Plik: https://dataset.gzowo.fun/media/photos/plaza/IMG_1160.jpg
- Gdzie: Plaża Gzowo 34. Data: 2026-08-08. Widać: Droga dojazdowa z latarnią i murem, ujęcie w stronę zarośli. Plik: https://dataset.gzowo.fun/media/photos/plaza/IMG_1161.jpg

## 14. Filmy

- **DANCE (Dropsik)** (zmontowany 2023-01-28, Gzowo 34, 37.5 s). Pionowy montaż z napisem DANCE. Chłopiec w czerwonym kombinezonie i zielonej czapce siedzi na liściach i bawi się z małym czarno-karmelowym szczeniakiem. Potem szczeniak na śniegu głaskany ręką, potem zabawa na trawie przy stercie kamieni, w tle wiata z autem i sosny. Na końcu czerwona kurtyna. W Galerii Gzowo grany w sali 2B jako "The Early Days of Gzowo". Jedyny film z Dropsikiem. Plik: https://dataset.gzowo.fun/media/wideo/dropsik_dance.mp4 Kadry: https://dataset.gzowo.fun/media/klatki/dropsik_dance/ (12 szt.)
- **Jurek i Rysio przed kamerką** (2020-11-30, Warszawa, 22.7 s). Nagranie z kamerki komputera. Dwóch małych chłopców, ciemnowłosy Jurek i blond Rysio w pasiastej bluzie, przepycha się do obiektywu i śmieje. Co mówią (transkrypcja automatyczna, poprawiona, przybliżona): "Nie wiem, czy uda się wysłać. Powiedz coś." "Hej, Tato!" "Teraz pa pa." "Pa pa." "Czekaj, bo trzymam komputer w ręce." Wiadomość wideo dla taty. Jeszcze sprzed Gzowa (działka od czerwca 2021). Jurek dał ją jako wspomnienie. Plik: https://dataset.gzowo.fun/media/wideo/kamerka_2020-11-30_jurek-i-rysio.mp4 Kadry: https://dataset.gzowo.fun/media/klatki/kamerka_2020-11-30_jurek-i-rysio/ (6 szt.)
- **KALAKASANYT ogląda 200 memes in 1 song** (2023-08-29, Warszawa, 87.4 s). Nagranie ekranu z OBS. W rogu okienko kamerki z Jurkiem, na ekranie YouTube z filmem "200 MEMES in 1 SONG" (pianista PACIL gra memiczne melodie). Jurek ogląda i reaguje. Co mówią (transkrypcja automatyczna, poprawiona, przybliżona): "Oglądamy gdzieś filmiki! Widzicie, już jestem profesjonalny!" [...] "Dobra, skończymy już na dzisiaj! Do widzenia!" Wspomnienie z czasów nicku KALAKASANYT. Obraz i dźwięk filmu z YouTube należą do jego autora. Plik: https://dataset.gzowo.fun/media/wideo/kalakasan_2023-08-29_200-memes.mp4 Kadry: https://dataset.gzowo.fun/media/klatki/kalakasan_2023-08-29_200-memes/ (6 szt.)
- **KALAKASANYT ogląda Ninjago** (nieznana, plik nazywał się "Jurek STRAREM", Warszawa, 418.6 s). Nagranie ekranu z OBS z zieloną ramką kamerki podpisaną "Kalakasan yt". Jurek w niebieskiej koszulce zapowiada transmisję i włącza odcinki LEGO Ninjago po polsku. Ogląda je z rodziną siedzącą w głębi pokoju, chwilami odchodzi od kamerki. W tle pokój z oknem i rośliną. Co mówią (transkrypcja automatyczna, poprawiona, przybliżona): "Siemano! Z tej strony Jurek Sukiennik. [...] Dziś będziemy oglądać Ninjago, pełne odcinki z drugiego sezonu po polsku. Będzie trwało to godzinę i trzy minuty. Jej, ale fajnie! I dziś tutaj jestem z rodziną. [...] My oglądamy z wami i komentujemy." Wspomnienie z czasów nicku KALAKASANYT. Odcinek Ninjago należy do LEGO. Plik: https://dataset.gzowo.fun/media/wideo/kalakasan_ninjago-stream.mp4 Kadry: https://dataset.gzowo.fun/media/klatki/kalakasan_ninjago-stream/ (12 szt.)
- **Dom z zewnątrz** (2026-07-28, Gzowo 34, 6.1 s). Kamera jedzie w bok po łące. Dom wsunięty w skarpę: na dole niska betonowa bryła z otwartym garażem, w którym stoi coś czerwonego, na niej przeszklony prostopadłościan. Dookoła stare sosny. Jedyne ujęcie domu z zewnątrz w datasecie (6 sekund). Plik: https://dataset.gzowo.fun/media/wideo/dom-z-zewnatrz_2026-07-28.mp4 Kadry: https://dataset.gzowo.fun/media/klatki/dom-z-zewnatrz_2026-07-28/ (4 szt.)
- **Dom w środku** (2026-07-28, Gzowo 34, 103.2 s). Jurek idzie z telefonem przez salon i kuchnię: ściana z OSB, marmurowa podłoga, sufit ze sklejki, wielkie okna na taras i sosny, kominek, pianino, telewizor, sofa, duży stół na limonkowych kozłach, stalowa kuchnia. Z tego filmu Jurek odtworzył wnętrze w 3D (projekt Gzowo House). Plik: https://dataset.gzowo.fun/media/wideo/dom-wnetrze_2026-07-28.mp4 Kadry: https://dataset.gzowo.fun/media/klatki/dom-wnetrze_2026-07-28/ (16 szt.)
- **Ściana domu** (2026-08-07, Gzowo 34, 16.9 s). Gładka, jasna, otynkowana ściana domu, u dołu czarna folia fundamentowa, trawa i piasek. Stoi przy niej pręt ze znacznikiem. Nagrane pod filmik, w którym maskotka Narek pisze kredą "Gzowo Jest Najlepsze <3". Plik: https://dataset.gzowo.fun/media/wideo/sciana-domu_2026-08-07.mp4 Kadry: https://dataset.gzowo.fun/media/klatki/sciana-domu_2026-08-07/ (5 szt.)
- **Plaża, przejście z kamerą** (2026-08-08, Plaża Gzowo 34, 30.7 s). Przejście po plaży: piaszczysta ścieżka do wody, zacumowany żółty skuter wodny, szeroka Narew pod niebem z chmurami, zarośla, łódki dnem do góry, na końcu drobna fala na piasku. Uzupełnia serię zdjęć plaży. Plik: https://dataset.gzowo.fun/media/wideo/plaza_2026-08-08.mp4 Kadry: https://dataset.gzowo.fun/media/klatki/plaza_2026-08-08/ (8 szt.)
- **Wielki obraz przed domkiem** (2025-05-25, Gzowo 34, 76.8 s). Na piaszczystym placu leży duże płótno w niebiesko-różowo-żółte plamy. Osoba w zielonej bluzie z kapturem maluje je szczotką na długim kiju, chodząc dookoła. W tle ciemny drewniany domek z czerwonymi drzwiami, szare skrzynie i drewno na opał. Leżał w folderze sali 3C Galerii Gzowo ("coming soon"). Widać jeden z trzech domków. Plik: https://dataset.gzowo.fun/media/wideo/sala-3c_2025-05-25.mp4 Kadry: https://dataset.gzowo.fun/media/klatki/sala-3c_2025-05-25/ (8 szt.)
- **Start rakiety z pola** (2025-10-19, GL Launch Site, 16.2 s). Ręka w czerwonej kurtce ustawia jasną rakietę na skraju zaoranego pola. Start z kłębem dymu, kamera gubi rakietę w chmurach. W Galerii: sala A1. Plik: https://dataset.gzowo.fun/media/wideo/rakieta_2025-10-19_start-z-daleka-pole.mp4 Kadry: https://dataset.gzowo.fun/media/klatki/rakieta_2025-10-19_start-z-daleka-pole/ (6 szt.)
- **Rakieta w locie** (2025-10-19, GL Launch Site, 15.8 s). Rakieta stoi na szutrowej drodze, startuje, kamera szuka jej na niebie, potem dym nad polem. W Galerii: sala A1. Plik: https://dataset.gzowo.fun/media/wideo/rakieta_2025-10-19_w-locie-niebo.mp4 Kadry: https://dataset.gzowo.fun/media/klatki/rakieta_2025-10-19_w-locie-niebo/ (6 szt.)
- **Lot i lądowanie na łące** (2025-10-19, GL Launch Site, 65.5 s). Rakieta jako mały punkt na błękitnym niebie, potem długa obserwacja łąki, nad którą unosi się dym.  Plik: https://dataset.gzowo.fun/media/wideo/rakieta_2025-10-19_WA0008.mp4 Kadry: https://dataset.gzowo.fun/media/klatki/rakieta_2025-10-19_WA0008/ (6 szt.)
- **Start i bieg po rakietę** (2025-10-19, GL Launch Site, 87.8 s). Start z zaoranego pola pod szarym niebem, smuga dymu w górę. Potem postać w czerwonej kurtce biegnie przez łąkę po rakietę.  Plik: https://dataset.gzowo.fun/media/wideo/rakieta_2025-10-19_WA0009.mp4 Kadry: https://dataset.gzowo.fun/media/klatki/rakieta_2025-10-19_WA0009/ (6 szt.)
- **Start z łąki o zmierzchu** (2025-11-01, GL Launch Site, 2.8 s). Trzy sekundy: kłąb dymu na łące i smuga w niebo o zmierzchu. W Galerii: sala A1. Plik: https://dataset.gzowo.fun/media/wideo/rakieta_2025-11-01_start-z-daleka-laka.mp4 Kadry: https://dataset.gzowo.fun/media/klatki/rakieta_2025-11-01_start-z-daleka-laka/ (6 szt.)
- **Zapłon z bliska** (2025-11-01, GL Launch Site, 8.5 s). Ujęcie od dołu: zielona rakieta na wyrzutni na tle chmur, iskry zapłonu i odlot.  Plik: https://dataset.gzowo.fun/media/wideo/rakieta_2025-11-01_WA0009.mp4 Kadry: https://dataset.gzowo.fun/media/klatki/rakieta_2025-11-01_WA0009/ (6 szt.)
- **The Orange Beauty na wyrzutni (Insta360)** (2025-11-29, GL Launch Site, 32.1 s). Czerwono-czarna rakieta na wyrzutni z bliska, zapłon, dym. Potem obraz 360 stopni z oszronioną łąką i wygiętą wyrzutnią. Nagrane kamerą Insta360. Plik: https://dataset.gzowo.fun/media/wideo/rakieta_2025-11-29_WA0002.mp4 Kadry: https://dataset.gzowo.fun/media/klatki/rakieta_2025-11-29_WA0002/ (6 szt.)
- **Start The Orange Beauty z daleka** (2025-11-29, GL Launch Site, 24.2 s). Rakieta startuje z oszronionej łąki, kamera śledzi smugę dymu w szarym niebie, na końcu pusta wyrzutnia. W Galerii: sala A1. Plik: https://dataset.gzowo.fun/media/wideo/rakieta_2025-11-29_start-z-daleka-2.mp4 Kadry: https://dataset.gzowo.fun/media/klatki/rakieta_2025-11-29_start-z-daleka-2/ (6 szt.)
- **Rysio nad wodą** (2021-07-10, Cypel, 12.9 s). Zachód słońca nad Narwią. Ciemna sylwetka dziecka stoi na brzegu wśród traw i rzuca coś do wody. GPS z pliku: Gzowo 34. Opisał Jurek. Plik: https://dataset.gzowo.fun/media/wideo/2021-07-10_rysio-nad-woda.mp4 Kadry: https://dataset.gzowo.fun/media/klatki/2021-07-10_rysio-nad-woda/ (4 szt.)
- **Czerwona postać nad Narwią** (2023-07-08, Cypel, 47.3 s). Zmierzch nad Narwią, niebo jeszcze pomarańczowe przy horyzoncie. W wysokiej trawie stoi tyłem postać w długim stroju, cała oświetlona na czerwono, i patrzy na wodę. Pod koniec filmu postaci już nie ma. GPS z pliku: Gzowo 34. Opisał Jurek. Plik: https://dataset.gzowo.fun/media/wideo/2023-07-08_czerwona-postac-nad-narwia.mp4 Kadry: https://dataset.gzowo.fun/media/klatki/2023-07-08_czerwona-postac-nad-narwia/ (9 szt.)
- **Helikopter nad Narwią** (2023-07-15, Cypel, 9.8 s). Granatowy helikopter wisi nisko nad Narwią tuż przy brzegu i marszczy wodę. Na skarpie stoi osoba w stroju kąpielowym i macha rękami, obok czerwone krzesła i turkusowy ręcznik, na pierwszym planie popiół z ogniska. GPS z pliku: Gzowo 34. Tytuł, kto i gdzie podał Jurek, opis kadru Claude. Plik: https://dataset.gzowo.fun/media/wideo/2023-07-15_helikopter-nad-narwia.mp4 Kadry: https://dataset.gzowo.fun/media/klatki/2023-07-15_helikopter-nad-narwia/ (4 szt.)
- **Święta w Gzowie z Kozami** (data nieznana, Dom, 40.0 s). Montaż pod muzykę z zimowego wieczoru w domu, jeszcze w surowym stanie (ściany z OSB i pustaków). Po kolei: pali się kominek-koza, na ścianie świeci niebieska ośmiokątna lampa, nad biurkiem wisi duży kolorowy obraz, przy nim stos drewna. Potem choinka z lampkami i paczkami, chłopiec przytulony do kozy z czerwoną obrożą przy beli siana, świąteczny stół ze świeczkami i talerzami, przy którym siedzi chłopiec w niebieskiej bluzie. Na końcu selfie mężczyzny w czarnej czapce i grubych czarnych okularach, z kręconymi włosami (tata). Opisał Jurek. Plik: https://dataset.gzowo.fun/media/wideo/bez-daty_swieta-w-gzowie-z-kozami.mp4 Kadry: https://dataset.gzowo.fun/media/klatki/bez-daty_swieta-w-gzowie-z-kozami/ (8 szt.)

## 15. Pozostałe foldery z mediami

- `media/geo/` (5 plików): Geodane okolicy: ortofotomapa kwadratu 1 x 1 km (północ u góry, środek 52.612456 N, 21.112375 E, Gzowo 34 leży 245 m na wschód i 39 m na północ od środka), zbliżenie na działkę z żółtym kółkiem, rzeźba terenu, mapa pokrycia terenu i szerszy widok okolicy.
- `media/mapa-pikselowa/` (37 plików): Pikselowe sprite'y z mapy działki na gzowo.fun: arcade, warsztat, lab, wyrzutnia, rakieta, hangar, pomost, skrzynka, znak, sosny, chmury, mewa, woda i inne. Plik _cala-mapa.webp pokazuje złożoną mapę.
- `media/postacie/osrodek-daje/` (6 plików): Kanciaste low-poly portrety postaci z gry Ośrodek Daje: KS (tata) w białym futrze, Jurek, Ryś, Dropsik. Gotowe jako inspiracja wyglądu pionków.
- `media/postacie/narek/` (1 plików): Render maskotki Narek.
- `media/brand/gzowo-labs/` (80 plików): Pełny kit logo Gzowo Labs (Wschód): SVG i PNG we wszystkich układach i kolorach, favicony, naklejki na rakiety, awatary, animacje MP4 oraz płonący GIF i grafika og ze strony.
- `media/brand/gsp/` (88 plików): Kit Gzowo Space Program: logo PNG, gify, zakończenia filmów, awatary.
- `media/klatki/` (150 plików): Kadry wycięte w równych odstępach z każdego filmu (nazwa pliku to numer i sekunda). Dla modeli, które nie oglądają wideo.
- `media/miniatury/` (67 plików): Małe wersje zdjęć (480 px) do szybkiego podglądu.

## 16. Pod grę (propozycje, nie fakty)

To NIE są wspomnienia, tylko propozycje Claude'a ułożone z faktów z tego datasetu, żeby łatwiej było zacząć grę. Każdą można zmienić albo wyrzucić.

**Pola planszy:** Dom (śniadanie przy dużym stole); Taras; Wiata z pasiastym fotelem; Trzy domki FSO; Panele słoneczne; Ognisko; Hamak w sosnach; Skarpa i stary skład; Plaża; Narew; Mur z gabionów; GL Launch Site; Dom Waldka; Stacja Moya; Sklep; Aleja Lipowa; Cypel; Kocia Wyspa; Kanał; Lądowisko helikoptera.

**Postacie:** Jurek (konstruktor rakiet); Rysio (czerwona bluza Spider-Man); KS, Kierownik Ośrodka (białe futro, buty z krokodyla); Zofia (Mama); Waldek (operator koparki, przyjaciel); Bożena; Ciszewscy: Bartek, Clu, Ignacy, Helena; Czupryńscy; Janek Kunstler; Benny; Major (wędkarz i drwal); Szamborski (przylatuje helikopterem); Paweł (łysy gość z kanału); Wójt; Panie ze stacji Moya; Dropsik; Kropka (pies Waldka); Koza (gość na święta); Beethoven (głuchy biały kot); szopy pracze; ośmiornica (logo).

**Przedmioty:** koparka, Tesla, motorówka, kajak, deska SUP, dron Avata, rakieta Gzofajfus, spadochron, AirTag z nosa rakiety, łopata, stara tablica FSO, mapa geodezyjna, niewypał, helikopter, wędka, drewno z wycinki, tafla lodu, lody ze stacji Moya, szyszki (waluta), puszka, hamak, pianino, białe futro, buty z krokodyla.

**Mechaniki:**
- Niewypały i saperzy: na polu trafia się niewypał, pole jest zablokowane, dopóki nie przyjadą saperzy. Saperzy to mechanika gry, nie postać.

**Karty wydarzeń:**
- Ośrodek daje: dostajesz coś za nic.
- Grad wielkości kostek lodu: wszyscy chowają się pod wiatę.
- Spadochron się nie otworzył: szukasz rakiety w polu.
- Spadochron otworzył się za pierwszym razem.
- Dropsik zniknął: wszyscy ruszają na poszukiwania.
- Niewypał! Pole jest zamknięte, dopóki nie przyjadą saperzy.
- Saperzy zabierają niewypał: pole znów otwarte.
- Szamborski ląduje helikopterem: przenosisz się na dowolne pole.
- Major robi wycinkę: jedno drzewo mniej, drewno na ognisko dla wszystkich.
- Major złowił rybę: kolacja nad Narwią.
- Wizyta Wójta: wszyscy na chwilę są bardzo grzeczni.
- Paweł macha z kanału obok Kociej Wyspy.
- Koza przyjechała z Warszawy na święta: wszyscy zbierają się przy choince.
- Znajdujesz starą tablicę FSO: poznajesz historię ośrodka.
- Czerwona noc na Cyplu: ktoś stoi nad wodą i patrzy w zmierzch.
- Narew zamarzła: można przejść po lodzie.
- Zimowy obiad: zjadasz taflę lodu.
- Ciężka droga do stacji Moya: przedzierasz się przez trawy.
- Waldek odpala koparkę: kopiesz dwa razy głębiej.
- Szopy tańczą przy ognisku.
- Beethoven nie słyszy, co się dzieje, i nic sobie z tego nie robi.
- Tata maluje światłem przy ognisku.
- Herbata nie wyklucza kawy: bierzesz obie karty.
- Odkrywasz wejście do starego składu w skarpie.
- Łoś przechodzi przez działkę: wszyscy stoją w miejscu.
- Zachód słońca nad Narwią: tura bez pośpiechu.

**Pytania quizowe:**
- Czym była działka, zanim trafiła do Sukienników? → Ośrodkiem wypoczynkowym FSO.
- Ile domków stało kiedyś w ośrodku i ile zostało? → Dziesięć, zostały trzy.
- Co znaczy KS? → Kierownik Ośrodka, czyli tata.
- Jak brzmi zasada nr 1 KS-a? → Ośrodek daje, Ośrodek daje.
- Kto głównie pracuje koparką? → Waldek.
- Jak ma na imię głuchy biały kot i czyj jest? → Beethoven, kot Czupryńskich.
- Co jest logo Gzowa 34? → Ośmiornica.
- Dokąd chodzi się na lody? → Na stację Moya.
- Jak nazywa się miejsce startów rakiet? → GL Launch Site.
- Co symbolizują dwa ogniwa w logo Gzowo Labs? → Dwóch braci, Jurka i Rysia.
- Która rakieta ma w nosie miejsce na AirTaga? → Gzofajfus Classic Mk III.
- Jakie hasło mają Ciszewscy i Sukiennicy? → Herbata nie wyklucza kawy.
- Od kiedy Sukiennicy mają działkę? → Od czerwca 2021.
- Co to jest zimowy obiad? → Tafla lodu z Narwi.
- Co jest napisane na starej czerwonej tablicy? → Fabryka Samochodów Osobowych, Ośrodek Wędkarski w Gzowie.
- Jakie zwierzę przyjechało do Gzowa na jedne święta? → Koza, przywieziona z Warszawy.
- Jaką rejestrację ma granatowy helikopter? → SP-MMM.
- Jak miał na imię pies Waldka, który stał pod helikopterem? → Kropka.

## 17. Czego jeszcze nie wiemy

- Czysty plik logo Gzowa 34: na razie jest tylko zdjęcie białej ośmiornicy.
- Pełne brzmienie powiedzonka "Tak to czasem w życiu bywa, pies się topi, ła...".
- Gdzie dokładnie jest sklep, do którego chodzi rodzina (podyktowane "w Nieporęcie").
- Imię śp. Gzowiańskiego somsiada (Jurek: "chyba Arek").
- Kto maluje wielki obraz na filmie z 25.05.2025 i co się z nim stało.
- Data lotu The Orange Beauty: 29.11.2025 (nazwy plików) czy 22.02.2026 (strona).
- Brak zdjęć koparki, Tesli, tarasu i kajaków. Dom z zewnątrz jest tylko na krótkim filmie.
- Kiedy dokładnie był Dropsik i jak go porwano.
- Kto z Ciszewskich jest kim (Bartek i Ola jako rodzice, Ignacy i Helena jako dzieci to wniosek ze zdjęć).
- Model Tesli i marka koparki.
- Gdzie dokładnie są Cypel, kanał i Kocia Wyspa i skąd nazwa Kocia Wyspa.
- Kim dokładnie są Major, Szamborski i Paweł (pełne imiona, skąd się znają z rodziną).
- Niewypały: kiedy je znajdowano, ile razy byli saperzy i gdzie na działce.
- Wójt: jak się nazywa i jaką rolę gra w historiach z Gzowa.
- W którym roku były święta z kozą.
- Gdzie wiszą stara tablica FSO i ośmiornica: Jurek podpisał je jako Dom, a GPS obu zdjęć wskazuje okolice Warszawy.
- Czy helikopter SP-MMM z 2022 to na pewno maszyna Szamborskiego.
