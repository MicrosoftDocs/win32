---
description: The OBJECT IDENTIFIER data type is encoded into a TLV triplet that begins with a Tag value of 0x06.
ms.assetid: 42c015c8-3de1-4482-bf27-b19c422b8cdb
title: OBJECT IDENTIFIER
ms.topic: article
ms.date: 05/31/2018
---

# OBJECT IDENTIFIER

The **OBJECT IDENTIFIER** data type is encoded into a TLV triplet that begins with a **Tag** value of 0x06. Each integer of a dotted decimal object identifier (OID) is encoded according to the following rules:

-   The first two nodes of the OID are encoded onto a single byte. The first node is multiplied by the decimal 40 and the result is added to the value of the second node.
-   Node values less than or equal to 127 are encoded on one byte.
-   Node values greater than or equal to 128 are encoded on multiple bytes. Bit 7 of the leftmost byte is set to one. Bits 0 through 6 of each byte contains the encoded value.

These points are shown by the following illustration.

![der encoding of the object identifier data type](images/der-tlv-oid.png)

The following example shows how the **ClientId** attribute is encoded in a certificate request.

``` syntax
06 09                                ; OBJECT_ID (9 Bytes)
|  2b 06 01 04 01 82 37 15  14       ;   1.3.6.1.4.1.311.21.20 
31 4a                                ; SET (4a Bytes)
   30 48                             ; SEQUENCE (48 Bytes)
      02 01                          ; INTEGER (1 Bytes)
      |  09
      0c 23                          ; UTF8_STRING (23 Bytes)
      |  76 69 63 68 33 64 2e 6a     ;   vich3d.j
      |  64 6f 6d 63 73 63 2e 6e     ;   domcsc.n
      |  74 74 65 73 74 2e 6d 69     ;   ttest.mi
      |  63 72 6f 73 6f 66 74 2e     ;   crosoft.
      |  63 6f 6d                    ;   com
      0c 15                          ; UTF8_STRING (15 Bytes)
      |  4a 44 4f 4d 43 53 43 5c     ;   JDOMCSC\
      |  61 64 6d 69 6e 69 73 74     ;   administ
      |  72 61 74 6f 72              ;   rator
      0c 07                          ; UTF8_STRING (7 Bytes)
         63 65 72 74 72 65 71        ;   certreq
```

 

 



