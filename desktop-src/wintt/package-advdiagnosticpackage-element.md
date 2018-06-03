---
title: AdvDiagnosticPackage Element
description: The root node for a troubleshooting manifest that uses local troubleshooters to detect the root causes defined in the manifest.
ms.assetid: cd984c9f-3d08-4831-817c-fc710a6600fa
keywords:
- AdvDiagnosticPackage element Windows Troubleshooting Toolkit
topic_type:
- apiref
api_name:
- AdvDiagnosticPackage
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# AdvDiagnosticPackage Element

The root node for a troubleshooting manifest that uses local troubleshooters to detect the root causes defined in the manifest.

``` syntax
<xs:element name="AdvDiagnosticPackage"
    type="dcmPS:LocalDiagnosticPackage"
 />
```

## Remarks

This node and the [**DiagnosticPackage**](package-diagnosticpackage-element.md) node are mutually exclusive a troubleshooting manifest cannot contain both nodes.

## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



 

 





