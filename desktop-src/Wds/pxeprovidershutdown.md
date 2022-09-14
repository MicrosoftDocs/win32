---
title: PxeProviderShutdown callback function
description: Called to shutdown the provider.
ms.assetid: 436d7428-18f9-4b73-b346-79c9a0738c31
keywords:
- PxeProviderShutdown callback function Windows Deployment Services
topic_type:
- apiref
api_name:
- PxeProviderShutdown
api_type:
- UserDefined
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# PxeProviderShutdown callback function

Called to shutdown the provider. This function is registered by calling the [**PxeRegisterCallback**](/windows/desktop/api/WdsPxe/nf-wdspxe-pxeregistercallback) function with the *CallbackType* parameter set to **PXE\_CALLBACK\_SHUTDOWN**. After this function is called, the *hProvider* handle passed to the [*PxeProviderInitialize*](pxeproviderinitialize.md) function is no longer valid.

## Syntax


```C++
DWORD PXEAPI PxeProviderShutdown(
  _In_ PVOID pContext
);
```



## Parameters

<dl> <dt>

*pContext* \[in\]
</dt> <dd>

Context value passed to the [**PxeRegisterCallback**](/windows/desktop/api/WdsPxe/nf-wdspxe-pxeregistercallback) function.

</dd> </dl>

## Return value

If the provider shutdown succeeds, the callback should return **ERROR\_SUCCESS**. In case of failure, an appropriate error code should be returned.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                          |
| Minimum supported server<br/> | Windows Server 2008, Windows Server 2003 with SP2 \[desktop apps only\]<br/> |



## See also

<dl> <dt>

[Windows Deployment Services Server Functions](windows-deployment-services-server-functions.md)
</dt> <dt>

[*PxeProviderInitialize*](pxeproviderinitialize.md)
</dt> <dt>

[**PxeRegisterCallback**](/windows/desktop/api/WdsPxe/nf-wdspxe-pxeregistercallback)
</dt> </dl>

 

 





