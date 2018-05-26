---
title: UnLoad method of the MSFT\_Providers class
description: The UnLoad Windows Management Instrumentation (WMI) class method unloads the COM server associated with the specific instance of the provider.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 24c58ec1-5b1a-42d6-900b-218e862d4114
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- UnLoad method
- UnLoad method, MSFT_Providers class
- MSFT_Providers class, UnLoad method
- UnLoad method, MSFT_Providers class
- MSFT_Providers class, UnLoad method
topic_type:
- apiref
api_name:
- MSFT_Providers.UnLoad
- MSFT_Providers.UnLoad
api_location:
- WmiPrvSD.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# UnLoad method of the MSFT\_Providers class

The **UnLoad** Windows Management Instrumentation (WMI) class method unloads the COM server associated with the specific instance of the provider. Subsequent calls into the provider with the same class identifier (CLSID) returns WBEM\_E\_PROVIDER\_DISABLED. If the COM server implementation is an in-process server hosted in the provider host process, it receives calls to the exported function [**DllCanUnloadNow**](_com_dllcanunloadnow). If the provider responds by returning **TRUE**, then the server unloads the executable image. COM is configured to unload the executable file approximately 2 minutes after the first successful call to **DllCanUnloadNow**. The provider can be re-enabled using the [**MSFT Providers.Load**](load-method-in-class-msft-providers.md) method, changing to the associated instance of [**\_\_Win32Provider**](https://msdn.microsoft.com/library/aa394688), or restarting the service.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
Uint32 UnLoad();
```



## Parameters

This method has no parameters.

## Return value

Returns a value of 0 (zero) if the provider is unloaded successfully. Any other number indicates an error.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMv2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>System.mof</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>WmiPrvSD.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_Providers**](msft-providers.md)
</dt> </dl>

 

 





