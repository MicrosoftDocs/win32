---
title: AuthorId (EapMethodType) Element
description: Learn about the AuthorId (EapMethodType) element. The AuthorID (EapMethodType) element refers to the method author.
ms.assetid: 1eb16a50-25b8-4883-b9ff-fde329d8dd81
keywords:
- AuthorId element EAPHost
topic_type:
- apiref
api_name:
- AuthorId
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
ROBOTS: INDEX,FOLLOW
---

# AuthorId (EapMethodType) Element

The **AuthorId (EapMethodType)** element refers to the method author.

The AuthorId is a unique number issued by the Internet Assigned Numbers Authority (IANA).

``` syntax
<xs:element name="AuthorId"
    type="unsignedInt"
 />
```

The **AuthorId** element is defined by the [**EapMethodType**](eapcommonschema-eapmethodtype-complextype.md) complex type.

## Remarks

The **AuthorId** and [**VendorId**](eapcommonschema-vendorid-eapmethodtype-element.md) elements do not need to be the same for a particular method.

## Requirements



| Role | Minimum supported OS version |
|------|------------------------------|
| Client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

**Definition context of element in schema**
</dt> <dt>

[**EapMethodType**](eapcommonschema-eapmethodtype-complextype.md)
</dt> <dt>

[EAPHost and Legacy Schema](eaphost-schemas.md)
</dt> <dt>

[eapcommon Schema](eapcommonschema-schema.md)
</dt> </dl>

 

 





