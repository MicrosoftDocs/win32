---
title: GetServerBpaResult method of the MSFT\_ServerManagerTasks class
description: Retrieves the BPA model results from the server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 001f0935-9312-4034-876f-44f784d1c19c
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetServerBpaResult method
- GetServerBpaResult method, MSFT_ServerManagerTasks class
- MSFT_ServerManagerTasks class, GetServerBpaResult method
topic_type:
- apiref
api_name:
- MSFT_ServerManagerTasks.GetServerBpaResult
api_location:
- MgmtProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetServerBpaResult method of the MSFT\_ServerManagerTasks class

Retrieves the BPA model results from the server.

## Syntax


```mof
uint32 GetServerBpaResult(
  [in]  string               BpaXPaths[],
  [in]  uint32               BatchSize,
  [out] MSFT_ServerBpaResult cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*BpaXPaths* \[in\]
</dt> <dd>

The BPA paths to query.

</dd> <dt>

*BatchSize* \[in\]
</dt> <dd>

The batch size to stream results in.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An array of embedded instances of [**MSFT\_ServerBpaResult**](msft-serverbparesult.md) that represent the results selected by the specified BPA paths.

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

[**MSFT\_ServerBpaResult**](msft-serverbparesult.md)
</dt> </dl>

 

 





