---
description: A SET contains an unordered series of fields of one or more types.
ms.assetid: 6bbe89da-1177-4cfa-9515-03b271e5ef6b
title: SET
ms.topic: article
ms.date: 05/31/2018
---

# SET

A **SET** contains an unordered series of fields of one or more types. It is encoded into a TLV triplet that begins with a **Tag** byte of 0x31. The following example, adapted from the [CMC Encoded ASN.1](cmc-encoded-asn-1.md) topic, shows how a **ClientId** attribute is encoded in a **SET** data structure. The attribute can be specified by using the [**IX509AttributeClientId**](/windows/desktop/api/CertEnroll/nn-certenroll-ix509attributeclientid) interface.

``` syntax
31 59                                     ; SET (59 Bytes)
   30 57                                  ; SEQUENCE (57 Bytes)
      06 09                               ; OBJECT_ID (9 Bytes)
      |  2b 06 01 04 01 82 37 15  14      ;   1.3.6.1.4.1.311.21.20 
      31 4a                               ; SET (4a Bytes)
         30 48                            ; SEQUENCE (48 Bytes)
            02 01                         ; INTEGER (1 Bytes)
            |  09
            0c 23                         ; UTF8_STRING (23 Bytes)
            |  76 69 63 68 33 64 2e 6a    ;   vich3d.j
            |  64 6f 6d 63 73 63 2e 6e    ;   domcsc.n
            |  74 74 65 73 74 2e 6d 69    ;   ttest.mi
            |  63 72 6f 73 6f 66 74 2e    ;   crosoft.
            |  63 6f 6d                   ;   com
            0c 15                         ; UTF8_STRING (15 Bytes)
            |  4a 44 4f 4d 43 53 43 5c    ;   JDOMCSC\
            |  61 64 6d 69 6e 69 73 74    ;   administ
            |  72 61 74 6f 72             ;   rator
            0c 07                         ; UTF8_STRING 
```

If the **SET** contains fewer than 128 bytes, the **Length** field of the TLV triplet requires only one byte to specify the content length. If it is more than 127 bytes, bit 7 of the **Length** field is set to 1 and bits 6 through 0 specify the number of additional bytes used to identify the content length. For more information, see [Encoded Length and Value Bytes](about-encoded-length-and-value-bytes.md).

## Related topics

<dl> <dt>

[ASN.1 Type System](about-asn-1-type-system.md)
</dt> <dt>

[DER Encoding of ASN.1 Types](about-der-encoding-of-asn-1-types.md)
</dt> </dl>

 

 



