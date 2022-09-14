---
title: Win32_TSLogonSetting class
description: Defines configuration settings for the Win32\_Terminal class related to client logon.
ms.assetid: a2ccb419-da1a-44d1-8a7a-4d0266fc1be8
ms.tgt_platform: multiple
keywords:
- Win32_TSLogonSetting class Remote Desktop Services
- Win32_TSLogonSetting class Remote Desktop Services , described
topic_type:
- apiref
api_name:
- Win32_TSLogonSetting
- Win32_TSLogonSetting.Caption
- Win32_TSLogonSetting.Description
- Win32_TSLogonSetting.InstallDate
- Win32_TSLogonSetting.Name
- Win32_TSLogonSetting.Status
- Win32_TSLogonSetting.TerminalName
- Win32_TSLogonSetting.ClientLogonInfoPolicy
- Win32_TSLogonSetting.Domain
- Win32_TSLogonSetting.Password
- Win32_TSLogonSetting.PolicySourceDomain
- Win32_TSLogonSetting.PolicySourcePromptForPassword
- Win32_TSLogonSetting.PolicySourceUserName
- Win32_TSLogonSetting.PromptForPassword
- Win32_TSLogonSetting.UserName
api_location:
- TSCfgWmi.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Win32\_TSLogonSetting class

The **Win32\_TSLogonSetting** WMI class defines configuration settings for the [**Win32\_Terminal**](win32-terminal.md) class related to client logon.

The following syntax is simplified from MOF code and includes all defined and inherited properties, in alphabetical order. For reference information on methods, see the table of methods later in this topic.

## Syntax

``` syntax
[dynamic, provider("Win32_WIN32_TSLOGONSETTING_Prov"), ClassContext("local|hkey_local_machine\\SYSTEM\\CurrentControlSet\\Control\\TerminalServer\\WinStations"), AMENDMENT]
class Win32_TSLogonSetting : Win32_TerminalSetting
{
  string   Caption;
  string   Description;
  datetime InstallDate;
  string   Name;
  string   Status;
  string   TerminalName;
  uint32   ClientLogonInfoPolicy;
  string   Domain;
  string   Password;
  uint32   PolicySourceDomain;
  uint32   PolicySourcePromptForPassword;
  uint32   PolicySourceUserName;
  uint32   PromptForPassword;
  string   UserName;
};
```

## Members

The **Win32\_TSLogonSetting** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Win32\_TSLogonSetting** class has these methods.



| Method                                                                    | Description                                                                    |
|:--------------------------------------------------------------------------|:-------------------------------------------------------------------------------|
| [**ExplicitLogon**](win32-tslogonsetting-explicitlogon.md)               | Sets the UserName, Password, and Domain authentication credentials.<br/> |
| [**SetPromptForPassword**](win32-tslogonsetting-setpromptforpassword.md) | Sets the **PromptForPassword** property.<br/>                            |



 

### Properties

The **Win32\_TSLogonSetting** class has these properties.

<dl> <dt>

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

**ClientLogonInfoPolicy**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The policy the server uses to determine connection settings.

<dt>

<span id="Per_User"></span><span id="per_user"></span><span id="PER_USER"></span>

<span id="Per_User"></span><span id="per_user"></span><span id="PER_USER"></span>**Per User** (0)


</dt> <dd>

Individual user connection settings are in effect.

</dd> <dt>

<span id="Server-Override"></span><span id="server-override"></span><span id="SERVER-OVERRIDE"></span>

<span id="Server-Override"></span><span id="server-override"></span><span id="SERVER-OVERRIDE"></span>**Server-Override** (1)


</dt> <dd>

Individual user connection settings are overridden by the server.

</dd> </dl>

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

**Domain**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The user's domain logon authentication credential. This is the domain in which the user's computer resides. This property cannot be longer than 17 characters.

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

**Password**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The user's password logon authentication credential. This property cannot be longer than 14 characters. It is recommended that you set the security level to packet privacy (wbemAuthenticationLevelPktPrivacy = 6) if you query this property. This is because the password is not encrypted on the wire without this level of security. For more information about setting security levels, see [Setting Client Application Process Security](/windows/desktop/WmiSdk/setting-client-application-process-security) in the WMI SDK documentation.

</dd> <dt>

**PolicySourceDomain**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the **Domain** property is configured by the server, group policy, or by default.

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

**PolicySourcePromptForPassword**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the **PromptForPassword** property is configured by the server, group policy, or by default.

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

**PolicySourceUserName**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the **UserName** property is configured by the server, group policy, or by default.

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

**PromptForPassword**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies whether the user is always prompted for a password while logging into the server.

<dt>

<span id="FALSE"></span><span id="false"></span>

<span id="FALSE"></span><span id="false"></span>**FALSE** (0)


</dt> <dd>

The user is not prompted for a password.

</dd> <dt>

<span id="TRUE"></span><span id="true"></span>

<span id="TRUE"></span><span id="true"></span>**TRUE** (1)


</dt> <dd>

The user is prompted for a password.

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

**UserName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The user's user name logon authentication credential. This property cannot be longer than 20 characters.

</dd> </dl>

## Remarks

Be aware that Winstations associated with the console session cannot access the methods and properties of this class. If an attempt is made to do so by specifying "Console" as the value of the TerminalName property, methods of this object return **WBEM\_E\_NOT\_SUPPORTED**. This error code is returned if a window station attempts to call methods of this object to add or modify the security properties of the LocalSystem, LocalService, or NetworkService accounts.

To connect to the \\root\\CIMV2\\TerminalServices namespace, the authentication level must include packet privacy. For C/C++ calls, this is an authentication level of **RPC\_C\_AUTHN\_LEVEL\_PKT\_PRIVACY**. For Visual Basic and scripting calls, this is an authentication level of **WbemAuthenticationLevelPktPrivacy** or "pktPrivacy", with a value of 6. The following Visual Basic Scripting Edition (VBScript) example shows how to connect to a remote computer with packet privacy.


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

[**Win32\_Terminal**](win32-terminal.md)
</dt> <dt>

[**Win32\_TerminalSetting**](win32-terminalsetting.md)
</dt> </dl>

 

