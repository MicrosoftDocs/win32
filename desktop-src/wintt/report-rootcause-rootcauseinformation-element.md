---
title: RootCause (RootCauseInformation) Element
description: Identifies a root cause that the package can detect.
ms.assetid: b0445b52-4648-4938-a58f-544c720c7769
keywords:
- RootCause element Windows Troubleshooting Toolkit
topic_type:
- apiref
api_name:
- RootCause
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# RootCause (RootCauseInformation) Element

Identifies a root cause that the package can detect.

``` syntax
<xs:element name="RootCause"
    type="dcmRR:RootCause"
 />
```

The **RootCause** element is defined by the [**RootCauseInformation**](report-rootcauseinformation-complextype.md) complex type.

## Remarks

This node will contain two child **Data** elements that provide a description of the root cause and its status. For details of the properties, see the [**RootCause**](report-rootcause-complextype.md) complex type.

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

**Parent element**
</dt> <dt>

[**RootCauseInformation (Problem)**](report-rootcauseinformation-problem-element.md)
</dt> </dl>

 

 





