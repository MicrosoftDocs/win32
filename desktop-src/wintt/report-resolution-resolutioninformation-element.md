---
title: Resolution (ResolutionInformation) Element
description: Identifies a resolver that the package can run to fix the root cause issue.
ms.assetid: ed033cf8-4330-4265-9d9a-8aadd03922aa
keywords:
- Resolution element Windows Troubleshooting Toolkit
topic_type:
- apiref
api_name:
- Resolution
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Resolution (ResolutionInformation) Element

Identifies a resolver that the package can run to fix the root cause issue.

``` syntax
<xs:element name="Resolution"
    type="dcmRR:Resolution"
 />
```

The **Resolution** element is defined by the [**ResolutionInformation**](report-resolutioninformation-complextype.md) complex type.

## Remarks

This node will contain two child **Data** elements that provide a description of the resolver and its status. For details of the properties, see the [**Resolution**](report-resolution-complextype.md) complex type.

## Requirements



|                                     |                                                      |
|-------------------------------------|------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>       |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

**Parent element**
</dt> <dt>

[**ResolutionInformation (RootCause)**](report-resolutioninformation-rootcause-element.md)
</dt> </dl>

 

 





