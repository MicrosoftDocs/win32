---
title: Win32_TSSessionSetting class
description: Defines configuration settings for the Win32\_Terminal class such as time-limits, and disconnection and reconnection actions.
ms.assetid: e115f370-270c-404f-b6c6-7781c1ff376f
ms.tgt_platform: multiple
keywords:
- Win32_TSSessionSetting class Remote Desktop Services
- Win32_TSSessionSetting class Remote Desktop Services , described
topic_type:
- apiref
api_name:
- Win32_TSSessionSetting
- Win32_TSSessionSetting.Caption
- Win32_TSSessionSetting.Description
- Win32_TSSessionSetting.InstallDate
- Win32_TSSessionSetting.Name
- Win32_TSSessionSetting.Status
- Win32_TSSessionSetting.TerminalName
- Win32_TSSessionSetting.ActiveSessionLimit
- Win32_TSSessionSetting.BrokenConnectionAction
- Win32_TSSessionSetting.BrokenConnectionPolicy
- Win32_TSSessionSetting.DisconnectedSessionLimit
- Win32_TSSessionSetting.IdleSessionLimit
- Win32_TSSessionSetting.PolicySourceActiveSessionLimit
- Win32_TSSessionSetting.PolicySourceBrokenConnectionAction
- Win32_TSSessionSetting.PolicySourceDisconnectedSessionLimit
- Win32_TSSessionSetting.PolicySourceIdleSessionLimit
- Win32_TSSessionSetting.PolicySourceReconnectionPolicy
- Win32_TSSessionSetting.ReconnectionPolicy
- Win32_TSSessionSetting.TimeLimitPolicy
- Win32_TSSessionSetting.EnableTimeoutWarning
api_location:
- TSCfgWmi.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Win32\_TSSessionSetting class

The **Win32\_TSSessionSetting** WMI class defines configuration settings for the [**Win32\_Terminal**](win32-terminal.md) class such as time-limits, and disconnection and reconnection actions.

The following syntax is simplified from MOF code and includes all defined and inherited properties, in alphabetical order. For reference information on methods, see the table of methods later in this topic.

## Syntax

``` syntax
[dynamic, provider("Win32_WIN32_TSSESSIONSETTING_Prov"), ClassContext("local|hkey_local_machine\\SYSTEM\\CurrentControlSet\\Control\\TerminalServer\\WinStations"), AMENDMENT]
class Win32_TSSessionSetting : Win32_TerminalSetting
{
  string   Caption;
  string   Description;
  datetime InstallDate;
  string   Name;
  string   Status;
  string   TerminalName;
  uint32   ActiveSessionLimit;
  uint32   BrokenConnectionAction;
  uint32   BrokenConnectionPolicy;
  uint32   DisconnectedSessionLimit;
  uint32   IdleSessionLimit;
  uint32   PolicySourceActiveSessionLimit;
  uint32   PolicySourceBrokenConnectionAction;
  uint32   PolicySourceDisconnectedSessionLimit;
  uint32   PolicySourceIdleSessionLimit;
  uint32   PolicySourceReconnectionPolicy;
  uint32   ReconnectionPolicy;
  uint32   TimeLimitPolicy;
  uint32   EnableTimeoutWarning;
};
```

## Members

The **Win32\_TSSessionSetting** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Win32\_TSSessionSetting** class has these methods.



| Method                                                              | Description                                                              |
|:--------------------------------------------------------------------|:-------------------------------------------------------------------------|
| [**BrokenConnection**](win32-tssessionsetting-brokenconnection.md) | Sets the broken connection properties included in this class.<br/> |
| [**TimeLimit**](win32-tssessionsetting-timelimit.md)               | Sets the time-limit properties included in this class.<br/>        |



 

### Properties

The **Win32\_TSSessionSetting** class has these properties.

<dl> <dt>

**ActiveSessionLimit**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The maximum amount of time, in milliseconds, allocated to an active session. A value of 0 specifies an infinite amount of time.

</dd> <dt>

**BrokenConnectionAction**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The action the server takes on the session when a connection has been broken due to network loss or exceeded time-limits.

