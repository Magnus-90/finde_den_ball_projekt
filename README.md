# Finde-den-Ball – EV3 MicroPython Projekt

Dieses Projekt enthält das vollständige Spiel *Finde den Ball*, implementiert für LEGO® Mindstorms EV3 mit MicroPython.  
Die Hauptspiellogik befindet sich in **Game.py**.

---

## 📘 Tutorial & Dokumentation

- **Installation — ev3-micropython 2.0.0 documentation**  
- **GitHub Repository:** *Magnus-90/finde_den_ball_projekt*  
  → **Game.py** enthält das komplette Spiel

---

# 📥 Download und Installation

## 1. MicroPython Image herunterladen
Lade das offizielle MicroPython-Image hier herunter:  
**MINDSTORMS EV3 Support | Everything You Need | LEGO® Education**

## 2. Image auf microSD-Karte flashen
Nutze z. B. **balenaEtcher**, um das Image auf die SD-Karte zu schreiben.

## 3. VS Code Erweiterung installieren
Installiere die Erweiterung:

**LEGO® MINDSTORMS® EV3 MicroPython**

Beispielbild:  
<img width="940" height="392" alt="32c4c216-6b04-44c5-b581-b95f037dab38" src="https://github.com/user-attachments/assets/e30d9349-7050-4ee7-8efc-54df904bcfbf" />


## 4. Neues MicroPython Projekt erstellen
- Neues Projekt anlegen  
- Namen vergeben  
- VS Code erstellt automatisch eine **main.py**
<img width="201" height="678" alt="6c522ae0-616c-4368-8610-0aeef120fbaf" src="https://github.com/user-attachments/assets/3e373901-5c0a-4f7f-b3af-f043d44f11fe" />

## 5. EV3 mit VS Code verbinden
Mit USB verbinden → EV3 auswählen

<img width="253" height="729" alt="c84faa93-0e0b-4c8c-918e-32292ffe5602" src="https://github.com/user-attachments/assets/9d563802-b4f7-459e-bdc6-af0ff64f6649" />
<img width="159" height="59" alt="de69e677-3166-4ddf-b211-3129e954ad2e" src="https://github.com/user-attachments/assets/0cde53db-12ce-4780-9214-0a9155376f45" />


## 6. Code auf EV3 hochladen
Nach dem Schreiben des Codes → **Upload to EV3**

<img width="303" height="220" alt="37332d2c-1c6d-4102-abfa-7bfc7089d7a4" src="https://github.com/user-attachments/assets/02939300-a0be-4297-b1ec-e3e4ac3d7e05" />

---

# 🔧 Wichtigste Befehle & Code-Blöcke

## ⚠️ Wichtiger Hinweis
Motoren, Sensoren und der Brick müssen **vor der Nutzung deklariert werden**.

### Beispiel:
```python
ev3 = EV3Brick()
motor_a = Motor(Port.A)
motor_b = Motor(Port.B)
motor_c = Motor(Port.C)
touch = TouchSensor(Port.S1)
remote = InfraredSensor(Port.S2)
