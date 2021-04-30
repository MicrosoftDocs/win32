---
description: Specifies the list of wireless LAN networks to which a machine must not connect.
ms.assetid: 01db3f7e-1e27-4378-9c42-bc38192f9507
title: blockList (networkFilter) Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- blockList
api_type: 
- Schema
api_location: 
---

# blockList (networkFilter) Element

The blockList (networkFilter) element specifies the list of wireless LAN networks to which a machine must not connect.

``` syntax
<xs:element name="blockList">
    <xs:complexType>
        <xs:sequence>
            <xs:element name="network"
                type="networkItemType"
                maxOccurs="unbounded"
             />
            <xs:any
                processContents="lax"
                minOccurs="0"
                maxOccurs="unbounded"
                namespace="##other"
             />
        </xs:sequence>
    </xs:complexType>
</xs:element>
```

The **blockList** element is defined by the [**networkFilter**](wlan-policyschema-networkfilter-wlanpolicy-element.md) element.

## Child elements



| Element                                                        | Type                                                                     | Description                      |
|----------------------------------------------------------------|--------------------------------------------------------------------------|----------------------------------|
| [**network**](wlan-policyschema-network-blocklist-element.md) | [**networkItemType**](wlan-policyschema-networkitemtype-complextype.md) | The blocked network. <br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

**Definition context of element in schema**
</dt> <dt>

[**networkFilter**](wlan-policyschema-networkfilter-wlanpolicy-element.md)
</dt> <dt>

**Possible immediate parent element in schema instance**
</dt> <dt>

[**networkFilter (WLANPolicy)**](wlan-policyschema-networkfilter-wlanpolicy-element.md)
</dt> </dl>

 

 




