---
title: Win32_SessionDirectoryVirtualDesktopServer class
description: Represents a Remote Desktop Virtualization Host (RD Virtualization Host) server joined to a session broker.
ms.assetid: a09221bd-d1b1-465b-91bb-9ca400a796b1
ms.tgt_platform: multiple
keywords:
- Win32_SessionDirectoryVirtualDesktopServer class Remote Desktop Services
- Win32_SessionDirectoryVirtualDesktopServer class Remote Desktop Services , described
topic_type:
- apiref
api_name:
- Win32_SessionDirectoryVirtualDesktopServer
- Win32_SessionDirectoryVirtualDesktopServer.Name
api_location:
- TssdWmi.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Win32\_SessionDirectoryVirtualDesktopServer class

Represents a Remote Desktop Virtualization Host (RD Virtualization Host) server joined to a session broker.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("Win32_SDVirtualDesktopServer_Prov"), AMENDMENT]
class Win32_SessionDirectoryVirtualDesktopServer
{
  string Name;
};
```

## Members

The **Win32\_SessionDirectoryVirtualDesktopServer** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_SessionDirectoryVirtualDesktopServer** class has these properties.

<dl> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

The DNS name of the RD Virtualization Host server. This name takes the form "*MachineName*.*Domain*.com".

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                      |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                               |
| MOF<br/>                      | <dl> <dt>TssdWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>TssdWmi.dll</dt> </dl> |



 

