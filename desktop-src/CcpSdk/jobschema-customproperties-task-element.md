---
Description: 'Contains a collection of custom properties that are defined for the task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '64891bcc-34ff-4e3b-8c68-2a9384f0a05c'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'CustomProperties (Task) Element'
---

# CustomProperties (Task) Element

Contains a collection of custom properties that are defined for the task.

``` syntax
<xs:element name="CustomProperties"
    type="NameValueCollection"
 />
```

The **CustomProperties** element is defined by the [**Task**](jobschema-job-complextype.md) complex type.

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

[**Task**](jobschema-task-complextype.md)
</dt> <dt>

**Possible immediate parent element in schema instance**
</dt> <dt>

[**Task**](jobschema-task-arrayoftask-element.md)
</dt> </dl>

 

 




