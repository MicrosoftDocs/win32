---
Description: 'Defines the parent of a parent/child task group relationship.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'f7f6d6a9-483e-4870-b5ac-c2d71975d5ae'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Parent Complex Type
---

# Parent Complex Type

Defines the parent of a parent/child task group relationship.

``` syntax
<xs:complexType name="Parent">
    <xs:sequence>
        <xs:element name="Child"
            minOccurs="0"
            maxOccurs="unbounded"
        >
            <xs:complexType>
                <xs:attribute name="GroupId"
                    type="int"
                 />
            </xs:complexType>
        </xs:element>
    </xs:sequence>
    <xs:attribute name="GroupId"
        type="int"
     />
</xs:complexType>
```

## Child elements



| Element                                         | Type | Description                                             |
|-------------------------------------------------|------|---------------------------------------------------------|
| [**Child**](jobschema-child-parent-element.md) |      | The child of the parent/child relationship. <br/> |



## Attributes



| Name    | Type | Description                                                   |
|---------|------|---------------------------------------------------------------|
| GroupId | int  | The child group identifier (inline complex type). <br/> |
| GroupId | int  | The parent group identifier.<br/>                       |



## Requirements



|                    |                                           |
|--------------------|-------------------------------------------|
| Product<br/> | HPC Pack 2008 Client Utilities<br/> |



 

 




