# Struttura del discorso di laurea

**Titolo tesi:** *Interface circuits for a six-phase variable reluctance energy harvester: a comparative study of rectification and power conditioning topologies*

**Autore:** Jacopo Garau (matr. 2141221)
**Corso di laurea:** Laurea Magistrale in Ingegneria Elettronica — Università degli Studi di Padova, Dipartimento di Ingegneria dell'Informazione
**Relatore:** Prof. Alessandro Pozzebon (Università di Padova)
**Correlatori:** Prof. Sebastian Bader, Dr. Ye Xu (Mid Sweden University, Svezia)
**Nota:** dai ringraziamenti (p. 117) risulta che la tesi è stata svolta in mobilità presso la Mid Sweden University, Sundsvall — lo confermo in apertura salvo tua indicazione contraria.

**Target:** 10 minuti, ~130-140 parole/min → **~1300-1400 parole totali**. Sotto ogni sezione trovi il budget di parole stimato (per farti un'idea prima della Fase 2) e i riferimenti a capitolo/sezione/pagina (da `main.toc`) da cui ho estratto i contenuti.

---

## 1. Apertura e saluti — 30 sec (~65 parole)

- Saluto alla commissione (Presidente + membri)
- Nome, titolo della tesi
- Contesto: laurea magistrale in Ingegneria Elettronica, Padova; lavoro svolto presso Mid Sweden University; relatore Prof. Pozzebon, correlatori Prof. Bader e Dr. Xu
- Una frase di inquadramento: interfacciare elettronicamente un harvester elettromagnetico a sei fasi con l'elettronica di gestione dell'energia

*Rif.: frontespizio/secondcover; Acknowledgments p. 117*

---

## 2. Contesto e motivazione del problema — 1-1.5 min (~170 parole)

- Crescita di reti di sensori wireless (WSN) e dispositivi IoT → criticità dell'alimentazione (Cap. 1, §1.1, p. 1)
- Limiti delle batterie: sostituzione, manutenzione, nodi difficili da raggiungere, costo ambientale (§1.1, p. 1)
- Energy harvesting come soluzione: conversione di energia ambientale (vibrazioni, calore, luce, RF) in energia elettrica (§1.1-1.2, p. 1-2)
- Le vibrazioni meccaniche sono la fonte più studiata; quattro tecnologie principali — piezoelettrica, elettromagnetica, elettrostatica, triboelettrica — ciascuna con vantaggi/limiti (§1.4, p. 4)
- Focus della tesi: tecnologia a **riluttanza variabile (VREH)** — magnete e bobina restano fissi, il flusso varia per il passaggio di una ruota dentata ferromagnetica rotante → nessuna parte elettrica/mobile sul rotore, sistema facilmente scalabile (§1.5, p. 5)
- Stato dell'arte: dai primi prototipi per monitoraggio ferroviario (Kroener et al.) al design ottimizzato "m-shaped" (Xu et al.), fino al sistema **multi-fase a sei unità (MP-VREH, Wu et al.)** pensato per veicoli commerciali pesanti (es. autobus) a 100-400 rpm, cioè 20-80 km/h (§1.6, p. 6-8)
- Problema aperto: sei uscite AC indipendenti sfasate di 60°, a bassa tensione — la letteratura esistente copre solo circuiti per singola fase (§1.7, p. 8)

---

## 3. Domanda di ricerca / obiettivi della tesi — 1 min (~135 parole)

- Obiettivo generale: individuare la topologia di circuito di interfaccia che massimizza la potenza trasferita al carico dal MP-VREH a sei fasi, nel range 100-400 rpm (§1.8, p. 9)
- Obiettivi specifici:
  1. Proporre topologie di raddrizzamento adatte a 6 ingressi AC sfasati e a bassa tensione
  2. Validarle tramite simulazione circuitale (Simulink)
  3. Validarle sperimentalmente con PCB dedicato e sensori di corrente calibrati
  4. Valutare la compatibilità con PMIC commerciali per completare la catena fino a un'uscita regolata

*Rif.: §1.8 (p. 9); §2.2.c "Design Requirements for the Interface Circuit" (p. 22)*

---

## 4. Metodologia / approccio seguito — 2-2.5 min (~300 parole)

- Modello elettrico: dalla legge di Faraday al modello di Thévenin della singola bobina (EMF + $R_{coil}$ + $L_{coil}$) (Cap. 2, §2.1, p. 11-19)
- Massimo trasferimento di potenza: a basse rpm basta l'adattamento resistivo, ma a rpm più alte la reattanza induttiva della bobina non è trascurabile → serve un condensatore di compensazione serie $C_m$ per l'adattamento coniugato complesso (§2.1, p. 19-21)
- Modello multi-fase: sei sorgenti identiche sfasate di 60° (§2.2, p. 21-22)
- Due famiglie di topologie proposte e confrontate (Cap. 3, p. 23-28):
  - **FWR**: raggruppa le 6 fasi in due terne trifase, ciascuna raddrizzata da un ponte trifase classico; testato in configurazione **Stella** e **Triangolo** (§3.2, p. 24)
  - **NVC**: raggruppa le 6 fasi in tre coppie in antifase (180°) collegate in anti-serie, raddrizzate da un ponte MOSFET auto-pilotato (cross-coupled) con diodi Schottky di backup alle basse tensioni (§3.3, p. 25)
- Simulazioni Simulink (Cap. 4, p. 29): alimentate con forme d'onda reali misurate (corrette per crest factor, non sinusoidi ideali) per maggiore realismo; sweep di $C_m$ e $R_L$ per trovare il punto operativo ottimo a 100 e 400 rpm
- Validazione sperimentale:
  - PCB dedicato con jumper riconfigurabili (FWR/NVC, stella/triangolo, banco di $C_m$) per testare ogni configurazione sulle stesse 6 bobine (Cap. 5, p. 55-64)
  - Banco di prova: motore asincrono + inverter per il controllo preciso della velocità, giunto elastico per minimizzare le vibrazioni trasmesse (Cap. 6, §6.2, p. 65)
  - Acquisizione dati: analizzatore logico Saleae, 16 canali differenziali (§6.3, p. 66)
  - Misura di corrente: shunt + amplificatori da strumentazione INA114, calibrati individualmente con SMU di precisione e tabelle di lookup — non valori nominali — per misure di potenza affidabili (§6.4-6.6, p. 67-71)

---

## 5. Risultati principali — 2.5-3 min (~370 parole)

- **Simulazioni** (Cap. 4, §4.4, p. 51-53): NVC offre la potenza più alta a entrambi gli estremi di velocità (fino a 6× la Delta e quasi 2× la Stella a 100 rpm; +42-67% a 400 rpm); Stella sempre meglio di Delta (vantaggio $\sqrt3$ sulla tensione); NVC ha anche il rendimento di raddrizzamento più alto (resistenza on dei MOSFET vs caduta sui diodi)
- **Misure sperimentali sul prototipo reale** (Cap. 7, §7.4, p. 90-92): confermano il quadro generale ma con un risultato più sfumato — NVC e FWR-Stella risultano molto simili:
  - A 100 rpm: NVC vince (57.7 mW vs 47.6 mW Stella, 14.9 mW Delta)
  - A 400 rpm: la **Stella sorpassa la NVC** (433.3 mW vs 425.7 mW) — non previsto dalla sola simulazione
  - Il rendimento resta sempre più alto per la NVC (0.701 vs 0.564 della Stella a 400 rpm)
  - Delta è la più debole delle tre in ogni condizione
- **Confronto simulazione vs misura** (Cap. 8, p. 93-98): il $C_m$ ottimo misurato è sistematicamente più alto di quello simulato (630 μF vs 490/455/260 μF) → induttanza reale della bobina più bassa del nominale + derating dei condensatori ceramici con la tensione; il divario di rendimento cresce con la velocità per la Stella → perdite dipendenti dalla frequenza (es. perdite nel nucleo) non incluse nel modello a resistenza fissa
- **Compatibilità con PMIC commerciali** (Cap. 9, p. 99-108): confronto tra tensione a vuoto misurata di ogni topologia e range di ingresso di 5 PMIC commerciali:
  - Delta e NVC restano sotto ~3.8 V → compatibili con tutti i PMIC testati, in tutto il range di velocità, senza protezioni aggiuntive
  - Stella sale fino a 7 V a 400 rpm → supera il range di ingresso di 4 PMIC su 6 sopra i 250-300 rpm, richiede un PMIC buck-boost a range esteso (SPV1050) oppure un clamp di protezione

---

## 6. Contributo originale — cosa aggiunge questa tesi allo stato dell'arte — 1.5 min (~200 parole)

- Primo studio sistematico di power conditioning specificamente per un **MP-VREH a sei fasi** (la letteratura precedente, es. Xu et al. 2021, confronta solo raddrizzatori per singola fase) (§1.7, p. 8)
- Due adattamenti multi-fase di topologie note, proposti e dimostrati funzionanti: raggruppamento a ponti trifase (FWR, stella/triangolo) e raggruppamento in coppie anti-serie (NVC) (Cap. 3, p. 23-28)
- Un'unica **piattaforma PCB riconfigurabile** che permette di testare tutte le configurazioni sulle stesse identiche bobine, nelle stesse condizioni meccaniche — un confronto sperimentale a parità di condizioni raro in questo ambito (Cap. 5, p. 55)
- Metodologia di misura della corrente rigorosa: calibrazione individuale di ogni sensore con tabelle di lookup e caratterizzazione a 4 fili degli shunt, per misure di potenza affidabili anche a livelli di μW-mW (Cap. 6, p. 67-71)
- Un risultato che **raffina la sola previsione simulativa**: nessuna topologia domina su tutto il range — la NVC è la scelta migliore per l'efficienza e per le basse velocità, ma la Stella vince in potenza assoluta alle alte velocità, contrariamente a quanto suggerito dalla sola simulazione (Cap. 7-8)
- Prima mappatura della compatibilità elettrica tra le tre topologie e 5 PMIC commerciali reali, per tradurre il risultato circuitale in un'indicazione di design pratica per la catena completa harvester → alimentazione regolata (Cap. 9, p. 99-108)

---

## 7. Conclusioni, limiti e sviluppi futuri — 1 min (~135 parole)

- NVC e FWR-Stella sono i due migliori candidati, complementari lungo il range di velocità; Delta è sempre la più debole (Cap. 10, §10.2, p. 109)
- Implicazione pratica: Delta e NVC si accoppiano con qualunque PMIC testato; la Stella richiede un PMIC a range esteso o una protezione in ingresso oltre i 250-300 rpm, pur dando la potenza più alta (§10.3, p. 110)
- Limiti: modello di bobina a resistenza fissa (non cattura le perdite dipendenti dalla frequenza); alloggiamento del prototipo stampato in 3D → sensibilità a vibrazioni/disallineamenti che limita la ripetibilità delle misure (§10.4, p. 110)
- Sviluppi futuri: rete di compensazione adattiva che insegua il $C_m$ ottimo lungo tutto il range di velocità; test hardware dell'intera catena harvester + PMIC per misurarne l'efficienza reale; scelta dell'applicazione finale a valle (§10.5, p. 110)

---

## 8. Ringraziamenti — 20 sec (~45 parole)

- Ringraziamento al relatore Prof. Pozzebon e ai correlatori Prof. Bader e Dr. Xu
- Ringraziamento alla commissione per l'attenzione
- Disponibilità a rispondere a domande

*Rif.: Acknowledgments, p. 117 (per i nomi esatti da citare)*

---

## Note da confermare prima della Fase 2

1. Titolo, relatore/correlatori e corso di laurea sono presi direttamente dal sorgente della tesi (`main.tex`, `secondcover.tex`, `acknowledgments.tex`) al posto dei segnaposto nel tuo messaggio — controlla che siano ancora corretti e aggiornati (es. l'anno accademico 2025/2026 indicato nel sorgente).
2. Ho assunto che tu voglia menzionare in apertura che la tesi è stata svolta alla Mid Sweden University: dimmi se preferisci ometterlo o darlo per scontato.
3. Ho incluso un piccolo insieme di numeri chiave (potenze in mW, rendimenti, tensioni, rpm) per rendere concreti i risultati nelle sezioni 5 e 6. Se preferisci un discorso più qualitativo (meno cifre a memoria) o viceversa più quantitativo, fammelo sapere.
4. Nella Fase 2 i placeholder `[MOSTRA SLIDE X]` saranno generici (es. `[MOSTRA SLIDE: confronto topologie]`) perché non conosco la numerazione delle tue slide — potrai sostituirli facilmente.
5. Capitoli 4 e 7 (Simulazioni e Misure) contengono moltissimi sweep e sotto-risultati di dettaglio (per ogni topologia: sweep di $C_m$, di $R_L$, di frequenza, efficienza) che ho **volutamente sintetizzato** nella sezione 5, riportando solo i confronti finali fra topologie. Segnalami se c'è un dettaglio specifico di quei capitoli che vuoi che compaia comunque nel discorso.

Confermami che la struttura va bene (o indicami le modifiche) e procedo con la Fase 2: il discorso completo in inglese in `discorso.md`.
