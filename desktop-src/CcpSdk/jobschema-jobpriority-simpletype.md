---
Description: 'Defines the job priority values.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '6baf2a64-71ae-4fa8-bdf9-58bb386dd729'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: JobPriority Simple Type
---

# JobPriority Simple Type

Defines the job priority values.

``` syntax
<xs:simpleType name="JobPriority">
    <xs:restriction
        base="string"
    >
        <xs:enumeration
            value="Lowest"
         />
        <xs:enumeration
            value="BelowNormal"
         />
        <xs:enumeration
            value="Normal"
         />
        <xs:enumeration
            value="AboveNormal"
         />
        <xs:enumeration
            value="Highest"
         />
    </xs:restriction>
</xs:simpleType>
```

## Enumeration values

The **JobPriority** simple type defines the following values.



| Value       | Description                                   |
|-------------|-----------------------------------------------|
| Lowest      | The job has the lowest priority. <br/>  |
| BelowNormal | The job has below-normal priority.<br/> |
| Normal      | The job has normal priority.<br/>       |
| AboveNormal | The job has above-normal priority.<br/> |
| Highest     | The job has the highest priority.<br/>  |



## Requirements



|                    |                                           |
|--------------------|-------------------------------------------|
| Product<br/> | HPC Pack 2008 Client Utilities<br/> |



 

 




