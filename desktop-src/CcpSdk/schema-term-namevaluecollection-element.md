---
Description: 'Defines an extended term for a job or task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'addf3c77-cf08-4c78-b616-ad119c197913'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'Term (NameValueCollection)'
---

# Term (NameValueCollection)

Defines an extended term for a job or task.

``` syntax
<xs:element name="Term"
    type="NameValue"
    minOccurs="0"
    maxOccurs="unbounded"
    nillable="true"
 />
```

## Remarks

This element is a child of the [**ExtendedTerms (Job)**](schema-extendedterms-job-element.md) element for a job and a child of the [**ExtendedTerms (Task)**](schema-extendedterms-task-element.md) element for a task.

## Requirements



|                    |                                                  |
|--------------------|--------------------------------------------------|
| Product<br/> | Compute Cluster Pack Client Utilities<br/> |



## See also

<dl> <dt>

[Job Schema Elements](schema-job-elements.md)
</dt> </dl>

 

 