<dt>

<span id="Disconnect"></span><span id="disconnect"></span><span id="DISCONNECT"></span>

<span id="Disconnect"></span><span id="disconnect"></span><span id="DISCONNECT"></span>**Disconnect** (0)


</dt> <dd>

The user is disconnected from the session.

</dd> <dt>

<span id="Terminate"></span><span id="terminate"></span><span id="TERMINATE"></span>

<span id="Terminate"></span><span id="terminate"></span><span id="TERMINATE"></span>**Terminate** (1)


</dt> <dd>

The session is permanently deleted from the server.

</dd> </dl>

</dd> <dt>

**BrokenConnectionPolicy**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The policy the server uses to determine when to break a connection because of network loss or exceeded time-limits.

<dt>

<span id="Server-Override"></span><span id="server-override"></span><span id="SERVER-OVERRIDE"></span>

<span id="Server-Override"></span><span id="server-override"></span><span id="SERVER-OVERRIDE"></span>**Server-Override** (1)


</dt> <dd>

The user's disconnection policy settings are overridden by the server.

</dd> <dt>

<span id="Per_User"></span><span id="per_user"></span><span id="PER_USER"></span>

<span id="Per_User"></span><span id="per_user"></span><span id="PER_USER"></span>**Per User** (0)


</dt> <dd>

The user's disconnection policy settings are in effect.

</dd> </dl>

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (64)
</dt> </dl>

Short description (one-line string) of the object.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Description of the object.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**DisconnectedSessionLimit**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The time interval, in milliseconds, after which a disconnected session is terminated. A value of 0 specifies an infinite amount of time.

</dd> <dt>

**EnableTimeoutWarning**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Enables the timeout warning.

**Windows 7, Windows Server 2008 R2, Windows Vista and Windows Server 2008:** This property is not available.

</dd> <dt>

**IdleSessionLimit**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The time interval, in milliseconds, after which an idle session is terminated. A value of 0 specifies an infinite amount of time.

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Mappingstrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("MIF.DMTF\|ComponentID\|001.5")
</dt> </dl>

The date the object was installed. A lack of a value does not indicate that the object is not installed.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the object.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

</dd> <dt>

**PolicySourceActiveSessionLimit**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the **ActiveSessionLimit** property is configured by the server, group policy, or by default.

<dt>

0
</dt> <dd>

Server

</dd> <dt>

1
</dt> <dd>

Group policy

</dd> <dt>

2
</dt> <dd>

Default

</dd> </dl>

</dd> <dt>

**PolicySourceBrokenConnectionAction**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the **BrokenConnectionAction** property is configured by the server, group policy, or by default.

<dt>

0
</dt> <dd>

Server

</dd> <dt>

1
</dt> <dd>

Group policy

</dd> <dt>

2
</dt> <dd>

Default

</dd> </dl>

</dd> <dt>

**PolicySourceDisconnectedSessionLimit**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the **DisconnectedSessionLimit** property is configured by the server, group policy, or by default.

<dt>

0
</dt> <dd>

Server

</dd> <dt>

1
</dt> <dd>

Group policy

</dd> <dt>

2
</dt> <dd>

Default

</dd> </dl>

</dd> <dt>

**PolicySourceIdleSessionLimit**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the **IdleSessionLimit** property is configured by the server, group policy, or by default.

<dt>

0
</dt> <dd>

Server

</dd> <dt>

1
</dt> <dd>

Group policy

</dd> <dt>

2
</dt> <dd>

Default

</dd> </dl>

</dd> <dt>

**PolicySourceReconnectionPolicy**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the **ReconnectPolicy** property is configured by the server, group policy, or by default.

<dt>

0
</dt> <dd>

Server

</dd> <dt>

1
</dt> <dd>

Group policy

</dd> <dt>

2
</dt> <dd>

Default

</dd> </dl>

</dd> <dt>

**ReconnectionPolicy**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Specifies whether a user must use the previous client to reconnect to a disconnected session.

<dt>

<span id="Any_Client"></span><span id="any_client"></span><span id="ANY_CLIENT"></span>

