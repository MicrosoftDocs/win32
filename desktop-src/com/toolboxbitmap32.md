---
title: ToolBoxBitmap32
description: Identifies the module name and resource ID for a 16 x 16 bitmap to use for the face of a toolbar or toolbox button.
ms.assetid: 87b3d8e1-4d54-465c-9e5e-5e4f7391f313
keywords:
- ToolBoxBitmap32 registry key COM
ms.topic: article
ms.date: 05/31/2018
---

# ToolBoxBitmap32

Identifies the module name and resource ID for a 16 x 16 bitmap to use for the face of a toolbar or toolbox button.

## Registry Entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Classes\CLSID
   {CLSID}
      ToolBoxBitmap32 = filename,  resourceID
```

## Remarks

This is a **REG\_SZ** value that specifies the module name and resource identifier for the bitmap.

The standard Windows icon size is too large to be used for this purpose. This requires control containers that have a design mode in which one selects controls and places them on a form being designed.

 

 




