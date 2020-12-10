---
title: Win32_VirtualDesktopSession class
description: Manages a virtual desktop session.
ms.assetid: a5a0d2a4-6e19-42ac-988c-2d3787946325
ms.tgt_platform: multiple
keywords:
- Win32_VirtualDesktopSession class Remote Desktop Services
- Win32_VirtualDesktopSession class Remote Desktop Services , described
topic_type:
- apiref
api_name:
- Win32_VirtualDesktopSession
- Win32_VirtualDesktopSession.VMHostName
- Win32_VirtualDesktopSession.SessionId
- Win32_VirtualDesktopSession.VMName
- Win32_VirtualDesktopSession.ConnectState
- Win32_VirtualDesktopSession.UserName
- Win32_VirtualDesktopSession.DomainName
- Win32_VirtualDesktopSession.CollectionId
- Win32_VirtualDesktopSession.ClientMachineName
api_location:
- RDMS.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Win32\_VirtualDesktopSession class

Manages a virtual desktop session.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("Win32_RDManagement_Prov"), AMENDMENT]
class Win32_VirtualDesktopSession
{
  string VMHostName;
  uint32 SessionId;
  string VMName;
  uint32 ConnectState;
  string UserName;
  string DomainName;
  string CollectionId;
  string ClientMachineName;
};
```

## Members

The **Win32\_VirtualDesktopSession** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Win32\_VirtualDesktopSession** class has these methods.



| Method                                                         | Description                                                                |
|:---------------------------------------------------------------|:---------------------------------------------------------------------------|
| [**Disconnect**](disconnect-win32-virtualdesktopsession.md)   | Disconnects the virtual desktop session.<br/>                        |
| [**Logoff**](logoff-win32-virtualdesktopsession.md)           | Logs off the user from the virtual desktop session.<br/>             |
| [**SendMessage**](sendmessage-win32-virtualdesktopsession.md) | Send a message to the user through the virtual desktop session.<br/> |



 

### Properties

The **Win32\_VirtualDesktopSession** class has these properties.

<dl> <dt>

**ClientMachineName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the name of the client machine that is connected to the session.

</dd> <dt>

**CollectionId**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the name of the virtual desktop collection that hosts the virtual machine.

</dd> <dt>

**ConnectState**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the state of the connection to the session.

</dd> <dt>

**DomainName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the domain name of the user.

</dd> <dt>

**SessionId**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

Gets the ID of the virtual desktop session.

</dd> <dt>

**UserName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the name of the user account that is assigned to the session.

</dd> <dt>

**VMHostName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

Gets the name of the Remote Desktop virtualization host server that hosts the virtual machine.

</dd> <dt>

**VMName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the name of the virtual machine that is assigned to the session.

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

 

