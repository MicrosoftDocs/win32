---
title: DhcpServerDatabase class
description: Dhcp Server Database Configuration.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '47e7d400-3f77-4ccd-a7e3-9280b57c39db'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dhcp-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DhcpServerDatabase class", "DhcpServerDatabase class, described"]
topic_type:
- apiref
api_name:
- DhcpServerDatabase
- DhcpServerDatabase.FileName
- DhcpServerDatabase.BackupPath
- DhcpServerDatabase.BackupInterval
- DhcpServerDatabase.CleanupInterval
- DhcpServerDatabase.LoggingEnabled
- DhcpServerDatabase.RestoreFromBackup
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
---

# DhcpServerDatabase class

Dhcp Server Database Configuration.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class DhcpServerDatabase
{
  string  FileName;
  string  BackupPath;
  uint32  BackupInterval;
  uint32  CleanupInterval;
  boolean LoggingEnabled;
  boolean RestoreFromBackup;
};
```

## Members

The **DhcpServerDatabase** class has these types of members:

-   [Properties](#properties)

### Properties

The **DhcpServerDatabase** class has these properties.

<dl> <dt>

**BackupInterval**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Periodicity of automatic database backup (in minutes).

</dd> <dt>

**BackupPath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Automatic database backup path.

</dd> <dt>

**CleanupInterval**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Periodicity of database cleanup (in minutes).

</dd> <dt>

**FileName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Fully qualified JET Database file name.

</dd> <dt>

**LoggingEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates if logging is enabled for Dhcp database.

</dd> <dt>

**RestoreFromBackup**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Database restore flag - Server will restore the database from the back-up database when the service is restarted.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





