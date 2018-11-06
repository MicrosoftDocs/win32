---
title: Control
description: Identifies an object as an ActiveX Control.
ms.assetid: 2487e642-1d21-4811-87dd-b280be98a44b
keywords:
- Control registry key COM
ms.topic: article
ms.date: 05/31/2018
---

# Control

Identifies an object as an ActiveX Control.

## Registry Entry

```
HKEY_LOCAL_MACHINE\SOFTWARE\Classes\CLSID
   {CLSID}
      Control
```

## Remarks

This optional entry is used by containers to fill in dialog boxes. The container uses this subkey to determine whether to include an object in a dialog box that displays ActiveX Controls. A control can omit this entry if it is designed to work only with a specific container and therefore does is not intended to be inserted in other containers.

 

 




