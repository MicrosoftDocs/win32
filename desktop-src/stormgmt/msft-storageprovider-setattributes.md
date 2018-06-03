---
title: SetAttributes method of the MSFT\_StorageProvider class
description: Sets the attributes of the provider.
ms.assetid: 649B08C0-CC46-4A93-8037-47CACBC1AD4E
keywords:
- SetAttributes method Windows Storage Management API
- SetAttributes method Windows Storage Management API , MSFT_StorageProvider class
- MSFT_StorageProvider class Windows Storage Management API , SetAttributes method
topic_type:
- apiref
api_name:
- MSFT_StorageProvider.SetAttributes
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

# SetAttributes method of the MSFT\_StorageProvider class

Sets the attributes of the provider.

## Syntax


```mof
UInt32 SetAttributes(
  [in]  UInt16 RemoteSubsystemCacheMode,
  [out] String ExtendedStatus
);
```



## Parameters

<dl> <dt>

*RemoteSubsystemCacheMode* \[in\]
</dt> <dd>

The caching mode to set. A value of 3 enables caching for all the registered remote subsystems. A value of 2 disables caching for all the registered remote subsystems. This method only affects the remote registered subsystems; local subsystem requests are reported directly with no caching.



| Value                                                                                                | Meaning                     |
|------------------------------------------------------------------------------------------------------|-----------------------------|
| <span id="2"></span><dl> <dt>**2**</dt> </dl> | Disabled<br/>         |
| <span id="3"></span><dl> <dt>**3**</dt> </dl> | Manual-Discovery<br/> |



 

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

 

 





