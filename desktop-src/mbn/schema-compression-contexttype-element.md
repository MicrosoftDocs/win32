---
description: Specifies if compression will be used at the data link for header and data transfer.
ms.assetid: 2aee93e4-d124-43cb-b974-19f00eb4d6a6
title: Compression (contextType) Element
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Compression
api_type: 
- Schema
---

# Compression (contextType) Element

The **Compression (contextType)** element specifies if compression will be used at the data link for header and data transfer.

This element can be one of the following values.

| Value     | Meaning                       |
|-----------|-------------------------------|
| "ENABLE"  | Compression will be used.     |
| "DISABLE" | Compression will not be used. |



 

This element is optional. If this element is not specified, then the Mobile Broadband system will not use compression.

``` syntax
<xs:element name="Compression">
    <xs:simpleType>
        <xs:restriction
            base="token"
        >
            <xs:enumeration
                value="DISABLE"
             />
            <xs:enumeration
                value="ENABLE"
             />
        </xs:restriction>
    </xs:simpleType>
</xs:element>
```

The **Compression** element is defined by the [**contextType**](schema-contexttype-complextype.md) complex type.

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

 

 




