---
description: Specifies the list of preferred network providers at the time of roaming.
ms.assetid: 5873fcd7-8e89-4edd-8dc5-f43675919c55
title: DataRoamingPartners (MBNProfile) Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DataRoamingPartners
api_type: 
- Schema
---

# DataRoamingPartners (MBNProfile) Element

The **DataRoamingPartners (MBNProfile)** element specifies the list of preferred network providers at the time of roaming.

The Mobile Broadband service uses this element to select the preferred network provide while roaming.

The element has the following child element which must be defined at least once but can be defined multiple times.

-   [**Provider**](schema-provider-dataroamingpartners-element.md)

This element can have a maximum of one occurrence.

This element is optional.

``` syntax
<xs:element name="DataRoamingPartners">
    <xs:complexType>
        <xs:sequence>
            <xs:element name="Provider"
                type="providerType"
                maxOccurs="unbounded"
             />
        </xs:sequence>
    </xs:complexType>
</xs:element>
```

The **DataRoamingPartners** element is defined by the [**MBNProfile**](schema-mbnprofile-element.md) element.

## Child elements



| Element                                                         | Type                                                    | Description                                            |
|-----------------------------------------------------------------|---------------------------------------------------------|--------------------------------------------------------|
| [**Provider**](schema-provider-dataroamingpartners-element.md) | [**providerType**](schema-providertype-complextype.md) | Name and provider ID of a cellular network.<br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps \| UWP apps\]<br/> |
| Minimum supported server<br/> | None supported<br/>                         |



## See also

<dl> <dt>

**Definition context of element in schema**
</dt> <dt>

[**MBNProfile**](schema-mbnprofile-element.md)
</dt> <dt>

**Possible immediate parent element in schema instance**
</dt> <dt>

[**MBNProfile**](schema-mbnprofile-element.md)
</dt> </dl>

 

 




