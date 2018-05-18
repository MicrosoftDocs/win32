---
Description: 'Defines the hardware resources that the scheduler can use to determine on which nodes the task can run.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '711cee00-4806-45b9-8a3b-6048aaac1b1e'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: UnitType Simple Type
---

# UnitType Simple Type

Defines the hardware resources that the scheduler can use to determine on which nodes the task can run.

``` syntax
<xs:simpleType name="UnitType">
    <xs:restriction
        base="string"
    >
        <xs:enumeration
            value="Core"
         />
        <xs:enumeration
            value="Socket"
         />
        <xs:enumeration
            value="Node"
         />
    </xs:restriction>
</xs:simpleType>
```

## Enumeration values

The **UnitType** simple type defines the following values.



| Value  | Description                                 |
|--------|---------------------------------------------|
| Core   | Use cores to schedule the job.<br/>   |
| Socket | Use sockets to schedule the job.<br/> |
| Node   | Use nodes to schedule the job.<br/>   |



## Remarks

Use these strings to specify the value for the **UnitType** task attribute of the [**Task**](taskschema-task-complextype.md) complex type.

## Requirements



|                    |                                           |
|--------------------|-------------------------------------------|
| Product<br/> | HPC Pack 2008 Client Utilities<br/> |



 

 




