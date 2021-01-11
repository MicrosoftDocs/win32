---
description: specifies the EAPHost configuration.
ms.assetid: 71ec3ed6-3670-46fc-a24b-580d15297437
title: EAPConfig (OneX) Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- EAPConfig
api_type: 
- Schema
api_location: 
---

# EAPConfig (OneX) Element

The **EAPConfig** (OneX) element specifies the EAPHost configuration.

Unlike most elements in the 802.1X profile schema, this element is in the `https://www.microsoft.com/provisioning/EapHostConfig` namespace. Its child elements are defined in the [eaphostconfig schema](../eaphost/eaphostconfigschema-schema.md). The [**EapHostConfig**](../eaphost/eaphostconfigschema-eaphostconfig-element.md) element is a child of the **EAPConfig** element.

``` syntax
<xs:element name="EAPConfig">
    <xs:complexType>
        <xs:sequence>
            <xs:any
                processContents="lax"
                minOccurs="1"
                maxOccurs="unbounded"
                namespace="##other"
             />
        </xs:sequence>
    </xs:complexType>
</xs:element>
```

The **EAPConfig** element is defined by the [**OneX**](onexschema-onex-element.md) element.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista, Windows XP with SP3 \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                |
| Redistributable<br/>          | Wireless LAN API for Windows XP with SP2<br/>                 |



## See also

<dl> <dt>

**Definition context of element in schema**
</dt> <dt>

[**OneX**](onexschema-onex-element.md)
</dt> <dt>

**Possible immediate parent element in schema instance**
</dt> <dt>

[**OneX**](onexschema-onex-element.md)
</dt> </dl>

 

 
