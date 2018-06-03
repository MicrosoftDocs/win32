---
title: IpcInitializeEnvironment function
description: Initializes the environment for use.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: F4EC6D11-1651-4825-98DA-C54D4B538865
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
keywords:
- IpcInitializeEnvironment function Active Directory Rights Management Services SDK 2.0
topic_type:
- apiref
api_name:
- IpcInitializeEnvironment
api_location:
- Msipc.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IpcInitializeEnvironment function

Initializes the environment for use. This method should only be called once per process, after calling [**IpcInitialize**](ipcinitialize.md) and before calling any other Rights Management Services SDK 2.1 method.

## Syntax


```C++
HRESULT WINAPI IpcInitializeEnvironment(void);
```



## Parameters

This function has no parameters.

## Return value

If the function succeeds, the return value is **S\_OK**. If the function fails, it returns an **HRESULT** value that indicates the error.

For more information, see [**Error codes**](error-codes.md) for a description of all RMS SDK 2.1 return values.

## Remarks

You will call [**IpcUninitializeEnvironment**](ipcuninitializeenvironment.md) in the close down of your application. For more information, see **IpcUninitializeEnvironment**.

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

[**IpcInitialize**](ipcinitialize.md)
</dt> <dt>

[**IpcUninitializeEnvironment**](ipcuninitializeenvironment.md)
</dt> </dl>

 

 





