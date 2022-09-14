---
description: The ASN.1 OCTET STRING data type is encoded into a TLV triplet that begins with a Tag byte of 0x04.
ms.assetid: 9d07a6c8-a15f-4030-838c-3063e315684f
title: OCTET STRING
ms.topic: article
ms.date: 05/31/2018
---

# OCTET STRING

The ASN.1 **OCTET STRING** data type is encoded into a TLV triplet that begins with a **Tag** byte of 0x04. The **OCTET STRING** and [BIT STRING](about-bit-string.md) data types are very similar. Thus, the two types are encoded in a similar manner except that, because the trailing byte of an **OCTET STRING** cannot have unused bits, no leading bytes must be added to the content. The following example, adapted from the [CMC Encoded ASN.1](cmc-encoded-asn-1.md) topic, shows how the name of a certificate template is encoded as a byte array.

``` syntax
30 17                                 ; SEQUENCE (17 Bytes)
|  06 09                              ; OBJECT_ID (9 Bytes)
|  |  2b 06 01 04 01 82 37 14  02     ;   1.3.6.1.4.1.311.20.2
|  04 0a                              ; OCTET_STRING (a Bytes)
|     1e 08 00 55 00 73 00 65  00 72  ;   ...U.s.e.r
```

If the byte array contains fewer than 128 bytes, the **Length** field of the TLV triplet requires only one byte to specify the content length. If it is more than 127 bytes, bit 7 of the **Length** field is set to 1 and bits 6 through 0 specify the number of additional bytes used to identify the content length. This is shown in the following example where the high order bit of the second byte on the first line is set to 1 and the byte indicates that there is a trailing **Length** byte. The third byte therefore specifies that the content is 0x80 bytes long.

``` syntax
04 81 80                       ; OCTET_STRING (80 Bytes)
   38 10 60 e2 70 69 91 4a     ;   8.`.pi.J
   8b b5 22 57 2a 62 ef de     ;   .."W*b..
   15 7d 59 d6 4e 20 9a 45     ;   .}Y.N .E
   2b e3 fd fc 68 ba af bf     ;   +...h...
   9c 17 b0 8e 6d c4 29 1e     ;   ....m.).
   e3 21 ac bb 5a 8a c9 67     ;   .!..Z..g
   0a d4 45 93 10 c0 26 eb     ;   ..E...&.
   0a 83 c2 b1 40 87 36 f7     ;   ....@.6.
   a0 26 da b9 bb 46 73 88     ;   .&...Fs.
   7a 67 b9 e6 b3 6f ea 59     ;   zg...o.Y
   28 8a d3 92 72 f6 7b 89     ;   (...r.{.
   a0 d8 2d 9e 40 eb 1e bb     ;   ..-.@...
   6e ae f0 5a ed 16 c9 e3     ;   n..Z....
   27 59 37 8f f3 4a 98 60     ;   'Y7..J.`
   f8 fb a7 0a ee 1b 6e 91     ;   ......n.
   95 96 cf 0d 56 ac ab 35     ;   ....V..5
```

## Related topics

<dl> <dt>

[ASN.1 Type System](about-asn-1-type-system.md)
</dt> <dt>

[DER Encoding of ASN.1 Types](about-der-encoding-of-asn-1-types.md)
</dt> </dl>

 

 



