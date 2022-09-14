---
description: Specifies the length of time, in seconds, in which a client will not re-attempt authentication after a failed authentication attempt.
ms.assetid: a6b32e88-da36-4aea-a01d-f5f7bc37d171
title: heldPeriod (OneX) Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- heldPeriod
api_type: 
- Schema
api_location: 
---

# heldPeriod (OneX) Element

The heldPeriod (OneX) element specifies the length of time, in seconds, in which a client will not re-attempt authentication after a failed authentication attempt.

This element is optional. When heldPeriod is not specified in a profile, a value of 1 second is used.

**Windows XP with SP3 and Wireless LAN API for Windows XP with SP2:** This element will be ignored if it is present in a profile.

``` syntax
<xs:element name="heldPeriod">
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

The **heldPeriod** element is defined by the [**OneX**](onexschema-onex-element.md) element.

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

 

 




