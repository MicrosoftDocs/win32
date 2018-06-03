---
title: Support RegisterEventManifest method
description: Registers an event manifest.
ms.assetid: 8FE654BE-8060-442E-91A0-2AF068062125
keywords:
- RegisterEventManifest method Access Execution Engine
- RegisterEventManifest method Access Execution Engine , Support interface
- Support interface Access Execution Engine , RegisterEventManifest method
topic_type:
- apiref
api_name:
- Support.RegisterEventManifest
api_location:
- AxeCore.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Support::RegisterEventManifest method

Registers an event manifest.

## Syntax


```C++
virtual HRESULT RegisterEventManifest() = 0;
```



## Parameters

This method has no parameters.

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Support**](support.md)
</dt> </dl>

 

 





