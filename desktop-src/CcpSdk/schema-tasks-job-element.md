---
Description: 'Contains a collection of tasks to run.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '3bdce1d6-8f91-4c99-b068-3899f1d07c74'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'Tasks (Job)'
---

# Tasks (Job)

Contains a collection of tasks to run.

``` syntax
<xs:element name="Tasks"
    type="ArrayOfTask"
    minOccurs="1"
    maxOccurs="1"
    nillable="true"
 />
```

## Remarks

The [**Job**](schema-job-element.md) element must contain this element even if you do not define tasks for your job.

## Requirements



|                    |                                                  |
|--------------------|--------------------------------------------------|
| Product<br/> | Compute Cluster Pack Client Utilities<br/> |



## See also

<dl> <dt>

[Job Schema Elements](schema-job-elements.md)
</dt> </dl>

 

 




