---
description: The Tag field in a TLV triplet identifies the type of the data structure being sent between computers.
ms.assetid: 4723cc02-8c48-488e-95b8-c646a99b6aab
title: Encoded Tag Bytes
ms.topic: article
ms.date: 05/31/2018
---

# Encoded Tag Bytes

The *Tag* field in a TLV triplet identifies the type of the data structure being sent between computers. For example, the tag for an integer is 0x02, and the tag for an object identifier is 0x06. Although multiple bytes are permitted, none of the data types used by the Certificate Enrollment API require more than one. The following illustration shows the breakdown of a *Tag* value. Bits 7 and 6 identify the ASN.1 tagging class. There are four available classes, but the Certificate Enrollment API uses data types that belong only to the UNIVERSAL class. Bit 5 identifies whether the encoding form is primitive or constructed. Basic and string types are encoded by using primitive forms, constructed types by using a constructed form. For more information, see [ASN.1 Type System](about-asn-1-type-system.md). Bits 4 through 0 contain the tag number.

![der tlv tag byte](images/der-tlv-tagbyte.png)

The following table lists the data types supported by the Certificate Enrollment API, the encoding form used, and the tag value.

| Type              | ASN.1 class | Encoding form | Tag value                             |
|-------------------|-------------|---------------|---------------------------------------|
| BIT STRING        | UNIVERSAL   | Primitive     | 00000011<br/> (0x03)<br/> |
| BOOLEAN           | UNIVERSAL   | Primitive     | 00000001<br/> (0x01)<br/> |
| INTEGER           | UNIVERSAL   | Primitive     | 00000010<br/> (0x02)<br/> |
| NULL              | UNIVERSAL   | Primitive     | 00000101<br/> (0x05)<br/> |
| OBJECT IDENTIFIER | UNIVERSAL   | Primitive     | 00000110<br/> (0x06)<br/> |
| OCTET STRING      | UNIVERSAL   | Primitive     | 00000100<br/> (0x04)<br/> |
| BMPString         | UNIVERSAL   | Primitive     | 00011110<br/> (0x1E)<br/> |
| IA5String         | UNIVERSAL   | Primitive     | 00010110<br/> (0x16)<br/> |
| PrintableString   | UNIVERSAL   | Primitive     | 00010011<br/> (0x13)<br/> |
| TeletexString     | UNIVERSAL   | Primitive     | 00010100<br/> (0x14)<br/> |
| UTF8String        | UNIVERSAL   | Primitive     | 00001100<br/> (0x0C)<br/> |
| SEQUENCE          | UNIVERSAL   | Constructed   | 00110000<br/> (0x30)<br/> |
| SEQUENCE OF       | UNIVERSAL   | Constructed   | 00110000<br/> (0x30)<br/> |
| SET               | UNIVERSAL   | Constructed   | 00110001<br/> (0x31)<br/> |
| SET OF            | UNIVERSAL   | Constructed   | 00110001<br/> (0x31)<br/> |



 

## Related topics

<dl> <dt>

[DER Transfer Syntax](about-der-transfer-syntax.md)
</dt> <dt>

[Encoded Length and Value Bytes](about-encoded-length-and-value-bytes.md)
</dt> </dl>

 

 




