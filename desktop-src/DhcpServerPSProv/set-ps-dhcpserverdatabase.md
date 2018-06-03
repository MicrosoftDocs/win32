---
title: Set method of the PS\_DhcpServerDatabase class
description: Modifies one or more configuration parameters of the database of the DHCP server.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 91e9614a-0dc5-4f89-88fd-e0408cdeba0b
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Set method
- Set method, PS_DhcpServerDatabase class
- PS_DhcpServerDatabase class, Set method
topic_type:
- apiref
api_name:
- PS_DhcpServerDatabase.Set
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Set method of the PS\_DhcpServerDatabase class

Modifies one or more configuration parameters of the database of the DHCP server

## Syntax


```mof
uint32 Set(
  [in]  string             FileName,
  [in]  string             BackupPath,
  [in]  uint32             BackupInterval,
  [in]  uint32             CleanupInterval,
  [in]  boolean            RestoreFromBackup,
  [in]  string             ComputerName,
  [in]  boolean            PassThru,
  [out] DhcpServerDatabase cmdletOutput
);
```



## Parameters

<dl> <dt>

*FileName* \[in\]
</dt> <dd>

Name of the database backup file

</dd> <dt>

*BackupPath* \[in\]
</dt> <dd>

Directory where the database should be backed up

</dd> <dt>

*BackupInterval* \[in\]
</dt> <dd>

Periodicity of automatic database backup (in minutes)

</dd> <dt>

*CleanupInterval* \[in\]
</dt> <dd>

Periodicity of database cleanup (in minutes)

</dd> <dt>

*RestoreFromBackup* \[in\]
</dt> <dd>

If set to true, indicates that database has to be restored from backup

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

DNS name or IP address of the target computer running the DHCP server service.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

If this parameter is specified, the cmdlet returns the PowerShell object which is modified.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DhcpServerDatabase**](dhcpserverdatabase.md) class.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DhcpServerDatabase**](ps-dhcpserverdatabase.md)
</dt> </dl>

 

 





