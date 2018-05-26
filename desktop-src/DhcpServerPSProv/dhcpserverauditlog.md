---
title: DhcpServerAuditLog class
description: Dhcp Server Audit Log Configuration.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3f89324d-02c5-4470-a53a-7cc16ff5fb5c
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DhcpServerAuditLog class
- DhcpServerAuditLog class, described
topic_type:
- apiref
api_name:
- DhcpServerAuditLog
- DhcpServerAuditLog.Enable
- DhcpServerAuditLog.Path
- DhcpServerAuditLog.MaxMBFileSize
- DhcpServerAuditLog.DiskCheckInterval
- DhcpServerAuditLog.MinMBDiskSpace
api_location:
- DhcpServerPsProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DhcpServerAuditLog class

Dhcp Server Audit Log Configuration.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DhcpServerPSProvider"), AMENDMENT]
class DhcpServerAuditLog
{
  boolean Enable;
  string  Path;
  uint32  MaxMBFileSize;
  uint32  DiskCheckInterval;
  uint32  MinMBDiskSpace;
};
```

## Members

The **DhcpServerAuditLog** class has these types of members:

-   [Properties](#properties)

### Properties

The **DhcpServerAuditLog** class has these properties.

<dl> <dt>

**DiskCheckInterval**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Number of times the DHCP server writes audit log events to the log file before checking for available disk space on the server.

</dd> <dt>

**Enable**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates whether logging is enabled on Dhcp Server.

</dd> <dt>

**MaxMBFileSize**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Maximum size (in megabytes) for the total amount of disk space available for all audit log files created and stored.

</dd> <dt>

**MinMBDiskSpace**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Minimum size (in megabytes) required to continue audit logging.

</dd> <dt>

**Path**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Directory path which stores audit log files.

</dd> </dl>

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\DHCP<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DhcpServerPsProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DhcpServerPsProvider.dll</dt> </dl> |



 

 





