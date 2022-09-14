---
title: VendorId (EapMethodType) Element
description: Refers to the vendor who defined the method if the Type (EapMethodType) element is 254 (an expanded EAP method).
ms.assetid: 14992940-2fe5-4f85-91c0-1f61345ee90f
keywords:
- VendorId element EAPHost
topic_type:
- apiref
api_name:
- VendorId
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
ROBOTS: INDEX,FOLLOW
---

# VendorId (EapMethodType) Element

The **VendorId (EapMethodType)** element refers to the vendor who defined the method if the [**Type (EapMethodType)**](eapcommonschema-type-eapmethodtype-element.md) element is 254 (an expanded EAP method).

The **VendorId** is optional. If used, the **VendorId** is a unique number issued by Internet Assigned Numbers Authority (IANA).

``` syntax
<xs:element name="VendorId"
    type="unsignedInt"
 />
```

The **VendorId** element is defined by the [**EapMethodType**](eapcommonschema-eapmethodtype-complextype.md) complex type.

## Remarks

The [**AuthorId**](eapcommonschema-authorid-eapmethodtype-element.md) and **VendorId** elements do not need to be the same for a particular method.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



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

 

 





