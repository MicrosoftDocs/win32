---
description: The Win32\_DCOMApplicationSetting&\#8194;WMI class represents the settings of a DCOM application.
ms.assetid: afa23faa-bf4d-4f54-9ee9-227956ff3292
ms.tgt_platform: multiple
title: Win32_DCOMApplicationSetting class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_DCOMApplicationSetting
- Win32_DCOMApplicationSetting.Caption
- Win32_DCOMApplicationSetting.Description
- Win32_DCOMApplicationSetting.SettingID
- Win32_DCOMApplicationSetting.AppID
- Win32_DCOMApplicationSetting.AuthenticationLevel
- Win32_DCOMApplicationSetting.CustomSurrogate
- Win32_DCOMApplicationSetting.EnableAtStorageActivation
- Win32_DCOMApplicationSetting.LocalService
- Win32_DCOMApplicationSetting.RemoteServerName
- Win32_DCOMApplicationSetting.RunAsUser
- Win32_DCOMApplicationSetting.ServiceParameters
- Win32_DCOMApplicationSetting.UseSurrogate
api_type: 
- DllExport
api_location: 
- CIMWin32.dll
---

# Win32\_DCOMApplicationSetting class

The **Win32\_DCOMApplicationSetting** [WMI class](/windows/desktop/WmiSdk/retrieving-a-class) represents the settings of a DCOM application. It contains DCOM configuration options associated with the **AppID** key in the registry. These options are valid on the components logically grouped under the given application class.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties. Properties are listed in alphabetic order, not MOF order.

## Syntax

``` syntax
[Dynamic, Provider("CIMWin32"), UUID("{E5D8A561-F6C0-11d2-B35E-00105A1F8569}"), AMENDMENT]
class Win32_DCOMApplicationSetting : Win32_COMSetting
{
  string  Caption;
  string  Description;
  string  SettingID;
  string  AppID;
  uint32  AuthenticationLevel;
  string  CustomSurrogate;
  boolean EnableAtStorageActivation;
  string  LocalService;
  string  RemoteServerName;
  string  RunAsUser;
  string  ServiceParameters;
  boolean UseSurrogate;
};
```

## Members

The **Win32\_DCOMApplicationSetting** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Win32\_DCOMApplicationSetting** class has these methods.



| Method                                                                                                                        | Description                                                                                                                                                                                                                     |
|:------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetAccessSecurityDescriptor**](getaccesssecuritydescriptor-method-in-class-win32-dcomapplicationsetting.md)               | Gets the security descriptor that controls who is allowed to access a DCOM application.<br/>                                                                                                                              |
| [**GetConfigurationSecurityDescriptor**](getconfigurationsecuritydescriptor-method-in-class-win32-dcomapplicationsetting.md) | Gets the security descriptor that controls who is allowed to configure a DCOM application.<br/>                                                                                                                           |
| [**GetLaunchSecurityDescriptor**](getlaunchsecuritydescriptor-in-class-win32-dcomapplicationsetting.md)                      | Gets the security descriptor that controls who is allowed to launch a DCOM application.<br/>                                                                                                                              |
| [**SetAccessSecurityDescriptor**](setaccesssecuritydescriptor-method-in-class-win32-dcomapplicationsetting.md)               | Updates the access security descriptor of the DCOM application with a new security descriptor that is defined by an instance of the [**Win32\_SecurityDescriptor**](/previous-versions/windows/desktop/secrcw32prov/win32-securitydescriptor) class.<br/>        |
| [**SetConfigurationSecurityDescriptor**](setconfigurationsecuritydescriptor-method-in-class-win32-dcomapplicationsetting.md) | Updates the configuration security descriptor of the DCOM application with a new security descriptor that is defined by an instance of the [**Win32\_SecurityDescriptor**](/previous-versions/windows/desktop/secrcw32prov/win32-securitydescriptor) class.<br/> |
| [**SetLaunchSecurityDescriptor**](setlaunchsecuritydescriptor-method-in-class-win32-dcomapplicationsetting.md)               | Updates the launch security descriptor of the DCOM application with a new security descriptor that is defined by an instance of the [**Win32\_SecurityDescriptor**](/previous-versions/windows/desktop/secrcw32prov/win32-securitydescriptor) class.<br/>        |



 

### Properties

The **Win32\_DCOMApplicationSetting** class has these properties.

<dl> <dt>

