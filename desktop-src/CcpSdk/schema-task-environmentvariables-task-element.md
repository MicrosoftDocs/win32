---
Description: 'Defines the list of the environment variables for the task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '3f848b40-a4a6-4206-80b3-8f8b6cfc216d'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'EnvironmentVariables (Task)'
---

# EnvironmentVariables (Task)

Defines the list of the environment variables for the task.

``` syntax
<xs:element name="EnvironmentVariables"
    type="NameValueCollection"
    maxOccurs="1"
    minOccurs="1"
    nillable="true"
 />
```

## Remarks

You must include this element as a child of the [**Task**](schema-task-element.md) element but it does not have to have any children (you do not have to specify environment variables for the task).

## Requirements



|                    |                                                  |
|--------------------|--------------------------------------------------|
| Product<br/> | Compute Cluster Pack Client Utilities<br/> |



## See also

<dl> <dt>

[Task Schema Elements](schema-task-elements.md)
</dt> </dl>

 

 




