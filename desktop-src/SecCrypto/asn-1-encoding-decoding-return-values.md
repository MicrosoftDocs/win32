---
description: The following table contains return values that may be returned by functions performing Abstract Syntax Notation One (ASN.1) encoding or decoding.
ms.assetid: cb1f34dd-dab4-4ffb-a73b-79a214290509
title: ASN.1 Encoding/Decoding Return Values
ms.topic: article
ms.date: 05/31/2018
---

# ASN.1 Encoding/Decoding Return Values

The following table contains return values that may be returned by functions performing [*Abstract Syntax Notation One*](../secgloss/a-gly.md) (ASN.1) encoding or decoding.



| Defined constant           | Text message                                      | Hexadecimal value |
|----------------------------|---------------------------------------------------|-------------------|
| CRYPT\_E\_ASN1\_ERROR      | ASN.1 Certificate encode/decode return value base | 0x80093100        |
| CRYPT\_E\_ASN1\_INTERNAL   | ASN.1 internal encode or decode error             | 0x80093101        |
| CRYPT\_E\_ASN1\_EOD        | ASN.1 unexpected end of data                      | 0x80093102        |
| CRYPT\_E\_ASN1\_CORRUPT    | ASN.1 corrupted data                              | 0x80093103        |
| CRYPT\_E\_ASN1\_LARGE      | ASN.1 value too large                             | 0x80093104        |
| CRYPT\_E\_ASN1\_CONSTRAINT | ASN.1 constraint violated                         | 0x80093105        |
| CRYPT\_E\_ASN1\_MEMORY     | ASN.1 out of memory                               | 0x80093106        |
| CRYPT\_E\_ASN1\_OVERFLOW   | ASN.1 buffer overflow                             | 0x80093107        |
| CRYPT\_E\_ASN1\_BADPDU     | ASN.1 function not supported for this PDU         | 0x80093108        |
| CRYPT\_E\_ASN1\_BADARGS    | ASN.1 bad arguments to function call              | 0x80093109        |
| CRYPT\_E\_ASN1\_BADREAL    | ASN.1 bad real value                              | 0x8009310A        |
| CRYPT\_E\_ASN1\_BADTAG     | ASN.1 bad tag value met                           | 0x8009310B        |
| CRYPT\_E\_ASN1\_CHOICE     | ASN.1 bad choice value                            | 0x8009310C        |
| CRYPT\_E\_ASN1\_RULE       | ASN.1 bad encoding rule                           | 0x8009310D        |
| CRYPT\_E\_ASN1\_UTF8       | ASN.1 bad Unicode (UTF8)                          | 0x8009310E        |
| CRYPT\_E\_ASN1\_PDU\_TYPE  | ASN.1 bad PDU type                                | 0x80093133        |
| CRYPT\_E\_ASN1\_NYI        | ASN.1 not yet implemented                         | 0x80093134        |
| CRYPT\_E\_ASN1\_EXTENDED   | ASN.1 skipped unknown extensions                  | 0x80093201        |
| CRYPT\_E\_ASN1\_NOEOD      | ASN.1 end of data expected                        | 0x80093202        |



 

 

 
