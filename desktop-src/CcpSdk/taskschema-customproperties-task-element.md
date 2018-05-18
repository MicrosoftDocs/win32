---
Description: 'Contains a collection of custom properties that are defined for the task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'afb19ac7-4607-43d6-9e20-3dff21a2ad6f'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'CustomProperties (Task) Element'
---

# CustomProperties (Task) Element

Contains a collection of custom properties that are defined for the task.

``` syntax
<xs:element name="CustomProperties"
    type="NameValueCollection1"
 />
```

The **CustomProperties** element is defined by the [**Task**](taskschema-task-complextype.md) complex type.

## Remarks

See [**ISchedulerTask::GetCustomProperties**](ischedulertask-getcustomproperties.md).

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

 

 




