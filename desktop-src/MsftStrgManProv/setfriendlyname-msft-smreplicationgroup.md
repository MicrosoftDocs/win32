---
title: SetFriendlyName method of the MSFT\_SMReplicationGroup class
description: Updates the user friendly name of a replication group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: bdb8dec8-4359-4a91-95c6-116b082f6492
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetFriendlyName method
- SetFriendlyName method, MSFT_SMReplicationGroup class
- MSFT_SMReplicationGroup class, SetFriendlyName method
topic_type:
- apiref
api_name:
- MSFT_SMReplicationGroup.SetFriendlyName
api_location:
- StorageService.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SetFriendlyName method of the MSFT\_SMReplicationGroup class

Updates the user friendly name of a replication group.

## Syntax


```mof
UInt32 SetFriendlyName(
  [in]            String                FriendlyName,
  [in, optional]  String                username,
  [in, optional]  String                password,
  [out]           MSFT_SMJob        REF Job,
  [out, optional] MSFT_SMExtendedStatus ExtendedStatus
);
```



## Parameters

<dl> <dt>

*FriendlyName* \[in\]
</dt> <dd>

The new name of the replication group.

</dd> <dt>

*username* \[in, optional\]
</dt> <dd>

The username used to authenticate the SMI-S provider.

</dd> <dt>

*password* \[in, optional\]
</dt> <dd>

The password used to authenticate the SMI-S provider.

</dd> <dt>

*Job* \[out\]
</dt> <dd>

If this operation is asynchronous, when this method returns, this parameter contains a reference to the object that represents the job; otherwise this parameter is set to **NULL**.

</dd> <dt>

*ExtendedStatus* \[out, optional\]
</dt> <dd>

When this method returns, this parameter contains a [**MSFT\_SMExtendedStatus**](msft-smextendedstatus.md) object that contains detailed status information about the results of this operation.

</dd> </dl>

## Return value

The possible return values are:

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



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage\\SM<br/>                                              |
| MOF<br/>                      | <dl> <dt>MsftStrgMan.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>StorageService.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_SMReplicationGroup**](msft-smreplicationgroup.md)
</dt> </dl>

 

 





