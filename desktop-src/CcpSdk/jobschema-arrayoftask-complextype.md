---
Description: 'Defines an array of tasks.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'f221c4f7-ec5b-4630-acbe-6934e7b70fd3'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: ArrayOfTask Complex Type
---

# ArrayOfTask Complex Type

Defines an array of tasks.

``` syntax
<xs:complexType name="ArrayOfTask">
    <xs:sequence>
        <xs:element name="Task"
            type="Task"
            minOccurs="0"
            maxOccurs="unbounded"
         />
    </xs:sequence>
</xs:complexType>
```

## Child elements



| Element                                            | Type                                       | Description         |
|----------------------------------------------------|--------------------------------------------|---------------------|
| [**Task**](jobschema-task-arrayoftask-element.md) | [**Task**](jobschema-task-complextype.md) | A task. <br/> |



## Requirements



|                    |                                           |
|--------------------|-------------------------------------------|
| Product<br/> | HPC Pack 2008 Client Utilities<br/> |



 

 




