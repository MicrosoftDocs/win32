---
title: IpcInitialize function
description: Locates the installed version of Msipc.dll and calls the Windows LoadLibrary against it.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 'B84BFBBD-E8CA-437D-8055-D365A70FACC9'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-rights-management'
ms.tgt_platform: multiple
keywords: ["IpcInitialize function Active Directory Rights Management Services SDK 2.0"]
topic_type:
- apiref
api_name:
- IpcInitialize
api_location:
- msipc_s.lib
api_type:
- LibDef
---

# IpcInitialize function

Locates the installed version of Msipc.dll and calls the Windows [**LoadLibrary**](https://msdn.microsoft.com/library/windows/desktop/ms684175) against it. **IpcInitialize** is made available through a static library, *msipc\_s.lib*.

> \[!Important\]  
> This function should be called before any other Rights Management Services SDK 2.1 function, otherwise the system may not work properly.

 

After calling **IpcInitialize**, your next call should be to [**IpcInitializeEnvironment**](ipcinitializeenvironment.md).

## Syntax


```C++
HRESULT WINAPI IpcInitialize(void);
```



## Parameters

This function has no parameters.

## Return value

If the function succeeds, the return value is **S\_OK**. If the function fails, it returns an **HRESULT** value that indicates the error.

For more information, see [**Error codes**](error-codes.md) for a description of all RMS SDK 2.1 return values.

## Remarks

For installation information about Msipc.dll, see the reference topic [SDK elements](https://msdn.microsoft.com/library/windows/desktop/hh971321).

The *msipc.dll* must be delay loaded as part of your project configuration in Visual Studio. For more information, see step 4 in [How to configure Visual Studio for AD RMS SDK 2.1](how-to-configure-a-visual-studio-project-to-use-the-ad-rms-sdk-2-0.md).

There is currently no corresponding **IpcUninitialize** function to free this library.

After Msipc.dll is loaded in a process, it cannot be unloaded.

It is not safe to call **IpcInitialize** from within [**DllMain**](https://msdn.microsoft.com/library/windows/desktop/ms682583).

**IpcInitialize** is made available through a static library, *msipc\_s.lib*.

## Requirements



|                                     |                                                                                                        |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP2<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                         |
| Header<br/>                   | <dl> <dt>Ipcbase.h (include Msipc.h)</dt> </dl> |
| Library<br/>                  | <dl> <dt>Msipc\_s.lib</dt> </dl>                |



## See also

<dl> <dt>

[**DllMain**](https://msdn.microsoft.com/library/windows/desktop/ms682583)
</dt> <dt>

[**Error codes**](error-codes.md)
</dt> <dt>

[**IpcInitialize**](ipcinitialize.md)
</dt> <dt>

[**IpcInitializeEnvironment**](ipcinitializeenvironment.md)
</dt> <dt>

[**LoadLibrary**](https://msdn.microsoft.com/library/windows/desktop/ms684175)
</dt> <dt>

[SDK elements](https://msdn.microsoft.com/library/windows/desktop/hh971321)
</dt> </dl>

 

 





