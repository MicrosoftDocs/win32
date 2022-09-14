---
title: Win32_RemoteAppChangeEvent class
description: Represents a change to Windows Server 2008 R2 RemoteApp settings on the Remote Desktop Session Host (RD Session Host) server.
ms.assetid: 3434ee4e-283e-4147-a73b-c131e8af6c57
ms.tgt_platform: multiple
keywords:
- Win32_RemoteAppChangeEvent class Remote Desktop Services
- Win32_RemoteAppChangeEvent class Remote Desktop Services , described
topic_type:
- apiref
api_name:
- Win32_RemoteAppChangeEvent
- Win32_RemoteAppChangeEvent.SECURITY_DESCRIPTOR
- Win32_RemoteAppChangeEvent.TIME_CREATED
api_location:
- TsPubWmi.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Win32\_RemoteAppChangeEvent class

Represents a change to Windows Server 2008 R2 RemoteApp settings on the Remote Desktop Session Host (RD Session Host) server.

## Syntax

``` syntax
class Win32_RemoteAppChangeEvent : ExtrinsicEvent
{
  uint8  SECURITY_DESCRIPTOR[];
  uint64 TIME_CREATED;
};
```

## Members

The **Win32\_RemoteAppChangeEvent** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_RemoteAppChangeEvent** class has these properties.

<dl> <dt>

**SECURITY\_DESCRIPTOR**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Descriptor used by the event provider to determine which users can receive the event. This property is inherited from [**\_\_Event**](/windows/desktop/WmiSdk/--event). For more information about constants used to set this security descriptor, see [WMI Security Constants](/windows/desktop/WmiSdk/wmi-security-constants).

</dd> <dt>

**TIME\_CREATED**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Unique value that indicates the time at which the event was generated. This is a 64-bit value that represents the number of 100-nanosecond intervals after January 1, 1601. The information is in the Coordinated Universal Times (UTC) format. This property is inherited from [**\_\_Event**](/windows/desktop/WmiSdk/--event).

For more information about using **uint64** values in scripts, see [Scripting in WMI](/previous-versions//aa393262(v=vs.85)).

</dd> </dl>

## Remarks

To connect to the "Root\\CIMV2\\TerminalServices" namespace, the authentication level must include packet privacy. For C/C++ calls, this is an authentication level of **RPC\_C\_AUTHN\_LEVEL\_PKT\_PRIVACY**, which can be set by using the [**CoSetProxyBlanket**](/windows/win32/api/combaseapi/nf-combaseapi-cosetproxyblanket) COM function. For Visual Basic and scripting calls, this is an authentication level of **WbemAuthenticationLevelPktPrivacy** or "pktPrivacy", with a value of 6. The following Visual Basic Scripting Edition (VBScript) example shows how to connect to a remote computer with packet privacy.


```VB
strComputer = "RemoteServer1" 
Set objServices = GetObject( _
    "winmgmts:{authenticationLevel=pktPrivacy}!Root/CIMv2/TerminalServices")
```



Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Microsoft Windows Software Development Kit (SDK). They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](/windows/desktop/WmiSdk/managed-object-format--mof-).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                                |
| MOF<br/>                      | <dl> <dt>Tsallow.mof</dt> </dl>  |
| DLL<br/>                      | <dl> <dt>TsPubWmi.dll</dt> </dl> |



 

