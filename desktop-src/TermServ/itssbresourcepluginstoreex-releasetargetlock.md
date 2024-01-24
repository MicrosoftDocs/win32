---
title: ITsSbResourcePluginStoreEx ReleaseTargetLock method
description: Releases a lock on a target.
ms.assetid: ab2ae9f3-2d38-4b31-9889-58297c574bd4
ms.tgt_platform: multiple
keywords:
- ReleaseTargetLock method Remote Desktop Services
- ReleaseTargetLock method Remote Desktop Services , ITsSbResourcePluginStoreEx interface
- ITsSbResourcePluginStoreEx interface Remote Desktop Services , ReleaseTargetLock method
topic_type:
- apiref
api_name:
- ITsSbResourcePluginStoreEx.ReleaseTargetLock
api_location:
- SbTsV.idl
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ITsSbResourcePluginStoreEx::ReleaseTargetLock method

Releases a lock on a target.

## Syntax


```C++
HRESULT ReleaseTargetLock(
  [in] IUnknown *pContext
);
```



## Parameters

<dl> <dt>

*pContext* \[in\]
</dt> <dd>

A pointer to the context returned by the [**AcquireTargetLock**](/windows/desktop/api/sbtsv/nf-sbtsv-itssbresourcepluginstore-acquiretargetlock) method.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

This method is only available on Windows Server 2012 R2 with [KB3091411](https://support.microsoft.com/kb/3091411) installed in the [**ITsSbResourcePluginStoreEx**](itssbresourcepluginstoreex.md) interface. This method is available on the [**ITsSbResourcePluginStore**](/windows/desktop/api/sbtsv/nn-sbtsv-itssbresourcepluginstore) interface starting with Windows Server 2016.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                             |
| End of server support<br/>    | Windows Server 2012 R2<br/>                                                             |
| IDL<br/>                      | <dl> <dt>SbTsV.idl</dt> </dl>          |
| IID<br/>                      | IID\_ITsSbResourcePluginStoreEx is defined as 80b83ffd-625d-11e5-bea1-a0481c7e9064<br/> |



## See also

<dl> <dt>

[**ITsSbResourcePluginStoreEx**](itssbresourcepluginstoreex.md)
</dt> </dl>

 

 





