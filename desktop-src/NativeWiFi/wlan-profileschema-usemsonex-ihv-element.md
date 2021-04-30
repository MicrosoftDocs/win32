---
description: Specifies the origin of 802.1X security settings used by an IHV security component.
ms.assetid: 9c216319-d962-4c68-89a3-116eff3f4376
title: useMSOneX (IHV) Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- useMSOneX
api_type: 
- Schema
api_location: 
---

# useMSOneX (IHV) Element

The **useMSOneX** (IHV) element specifies the origin of 802.1X security settings used by an IHV security component.

When **useMSOneX** is true, IHV security components use Microsoft-defined 802.1X settings. When **useMSOneX** is false, IHV security components use vendor-supplied 802.1X settings.

**Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element is not supported.

``` syntax
<xs:element name="useMSOneX"
    type="boolean"
    minOccurs="0"
 />
```

The element is defined by the [**IHV**](wlan-profileschema-ihv-wlanprofile-element.md) element.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

**Definition context of element in schema**
</dt> <dt>

[**IHV**](wlan-profileschema-ihv-wlanprofile-element.md)
</dt> <dt>

**Possible immediate parent element in schema instance**
</dt> <dt>

[**IHV (WLANProfile)**](wlan-profileschema-ihv-wlanprofile-element.md)
</dt> </dl>

 

 




