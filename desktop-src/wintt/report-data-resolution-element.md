---
title: Data (Resolution) Element
description: Identifies a property of a resolver.
ms.assetid: 3468740f-4267-43c7-9130-ab0910786e87
keywords:
- Data element Windows Troubleshooting Toolkit
topic_type:
- apiref
api_name:
- Data
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Data (Resolution) Element

Identifies a property of a resolver.

``` syntax
<xs:element name="Data"
    type="dcmRR:Data"
 />
```

The **Data** element is defined by the [**Resolution**](report-resolution-complextype.md) complex type.

## Remarks

The [**Resolution (ResolutionInformation)**](report-resolution-resolutioninformation-element.md) node will contain two child **Data** elements that provide a description of the resolver and its status. For details of the properties, see the [**Resolution**](report-resolution-complextype.md) complex type.

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

**Parent element**
</dt> <dt>

[**Resolution (ResolutionInformation)**](report-resolution-resolutioninformation-element.md)
</dt> </dl>

 

 





