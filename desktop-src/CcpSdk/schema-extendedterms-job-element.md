---
Description: 'Contains a collection of application-defined terms (properties) for the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '14ca42e2-9d9e-4179-a053-0ef765a5fc42'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ExtendedTerms (Job)'
---

# ExtendedTerms (Job)

Contains a collection of application-defined terms (properties) for the job.

``` syntax
<xs:element name="ExtendedTerms"
    type="NameValueCollection"
    maxOccurs="1"
    minOccurs="1"
    nillable="true"
 />
```

## Remarks

The [**Job**](schema-job-element.md) element must contain this element even if you do not define extended terms for your application.

## Requirements



|                    |                                                  |
|--------------------|--------------------------------------------------|
| Product<br/> | Compute Cluster Pack Client Utilities<br/> |



## See also

<dl> <dt>

[Job Schema Elements](schema-job-elements.md)
</dt> </dl>

 

 




