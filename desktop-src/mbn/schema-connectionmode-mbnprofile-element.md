---
description: Specifies the auto connection setting to be used for a Mobile Broadband device.
ms.assetid: 789016d5-47f1-4506-bcb9-1a4019d236fd
title: ConnectionMode (MBNProfile) Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ConnectionMode
api_type: 
- Schema
---

# ConnectionMode (MBNProfile) Element

The **ConnectionMode (MBNProfile)** element specifies the auto connection setting to be used for a Mobile Broadband device.

This element can have one of the following values.



| Value       | Meaning                                                                |
|-------------|------------------------------------------------------------------------|
| "manual"    | Never automatically connect to the network.                            |
| "auto"      | Always automatically connect to the network.                           |
| "auto-home" | Automatically connect to the network except when in a roaming network. |



 

This element can have a maximum of one occurrence.

This is a required element.

``` syntax
<xs:element name="ConnectionMode">
    <xs:simpleType>
        <xs:restriction
            base="string"
        >
            <xs:enumeration
                value="manual"
             />
            <xs:enumeration
                value="auto"
             />
            <xs:enumeration
                value="auto-home"
             />
        </xs:restriction>
    </xs:simpleType>
</xs:element>
```

The **ConnectionMode** element is defined by the [**MBNProfile**](schema-mbnprofile-element.md) element.

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

 

 




