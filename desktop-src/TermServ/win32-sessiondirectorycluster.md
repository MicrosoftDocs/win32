---
title: Win32_SessionDirectoryCluster class
description: Provides properties for viewing the properties of a farm in Remote Desktop Connection Broker (RD Connection Broker).
ms.assetid: a4a924fd-88ea-46db-968e-378c3dc46cfc
ms.tgt_platform: multiple
keywords:
- Win32_SessionDirectoryCluster class Remote Desktop Services
- Win32_SessionDirectoryCluster class Remote Desktop Services , described
topic_type:
- apiref
api_name:
- Win32_SessionDirectoryCluster
- Win32_SessionDirectoryCluster.ClusterName
- Win32_SessionDirectoryCluster.NumberOfServers
- Win32_SessionDirectoryCluster.SingleSessionMode
api_location:
- TssdWmi.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Win32\_SessionDirectoryCluster class

Provides properties for viewing the properties of a farm in Remote Desktop Connection Broker (RD Connection Broker).

> [!Note]  
> In Windows Server 2008 R2, the name of Terminal Services Session Broker (TS Session Broker) was changed to RD Connection Broker. These properties apply to all supported operating systems unless otherwise noted.

 

## Syntax

``` syntax
[dynamic, provider("Win32_WIN32_SESSIONDIRECTORYCLUSTER_Prov"), AMENDMENT]
class Win32_SessionDirectoryCluster
{
  string ClusterName;
  uint32 NumberOfServers;
  uint32 SingleSessionMode;
};
```

## Members

The **Win32\_SessionDirectoryCluster** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_SessionDirectoryCluster** class has these properties.

<dl> <dt>

**ClusterName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

Name of the farm in RD Connection Broker.

</dd> <dt>

**NumberOfServers**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of servers in the farm in RD Connection Broker.

</dd> <dt>

**SingleSessionMode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Single session mode of the farm in RD Connection Broker.

<dt>

0
</dt> <dd>

The farm in RD Connection Broker is not in single session mode.

</dd> <dt>

1
</dt> <dd>

The farm in RD Connection Broker is in single session mode.

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

[**Win32\_SessionDirectoryServer**](win32-sessiondirectoryserver.md)
</dt> <dt>

[**Win32\_SessionDirectorySession**](win32-sessiondirectorysession.md)
</dt> </dl>

 

