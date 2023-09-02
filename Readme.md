# Tic Tac Toe (Boter, Kaas en Eieren)

## Inleiding

Assessment voor een Medior Software Engineer functie. De opdracht is om een implementatie te schrijven in Python voor het spelletje 'boter, kaas en eieren' (tic tac toe).

## Inhoudsopgave

- [Tic Tac Toe (Boter, Kaas en Eieren)](#tic-tac-toe-boter-kaas-en-eieren)
  - [Inleiding](#inleiding)
  - [Inhoudsopgave](#inhoudsopgave)
  - [Opdracht](#opdracht)
  - [Gebruik](#gebruik)
  - [Testen](#testen)

## Opdracht

Schrijf een implementatie in Python voor het spelletje 'boter, kaas en eieren' (tic tac toe).

Je mag er vanuit gaan dat er twee spelers zijn die achter een console zitten.

Natuurlijk! Laten we elk van de genoemde punten nader bekijken en enkele overwegingen voor elk ervan opnoemen:

1. **Wat jede beste datastructuur voor het spelletje vindt?**

   - **Matrix**: Een 3x3 matrix (lijst van lijsten) is het speelveld van boter, kaas en eieren te representeren.

2. **Wat je de beste naamgeving voor je functies/methoden vindt?**

   - Het is essentieel dat functie- en methodenamen beschrijvend zijn en hun doel aangeven.
   - Voorbeelden:
     - `is_winner()`: Controleert of een speler heeft gewonnen.
     - `fix_spot()`: Plaatst een symbool op het bord.
     - `is_draw()`: Controleert of het spel in een gelijkspel eindigt.

3. **Wat je de beste flow in je code vindt?**

   - Begin met het initialiseren van het bord en het vaststellen van de huidige speler.
   - Ga verder met een lus waarin spelers om beurten hun zet doen.
   - Controleer na elke zet of er een winnaar is, of het gelijk spel is, of het spel doorgaat.
   - Een duidelijke scheiding tussen het Board, de Player en de Game logic.

4. **Hoe je het spel het beste kunt testen?**

   - **Unit Tests**: Test individuele functies, zoals het controleren van een overwinning of een gelijkspel.
   - **Integration Tests**: Simuleer een volledige spelrun met vooraf bepaalde zetten om te controleren of het spel correct eindigt.
   - Gebruik het `unittest` framework in Python voor geautomatiseerd testen.

5. **Bonus: Maak de implementatie volgens object georiënteerd ontwerp**

   - **Encapsulatie**: Verberg interne details van klassen en bied openbare methoden voor interactie. Bijvoorbeeld: houd de matrix die het bord voorstelt privé en bied methoden zoals `fix_spot()` om het te manipuleren.
   - **Toestand van het spel beleggen**: De staat van het spel kan het beste worden belegd in een `Game`-klasse. Deze klasse zou het bord en de huidige speler bevatten en logica voor het beheren van de spelstatus.

## Gebruik

1. **Starten**: Voer het volgende commando uit in de terminal om het spel te starten:

   ```bash
   python3 main.py
   ```

2. **Spelen**: Na het starten van het spel wordt de huidige status van het bord weergegeven, gevolgd door een prompt voor de huidige speler om een zet te doen.

   Voorbeeld van output:

   ```
   Welcome to Tic Tac Toe!
   -----------------------
   - - -
   - - -
   - - -
   -----------------------
   Player X, please enter a row and column number (e.g. 1 2):
   ```

   Geef een rij- en kolomnummer op gescheiden door een spatie, bijvoorbeeld: `1 2`.

3. **Spel voortzetten**: Het spel blijft doorgaan totdat een speler wint of het een gelijkspel is.

## Testen

1. Voer het volgende commando uit in de terminal om de unit tests uit te voeren:

   ```bash
   python3 test.py
   ```

2. De tests worden uitgevoerd en de resultaten worden weergegeven in de console.

## Afsluiting

Dit is een eenvoudige maar functionele implementatie van Tic Tac Toe in Python. Hoewel het spel zelf vrij eenvoudig is, zijn er veel overwegingen en beslissingen die in de implementatie gaan om het spel zo soepel en gebruiksvriendelijk mogelijk te maken. Veel plezier met spelen!
