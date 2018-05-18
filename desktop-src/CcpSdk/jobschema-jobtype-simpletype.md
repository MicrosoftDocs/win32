---
Description: 'Defines the types of jobs that can run in the cluster.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '0001a648-0c15-4bfb-bd36-9fee3abd2554'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: JobType Simple Type
---

# JobType Simple Type

Defines the types of jobs that can run in the cluster.

``` syntax
<xs:simpleType name="JobType">
    <xs:restriction
        base="string"
    >
        <xs:enumeration
            value="Batch"
         />
        <xs:enumeration
            value="Admin"
         />
        <xs:enumeration
            value="Service"
         />
        <xs:enumeration
            value="Broker"
         />
    </xs:restriction>
</xs:simpleType>
```

## Enumeration values

The **JobType** simple type defines the following values.



| Value   | Description                                                                                            |
|---------|--------------------------------------------------------------------------------------------------------|
| Batch   | A normally scheduled job.<br/>                                                                   |
| Admin   | Commands which run immediately.<br/>                                                             |
| Service | A SOA-based service job.<br/>                                                                    |
| Broker  | A broker job which routes requests from a SOA-based client to an instance of a service job.<br/> |



## Requirements



|                    |                                           |
|--------------------|-------------------------------------------|
| Product<br/> | HPC Pack 2008 Client Utilities<br/> |



 

 




