---
title: AuthorId (EapMethodType) Element
description: Refers to the method author.
ms.assetid: '1eb16a50-25b8-4883-b9ff-fde329d8dd81'
keywords: ["AuthorId element EAPHost"]
topic_type:
- apiref
api_name:
- AuthorId
api_type:
- Schema
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



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



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

 

 





