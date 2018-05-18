---
Description: 'Contains a collection of custom properties that are defined for the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '7cafc5ba-9a68-4814-b82a-19c3760e0eb7'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'CustomProperties (Job) Element'
---

# CustomProperties (Job) Element

Contains a collection of custom properties that are defined for the job.

``` syntax
<xs:element name="CustomProperties"
    type="NameValueCollection"
 />
```

The **CustomProperties** element is defined by the [**Job**](jobschema-job-complextype.md) complex type.

## Remarks

See [**ISchedulerJob::GetCustomProperties**](ischedulerjob-getcustomproperties.md).

## Requirements



|                    |                                           |
|--------------------|-------------------------------------------|
| Product<br/> | HPC Pack 2008 Client Utilities<br/> |



## See also

<dl> <dt>

**Definition context of element in schema**
</dt> <dt>

[**Job**](jobschema-job-complextype.md)
</dt> <dt>

**Possible immediate parent element in schema instance**
</dt> <dt>

[**Job**](jobschema-job-element.md)
</dt> </dl>

 

 




