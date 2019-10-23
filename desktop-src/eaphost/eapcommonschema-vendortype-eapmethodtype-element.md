---
title: VendorType (EapMethodType) Element
description: Is the vendor defined type for the method.
ms.assetid: baa43e60-05e2-43f9-bb38-896725be76b4
keywords:
- VendorType element EAPHost
topic_type:
- apiref
api_name:
- VendorType
api_type:
- Schema
ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
api_location: 
ROBOTS: INDEX,FOLLOW
---

# VendorType (EapMethodType) Element

The **VendorType (EapMethodType)** element is the vendor defined type for the method.

The **VendorType** element is optional. If used, the **VendorType** is a unique number issued by Internet Assigned Numbers Authority (IANA).

``` syntax
<xs:element name="VendorType"
    type="unsignedInt"
 />
```

The **VendorType** element is defined by the [**EapMethodType**](eapcommonschema-eapmethodtype-complextype.md) complex type.

## Requirements



|                                     |                                                      |
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

 

 





