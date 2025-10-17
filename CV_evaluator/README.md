# AI darbināts CV vērtētājs

## Apraksts
Šī Python lietotne salīdzina darba aprakstu ar trim kandidātu CV, izmantojot Gemini Flash 2.5 modeli, un sagatavo novērtējumu JSON un Markdown pārskata formātā.

## Instalācija
1. Klonējiet repozitoriju un ieejiet mapē:
   ```bash
   git clone <repo-url>
   cd cv_evaluator
   ```

2. Instalējiet nepieciešamās Python pakotnes:
   ```bash
   pip install requests
   ```

3. Sagatavojiet ievades failus mapē `input_files`:
   - `jd.txt` (darba apraksts)
   - `cv1.txt`, `cv2.txt`, `cv3.txt` (kandidātu CV)

4. Saglabājiet savu Gemini API atslēgu kā vides mainīgo:
**Windows PowerShell:**
```
$env:GEMINI_API_KEY="TAVA_GEMINI_API_ATSLĒGA"
```

**Windows CMD:**
```
set GEMINI_API_KEY=TAVA_GEMINI_API_ATSLĒGA
```

**Linux/Mac bash:**
```
export GEMINI_API_KEY=TAVA_GEMINI_API_ATSLĒGA
```

## Lietošana
```bash
python app.py
```

Rezultāti tiks saglabāti mapē `output_files`.

### Izvades struktūra:
- `cvN.json` — atbilstības novērtējums JSON formātā
- `cvN_report.md` — pārskats cilvēkam saprotamā formā

---

## Konfigurācija
- API atslēga tiek nolasīta no vides mainīgā `GEMINI_API_KEY`
- Temperatūru un citus parametrus var mainīt `config.py`

---

## Drošība
Nekad nepublicējiet savu API atslēgu publiski!