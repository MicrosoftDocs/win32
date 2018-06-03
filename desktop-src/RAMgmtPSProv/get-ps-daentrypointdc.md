---
title: Get method of the PS\_DAEntryPointDC class
description: Retrieves the domain controller that is associated with the specified entry point.
audience: developer
ms.assetid: e91c5f8d-17ef-4db1-8624-33df87eb4962
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Get method
- Get method, PS_DAEntryPointDC class
- PS_DAEntryPointDC class, Get method
topic_type:
- apiref
api_name:
- PS_DAEntryPointDC.Get
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Get method of the PS\_DAEntryPointDC class

Retrieves the domain controller that is associated with the specified entry point.

## Syntax


```mof
uint32 Get(
  [in]  string             ComputerName,
  [in]  string             EntryPointName,
  [out] DADomainController cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

Name or IP address of the remote access server or server cluster in the specified entry point.

</dd> <dt>

*EntryPointName* \[in\]
</dt> <dd>

The name of the entry point for which domain controller information should be retrieved.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

Returns a list of entry points and their associated domain controllers.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DAEntryPointDC**](ps-daentrypointdc.md)
</dt> </dl>

 

 





