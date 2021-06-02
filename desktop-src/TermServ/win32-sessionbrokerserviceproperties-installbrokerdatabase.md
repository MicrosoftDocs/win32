---
title: InstallBrokerDatabase method of the Win32_SessionBrokerServiceProperties class
description: Installs an RD connection broker database on a central SQL server.
ms.assetid: 9cc6fa4a-f1eb-49eb-bec4-acaff73190e8
ms.tgt_platform: multiple
keywords:
- InstallBrokerDatabase method Remote Desktop Services
- InstallBrokerDatabase method Remote Desktop Services , Win32_SessionBrokerServiceProperties class
- Win32_SessionBrokerServiceProperties class Remote Desktop Services , InstallBrokerDatabase method
topic_type:
- apiref
api_name:
- Win32_SessionBrokerServiceProperties.InstallBrokerDatabase
api_location:
- TssdWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# InstallBrokerDatabase method of the Win32\_SessionBrokerServiceProperties class

Installs an RD connection broker database on a central SQL server.

## Syntax


```mof
uint32 InstallBrokerDatabase(
  [in] string newDbFilePath,
  [in] string connStringToCentralDBMaster,
  [in] string centralRdcmsDbName
);
```



## Parameters

<dl> <dt>

*newDbFilePath* \[in\]
</dt> <dd>

new database file path.

</dd> <dt>

*connStringToCentralDBMaster* \[in\]
</dt> <dd>

Connection string to the central database master.

</dd> <dt>

*centralRdcmsDbName* \[in\]
</dt> <dd>

Name of the central database.

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

 

 





