---
title: Win32_SessionDirectoryServer class
description: Provides properties for viewing the properties of a Remote Desktop Connection Broker (RD Connection Broker) server.
ms.assetid: 73017b71-eff9-4ef6-aba0-71ddb969491f
ms.tgt_platform: multiple
keywords:
- Win32_SessionDirectoryServer class Remote Desktop Services
- Win32_SessionDirectoryServer class Remote Desktop Services , described
topic_type:
- apiref
api_name:
- Win32_SessionDirectoryServer
- Win32_SessionDirectoryServer.ServerName
- Win32_SessionDirectoryServer.ServerIPAddress
- Win32_SessionDirectoryServer.ClusterName
- Win32_SessionDirectoryServer.NumberOfSessions
- Win32_SessionDirectoryServer.SingleSessionMode
- Win32_SessionDirectoryServer.ServerWeight
- Win32_SessionDirectoryServer.NumPendRedir
- Win32_SessionDirectoryServer.LoadIndicator
api_location:
- TssdWmi.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Win32\_SessionDirectoryServer class

Provides properties for viewing the properties of a Remote Desktop Connection Broker (RD Connection Broker) server.

> [!Note]  
> In Windows Server 2008 R2, the name of Terminal Services Session Broker (TS Session Broker) was changed to RD Connection Broker. These properties apply to all supported operating systems unless otherwise noted.

 

## Syntax

``` syntax
[dynamic, provider("Win32_WIN32_SESSIONDIRECTORYSERVER_Prov"), AMENDMENT]
class Win32_SessionDirectoryServer
{
  string ServerName;
  string ServerIPAddress;
  string ClusterName;
  uint32 NumberOfSessions;
  uint32 SingleSessionMode;
  uint32 ServerWeight;
  uint32 NumPendRedir;
  uint32 LoadIndicator;
};
```

## Members

The **Win32\_SessionDirectoryServer** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_SessionDirectoryServer** class has these properties.

<dl> <dt>

**ClusterName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the farm that includes the server.

</dd> <dt>

**LoadIndicator**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A relative number that represents the RD Session Host server load when the default load-balancing algorithm is used. The *LoadIndicator* property value is based on the number of sessions, the number of pending redirection requests, and the server weight value.

</dd> <dt>

**NumberOfSessions**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of sessions in the RD Connection Broker server.

</dd> <dt>

**NumPendRedir**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of pending redirection requests.

</dd> <dt>

**ServerIPAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

IP address of the RD Connection Broker server. If the server is configured for both IPv4 and IPv6 addresses, this will contain the IPv4 address.

</dd> <dt>

**ServerName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

Name of the RD Connection Broker server.

</dd> <dt>

**ServerWeight**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Server weight value, used in load balancing.

</dd> <dt>

**SingleSessionMode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Single session mode setting of the RD Connection Broker server.

<dt>

0
</dt> <dd>

The farm is not in single session mode.

</dd> <dt>

1
</dt> <dd>

The farm in is in single session mode.

</dd> </dl>

</dd> </dl>

## Remarks

Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Microsoft Windows Software Development Kit (SDK). They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](/windows/desktop/WmiSdk/managed-object-format--mof-).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\CIMv2<br/>                                                                 |
| MOF<br/>                      | <dl> <dt>TssdWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>TssdWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_SessionDirectoryCluster**](win32-sessiondirectorycluster.md)
</dt> <dt>

[**Win32\_SessionDirectorySession**](win32-sessiondirectorysession.md)
</dt> </dl>

 

