---
title: RemoveMembers method of the MSFT\_SMReplicationGroup class
description: Removes members from the replication group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8122df70-6466-40d9-a98c-87277a594415
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RemoveMembers method
- RemoveMembers method, MSFT_SMReplicationGroup class
- MSFT_SMReplicationGroup class, RemoveMembers method
topic_type:
- apiref
api_name:
- MSFT_SMReplicationGroup.RemoveMembers
api_location:
- StorageService.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RemoveMembers method of the MSFT\_SMReplicationGroup class

Removes members from the replication group.

## Syntax


```mof
UInt32 RemoveMembers(
  [in]            MSFT_SMStorageObject REF STorageObjects[],
  [in, optional]  String                   username,
  [in, optional]  String                   password,
  [out]           MSFT_SMJob           REF Job,
  [out, optional] MSFT_SMExtendedStatus    ExtendedStatus
);
```



## Parameters

<dl> <dt>

*STorageObjects* \[in\]
</dt> <dd>

A reference to an array that contains the storage objects to remove from the replication group.

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

Returns "0" on success, otherwise returns a WMI error code.

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

 

 





