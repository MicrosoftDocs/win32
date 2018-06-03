---
title: SetByAll method of the PS\_DnsServerDiagnostics class
description: Sets debug and logging parameters.
audience: developer
ms.assetid: 5b7aac00-6d68-471f-a978-4d36ff6dd901
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetByAll method
- SetByAll method, PS_DnsServerDiagnostics class
- PS_DnsServerDiagnostics class, SetByAll method
topic_type:
- apiref
api_name:
- PS_DnsServerDiagnostics.SetByAll
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetByAll method of the PS\_DnsServerDiagnostics class

Sets debug and logging parameters.

## Syntax


```mof
uint32 SetByAll(
  [in]  boolean              All,
  [in]  string               ComputerName,
  [in]  boolean              PassThru,
  [out] DnsServerDiagnostics cmdletOutput
);
```



## Parameters

<dl> <dt>

*All* \[in\]
</dt> <dd>

Sets all the settings.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

**True** to return the object that was modified by the method. By default, this method does not generate any output.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

On return, contains an instance of the current object. This parameter returns a value only if *PassThru* is set to **true.**

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DnsServerDiagnostics**](ps-dnsserverdiagnostics.md)
</dt> </dl>

 

 





