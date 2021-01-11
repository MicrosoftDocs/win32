---
description: Specifies the list of wireless LAN networks to which any machine must be allowed to connect.
ms.assetid: e24557d8-dedf-4381-bba0-cdb7ea26083b
title: allowList (networkFilter) Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- allowList
api_type: 
- Schema
api_location: 
---

# allowList (networkFilter) Element

The allowList (networkFilter) element specifies the list of wireless LAN networks to which any machine must be allowed to connect.

``` syntax
<xs:element name="allowList">
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

The **allowList** element is defined by the [**networkFilter**](wlan-policyschema-networkfilter-wlanpolicy-element.md) element.

## Child elements



| Element                                                        | Type                                                                     | Description                                              |
|----------------------------------------------------------------|--------------------------------------------------------------------------|----------------------------------------------------------|
| [**network**](wlan-policyschema-network-allowlist-element.md) | [**networkItemType**](wlan-policyschema-networkitemtype-complextype.md) | The network to which the machine can connect.<br/> |



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

 

 




