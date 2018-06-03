---
title: IpcUninitializeEnvironment function
description: Un-initializes the environment.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 5F1CD228-11D8-4577-AC3F-34F1561C93E1
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- IpcUninitializeEnvironment function Active Directory Rights Management Services SDK 2.0
topic_type:
- apiref
api_name:
- IpcUninitializeEnvironment
api_location:
- Msipc.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IpcUninitializeEnvironment function

Un-initializes the environment. This method should be called before exiting the application and after all Rights Management Services SDK 2.1 methods have returned. No other RMS SDK 2.1 methods should be called after **IpcUninitializeEnvironment** is called.

## Syntax


```C++
HRESULT WINAPI IpcUninitializeEnvironment(void);
```



## Parameters

This function has no parameters.

## Return value

If the function succeeds, the return value is **S\_OK**. If the function fails, it returns an **HRESULT** value that indicates the error.

For more information, see [**Error codes**](error-codes.md) for a description of all RMS SDK 2.1 return values.

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP2 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                   |
| Header<br/>                   | <dl> <dt>Ipcprot.h (include Msipc.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Msipc.lib</dt> </dl>                   |
| DLL<br/>                      | <dl> <dt>Msipc.dll</dt> </dl>                   |



## See also

<dl> <dt>

[**Error codes**](error-codes.md)
</dt> <dt>

[**IpcInitializeEnvironment**](ipcinitializeenvironment.md)
</dt> </dl>

 

 





