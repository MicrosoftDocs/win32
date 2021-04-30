---
title: SetBrokerNonHAMode method of the Win32_SessionBrokerServiceProperties class
description: Migrates data from central SQL Server to a local database. It also configures the broker server to use the local database.
ms.assetid: a73908be-0cc8-4512-842c-439d5cf18ed4
ms.tgt_platform: multiple
keywords:
- SetBrokerNonHAMode method Remote Desktop Services
- SetBrokerNonHAMode method Remote Desktop Services , Win32_SessionBrokerServiceProperties class
- Win32_SessionBrokerServiceProperties class Remote Desktop Services , SetBrokerNonHAMode method
topic_type:
- apiref
api_name:
- Win32_SessionBrokerServiceProperties.SetBrokerNonHAMode
api_location:
- TssdWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SetBrokerNonHAMode method of the Win32\_SessionBrokerServiceProperties class

Migrates data from central SQL Server to a local database. It also configures the broker server to use the local database.

## Syntax


```mof
uint32 SetBrokerNonHAMode(
  [in] string connStringToCentralDBRdcms
);
```



## Parameters

<dl> <dt>

*connStringToCentralDBRdcms* \[in\]
</dt> <dd>

Connection string to the central database.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                               |
| MOF<br/>                      | <dl> <dt>TssdWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>TssdWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_SessionBrokerServiceProperties**](win32-sessionbrokerserviceproperties.md)
</dt> </dl>

 

 





