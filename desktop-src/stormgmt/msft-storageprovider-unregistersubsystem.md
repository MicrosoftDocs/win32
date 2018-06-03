---
title: UnregisterSubsystem method of the MSFT\_StorageProvider class
description: Unregisters a subsystem. The provider will no longer manage this subsystem.
ms.assetid: AD78886B-F238-4FFA-94AC-512606393066
keywords:
- UnregisterSubsystem method Windows Storage Management API
- UnregisterSubsystem method Windows Storage Management API , MSFT_StorageProvider class
- MSFT_StorageProvider class Windows Storage Management API , UnregisterSubsystem method
topic_type:
- apiref
api_name:
- MSFT_StorageProvider.UnregisterSubsystem
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# UnregisterSubsystem method of the MSFT\_StorageProvider class

Unregisters a subsystem. The provider will no longer manage this subsystem.

## Syntax


```mof
UInt32 UnregisterSubsystem(
  [in]  String  Subsystem,
  [in]  String  StorageSubSystemUniqueId,
  [in]  Boolean Force,
  [out] String  ExtendedStatus
);
```



## Parameters

<dl> <dt>

*Subsystem* \[in\]
</dt> <dd>

The subsystem to unregister, an [**MSFT\_StorageSubSystem**](msft-storagesubsystem.md) object.

</dd> <dt>

*StorageSubSystemUniqueId* \[in\]
</dt> <dd>

Unique identifier of the storage subsystem.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

**TRUE** to force the unregister operation when the subsystem is registered with the credentials of a different user; otherwise, **FALSE**.

</dd> <dt>

*ExtendedStatus* \[out\]
</dt> <dd>

Extended error information from the storage provider in a [**MSFT\_StorageExtendedStatus**](msft-storageextendedstatus.md) object. The information is implementation-specific.

</dd> </dl>

## Return value

<dl> <dt>

**Success** (0)
</dt> <dt>

**Not Supported** (1)
</dt> <dt>

**Unspecified Error** (2)
</dt> <dt>

**Timeout** (3)
</dt> <dt>

**Failed** (4)
</dt> <dt>

**Invalid Parameter** (5)
</dt> <dt>

**Access denied** (40001)
</dt> <dt>

**There are not enough resources to complete the operation.** (40002)
</dt> <dt>

**Cannot connect to the storage provider.** (46000)
</dt> <dt>

**The storage provider cannot connect to the storage subsystem.** (46001)
</dt> <dt>

**Cannot register/unregister the storage subsystem on local host.** (46004)
</dt> <dt>

**The storage subsystem is not registered.** (46005)
</dt> <dt>

**This subsystem is already registered with another user's credentials. Use the -Force flag to remove the existing registration and add a new one anyway.** (46007)
</dt> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                   |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_StorageProvider**](msft-storageprovider.md)
</dt> </dl>

 

 





