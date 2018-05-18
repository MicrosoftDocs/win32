---
Description: 'Represents the top-level element in the XML document.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '47a91387-e4ca-4dfb-a19d-aef1c37bceab'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Task
---

# Task

Represents the top-level element in the XML document.

``` syntax
<xs:element name="Task"
    type="Task"
    nillable="true"
 />
```

## Remarks

The XML document can contain only one **Task** element. The **Task** element defines the terms of the task, the application-defined extended terms used by the submission and activation filters, and any environment variables.

The **Task** element is of type [**Task**](schema-task-task-complextype.md).

## Requirements



|                    |                                                  |
|--------------------|--------------------------------------------------|
| Product<br/> | Compute Cluster Pack Client Utilities<br/> |



## See also

<dl> <dt>

[Task Schema Elements](schema-task-elements.md)
</dt> </dl>

 

 




