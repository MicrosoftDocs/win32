---
title: Set method of the PS\_DhcpServerAuditLog class
description: Sets DHCP server audit log configuration on the server - including enabling or disabling it.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 26715337-a12b-4acd-8bc5-146368426f1f
ms.prod: windows-server-dev
ms.technology:
- dhcp-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Set method
- Set method, PS_DhcpServerAuditLog class
- PS_DhcpServerAuditLog class, Set method
topic_type:
- apiref
api_name:
- PS_DhcpServerAuditLog.Set
api_location:
- DhcpServerPsProvider.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Set method of the PS\_DhcpServerAuditLog class

Sets DHCP server audit log configuration on the server - including enabling or disabling it.

## Syntax


```mof
uint32 Set(
  [in]  boolean            Enable,
  [in]  string             Path,
  [in]  uint32             MaxMBFileSize,
  [in]  uint32             DiskCheckInterval,
  [in]  uint32             MinMBDiskSpace,
  [in]  string             ComputerName,
  [in]  boolean            PassThru,
  [out] DhcpServerAuditLog cmdletOutput
);
```



## Parameters

<dl> <dt>

*Enable* \[in\]
</dt> <dd>

Enable/Disable the DHCP server audit log. Valid values are True and False.

</dd> <dt>

*Path* \[in\]
</dt> <dd>

Path to the directory where the audit log files should be created by the server

</dd> <dt>

*MaxMBFileSize* \[in\]
</dt> <dd>

Maximum size of the audit log in MB

</dd> <dt>

*DiskCheckInterval* \[in\]
</dt> <dd>

Number of audit log events after which the DHCP server should check available disk space (MinMBDiskSpace)

</dd> <dt>

*MinMBDiskSpace* \[in\]
</dt> <dd>

The minimum required disk space, in bytes, for audit log storage. Before logging a new audit log message, the DHCP server checks if the minimum disk space specified by this parameter is available on the disk or not. If it is not available, DHCP server halts audit logging till the time the required minimum disk space is available. If the value configured is 0 or left as default, minimum disk is set to 20MB.

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

An embedded instance of the [**DhcpServerAuditLog**](dhcpserverauditlog.md) class.

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

[**PS\_DhcpServerAuditLog**](ps-dhcpserverauditlog.md)
</dt> </dl>

 

 





