---
Description: 'Defines the child of a parent/child task group relationship.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '0fc73237-077f-4c93-84ed-3d4e3fed1b68'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'Child (Parent) Element'
---

# Child (Parent) Element

Defines the child of a parent/child task group relationship.

``` syntax
<xs:element name="Child">
    <xs:complexType>
        <xs:attribute name="GroupId"
            type="int"
         />
    </xs:complexType>
</xs:element>
```

The **Child** element is defined by the [**Parent**](jobschema-parent-complextype.md) complex type.

## Attributes



| Name    | Type | Description                             |
|---------|------|-----------------------------------------|
| GroupId | int  | The child group identifier. <br/> |



## Requirements



|                    |                                           |
|--------------------|-------------------------------------------|
| Product<br/> | HPC Pack 2008 Client Utilities<br/> |



## See also

<dl> <dt>

**Definition context of element in schema**
</dt> <dt>

[**Parent**](jobschema-parent-complextype.md)
</dt> <dt>

**Possible immediate parent element in schema instance**
</dt> <dt>

[**Parent (ArrayOfTaskGroupDependency)**](jobschema-parent-arrayoftaskgroupdependency-element.md)
</dt> </dl>

 

 




