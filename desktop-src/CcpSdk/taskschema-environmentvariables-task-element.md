---
Description: 'Contains a collection of task-specific environment variables.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'a79ac9b2-c1d2-427e-9f83-c78eafcf7e34'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'EnvironmentVariables (Task) Element'
---

# EnvironmentVariables (Task) Element

Contains a collection of task-specific environment variables.

``` syntax
<xs:element name="EnvironmentVariables"
    type="NameValueCollection"
 />
```

The **EnvironmentVariables** element is defined by the [**Task**](taskschema-task-complextype.md) complex type.

## Remarks

See [**ISchedulerTask::EnvironmentVariables**](ischedulertask-environmentvariables.md).

## Requirements



|                    |                                           |
|--------------------|-------------------------------------------|
| Product<br/> | HPC Pack 2008 Client Utilities<br/> |



## See also

<dl> <dt>

**Definition context of element in schema**
</dt> <dt>

[**Task**](taskschema-task-complextype.md)
</dt> <dt>

**Possible immediate parent element in schema instance**
</dt> <dt>

[**Task**](taskschema-task-element.md)
</dt> </dl>

 

 




