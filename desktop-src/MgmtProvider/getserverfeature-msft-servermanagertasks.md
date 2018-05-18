---
title: GetServerFeature method of the MSFT\_ServerManagerTasks class
description: Gets the server features on the managed node.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'dc722ff4-08ae-4738-bae8-305ef21ce9ba'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetServerFeature method", "GetServerFeature method, MSFT_ServerManagerTasks class", "MSFT_ServerManagerTasks class, GetServerFeature method"]
topic_type:
- apiref
api_name:
- MSFT_ServerManagerTasks.GetServerFeature
api_location:
- MgmtProvider.dll
api_type:
- COM
---

# GetServerFeature method of the MSFT\_ServerManagerTasks class

Gets the server features on the managed node.

## Syntax


```mof
uint32 GetServerFeature(
  [in]  uint32             FilterFlags,
  [in]  uint32             BatchSize,
  [out] boolean            RequiresReboot,
  [out] MSFT_ServerFeature cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*FilterFlags* \[in\]
</dt> <dd>

Return only features that are in a particular install state. Valid values are 0 through 6.

</dd> <dt>

*BatchSize* \[in\]
</dt> <dd>

The batch size to stream results in.

</dd> <dt>

*RequiresReboot* \[out\]
</dt> <dd>

Flag indicating whether a reboot required status is reported by CBS.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An array of embedded instances of the [**MSFT\_ServerFeature**](msft-serverfeature.md) class that represent the requested list of features.

</dd> </dl>

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                              |
| Namespace<br/>                | Root\\Windows\\ServerManager<br/>                                                     |
| MOF<br/>                      | <dl> <dt>MgmtProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MgmtProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_ServerManagerTasks**](msft-servermanagertasks.md)
</dt> <dt>

[**MSFT\_ServerFeature**](msft-serverfeature.md)
</dt> </dl>

 

 





