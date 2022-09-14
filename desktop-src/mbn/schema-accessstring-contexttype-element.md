---
description: Identifies the APN or dial string to be used to establish a data connection.
ms.assetid: e791ffa1-b417-480c-adb8-b1dda7547d89
title: AccessString (contextType) Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- AccessString
api_type: 
- Schema
---

# AccessString (contextType) Element

The **AccessString (contextType)** element identifies the APN or dial string to be used to establish a data connection.

This element can have a maximum length of 100 characters.

This element is optional.

``` syntax
<xs:element name="AccessString">
    <xs:simpleType>
        <xs:restriction
            base="token"
        >
            <xs:minLength
                value="1"
             />
            <xs:maxLength
                value="100"
             />
        </xs:restriction>
    </xs:simpleType>
</xs:element>
```

The **AccessString** element is defined by the [**contextType**](schema-contexttype-complextype.md) complex type.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps \| UWP apps\]<br/> |
| Minimum supported server<br/> | None supported<br/>                         |



## See also

<dl> <dt>

**Definition context of element in schema**
</dt> <dt>

[**contextType**](schema-contexttype-complextype.md)
</dt> <dt>

**Possible immediate parent element in schema instance**
</dt> <dt>

[**Context (MBNProfile)**](schema-context-mbnprofile-element.md)
</dt> </dl>

 

 




