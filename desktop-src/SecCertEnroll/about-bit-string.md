---
description: The BIT STRING data type is encoded into a TLV triplet that begins with a Tag byte of 0x03.
ms.assetid: 7464dd20-5e79-4ca1-a6ae-9b706e9cb925
title: BIT STRING
ms.topic: article
ms.date: 05/31/2018
---

# BIT STRING

The **BIT STRING** data type is encoded into a TLV triplet that begins with a **Tag** byte of 0x03. The **Value** field of the TLV triplet contains a leading byte that specifies the number of bits left unused in the final byte of content. In the following example, the **Length** field is set to 0x03 because three content bytes follow, and the leading byte of the **Value** field is set to 0x04 because there are four unused bits in the last content byte. Each unused bit is denoted by the letter x.

![der encoding of bit string data type](images/der-tlv-bitstring.png)

The following example, adapted from the [PKCS \#10 Encoded ASN.1](pkcs--10-encoded-asn-1.md) topic, shows the encoded signature of a sample PKCS \#10 certificate request. The first byte contains the **Tag** value for the **BIT STRING** data type, 0x03. The second and third bytes contain the length of the byte array. Bit 7 of the second byte is set to 1 because there are more than 127 bytes of content. Bits 0 through 6 of the second byte specify the number of trailing **Length** bytes, in this case one. The third byte specifies the number of content bytes, 0x81. The fourth byte, 0x00, specifies the number of unused bits that exist in the last content byte. Note that the signature is encoded in big-endian byte order.

``` syntax
0299:    03 81 81           ; BIT_STRING (81 Bytes)
029c:       00
029d:       47 eb 99 5a df 9e 70 0d  fb a7 31 32 c1 5f 5c 24
02ad:       c2 e0 bf c6 24 af 15 66  0e b8 6a 2e ab 2b c4 97
02bd:       1f e3 cb dc 63 a5 25 ec  c7 b4 28 61 66 36 a1 31
02cd:       1b bf dd d0 fc bf 17 94  90 1d e5 5e c7 11 5e c9
02dd:       55 9f eb a3 3e 14 c7 99  a6 cb ba a1 46 0f 39 d4
02ed:       44 c4 c8 4b 76 0e 20 5d  6d a9 34 9e d4 d5 87 42
02fd:       eb 24 26 51 14 90 b4 0f  06 5e 52 88 32 7a 95 20
030d:       a0 fd f7 e5 7d 60 dd 72  68 9b f5 7b 05 8f 6d 1e
```

## Related topics

<dl> <dt>

[ASN.1 Type System](about-asn-1-type-system.md)
</dt> <dt>

[DER Encoding of ASN.1 Types](about-der-encoding-of-asn-1-types.md)
</dt> <dt>

[Encoded Length and Value Bytes](about-encoded-length-and-value-bytes.md)
</dt> </dl>

 

 



