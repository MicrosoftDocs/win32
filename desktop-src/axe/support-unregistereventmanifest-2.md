---
title: Support UnregisterEventManifest method
description: Unregisters an event manifest.
ms.assetid: 7D8E908F-E0EE-407A-8E48-CD5361303628
keywords:
- UnregisterEventManifest method Access Execution Engine
- UnregisterEventManifest method Access Execution Engine , Support interface
- Support interface Access Execution Engine , UnregisterEventManifest method
topic_type:
- apiref
api_name:
- Support.UnregisterEventManifest
api_location:
- AxeCore.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Support::UnregisterEventManifest method

Unregisters an event manifest.

## Syntax


```C++
virtual HRESULT UnregisterEventManifest(
  [in] LPCWSTR manifestFileName
) = 0;
```



## Parameters

<dl> <dt>

*manifestFileName* \[in\]
</dt> <dd>

The name of the manifest file.

</dd> </dl>

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

 

 





