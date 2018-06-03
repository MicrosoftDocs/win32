---
title: Data (RootCause) Element
description: Identifies a property of a root cause.
ms.assetid: e4043ab4-bef6-4adb-b151-b003a2529b01
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

# Data (RootCause) Element

Identifies a property of a root cause.

``` syntax
<xs:element name="Data"
    type="dcmRR:Data"
 />
```

The **Data** element is defined by the [**RootCause**](report-rootcause-complextype.md) complex type.

## Remarks

The [**RootCause (RootCauseInformation)**](report-rootcause-rootcauseinformation-element.md) node will contain two child **Data** elements that provide a description of the root cause and its status. For details of the properties, see the [**RootCause**](report-rootcause-complextype.md) complex type.

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

**Parent element**
</dt> <dt>

[**RootCause (RootCauseInformation)**](report-rootcause-rootcauseinformation-element.md)
</dt> </dl>

 

 





