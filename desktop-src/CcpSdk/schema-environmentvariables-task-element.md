---
Description: 'Contains the list of the environment variables for the task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'dd216691-7caa-4012-b1c3-cb3ad0f7a8cc'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'EnvironmentVariables (Task)'
---

# EnvironmentVariables (Task)

Contains the list of the environment variables for the task.

``` syntax
<xs:element name="EnvironmentVariables"
    type="NameValueCollection1"
    maxOccurs="1"
    minOccurs="1"
    nillable="true"
 />
```

## Remarks

You must include this element as a child of the [**Task**](schema-task-arrayoftask-element.md) element but it does not have to have any children (you do not have to specify environment variables for the task).

## Requirements



|                    |                                                  |
|--------------------|--------------------------------------------------|
| Product<br/> | Compute Cluster Pack Client Utilities<br/> |



## See also

<dl> <dt>

[Job Schema Elements](schema-job-elements.md)
</dt> </dl>

 

 




