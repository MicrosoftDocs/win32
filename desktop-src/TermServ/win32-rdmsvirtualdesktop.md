---
title: Win32_RDMSVirtualDesktop class
description: Represents a virtual desktop.
ms.assetid: e2952ec0-38d0-4a1c-b423-3ae1fbc701b3
ms.tgt_platform: multiple
keywords:
- Win32_RDMSVirtualDesktop class Remote Desktop Services
- Win32_RDMSVirtualDesktop class Remote Desktop Services , described
topic_type:
- apiref
api_name:
- Win32_RDMSVirtualDesktop
- Win32_RDMSVirtualDesktop.Name
- Win32_RDMSVirtualDesktop.HostName
- Win32_RDMSVirtualDesktop.Status
- Win32_RDMSVirtualDesktop.CollectionAlias
- Win32_RDMSVirtualDesktop.SessionState
- Win32_RDMSVirtualDesktop.SessionUserName
- Win32_RDMSVirtualDesktop.UserName
- Win32_RDMSVirtualDesktop.UserDomain
- Win32_RDMSVirtualDesktop.VMState
api_location:
- RDMS.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Win32\_RDMSVirtualDesktop class

Represents a virtual desktop.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("Win32_RDManagement_Prov"), AMENDMENT]
class Win32_RDMSVirtualDesktop
{
  string Name;
  string HostName;
  uint32 Status;
  string CollectionAlias;
  string SessionState;
  string SessionUserName;
  string UserName;
  string UserDomain;
  uint32 VMState;
};
```

## Members

The **Win32\_RDMSVirtualDesktop** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Win32\_RDMSVirtualDesktop** class has these methods.



| Method                                                                                              | Description                                                                                            |
|:----------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------|
| [**GetUserAssignment**](getuserassignment-win32-rdmsvirtualdesktop.md)                             | Retrieves the username and domain name of the user that is assigned to the virtual desktop.<br/> |
| [**GetVirtualDesktopAssignedToUser**](getvirtualdesktopassignedtouser-win32-rdmsvirtualdesktop.md) | Retrieves the virtual desktop that is assigned to the specified user.<br/>                       |
| [**GetVirtualDesktopDetails**](getvirtualdesktopdetails-win32-rdmsvirtualdesktop.md)               | Retrieves the additional information about the virtual desktop.<br/>                             |
| [**GetVirtualDesktopState**](getvirtualdesktopstate-win32-rdmsvirtualdesktop.md)                   | Retrieves the state of the virtual desktop.<br/>                                                 |
| [**RemoveUserAssignment**](removeuserassignment-win32-rdmsvirtualdesktop.md)                       | Removes the user assignment from the virtual desktop.<br/>                                       |
| [**SetUserAssignment**](setuserassignment-win32-rdmsvirtualdesktop.md)                             | Assigns a virtual desktop to a user.<br/>                                                        |
| [**SetVirtualDesktopState**](setvirtualdesktopstate-win32-rdmsvirtualdesktop.md)                   | Updates the state of the virtual desktop.<br/>                                                   |



 

### Properties

The **Win32\_RDMSVirtualDesktop** class has these properties.

<dl> <dt>

**CollectionAlias**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**optional**](/windows/desktop/WmiSdk/standard-wmi-qualifiers)
</dt> </dl>

Gets the alias to the virtual desktop collection that manages the virtual machine.

</dd> <dt>

**HostName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the name of the machine that hosts the virtual machine.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

Gets the name of the of virtual machine.

</dd> <dt>

**SessionState**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**optional**](/windows/desktop/WmiSdk/standard-wmi-qualifiers)
</dt> </dl>

Gets the state of the virtual desktop session.

</dd> <dt>

**SessionUserName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**optional**](/windows/desktop/WmiSdk/standard-wmi-qualifiers)
</dt> </dl>

Gets the username of the user that is logged in to the virtual desktop session.

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the status of the virtual machine.

</dd> <dt>

**UserDomain**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**optional**](/windows/desktop/WmiSdk/standard-wmi-qualifiers)
</dt> </dl>

Gets the domain name of the user that is assigned to the virtual desktop.

</dd> <dt>

**UserName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**optional**](/windows/desktop/WmiSdk/standard-wmi-qualifiers)
</dt> </dl>

Gets the username of the user that is assigned to the virtual desktop.

</dd> <dt>

**VMState**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the state of the virtual desktop.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                              |
| Namespace<br/>                | Root\\cimv2\\rdms<br/>                                                                |
| MOF<br/>                      | <dl> <dt>RDManagement.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RDMS.dll</dt> </dl>         |



## See also

<dl> <dt>

[Remote Desktop Management Services Provider](rdms-api-reference.md)
</dt> </dl>

 

