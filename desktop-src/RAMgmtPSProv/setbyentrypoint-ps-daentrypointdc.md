---
title: SetByEntryPoint method of the PS\_DAEntryPointDC class
description: Modifies domain controller settings for the entry point.
audience: developer
ms.assetid: 2ba0ce9e-2f74-4811-b768-3d4c8bc5cb06
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetByEntryPoint method
- SetByEntryPoint method, PS_DAEntryPointDC class
- PS_DAEntryPointDC class, SetByEntryPoint method
topic_type:
- apiref
api_name:
- PS_DAEntryPointDC.SetByEntryPoint
api_location:
- RAMgmtPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetByEntryPoint method of the PS\_DAEntryPointDC class

Modifies domain controller settings for the entry point.

## Syntax


```mof
uint32 SetByEntryPoint(
  [in]  string             ComputerName,
  [in]  string             EntryPointName,
  [in]  string             NewDC,
  [in]  boolean            Force,
  [in]  boolean            PassThru,
  [out] DADomainController cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

Name or IP address of the remote access server in the entry point.

</dd> <dt>

*EntryPointName* \[in\]
</dt> <dd>

The name of the entry point for which the domain controller needs to be updated.

</dd> <dt>

*NewDC* \[in\]
</dt> <dd>

The FQDN of the new domain controller. If no value is provided the domain controller closest to the server specified in ComputerName will be used.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

Suppresses the user confirmation that prompts during running the cmdlet.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Specifying PassThru returns the DAEntrypointDC object which contains the DAEntrypointDC configuration. This cmdlet doesn't generate an object by default.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

1. ChangeByDCName: Provides a list of entry points for which the associated domain controllers have been changed, and the name of the new domain controller. ExistingDC has a specified value. EntryPointName does not have a specified value. 2. ChangeByEntryPoint: Provides information about the specified entry point and its updated domain controller. ExistingDC does not have a specified value. EntryPointName has a specified value.

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

 

 





