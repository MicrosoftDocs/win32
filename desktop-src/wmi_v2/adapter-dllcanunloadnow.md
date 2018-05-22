---
title: Adapter\_DllCanUnloadNow function
description: Exposes the DllCanUnloadNow function to a provider. This function allows a provider to call the adapter function DllCanUnloadNow, which determines whether the DLL that implements this function is in use.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'e7722471-c5af-4ef5-9009-daa16a501631'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Adapter_DllCanUnloadNow function Windows Management Infrastructure (MI)"]
topic_type:
- apiref
api_name:
- Adapter_DllCanUnloadNow
api_location:
- WmiToMi.dll
api_type:
- DllExport
---

# Adapter\_DllCanUnloadNow function

Exposes the [**DllCanUnloadNow**](https://msdn.microsoft.com/library/windows/desktop/ms690368) function to a provider. This function allows a provider to call the adapter function **DllCanUnloadNow**, which determines whether the DLL that implements this function is in use.

> \[!Important\]  
> This function is only used by generated code and should not be used by developers.

 

## Syntax


```C++
STDAPI Adapter_DllCanUnloadNow(void);
```



## Parameters

This function has no parameters.

## Return value

If the function succeeds, the return value is **S\_OK**. If the function fails, the return value is **S\_FALSE**.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| DLL<br/>                      | <dl> <dt>WmiToMi.dll</dt> </dl> |



## See also

<dl> <dt>

[Adapter Functions](adapter-functions.md)
</dt> </dl>

 

 





