---
Description: 'Defines the job priority values.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'c3f3e2b0-9f67-4bbc-afe2-9f3799da0940'
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
| Lowest      | The job has the lowest priority.<br/>   |
| BelowNormal | The job has below-normal priority.<br/> |
| Normal      | The job has normal priority.<br/>       |
| AboveNormal | The job has above-normal priority.<br/> |
| Highest     | The job has the highest priority.<br/>  |



## Requirements



|                    |                                                  |
|--------------------|--------------------------------------------------|
| Product<br/> | Compute Cluster Pack Client Utilities<br/> |



## See also

<dl> <dt>

[Job Schema Simple Types](schema-simple-types.md)
</dt> </dl>

 

 




