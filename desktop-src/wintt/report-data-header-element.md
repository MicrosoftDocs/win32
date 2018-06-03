---
title: Data (Header) Element
description: Identifies a property of the header section of the report.
ms.assetid: 421cf389-e8de-4632-a318-bf3890080c53
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

# Data (Header) Element

Identifies a property of the header section of the report.

``` syntax
<xs:element name="Data"
    type="dcmRR:Data"
 />
```

The **Data** element is defined by the [**Header**](report-header-complextype.md) complex type.

## Remarks

The [**Header (ResultReport)**](report-header-resultreport-element.md) node will contain two child **Data** elements that identify when the report ran and whether the user used elevated privileges to run the package. For details of the properties, see the [**Header**](report-header-complextype.md) complex type.

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

**Parent element**
</dt> <dt>

[**Header (ResultReport)**](report-header-resultreport-element.md)
</dt> </dl>

 

 