**AppID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](/windows/desktop/WmiSdk/key-qualifier), [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("Win32Registry\|HKEY\_LOCAL\_MACHINE\\\\SOFTWARE\\\\Classes\\\\AppID\\\\{GUID}\[Default\]")
</dt> </dl>

Globally unique identifier (GUID) for this DCOM application.

</dd> <dt>

**AuthenticationLevel**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("Win32Registry\|HKEY\_LOCAL\_MACHINE\\\\SOFTWARE\\\\Classes\\\\AppID\\\\{GUID}\[AuthenticationLevel\]")
</dt> </dl>

Minimum client authentication level required by this COM server. If **NULL**, the default values are used.

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

<span id="None"></span><span id="none"></span><span id="NONE"></span>**None** (1)


</dt> <dd>

None (no authentication is performed)

</dd> <dt>

<span id="Connect"></span><span id="connect"></span><span id="CONNECT"></span>

<span id="Connect"></span><span id="connect"></span><span id="CONNECT"></span>**Connect** (2)


</dt> <dd>

Connect (authentication is performed only when the client establishes a relationship with the application)

</dd> <dt>

<span id="Call"></span><span id="call"></span><span id="CALL"></span>

<span id="Call"></span><span id="call"></span><span id="CALL"></span>**Call** (3)


</dt> <dd>

Call (authentication is performed only at the beginning of each call when the application receives the request)

</dd> <dt>

<span id="Packet"></span><span id="packet"></span><span id="PACKET"></span>

<span id="Packet"></span><span id="packet"></span><span id="PACKET"></span>**Packet** (4)


</dt> <dd>

Packet (authentication is performed on all of the data received from the client)

</dd> <dt>

<span id="PacketIntegrity"></span><span id="packetintegrity"></span><span id="PACKETINTEGRITY"></span>

<span id="PacketIntegrity"></span><span id="packetintegrity"></span><span id="PACKETINTEGRITY"></span>**PacketIntegrity** (5)


</dt> <dd>

PacketIntegrity (all of the data transferred between the client and the application is authenticated and verified)

</dd> <dt>

<span id="PacketPrivacy"></span><span id="packetprivacy"></span><span id="PACKETPRIVACY"></span>

<span id="PacketPrivacy"></span><span id="packetprivacy"></span><span id="PACKETPRIVACY"></span>**PacketPrivacy** (6)


</dt> <dd>

PacketPrivacy (the properties of the other authentication levels are used and all of the data is encrypted)

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

Short textual description of the current object.

This property is inherited from [**CIM\_Setting**](cim-setting.md).

</dd> <dt>

**CustomSurrogate**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("Win32Registry\|HKEY\_LOCAL\_MACHINE\\\\SOFTWARE\\\\Classes\\\\AppID\\\\{GUID}\[DllSurrogate\]")
</dt> </dl>

Name of the custom surrogate in which the in-process DCOM application is activated. If this value is **NULL** and the **UseSurrogate** key is **TRUE**, then the system provides a surrogate process.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Textual description of the current object.

This property is inherited from [**CIM\_Setting**](cim-setting.md).

</dd> <dt>

**EnableAtStorageActivation**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("Win32Registry\|HKEY\_LOCAL\_MACHINE\\\\SOFTWARE\\\\Classes\\\\AppID\\\\{GUID}\[ActivateAtStorage\]")
</dt> </dl>

DCOM application retrieves the saved state of the application or begins from the state in which the application is first initialized.

</dd> <dt>

**LocalService**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("Win32Registry\|HKEY\_LOCAL\_MACHINE\\\\SOFTWARE\\\\Classes\\\\AppID\\\\{GUID}\[LocalService\]")
</dt> </dl>

Name for the services provided by the DCOM application.

</dd> <dt>

**RemoteServerName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("Win32Registry\|HKEY\_LOCAL\_MACHINE\\\\SOFTWARE\\\\Classes\\\\AppID\\\\{GUID}\[RemoteServerName\]")
</dt> </dl>

Name of the remote server where the application is activated.

</dd> <dt>

**RunAsUser**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("Win32Registry\|HKEY\_LOCAL\_MACHINE\\\\SOFTWARE\\\\Classes\\\\AppID\\\\{GUID}\[RunAs\]")
</dt> </dl>

Specific user account under which the application is to be run on activation.

</dd> <dt>

**ServiceParameters**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("Win32Registry\|HKEY\_LOCAL\_MACHINE\\\\SOFTWARE\\\\Classes\\\\AppID\\\\{GUID}\[ServiceParameters\]")
</dt> </dl>

Command-line parameters passed to the DCOM application. This is valid only if the application is written as a Windows-based service.

</dd> <dt>

**SettingID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (256)
</dt> </dl>

Identifier by which the current object is known.

This property is inherited from [**CIM\_Setting**](cim-setting.md).

</dd> <dt>

**UseSurrogate**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MappingStrings**](/windows/desktop/WmiSdk/standard-qualifiers) ("Win32Registry\|HKEY\_LOCAL\_MACHINE\\\\SOFTWARE\\\\Classes\\\\AppID\\\\{GUID}\[DllSurrogate\]")
</dt> </dl>

DCOM application can be activated as an out-of-process server by use of a surrogate executable file.

</dd> </dl>

## Remarks

The **Win32\_DCOMApplicationSetting** class is derived from [**Win32\_COMSetting**](win32-comsetting.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CIMWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>CIMWin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_COMSetting**](win32-comsetting.md)
</dt> <dt>

[Operating System Classes](/previous-versions//aa392727(v=vs.85))
</dt> <dt>

[**Privilege Constants**](/windows/desktop/WmiSdk/privilege-constants)
</dt> <dt>

[WMI Security Descriptor Objects](/windows/desktop/WmiSdk/wmi-security-descriptor-objects)
</dt> <dt>

[Changing Access Security on Securable Objects](/windows/desktop/WmiSdk/changing-access-security-on-securable-objects)
</dt> </dl>

 

