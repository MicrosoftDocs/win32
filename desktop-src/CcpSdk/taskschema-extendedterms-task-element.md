---
Description: 'Contains a collection of extended terms used by the task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '2961fc3d-6233-4e07-82bb-0a71a6b9fc82'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ExtendedTerms (Task) Element'
---

# ExtendedTerms (Task) Element

Contains a collection of extended terms used by the task. All HPC implementations should use [**CustomProperties**](taskschema-customproperties-task-element.md) instead.

**Microsoft Compute Cluster Server 2003 (CSS):** This is a CSS element included for backward compatibility.

``` syntax
<xs:element name="ExtendedTerms"
    type="NameValueCollection1"
 />
```

The **ExtendedTerms** element is defined by the [**Task**](taskschema-task-complextype.md) complex type.

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

 

 




