---
title: RegisterSubsystem method of the MSFT\_StorageProvider class
description: Registers a subsystem to be managed by this provider.
ms.assetid: 0C882319-FC92-4C79-A89C-F16C6439A221
keywords:
- RegisterSubsystem method Windows Storage Management API
- RegisterSubsystem method Windows Storage Management API , MSFT_StorageProvider class
- MSFT_StorageProvider class Windows Storage Management API , RegisterSubsystem method
topic_type:
- apiref
api_name:
- MSFT_StorageProvider.RegisterSubsystem
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# RegisterSubsystem method of the MSFT\_StorageProvider class

Registers a subsystem to be managed by this provider. Note that the subsystem must be compatible with the provider software.

## Syntax


```mof
UInt32 RegisterSubsystem(
  [in]  String ComputerName,
  [in]  String Credential,
  [out] String ExtendedStatus
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

Name of the computer where the subsystem resides.

</dd> <dt>

*Credential* \[in\]
</dt> <dd>

Credential providing access to the computer.

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

**In use** (6)
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

**This subsystem is already registered.** (46006)
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

 

 





