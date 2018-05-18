---
Description: 'Represents the top-level element in the XML document.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '9e90a3d9-81c4-4cba-bd34-3fb053d213fe'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Job
---

# Job

Represents the top-level element in the XML document.

``` syntax
<xs:element name="Job"
    type="Job"
    nillable="true"
 />
```

## Remarks

The XML document can contain only one **Job** element. The **Job** element defines the terms of the job, the application-defined extended terms used by the submission and activation filters, and the tasks to run.

The **Job** element is of type [**Job**](schema-job-complextype.md).

## Requirements



|                    |                                                  |
|--------------------|--------------------------------------------------|
| Product<br/> | Compute Cluster Pack Client Utilities<br/> |



## See also

<dl> <dt>

[Job Schema Elements](schema-job-elements.md)
</dt> </dl>

 

 




