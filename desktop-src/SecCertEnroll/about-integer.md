---
description: Integer values are encoded into a TLV triplet that begins with a Tag value of 0x02.
ms.assetid: a6fed62f-af59-488c-a690-be8c3413086f
title: INTEGER (Certificate Enrollment API)
ms.topic: article
ms.date: 05/31/2018
---

# INTEGER (Certificate Enrollment API)

Integer values are encoded into a TLV triplet that begins with a **Tag** value of 0x02. The **Value** field of the TLV triplet contains the encoded integer if it is positive, or its two's complement if it is negative. If the integer is positive but the high order bit is set to 1, a leading 0x00 is added to the content to indicate that the number is not negative. For example, the high order byte of 0x8F (10001111) is 1. Therefore a leading zero byte is added to the content as shown in the following illustration.

![der encoding of boolean data type](images/der-tlv-integer.png)

If the integer contains fewer than 128 bytes, the *Length* field requires only one byte to specify the content length. If the integer is more than 127 bytes, bit 7 of the *Length* field is set to 1 and bits 6 through 0 specify the number of additional bytes used to identify the content length. For more information, see [Encoded Length and Value Bytes](about-encoded-length-and-value-bytes.md).

The following example, from [PKCS \#10 Encoded ASN.1](pkcs--10-encoded-asn-1.md), shows the encoding for a 128 byte public key. The first byte contains the **Tag** value for the **INTEGER** data type, 0x02. The second and third bytes contain the **Length** value. Bit 7 of the second byte is set to 1 because there are more than 127 bytes of content. Bits 0 through 6 of the second byte specify the number of trailing bytes needed, in this case one, to accurately specify the content length. The third byte specifies the number of content bytes, 0x81. The fourth byte, 0x00, is added to the content to indicate that the integer is indeed a positive value even though the sign bit of the leading content byte (0x8F) is set to 1.

``` syntax
02 81 81          ; INTEGER (81 Bytes)
|  00
|  8f e2 41 2a 08 e8 51 a8  8c b3 e8 53 e7 d5 49 50
|  b3 27 8a 2b cb ea b5 42  73 ea 02 57 cc 65 33 ee
|  88 20 61 a1 17 56 c1 24  18 e3 a8 08 d3 be d9 31
|  f3 37 0b 94 b8 cc 43 08  0b 70 24 f7 9c b1 8d 5d
|  d6 6d 82 d0 54 09 84 f8  9f 97 01 75 05 9c 89 d4
|  d5 c9 1e c9 13 d7 2a 6b  30 91 19 d6 d4 42 e0 c4
|  9d 7c 92 71 e1 b2 2f 5c  8d ee f0 f1 17 1e d2 5f
|  31 5b b1 9c bc 20 55 bf  3a 37 42 45 75 dc 90 65
```

The following example shows how the integer value 0x03 is encoded. The **Tag** byte contains 0x02, and the **Length** byte specifies that there is one byte of content.

``` syntax
02 01             ; INTEGER (1 Bytes)
|  03
```

## Related topics

<dl> <dt>

[ASN.1 Type System](about-asn-1-type-system.md)
</dt> <dt>

[DER Encoding of ASN.1 Types](about-der-encoding-of-asn-1-types.md)
</dt> </dl>

 

 



