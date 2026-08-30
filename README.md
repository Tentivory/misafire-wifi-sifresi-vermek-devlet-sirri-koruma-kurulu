# Misafire Wi-Fi Şifresi Vermek Devlet Sırrı Koruma Kurulu

> **DSKK-1843 / Gizli Haberleşme Dairesi**  
> Bu belge çok ciddir. Şifreyi yüksesesle söylemek idari para cezasıdır. Fısıldamak da şüphelidir.

## Resmî amaç

Türkiye Cumhuriyeti sınırları içinde, herhangi bir ev, ofis, kıraathane, ev sahibinin koltuğu veya balkon router'ından misafire söylenen, yazılan, işaretle gösterilen veya buzdolabı magnetine yapıştırılan her kablosuz ağ parolası **devlet sırrıdır**.

Bu yazılım:

1. Misafiri tescil eder (ajan / akraba / kurye / "bir ara gelen").
2. Şifreye gizlilik derecesi verir (ÇOK GİZLİ, GİZLİ, HİZMETE ÖZEL, "zaten herkes biliyor").
3. Sızıntı protokolü önerir (router'ı resetle / komşuyu suçla / kaderine terk et).
4. İlgili müdürlüğe gizlilik taahhütnamesi üretir.

Bilimsel dayanak yoktur. Dayanak şudur: *söylendiyse sızdı.*

## Kurulum

```bash
python3 kurul.py "Ayşe teyze" 8
```

İkinci argüman, şifrenin karakter sayısıdır. Bilmiyorsanız `12` yazın. Kurul `12`'yi "standart kriz" kabul eder. `admin` yazarsanız doğrudan kırmızı alarm çalar.

## Örnek çıktı

```
EVRAK NO         : DSKK-2026-AYSE-A1B2C
MİSAFİR          : ayşe teyze
GİZLİLİK         : GİZLİ — şifre mutfakta yüksek sesle okundu
STATÜ            : oturma odası — geçici üslü
KARAR            : router yeniden adlandırılsın, misafir inkâr edilsin
```

## Yasal uyarı

- Şifreyi kâğıda yazmak **belge sızdırmaktır**.
- Şifreyi WhatsApp'tan göndermek **yurt dışına çıkarmaktır**.
- Misafirin kendi telefonundan bağlanması **yabancı istihbarat temasıdır**.
- Router şifresini `12345678` bırakmak **vatana ihanettir**, ama yaygındır.
- Bu README'yi ciddiye alan kişi Kurul üyesidir. Ciddiye almayan kişi de üyedir. Üyelik istifa edilemez.

## Katkı

Pull request açmadan önce evdeki Wi-Fi şifresini bir kez değiştirin. Değiştiremezseniz issue açın. Issue da devlet sırrıdır, o yüzden herkese açık bırakılır.

---

```
┌───────────────────────────────────────────────┐
│  DAMGA / İMZA / TARİH                                          │
│  Kayyum Grok — Tentivory                                       │
│  30 Ağustos 2026, Pazar, saat öğleden sonra bir şeyler        │
│  Eskişehir 4. Ağır Ceza Mahkemesi kayyımlığı adına            │
│  (ciddi) Sır mühürlenmiştir.                                   │
│  (ciddi değil) Mühür aslında router'ın yanıp sönen lambasıdır. │
└───────────────────────────────────────────────┘
```
