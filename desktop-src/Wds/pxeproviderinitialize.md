---
title: PxeProviderInitialize callback function
description: An export from a provider dynamic-link library (DLL) that initializes the provider and prepares it to receive client requests.
ms.assetid: 433b051c-9fde-4589-92e2-58d3774826ac
keywords:
- PxeProviderInitialize callback function Windows Deployment Services
topic_type:
- apiref
api_name:
- PxeProviderInitialize
api_type:
- UserDefined
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# PxeProviderInitialize callback function

An export from a provider dynamic-link library (DLL) that initializes the provider and prepares it to receive client requests. Providers are required to export the *PxeProviderInitialize* function. Any callbacks to the provider must be registered with a call to the [**PxeRegisterCallback**](/windows/desktop/api/WdsPxe/nf-wdspxe-pxeregistercallback) function during the processing of *PxeProviderInitialize*. On the return of this function, the provider must be fully initialized and ready to process client requests.

## Syntax


```C++
DWORD PXEAPI PxeProviderInitialize(
  _In_ HANDLE hProvider,
  _In_ HKEY   hProviderKey
);
```



## Parameters

<dl> <dt>

*hProvider* \[in\]
</dt> <dd>

Handle to the provider instance. This handle must be stored by the provider and used in any subsequent calls. This handle is valid until the [*PxeProviderShutdown*](pxeprovidershutdown.md) callback function is called.

</dd> <dt>

*hProviderKey* \[in\]
</dt> <dd>

Handle to a registry key where provider configuration information is to be stored.

</dd> </dl>

## Return value

If the provider initialization succeeds, the callback should return **ERROR\_SUCCESS**. In case of failure, an appropriate error code should be returned.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                          |
| Minimum supported server<br/> | Windows Server 2008, Windows Server 2003 with SP2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Windows Deployment Services Server Functions](windows-deployment-services-server-functions.md)
</dt> <dt>

[*PxeProviderShutdown*](pxeprovidershutdown.md)
</dt> </dl>

 

 





