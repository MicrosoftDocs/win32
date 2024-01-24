---
description: Contains information about the creator of the profile.
ms.assetid: a3adb323-d1de-4026-976e-a106007f4cc2
title: ProfileCreationType (MBNProfile) Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ProfileCreationType
api_type: 
- Schema
---

# ProfileCreationType (MBNProfile) Element

The **ProfileCreationType (MBNProfile)** element contains information about the creator of the profile.

This element can have one of the following values.



| Value                 | Meaning                                                                                                                    |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------|
| "UserProvisioned"     | This profile is created by information provided by the user of device.                                                     |
| "AdminProvisioned"    | This profile is created by IT administrators and distributed to users.                                                     |
| "OperatorProvisioned" | This profile is created by a network operator and distributed to users.                                                    |
| "DeviceProvisioned"   | This profile is created by the Mobile Broadband service by using the information stored in the device provisioned context. |



 

This is an optional element.

``` syntax
<xs:element name="ProfileCreationType">
    <xs:simpleType>
        <xs:restriction
            base="token"
        >
            <xs:enumeration
                value="UserProvisioned"
             />
            <xs:enumeration
                value="AdminProvisioned"
             />
            <xs:enumeration
                value="OperatorProvisioned"
             />
            <xs:enumeration
                value="DeviceProvisioned"
             />
        </xs:restriction>
    </xs:simpleType>
</xs:element>
```

The **ProfileCreationType** element is defined by the [**MBNProfile**](schema-mbnprofile-element.md) element.

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

 

 




