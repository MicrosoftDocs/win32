---
Description: 'Defines the hardware resources that the scheduler can use to determine on which nodes the job can run.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'bc675a09-e461-4ec0-a744-5062e458ff59'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: UnitType Simple Type
---

# UnitType Simple Type

Defines the hardware resources that the scheduler can use to determine on which nodes the job can run.

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



## Requirements



|                    |                                           |
|--------------------|-------------------------------------------|
| Product<br/> | HPC Pack 2008 Client Utilities<br/> |



 

 




