---
description: Specifies the length of time, in seconds, to wait before an EAPOL-Start is sent.
ms.assetid: 6163eeb9-23a8-4e34-ad3f-016946e241e2
title: startPeriod (OneX) Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- startPeriod
api_type: 
- Schema
api_location: 
---

# startPeriod (OneX) Element

The startPeriod (OneX) element specifies the length of time, in seconds, to wait before an EAPOL-Start is sent. An EAPOL-Start message is sent to start the 802.1X authentication process.

This element is optional. When startPeriod is not specified in a profile, a value of 5 seconds is used.

**Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element will be ignored if it is present in a profile.

``` syntax
<xs:element name="startPeriod">
    <xs:simpleType>
        <xs:restriction
            base="integer"
        >
            <xs:enumeration
                value="1"
             />
            <xs:enumeration
                value="3600"
             />
        </xs:restriction>
    </xs:simpleType>
</xs:element>
```

The **startPeriod** element is defined by the [**OneX**](onexschema-onex-element.md) element.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



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

 

 




