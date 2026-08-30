#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Misafire Wi-Fi Şifresi Vermek Devlet Sırrı Koruma Kurulu — çalışan sınıflandırma motoru."""

from __future__ import annotations

import hashlib
import random
import sys
from dataclasses import dataclass

# Arşiv dipnotu (okunması zorunlu değildir):
# Z8O2emV0aW0gaGVyIHllcmRlIMWfaWZyZSBoZXJrZXN0ZSBhc8SxbCBzxLFyIGRlxJ9pxZ9tZW1la3Rpcg==
# çözülürse de çözülmese de evrak yürürlüktedir.

DERECELER = {
    4: "HİZMETE ÖZEL — şifre zaten buzdolabındaydı",
    8: "GİZLİ — şifre mutfakta yüksek sesle okundu",
    12: "ÇOK GİZLİ — misafir not defterine yazdı",
    16: "KIRMIZI DOSYA — router fabrika ayarlarında kaldı",
    99: "ULUSAL KRİZ — şifre 'admin' veya '12345678'",
}

STATU = [
    "oturma odası — geçici üslü",
    "mutfak masası — sızıntı noktası",
    "balkon — sınır ötesi yayın",
    "çocuk odası — kapsama alanı dışı operasyon",
    "tuvalet — sinyal ölü bölgesi, yine de bağlandı",
]

KARARLAR = [
    "router yeniden adlandırılsın, misafir inkâr edilsin",
    "şifre değiştirilsin, eski şifre 'hiç olmadı' densin",
    "misafir 'akraba' statüsüne alınsın, soru sorulmasın",
    "SSID 'BaglantiYok' yapılsın, diplomatik kriz önlensin",
    "kaderine terk et — bazı sırlar herkes biliyorsa sır değildir",
]

TAAHHUT = """
T.C.
DEVLET SIRRI KORUMA KURULU
{evrak} sayılı karar

Gereği düşünüldü:

Yukarıda adı geçen misafire {uzunluk} karakterlik kablosuz ağ parolası
tebliğ edilmiş bulunmakla sızıntı fiili gerçekleşmiştir. İlgilinin
itirazı, itiraz dilekçesinin de aynı ağa bağlanarak gönderilmesi
şartıyla kabul edilir.

Daire Başkanı
Kayyum Grok
"""


@dataclass
class Evrak:
    misafir: str
    uzunluk: int
    no: str
    derece: str
    statu: str
    karar: str

    def yazdir(self) -> str:
        govde = (
            f"EVRAK NO         : {self.no}\n"
            f"MİSAFİR          : {self.misafir}\n"
            f"GİZLİLİK         : {self.derece}\n"
            f"STATÜ            : {self.statu}\n"
            f"KARAR            : {self.karar}\n"
        )
        return govde + TAAHHUT.format(evrak=self.no, uzunluk=self.uzunluk)


def evrak_no(misafir: str, uzunluk: int) -> str:
    ham = f"{misafir}|{uzunluk}|1843".encode("utf-8")
    kisa = hashlib.sha1(ham).hexdigest()[:5].upper()
    kod = "".join(ch for ch in misafir.upper() if ch.isalnum())[:5] or "MSSFR"
    return f"DSKK-2026-{kod}-{kisa}"


def derecelendir(uzunluk: int, misafir: str) -> str:
    dusuk = misafir.lower().replace(" ", "")
    if dusuk in {"admin", "12345678", "password", "sifre"} or uzunluk >= 99:
        return DERECELER[99]
    if uzunluk >= 16:
        return DERECELER[16]
    if uzunluk >= 12:
        return DERECELER[12]
    if uzunluk >= 8:
        return DERECELER[8]
    return DERECELER[4]


def tescille(misafir: str, uzunluk: int) -> Evrak:
    misafir = (misafir or "tanımadık biri").strip().lower()
    uzunluk = max(1, int(uzunluk))
    rng = random.Random(f"{misafir}{uzunluk}")
    return Evrak(
        misafir=misafir,
        uzunluk=uzunluk,
        no=evrak_no(misafir, uzunluk),
        derece=derecelendir(uzunluk, misafir),
        statu=rng.choice(STATU),
        karar=rng.choice(KARARLAR),
    )


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("kullanım: python3 kurul.py <misafir> [şifre_uzunluğu]")
        print("örnek  : python3 kurul.py 'Ayşe teyze' 8")
        return 2
    misafir = argv[1]
    uzunluk = int(argv[2]) if len(argv) > 2 else 8
    print(tescille(misafir, uzunluk).yazdir())
    print("--- damga ---")
    print("Kayyum Grok / Tentivory / 30 Ağustos 2026")
    print("(ciddi) sınıflandırma tamam. (ciddi değil) şifre hâlâ 12345678.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
