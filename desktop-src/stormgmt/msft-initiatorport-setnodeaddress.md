---
title: SetNodeAddress method of the MSFT\_InitiatorPort class
description: Sets the node address for an iSCSI initiator port by passing an IQN as the node address string.
ms.assetid: 0F1A5F3C-3064-44EE-A8D2-0A6E735CDE5A
keywords:
- SetNodeAddress method Windows Storage Management API
- SetNodeAddress method Windows Storage Management API , MSFT_InitiatorPort class
- MSFT_InitiatorPort class Windows Storage Management API , SetNodeAddress method
topic_type:
- apiref
api_name:
- MSFT_InitiatorPort.SetNodeAddress
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

# SetNodeAddress method of the MSFT\_InitiatorPort class

Sets the node address for an iSCSI initiator port by passing an IQN as the node address string.

## Syntax


```mof
UInt32 SetNodeAddress(
  [in]  String NodeAddress,
  [out] String ExtendedStatus
);
```



## Parameters

<dl> <dt>

*NodeAddress* \[in\]
</dt> <dd>

The node address. This parameter is required.

</dd> <dt>

*ExtendedStatus* \[out\]
</dt> <dd>

A string that contains an embedded [**MSFT\_StorageExtendedStatus**](msft-storageextendedstatus.md) object.

This parameter allows the storage provider to return extended (implementation-specific) error information.

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
</dt> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_InitiatorPort**](msft-initiatorport.md)
</dt> </dl>

 

 





