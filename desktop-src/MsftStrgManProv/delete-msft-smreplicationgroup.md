---
title: Delete method of the MSFT\_SMReplicationGroup class
description: Deletes an empty replication group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 944c1afa-8c92-485f-99bd-d93f7bc92cd5
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Delete method
- Delete method, MSFT_SMReplicationGroup class
- MSFT_SMReplicationGroup class, Delete method
topic_type:
- apiref
api_name:
- MSFT_SMReplicationGroup.Delete
api_location:
- StorageService.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Delete method of the MSFT\_SMReplicationGroup class

Deletes an empty replication group.

> [!Note]  
> In order to use this method, you must first remove all replicas from the replication group.

 

## Syntax


```mof
Uint32 Delete(
  [in, optional]  String                username,
  [in, optional]  String                password,
  [out, optional] MSFT_SMExtendedStatus ExtendedStatus
);
```



## Parameters

<dl> <dt>

*username* \[in, optional\]
</dt> <dd>

The username used to authenticate the SMI-S provider.

</dd> <dt>

*password* \[in, optional\]
</dt> <dd>

The password used to authenticate the SMI-S provider.

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
</dt> <dt>

**The replication group contains replicas.** (48000)
</dt> <dt>

**TBD** (48006)
</dt> <dt>

**TBD** (48007)
</dt> <dt>

**TBD** (57000)
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

 

 