<span id="Any_Client"></span><span id="any_client"></span><span id="ANY_CLIENT"></span>**Any Client** (0)


</dt> <dd>

Any client will be used to reconnect.

</dd> <dt>

<span id="Previous_Client"></span><span id="previous_client"></span><span id="PREVIOUS_CLIENT"></span>

<span id="Previous_Client"></span><span id="previous_client"></span><span id="PREVIOUS_CLIENT"></span>**Previous Client** (1)


</dt> <dd>

The previous client used in a connection will be used to reconnect.

</dd> </dl>

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (10)
</dt> </dl>

Current status of the object. Various operational and nonoperational statuses can be defined. Operational statuses include: "OK", "Degraded", and "Pred Fail" (an element, such as a SMART-enabled hard disk drive, may be functioning properly but predicting a failure in the near future). Nonoperational statuses include: "Error", "Starting", "Stopping", and "Service". The latter, "Service", could apply during mirror-resilvering of a disk, reload of a user permissions list, or other administrative work. Not all such work is on-line, yet the managed element is neither "OK" nor in one of the other states.

This property is inherited from [**CIM\_ManagedSystemElement**](cim-managedsystemelement.md).

<dt>



 ("OK")


</dt> <dd></dd> <dt>



 ("Error")


</dt> <dd></dd> <dt>



 ("Degraded")


</dt> <dd></dd> <dt>



 ("Unknown")


</dt> <dd></dd> <dt>



 ("Pred Fail")


</dt> <dd></dd> <dt>



 ("Starting")


</dt> <dd></dd> <dt>



 ("Stopping")


</dt> <dd></dd> <dt>



 ("Service")


</dt> <dd></dd> </dl>

</dd> <dt>

**TerminalName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the terminal.

This property is inherited from [**Win32\_TerminalSetting**](win32-terminalsetting.md).

</dd> <dt>

**TimeLimitPolicy**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The policy the server uses to determine time-limits for user sessions.

<dt>

<span id="Per_User"></span><span id="per_user"></span><span id="PER_USER"></span>

<span id="Per_User"></span><span id="per_user"></span><span id="PER_USER"></span>**Per User** (0)


</dt> <dd>

The user's time-limits policy settings are in effect.

</dd> <dt>

<span id="Server_Override"></span><span id="server_override"></span><span id="SERVER_OVERRIDE"></span>

<span id="Server_Override"></span><span id="server_override"></span><span id="SERVER_OVERRIDE"></span>**Server Override** (1)


</dt> <dd>

The user's time-limits policy settings are overridden by the server.

</dd> </dl>

</dd> </dl>

## Remarks

Be aware that Winstations associated with the console session cannot access the methods and properties of this class. If an attempt is made to do so by specifying "Console" as the value of the TerminalName property, methods of this object will return **WBEM\_E\_NOT\_SUPPORTED**. This error code will also be returned if a window station attempts to call methods of this object for the purpose of adding or modifying the security properties of the LocalSystem, LocalService, or NetworkService accounts.

To connect to the "root\\CIMV2\\TerminalServices" namespace, the authentication level must include packet privacy. For C/C++ calls, this would be an authentication level of **RPC\_C\_AUTHN\_LEVEL\_PKT\_PRIVACY**. For Visual Basic and scripting calls, this would be an authentication level of **WbemAuthenticationLevelPktPrivacy** or "pktPrivacy", with a value of 6. The following Visual Basic Scripting Edition (VBScript) example shows how to connect to a remote computer with packet privacy.


```VB
strComputer = "RemoteServer1" 
Set objServices = GetObject( _
    "winmgmts:{authenticationLevel=pktPrivacy}!Root/CIMv2/TerminalServices")
```



Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Microsoft Windows Software Development Kit (SDK). They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](/windows/desktop/WmiSdk/managed-object-format--mof-).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                                |
| MOF<br/>                      | <dl> <dt>TSCfgWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>TSCfgWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_TerminalSetting**](win32-terminalsetting.md)
</dt> <dt>

[**CIM\_Setting**](/windows/desktop/CIMWin32Prov/cim-setting)
</dt> </dl>

 

