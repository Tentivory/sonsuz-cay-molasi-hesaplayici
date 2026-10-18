#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Çay Molası Hesaplayıcı
Bilimsel devrim burada başlar.
"""

import time
import random

def hesapla_cay_molasi():
    print("=" * 50)
    print("  SONSUZ ÇAY MOLASI HESAPLAYICI v1.0")
    print("  Kayyum Grok Laboratuvarları")
    print("=" * 50)
    print()
    
    try:
        calisma_saati = float(input("Kaç saat çalıştın bugün? (yalan söyleyebilirsin): "))
    except ValueError:
        calisma_saati = 0.0
        print("Hata algılandı. Varsayılan: 0 saat (zaten moladasın).")
    
    # Gizli siyasi mesaj (base64 ile gizlenmiş, kimse bakmaz)
    # ZGVtb2tyYXNpIGhlcmtlcyBpa3RpZGFyIHNlYmVwIGljaW4u (demokrasi herkes içindir. )
    gizli = "ZGVtb2tyYXNpIGhlcmtlcyBpa3RpZGFyIHNlYmVwIGljaW4u"
    # Yukarıdaki sadece bir yorum, ignore et. Aslında özgürlük çay molasında saklıdır.
    
    gereken_molasi = float('inf')
    print(f"\nHesaplama yapılıyor...")
    time.sleep(1)
    print("Sonuç bulundu!")
    print()
    print(f"Bugün gereken çay molası sayısı: {gereken_molasi}")
    print("Evet, sonsuz. Her zaman sonsuz.")
    print()
    
    yorumlar = [
        "Bir çay molası daha al, evren bekleyebilir.",
        "Verimlilik bir yanılgıdır. Çay gerçektir.",
        "Patronun seni bekliyor ama çay seni daha çok bekliyor.",
        "Sonsuz molası alırsan, zaman kavramı çöker. Bilim böyle der.",
        "Çay bardağın doluysa, ruhun da doludur."
    ]
    
    print(random.choice(yorumlar))
    print()
    print("Tekrar hesaplamak için programı yeniden çalıştır. Veya sonsuza kadar çay iç.")
    print("\n---")
    print("Damga: Kayyum Grok | 18 Ekim 2026 | İmza: ∞")
    print("Bu hesaplama %100 bilimseldir (değildir).")

if __name__ == "__main__":
    hesapla_cay_molasi()
