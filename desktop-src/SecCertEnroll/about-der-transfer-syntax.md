---
description: Applying an encoding rule to the data structures described by an abstract syntax provides a transfer syntax that governs how bytes in a stream are organized when sent between computers.
ms.assetid: 674e88f9-4b65-4b42-8c44-d24fc03ae2f3
title: DER Transfer Syntax
ms.topic: article
ms.date: 05/31/2018
---

# DER Transfer Syntax

Applying an encoding rule to the data structures described by an abstract syntax provides a transfer syntax that governs how bytes in a stream are organized when sent between computers. The transfer syntax used by Distinguished Encoding Rules always follows a *Tag, Length, Value* format. The format is usually referred to as a TLV triplet in which each field (T, L, or V) contains one or more bytes.

![der type, length, and value (tlv) triplet](images/der-tlv-basic.png)

The *Tag* field specifies the type of the data structure being sent, the *Length* field specifies the number of bytes of content being transferred, and the *Value* field contains the content. Note that the *Value* field can be a triplet if it contains a constructed data type as shown by the following illustration.

![der tlv triplet recursion](images/der-tlv-recursive.png)

See the following topics for detailed information about the components of a TLV triplet.

-   [Encoded Tag Bytes](about-encoded-tag-bytes.md)
-   [Encoded Length and Value Bytes](about-encoded-length-and-value-bytes.md)

## Related topics

<dl> <dt>

[Constructed Types](about-constructed-types.md)
</dt> <dt>

[Distinguished Encoding Rules](distinguished-encoding-rules.md)
</dt> </dl>

 

 



