---
Description: 'Defines an array of tasks.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '58d9b7a1-c1d5-49e0-99d8-5a419ea3d27e'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: ArrayOfTask
---

# ArrayOfTask

Defines an array of tasks.

``` syntax
<xs:complexType name="ArrayOfTask">
    <xs:sequence>
        <xs:element name="Task"
            type="Task"
            minOccurs="0"
            maxOccurs="unbounded"
            nillable="true"
         />
    </xs:sequence>
</xs:complexType>
```

## Child elements



| Element                                         | Type                                    | Description        |
|-------------------------------------------------|-----------------------------------------|--------------------|
| [**Task**](schema-task-arrayoftask-element.md) | [**Task**](schema-task-complextype.md) | A task.<br/> |



## Remarks

The [**Tasks**](schema-tasks-job-element.md) element is of this type.

## Requirements



|                    |                                                  |
|--------------------|--------------------------------------------------|
| Product<br/> | Compute Cluster Pack Client Utilities<br/> |



## See also

<dl> <dt>

[Job Schema Complex Types](schema-job-complex-types.md)
</dt> </dl>

 

 




