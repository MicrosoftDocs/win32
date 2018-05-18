---
Description: 'Contains a collection of extended terms that are defined for the job.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'c4d07fea-4312-4c44-b501-b597af09a7e8'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ExtendedTerms (Job) Element'
---

# ExtendedTerms (Job) Element

Contains a collection of extended terms that are defined for the job. All HPC implementations should use [**CustomProperties**](jobschema-customproperties-job-element.md) instead.

**Microsoft Compute Cluster Server 2003 (CSS):** This is a CSS element included for backward compatibility.

``` syntax
<xs:element name="ExtendedTerms"
    type="NameValueCollection"
 />
```

The **ExtendedTerms** element is defined by the [**Job**](jobschema-job-complextype.md) complex type.

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

 

 




