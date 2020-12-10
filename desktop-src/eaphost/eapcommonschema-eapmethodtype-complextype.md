---
title: EapMethodType Complex Type
description: Defines the elements that uniquely identify a single EAP method Type, VendorId, VendorType, and AuthorId.
ms.assetid: 3ef96187-7376-438d-9d47-a87d5a6c9b8b
keywords:
- EapMethodType complex type EAPHost
topic_type:
- apiref
api_name:
- EapMethodType
api_type:
- Schema
ms.topic: reference
ms.date: 05/31/2018
api_location: 
ROBOTS: INDEX,FOLLOW
---

# EapMethodType Complex Type

The **EapMethodType** complex type defines the elements that uniquely identify a single EAP method: [**Type**](eapcommonschema-type-eapmethodtype-element.md), [**VendorId**](eapcommonschema-vendorid-eapmethodtype-element.md), [**VendorType**](eapcommonschema-vendortype-eapmethodtype-element.md), and [**AuthorId**](eapcommonschema-authorid-eapmethodtype-element.md).

[**Type**](eapcommonschema-type-eapmethodtype-element.md) and [**AuthorId**](eapcommonschema-authorid-eapmethodtype-element.md) are mandatory elements, whereas [**VendorType**](eapcommonschema-vendortype-eapmethodtype-element.md) and [**VendorId**](eapcommonschema-vendorid-eapmethodtype-element.md) are required only when the **Type** element is 254 (an expanded EAP method).

``` syntax
<xs:complexType name="EapMethodType">
    <xs:sequence>
        <xs:element name="Type"
            type="unsignedByte"
         />
        <xs:element name="VendorId"
            type="unsignedInt"
            default="0"
            minOccurs="0"
         />
        <xs:element name="VendorType"
            type="unsignedInt"
            default="0"
            minOccurs="0"
         />
        <xs:element name="AuthorId"
            type="unsignedInt"
         />
    </xs:sequence>
</xs:complexType>
```

## Child elements



| Element                                                                | Type         | Description                                                                                                                                                                                                                                              |
|------------------------------------------------------------------------|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AuthorId**](eapcommonschema-authorid-eapmethodtype-element.md)     | unsignedInt  | Refers to the method author. <br/>                                                                                                                                                                                                                 |
| [**Type**](eapcommonschema-type-eapmethodtype-element.md)             | unsignedByte | Refers to the EAP method type. <br/>                                                                                                                                                                                                               |
| [**VendorId**](eapcommonschema-vendorid-eapmethodtype-element.md)     | unsignedInt  | Refers to the vendor who defined the method - if the [**Type**](eapcommonschema-type-eapmethodtype-element.md) element is 254 (an expanded EAP method). The [**VendorId**](eapcommonschema-vendorid-eapmethodtype-element.md) is optional. <br/> |
| [**VendorType**](eapcommonschema-vendortype-eapmethodtype-element.md) | unsignedInt  | Is the vendor defined type for the method. The [**VendorType**](eapcommonschema-vendortype-eapmethodtype-element.md) is optional. <br/>                                                                                                           |



## Remarks

The [**AuthorId**](eapcommonschema-authorid-eapmethodtype-element.md) and [**VendorId**](eapcommonschema-vendorid-eapmethodtype-element.md) elements do not need to be the same for a particular method.

The [**AuthorId**](eapcommonschema-authorid-eapmethodtype-element.md), [**Type**](eapcommonschema-type-eapmethodtype-element.md), [**VendorId**](eapcommonschema-vendorid-eapmethodtype-element.md) and [**VendorType**](eapcommonschema-vendortype-eapmethodtype-element.md) elements are each a unique number issued by the Internet Assigned Numbers Authority (IANA).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[EAPHost and Legacy Schema](eaphost-schemas.md)
</dt> <dt>

[eapcommon Schema](eapcommonschema-schema.md)
</dt> </dl>

 

 





