---
title: ITsSbResourcePluginStoreEx AcquireTargetLock method
description: Locks a target.
ms.assetid: 76707f1d-1f13-4d81-8954-2acf05cda2cd
ms.tgt_platform: multiple
keywords:
- AcquireTargetLock method Remote Desktop Services
- AcquireTargetLock method Remote Desktop Services , ITsSbResourcePluginStoreEx interface
- ITsSbResourcePluginStoreEx interface Remote Desktop Services , AcquireTargetLock method
topic_type:
- apiref
api_name:
- ITsSbResourcePluginStoreEx.AcquireTargetLock
api_location:
- SbTsV.idl
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ITsSbResourcePluginStoreEx::AcquireTargetLock method

Locks a target.

## Syntax


```C++
HRESULT AcquireTargetLock(
  [in]  BSTR     targetName,
  [in]  DWORD    dwTimeout,
  [out] IUnknown **ppContext
);
```



## Parameters

<dl> <dt>

*targetName* \[in\]
</dt> <dd>

The name of the target to lock.

</dd> <dt>

*dwTimeout* \[in\]
</dt> <dd>

The timeout for the operation, in milliseconds.

</dd> <dt>

*ppContext* \[out\]
</dt> <dd>

Returns a pointer to the context of the lock. To release the lock, supply this pointer to the [**ReleaseTargetLock**](/windows/desktop/api/sbtsv/nf-sbtsv-itssbresourcepluginstore-releasetargetlock) method.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

After the lock is acquired, the calling thread is assumed to have exclusive access to the target object and therefore no other thread (within the same machine) can update it. Therefore the calling thread must call the [**ReleaseTargetLock**](/windows/desktop/api/sbtsv/nf-sbtsv-itssbresourcepluginstore-releasetargetlock) method as soon as it has made the necessary updates to the target object.

> [!IMPORTANT]
> this lock does not completely prevent target objects from being modified externally if more than one Connection Broker exists in the deployment. The calling thread must be prepared to handle a failure gracefully and retry the target update.

 

This method is available on Windows Server 2012 R2 with [KB3091411](https://support.microsoft.com/kb/3091411) installed in the [**ITsSbResourcePluginStoreEx**](itssbresourcepluginstoreex.md) interface.

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

 

 





