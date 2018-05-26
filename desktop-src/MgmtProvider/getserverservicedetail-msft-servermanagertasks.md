---
title: GetServerServiceDetail method of the MSFT\_ServerManagerTasks class
description: Retrieves the details of the specified Win32 services on the managed node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5190ca4a-4499-4734-8f69-b6b0e40b0d9f
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetServerServiceDetail method
- GetServerServiceDetail method, MSFT_ServerManagerTasks class
- MSFT_ServerManagerTasks class, GetServerServiceDetail method
topic_type:
- apiref
api_name:
- MSFT_ServerManagerTasks.GetServerServiceDetail
api_location:
- MgmtProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# GetServerServiceDetail method of the MSFT\_ServerManagerTasks class

Retrieves the details of the specified Win32 services on the managed node.

## Syntax


```mof
uint32 GetServerServiceDetail(
  [in]  string                   Services[],
  [in]  uint32                   BatchSize,
  [out] MSFT_ServerServiceDetail cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*Services* \[in\]
</dt> <dd>

The list of services to query on the managed node.

</dd> <dt>

*BatchSize* \[in\]
</dt> <dd>

The batch size for streamed results.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An array of embedded [**MSFT\_ServerServiceDetail**](msft-serverservicedetail.md) instances that represent the details regarding the list of Win32 services selected from server.

</dd> </dl>

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                              |
| Namespace<br/>                | Root\\Windows\\ServerManager<br/>                                                     |
| MOF<br/>                      | <dl> <dt>MgmtProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MgmtProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_ServerManagerTasks**](msft-servermanagertasks.md)
</dt> <dt>

[**MSFT\_ServerServiceDetail**](msft-serverservicedetail.md)
</dt> </dl>

 

 





