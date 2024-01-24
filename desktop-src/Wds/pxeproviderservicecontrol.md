---
title: PxeProviderServiceControl callback function
description: Called when a service control code is received by the WDS service.
ms.assetid: 180ddcda-d111-4c81-9177-db99cbf1449f
keywords:
- PxeProviderServiceControl callback function Windows Deployment Services
topic_type:
- apiref
api_name:
- PxeProviderServiceControl
api_type:
- UserDefined
ms.topic: reference
ms.date: 05/31/2018
api_location: 
---

# PxeProviderServiceControl callback function

Called when a service control code is received by the WDS service. This callback function is registered by calling the [**PxeRegisterCallback**](/windows/desktop/api/WdsPxe/nf-wdspxe-pxeregistercallback) function with the *CallbackType* parameter set to **PXE\_CALLBACK\_SERVICE\_CONTROL**.

## Syntax


```C++
DWORD PXEAPI PxeProviderServiceControl(
  _In_ PVOID pContext,
       DWORD dwControl
);
```



## Parameters

<dl> <dt>

*pContext* \[in\]
</dt> <dd>

Context value passed to the [**PxeRegisterCallback**](/windows/desktop/api/WdsPxe/nf-wdspxe-pxeregistercallback) function.

</dd> <dt>

*dwControl* 
</dt> <dd>

Control code. For the list of possible values, see the *dwControl* parameter of the [*HandlerEx*](/windows/desktop/api/winsvc/nc-winsvc-lphandler_function_ex) function.

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

[**PxeRegisterCallback**](/windows/desktop/api/WdsPxe/nf-wdspxe-pxeregistercallback)
</dt> </dl>

 

