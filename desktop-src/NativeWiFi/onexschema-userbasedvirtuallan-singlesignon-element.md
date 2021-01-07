---
description: Specifies if the virtual LAN (VLAN) used by the device changes based on the user's credentials.
ms.assetid: 4ac92954-adb2-4b0c-9c4e-81f772ea03ed
title: userBasedVirtualLan (singleSignOn) Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- userBasedVirtualLan
api_type: 
- Schema
api_location: 
---

# userBasedVirtualLan (singleSignOn) Element

The userBasedVirtualLan (singleSignOn) element specifies if the virtual LAN (VLAN) used by the device changes based on the user's credentials. Some network access server (NAS) devices change the VLAN after a user authenticates. When userBasedVirtualLan is TRUE, the NAS may change a device's VLAN after a user authenticates.

This element is optional. When userBasedVirtualLan is not specified in a profile, a value of FALSE is used.

**Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element will be ignored if it is present in a profile.

``` syntax
<xs:element name="userBasedVirtualLan"
    type="boolean"
    minOccurs="0"
 />
```

The **userBasedVirtualLan** element is defined by the [**singleSignOn**](onexschema-singlesignon-onex-element.md) element.

## Remarks

This parameter can be set at the command line using the **netsh wlan set profileparameter** command. For more information, see [Netsh Commands for Wireless Local Area Network (wlan)](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc755301(v=ws.10)).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

**Definition context of element in schema**
</dt> <dt>

[**singleSignOn**](onexschema-singlesignon-onex-element.md)
</dt> <dt>

**Possible immediate parent element in schema instance**
</dt> <dt>

[**singleSignOn (OneX)**](onexschema-singlesignon-onex-element.md)
</dt> </dl>

 

 
