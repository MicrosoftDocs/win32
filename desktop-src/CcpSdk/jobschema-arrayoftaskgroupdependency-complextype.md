---
Description: 'Defines an array of task group dependencies.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'a10cd84f-b54d-435b-a6f3-793038cce006'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: ArrayOfTaskGroupDependency Complex Type
---

# ArrayOfTaskGroupDependency Complex Type

Defines an array of task group dependencies.

``` syntax
<xs:complexType name="ArrayOfTaskGroupDependency">
    <xs:sequence>
        <xs:element name="Parent"
            type="Parent"
            minOccurs="0"
            maxOccurs="unbounded"
         />
    </xs:sequence>
</xs:complexType>
```

## Child elements



| Element                                                               | Type                                           | Description                                                     |
|-----------------------------------------------------------------------|------------------------------------------------|-----------------------------------------------------------------|
| [**Parent**](jobschema-parent-arrayoftaskgroupdependency-element.md) | [**Parent**](jobschema-parent-complextype.md) | The parent of a parent/child task group dependency. <br/> |



## Requirements



|                    |                                           |
|--------------------|-------------------------------------------|
| Product<br/> | HPC Pack 2008 Client Utilities<br/> |



 

 




