---
title: Win32_SessionDirectorySession class
description: Provides properties for viewing the properties of a Remote Desktop Connection Broker (RD Connection Broker) session.
ms.assetid: 34b5a898-3952-493c-ba62-dd0d298b0600
ms.tgt_platform: multiple
keywords:
- Win32_SessionDirectorySession class Remote Desktop Services
- Win32_SessionDirectorySession class Remote Desktop Services , described
topic_type:
- apiref
api_name:
- Win32_SessionDirectorySession
- Win32_SessionDirectorySession.ServerName
- Win32_SessionDirectorySession.SessionID
- Win32_SessionDirectorySession.UserName
- Win32_SessionDirectorySession.DomainName
- Win32_SessionDirectorySession.ServerIPAddress
- Win32_SessionDirectorySession.TSProtocol
- Win32_SessionDirectorySession.ApplicationType
- Win32_SessionDirectorySession.ResolutionWidth
- Win32_SessionDirectorySession.ResolutionHeight
- Win32_SessionDirectorySession.ColorDepth
- Win32_SessionDirectorySession.CreateTime
- Win32_SessionDirectorySession.DisconnectTime
- Win32_SessionDirectorySession.SessionState
api_location:
- TssdWmi.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Win32\_SessionDirectorySession class

Provides properties for viewing the properties of a Remote Desktop Connection Broker (RD Connection Broker) session.

> [!Note]  
> In Windows Server 2008 R2, the name of Terminal Services Session Broker (TS Session Broker) was changed to RD Connection Broker. These properties apply to all supported operating systems unless otherwise noted.

 

## Syntax

``` syntax
[dynamic, provider("Win32_WIN32_SESSIONDIRECTORYSESSION_Prov"), AMENDMENT]
class Win32_SessionDirectorySession
{
  string   ServerName;
  uint32   SessionID;
  string   UserName;
  string   DomainName;
  string   ServerIPAddress;
  uint32   TSProtocol;
  string   ApplicationType;
  uint32   ResolutionWidth;
  uint32   ResolutionHeight;
  uint32   ColorDepth;
  DateTime CreateTime;
  DateTime DisconnectTime;
  uint32   SessionState;
};
```

## Members

The **Win32\_SessionDirectorySession** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_SessionDirectorySession** class has these properties.

<dl> <dt>

**ApplicationType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Application started with this session. This is the same as the **StartProgram** property of [**IMsTscSecuredSettings**](imstscsecuredsettings-interface.md).

</dd> <dt>

**ColorDepth**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Color depth of the session, measured in bits per pixel.

</dd> <dt>

**CreateTime**
</dt> <dd> <dl> <dt>

Data type: **DateTime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Date and time the session was created. This value is not reset when a session is disconnected and reconnected.

</dd> <dt>

**DisconnectTime**
</dt> <dd> <dl> <dt>

Data type: **DateTime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Date and time the session was disconnected (if applicable).

</dd> <dt>

**DomainName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Domain name of the user logged on to this session.

</dd> <dt>

**ResolutionHeight**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Height of the session, in pixels, for this session.

</dd> <dt>

**ResolutionWidth**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Width of the session, in pixels, for this session.

</dd> <dt>

**ServerIPAddress**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

IP address of the RD Connection Broker server for this session.

</dd> <dt>

**ServerName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

Name of the RD Connection Broker server for this session.

</dd> <dt>

**SessionID**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

Session ID for this session.

</dd> <dt>

**SessionState**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

State of this session.

<dt>

0
</dt> <dd>

The session is active.

</dd> <dt>

1
</dt> <dd>

The session is disconnected.

</dd> </dl>

</dd> <dt>

**TSProtocol**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Protocol for this session.

<dt>

0
</dt> <dd>

This session is running on a physical console.

</dd> <dt>

1
</dt> <dd>

A proprietary third-party protocol is used for this session.

</dd> <dt>

2
</dt> <dd>

Remote Desktop Protocol (RDP) is used for this session.

</dd> </dl>

</dd> <dt>

**UserName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

User name of the user logged on to this session.

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

[**Win32\_SessionDirectoryServer**](win32-sessiondirectoryserver.md)
</dt> </dl>

 

