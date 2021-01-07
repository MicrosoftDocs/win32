---
description: The ASN.1 IA5tring data type is encoded into a TLV triplet that begins with a Tag byte of 0x16.
ms.assetid: c1268524-4304-4c21-8f7d-f0a2826cd74e
title: IA5String
ms.topic: article
ms.date: 05/31/2018
---

# IA5String

The ASN.1 **IA5tring** data type is encoded into a TLV triplet that begins with a **Tag** byte of 0x16. The following example, adapted from the [CMC Encoded ASN.1](cmc-encoded-asn-1.md) topic, shows how the **OSVersion** attribute is encoded as an **IA5tring** type. The version number can be specified by using the [**IX509AttributeOSVersion**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509attributeosversion) interface. The object identifier for the attribute is 1.3.6.1.4.1.311.13.2.3.

``` syntax
06 0a                                   ; OBJECT_ID (a Bytes)
|  2b 06 01 04 01 82 37 0d  02 03       ;   1.3.6.1.4.1.311.13.2.3 
31 0c                                   ; SET (c Bytes)
   16 0a                                ; IA5_STRING (a Bytes)
      36 2e 30 2e 35 33 36 31  2e 32    ;   6.0.5361.2
```

If the string contains fewer than 128 bytes, the **Length** field of the TLV triplet requires only one byte to specify the content length. If the string is more than 127 bytes, bit 7 of the **Length** field is set to 1 and bits 6 through 0 specify the number of additional bytes used to identify the content length. For more information, see [Encoded Length and Value Bytes](about-encoded-length-and-value-bytes.md).

## Related topics

<dl> <dt>

[ASN.1 Type System](about-asn-1-type-system.md)
</dt> <dt>

[DER Encoding of ASN.1 Types](about-der-encoding-of-asn-1-types.md)
</dt> </dl>

 

 



