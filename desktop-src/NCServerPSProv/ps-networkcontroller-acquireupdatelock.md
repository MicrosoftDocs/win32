---
title: AcquireUpdateLock method of the PS\_NetworkController class
description: Acquires a network controller update lock.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'e9dcff3f-50ee-4730-95e3-2e158961274b'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["AcquireUpdateLock method", "AcquireUpdateLock method, PS_NetworkController class", "PS_NetworkController class, AcquireUpdateLock method"]
topic_type:
- apiref
api_name:
- PS_NetworkController.AcquireUpdateLock
api_location:
- NCServerPSProvider.dll
api_type:
- COM
---

# AcquireUpdateLock method of the PS\_NetworkController class

Acquires a network controller update lock.

## Syntax


```mof
uint32 AcquireUpdateLock(
  [out] boolean LockAcquired
);
```



## Parameters

<dl> <dt>

*LockAcquired* \[out\]
</dt> <dd>

on return, contains **true** if the lock was successfully acquired; otherwise, **false**.

</dd> </dl>

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                    |
| Namespace<br/>                | Root\\Microsoft\\Windows\\NetworkController\\Server<br/>                                    |
| MOF<br/>                      | <dl> <dt>NCServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NCServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_NetworkController**](ps-networkcontroller.md)
</dt> </dl>

 

 





