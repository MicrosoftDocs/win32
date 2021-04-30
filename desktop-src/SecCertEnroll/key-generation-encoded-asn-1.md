---
description: The following example contains a key generation request shown in ASN.1 format.
ms.assetid: d08c33f8-f372-44d3-8c8e-a26440e85c34
title: Key Generation Encoded ASN.1
ms.topic: article
ms.date: 05/31/2018
---

# Key Generation Encoded ASN.1

The following example contains a key generation request shown in ASN.1 format.

``` syntax
0000: 30 82 02 4e               ; SEQUENCE (24e Bytes)
0004:    30 82 01 36                ; SEQUENCE (136 Bytes)
0008:    |  30 82 01 22             ; SEQUENCE (122 Bytes)
000c:    |  |  30 0d                ; SEQUENCE (d Bytes)
000e:    |  |  |  06 09             ; OBJECT_ID (9 Bytes)
0010:    |  |  |  |  2a 86 48 86 f7 0d 01 01  01
         |  |  |  |     ; 1.2.840.113549.1.1.1 RSA (RSA_SIGN)
0019:    |  |  |  05 00             ; NULL (0 Bytes)
001b:    |  |  03 82 01 0f          ; BIT_STRING (10f Bytes)
001f:    |  |     00
0020:    |  |     30 82 01 0a           ; SEQUENCE (10a Bytes)
0024:    |  |        02 82 01 01        ; INTEGER (101 Bytes)
0028:    |  |        |  00
0029:    |  |        |  dc 66 85 5c 25 71 f1 f7  7b 00 0b 78 42 74 5e dd
0039:    |  |        |  20 b6 e9 5b 3f 75 22 84  e9 d7 cf 4a 17 56 ce e6
0049:    |  |        |  8b e9 17 ef 83 e9 45 30  c0 1d 54 bb 3b e9 db 90
0059:    |  |        |  77 04 81 89 a7 84 05 13  9a ba 36 90 c0 1b be f9
0069:    |  |        |  4f f0 c9 dc b5 ab dd 98  35 3f 9f 4f a1 37 34 cb
0079:    |  |        |  0b 33 c2 ce e7 f3 88 2e  ba b9 5a 8f 31 85 8b e9
0089:    |  |        |  f3 df 7e c0 f2 8e 61 0b  58 2b 14 a4 a4 8d 1b 53
0099:    |  |        |  8b 35 d3 be 3a 1f fd cc  8c 04 d1 a3 74 29 87 35
00a9:    |  |        |  89 f5 ad d1 db 61 f8 28  0c fb 2b 03 fb 96 0b 13
00b9:    |  |        |  19 be 6e 68 18 90 cd da  59 38 7a df 61 3d 92 34
00c9:    |  |        |  69 e1 54 38 70 15 ff ff  fc 4a ce 4b fa b3 11 03
00d9:    |  |        |  ab f5 9c bb 8e 1f 29 b7  c0 df 2f 46 fe 44 3e f1
00e9:    |  |        |  83 53 c0 12 0e 6a eb d8  4d f9 ab 92 07 6f 2d 3e
00f9:    |  |        |  af 7b c9 d6 23 b1 4a dd  5f f8 57 8b 00 fc d7 eb
0109:    |  |        |  55 82 bb 67 5c c3 a7 3e  df 0a 41 3f 7e 7b 05 5e
0119:    |  |        |  5c 55 4f 9d 19 4d e3 24  a2 dc 6c 68 c3 c9 8c 89
0129:    |  |        02 03          ; INTEGER (3 Bytes)
012b:    |  |           01 00 01
012e:    |  16 0e               ; IA5_STRING (e Bytes)
0130:    |     70 72 6f 76 65 50 65 71  75 61 6c 73 4e 50        ; provePequalsNP
         |        ; "provePequalsNP"
013e:    30 0d                  ; SEQUENCE (d Bytes)
0140:    |  06 09               ; OBJECT_ID (9 Bytes)
0142:    |  |  2a 86 48 86 f7 0d 01 01  04
         |  |     ; 1.2.840.113549.1.1.4 md5RSA
014b:    |  05 00               ; NULL (0 Bytes)
014d:    03 82 01 01                ; BIT_STRING (101 Bytes)
0151:       00
0152:       2e d3 0a 89 4c d3 25 f0  e9 ea 49 b2 04 ec d5 d5
0162:       5b fe 1e 4b 26 c9 a8 fc  4b 5a 41 3c d1 6a 8f 3d
0172:       39 11 4a b5 d2 84 2b d5  b8 c5 45 f6 ef a9 72 bf
0182:       18 dc 5d dc 18 53 57 59  0f b5 ce a4 2e 66 76 f1
0192:       47 bd b0 57 ed 40 1c 46  4a e2 b6 92 22 2e 9a fe
01a2:       87 9a c6 2b 71 30 2d 96  fa 45 f3 1d bc cb 31 9d
01b2:       5c 08 89 e6 f0 95 33 dd  17 f1 02 98 77 27 31 e0
01c2:       e2 3a 38 61 59 41 88 1f  49 8e 5e da db 2b 41 a0
01d2:       6c f4 70 25 2d b2 4c 27  91 f1 8f af d8 7c 2d 67
01e2:       2c cf 05 5e 91 7b 7d b2  4f 7f 7d 5f ef 87 ec 35
01f2:       59 96 87 3f f5 a1 b3 35  27 15 ae 98 cd 7c c3 8e
0202:       4f 2b 1f fb 00 e3 bc 4f  23 37 11 7b 8f f6 0e 28
0212:       99 2f dc aa 95 85 ed 6d  ca f6 04 3b 25 00 b9 c0
0222:       e3 a8 49 42 a1 f6 de ed  62 ad 74 26 8d 2f d3 ef
0232:       2a 72 2d ee d8 1e 83 46  05 3d 67 56 b7 59 82 59
0242:       99 49 50 3a a9 86 31 67  ce 95 82 0f 90 3f ab 25
CertUtil: -asn command completed successfully.
```

## Related topics

<dl> <dt>

[Sample Requests](sample-requests.md)
</dt> </dl>

 

 



