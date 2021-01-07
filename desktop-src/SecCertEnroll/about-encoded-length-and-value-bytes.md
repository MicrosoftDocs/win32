---
description: The Length field in a TLV triplet identifies the number of bytes encoded in the Value field.
ms.assetid: d72371f9-fe55-468d-b15b-0f8948674619
title: Encoded Length and Value Bytes
ms.topic: article
ms.date: 05/31/2018
---

# Encoded Length and Value Bytes

The *Length* field in a TLV triplet identifies the number of bytes encoded in the *Value* field. The *Value* field contains the content being sent between computers. If the *Value* field contains fewer than 128 bytes, the *Length* field requires only one byte. Bit 7 of the *Length* field is zero (0) and the remaining bits identify the number of bytes of content being sent. If the *Value* field contains more than 127 bytes, bit 7 of the *Length* field is one (1) and the remaining bits identify the number of bytes needed to contain the length. Examples are shown in the following illustration.

![der tlv length byte](images/der-tlv-lengthbyte.png)

## Related topics

<dl> <dt>

[DER Transfer Syntax](about-der-transfer-syntax.md)
</dt> <dt>

[Encoded Tag Bytes](about-encoded-tag-bytes.md)
</dt> </dl>

 

 



