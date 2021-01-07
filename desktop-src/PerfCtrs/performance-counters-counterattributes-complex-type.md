---
description: Defines a list that contains up to five counter attributes.
ms.assetid: d710c3d2-2886-4f1a-bd27-f11451d2f3c6
title: counterAttributes Complex Type
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- kbSyntax
api_name: 
api_type: 
api_location: 
---

# counterAttributes Complex Type

Defines a list that contains up to five counter attributes.

``` syntax
<xs:complexType name="counterAttributes">
    <xs:choice
        minOccurs="1"
        maxOccurs="5"
    >
        <xs:element name="counterAttribute"
            type="man:counterAttribute"
         />
    </xs:choice>
</xs:complexType>
```

## Child elements



| Element              | Type                                                                               | Description                                                                                                |
|----------------------|------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| **counterAttribute** | [**man:counterAttribute**](performance-counters-counterattribute-complex-type.md) | A counter attribute that specifies how the counter data is displayed in a consumer application.<br/> |



## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



 

 




