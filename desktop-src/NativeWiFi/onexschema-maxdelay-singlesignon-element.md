---
description: Specifies, in seconds, the maximum delay before the single sign on connection attempt fails.
ms.assetid: ba8c137e-dd05-4ebc-9a83-cd612f65d4dc
title: maxDelay (singleSignOn) Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- maxDelay
api_type: 
- Schema
api_location: 
---

# maxDelay (singleSignOn) Element

The maxDelay (singleSignOn) element specifies, in seconds, the maximum delay before the single sign on connection attempt fails.

This element is optional. When maxDelay is not specified in a profile, a value of 10 seconds is used.

**Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element will be ignored if it is present in a profile.

``` syntax
<xs:element name="maxDelay">
    <xs:simpleType>
        <xs:restriction
            base="integer"
        >
            <xs:enumeration
                value="0"
             />
            <xs:enumeration
                value="120"
             />
        </xs:restriction>
    </xs:simpleType>
</xs:element>
```

The **maxDelay** element is defined by the [**singleSignOn**](onexschema-singlesignon-onex-element.md) element.

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

 

 
