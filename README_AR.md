# أكواد رسالة EUMH-ATM — النسخة المطابقة للرسالة (PR-3، المراحل S0–S13)

## الحزمة دي فيها إيه

ده **الكود الفعلي اللي اتنفّذ وطلّع أرقام الرسالة** (اخر وضع 8)، مش كود جديد مكتوب عشان يطابق النتايج. الكود ما اتغيّرش فيه ولا سطر. اللي اتضاف بس: ملف تحقق واحد، والملفات التوثيقية دي.

| المجلد | المحتوى |
|---|---|
| `config/protocol_pr3.yaml` | الـ protocol المجمّد PR-3 |
| `python/eumh/` | مكتبة Python: البيانات، الـ features، الـ preprocessing، النماذج (baselines، hybrids A وB، fusion C، TFT وPatchTST)، XAI، UQ، downstream |
| `R/` | 18 script: ingest، EDA، STL، ADF/KPSS، الـ statistical baselines، الـ metrics، الـ scoring، coverage، inference (DM، bootstrap، ANOVA)، confirmation، matched service |
| `scripts/` | مدخل تشغيل لكل مرحلة من S1 لـ S13 + `fetch_data.py` + `make_report_figures.py` |
| `tests/` | `test_s0_s13.R` (الـ 404 gate)، `verify_chapter_numbers.py`، و`verify_appendix_c_against_tables.py` (جديد) |
| `environment/` | requirements، حزم R، سجل البيئة (Python 3.11.15، R 4.3.3، torch 2.13.0) |
| `results/tables/` | 281 جدول ناتج (منهم s11 اللي منه Appendix C) |
| `results/manifests/` | 37 ملف (36 stage manifest + amendments.json) |
| `results/ledgers/` | 18 prediction ledger (S4 لـ S12) |
| `results/figures/` | 32 figure |
| `supplementary/prophet_post_hoc/` | script الـ Prophet الـ post hoc (برّه PR-3) |
| `archive_superseded/` | أكواد قديمة **مش** هي اللي طلّعت أرقام الرسالة، محفوظة للتوثيق بس (شوفي تحت) |

التشغيل الكامل في `README.md` و`SETUP.md`.

## نتيجة التحقق

| الفحص | النتيجة |
|---|---|
| كل قيم Appendix C.1 وC.2 (25 نموذج × 8 أعمدة × 2 panel) مقابل `s11_*_metrics_consolidated.csv` | **400 من 400 متطابقين** |
| الـ acceptance gates في `acceptance_gates_s0_s13.csv` | **404 من 404 PASS** — زي ما الرسالة بتقول |
| عدد الـ manifests | **37** — زي الرسالة |
| الملفات اللي Appendix D بيذكرها بالاسم | **19 من 20 موجودين** |
| كل ملفات Python بتعمل compile | نعم |

تقدري تعيدي الفحص الأول بنفسك:
```bash
pandoc "EUMH_ATM_Dissertation.docx" -t plain -o dissertation.txt
python3 tests/verify_appendix_c_against_tables.py dissertation.txt
```

## ⚠️ حاجتين لازم يتظبطوا في نص Appendix D (مش في الكود)

**1. بصمة الـ protocol.** الرسالة بتقول إن الـ protocol له بصمة واحدة `451a1cb9…`، وإن أي stage بصمته مختلفة بتقع في الـ gate. الـ manifests الفعلية فيها **4 بصمات متتالية**، كل واحدة بعد amendment:

| البصمة | المراحل | التاريخ |
|---|---|---|
| `d5205deb…` | S1، S2 | 18 أغسطس، قبل A-001 |
| `451a1cb9…` | S3 لـ S7 | 18–19 أغسطس، بعد A-001 |
| `f23c204a…` | S7b لـ S12 | 19–20 أغسطس، بعد A-002 وA-003 |
| `26c488ce…` | S9b، S13 | 20 أغسطس، بعد A-004 وA-005 |

الملف `protocol_pr3.yaml` الموجود بصمته `26c488ce…` (النسخة الأخيرة). والـ `amendments.json` بيسجّل الانتقال من `f23c204a` لـ `26c488ce` صراحة. يعني ده **مش تلاعب**، ده سلسلة amendments متسجلة. لكن الجملة اللي في الرسالة مش دقيقة، وممتحن يفتح الـ manifests هيلاقي الفرق. الصياغة المقترحة:

> Protocol: PR-3. The protocol file was amended three times during execution (Appendix E), so the stage manifests carry four successive SHA-256 values: d5205deb (S1–S2), 451a1cb9 (S3–S7), f23c204a (S7b–S12) and 26c488ce (S9b, S13; the file as archived). Each manifest records the hash in force when its stage ran, and amendments.json records each transition.

**2. اسم script الـ Prophet.** Appendix D بيقول `run_prophet_nn5_validated.py` ومعاه `prophet_nn5_result.json` و`prophet_nn5_predictions.csv`. اللي لقيته في الملفات اسمه `run_prophet_nn5.py`، وفيه الـ self-validation gate، بس الـ JSON والـ CSV الناتجين مش موجودين في أي أرشيف. محتاجين يا إما يتلاقوا، يا إما اسم الملف في Appendix D يتعدّل.

## الأرشيف القديم `archive_superseded/`

- `cycle_phases_1_27_aug02_17/` — الدورة السابقة (Phases 1–27، من 2 لـ 17 أغسطس، Node.js/TensorFlow.js). الـ protocol PR-3 نفسه بيقول إنه `supersedes: previous cycle Phases 1-28`. أرقامها مختلفة عن الرسالة الحالية (مثلاً TFT sMAPE 21.8587 هناك)، فما ينفعش تتقدّم على إنها كود الرسالة.
- `esaf_prototype_apr2026/` — أمثلة الـ prototype الأول (ESAF، أبريل 2026).

ملحوظة: حزمة `Thesis_All_Codes_Collected.zip` اللي كانت متجمعة قبل كده كانت معتبرة Phase23 هي "نقطة البداية"، وماكانش فيها كود S0–S13 خالص. الحزمة دي بتصحّح ده.

## حاجات مش موجودة في الحزمة

- **البيانات الخام**: NN5 بيتنزل بـ `scripts/fetch_data.py` ويتأكد من الـ hash. XYZ Bank من Kaggle وما ينفعش يتوزع (الترخيص مش معروف).
- **أوزان النماذج المدرّبة**: مش في أي أرشيف.
- **إعادة التشغيل الكامل** ما اتعملتش هنا. اللي اتعمل هو التحقق إن أرقام الرسالة = مخرجات الكود المحفوظة.
