---
description: Indicates whether connection to a wireless LAN should be automatic or initiated by user.
ms.assetid: 0fad8392-3053-494b-9b30-1db85408a437
title: connectionMode (WLANProfile) Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- connectionMode
api_type: 
- Schema
api_location: 
---

# connectionMode (WLANProfile) Element

The connectionMode (WLANProfile) element indicates whether connection to a wireless LAN should be automatic or initiated by user.

If [**connectionType**](wlan-profileschema-connectiontype-wlanprofile-element.md) is set to ESS, this value can be either auto or manual. The default value is auto if this element is absent.

If [**connectionType**](wlan-profileschema-connectiontype-wlanprofile-element.md) is set to IBSS, this value must be manual.

``` syntax
<xs:element name="connectionMode">
    <xs:simpleType>
        <xs:restriction
            base="string"
        >
            <xs:enumeration
                value="auto"
             />
            <xs:enumeration
                value="manual"
             />
        </xs:restriction>
    </xs:simpleType>
</xs:element>
```

The **connectionMode** element is defined by the [**WLANProfile**](wlan-profileschema-wlanprofile-element.md) element.

## Remarks

The following table describes the enumeration values.



| Value  | Description                                                                                                |
|--------|------------------------------------------------------------------------------------------------------------|
| auto   | The connection to the wireless network should be initiated automatically whenever the network is in range. |
| manual | The connection to the wireless network is only initated upon the explicit request of a user.               |



 

## Examples

To view sample profiles that use the **connectionMode** element, see [Wireless Profile Samples](wireless-profile-samples.md).

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

[**WLANProfile**](wlan-profileschema-wlanprofile-element.md)
</dt> <dt>

**Possible immediate parent element in schema instance**
</dt> <dt>

[**WLANProfile**](wlan-profileschema-wlanprofile-element.md)
</dt> </dl>

 

 




