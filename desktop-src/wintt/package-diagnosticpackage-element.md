---
title: DiagnosticPackage Element
description: The root node for a troubleshooting manifest that uses a global troubleshooter to detect the root causes defined in the manifest.
ms.assetid: e4abec79-fe23-40bb-b129-8affd6081f62
keywords:
- DiagnosticPackage element Windows Troubleshooting Toolkit
topic_type:
- apiref
api_name:
- DiagnosticPackage
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DiagnosticPackage Element

The root node for a troubleshooting manifest that uses a global troubleshooter to detect the root causes defined in the manifest.

``` syntax
<xs:element name="DiagnosticPackage"
    type="dcmPS:GlobalDiagnosticPackage"
 />
```

## Remarks

This node and the [**AdvDiagnosticPackage**](package-advdiagnosticpackage-element.md) node are mutually exclusive a troubleshooting manifest cannot contain both nodes.

## Requirements



|                                     |                                                         |
|-------------------------------------|---------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/> |



 

 





