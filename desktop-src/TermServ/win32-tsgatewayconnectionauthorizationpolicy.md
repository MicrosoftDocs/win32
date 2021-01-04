---
title: Win32_TSGatewayConnectionAuthorizationPolicy class
description: Describes a Remote Desktop connection authorization policy (RD \ 160;CAP). RD \ 160;CAPs are used to determine whether a user is allowed to connect to the Remote Desktop Gateway (RD Gateway) server.
ms.assetid: 50ff3f97-0818-4e9c-9db7-a822cfed0e82
ms.tgt_platform: multiple
keywords:
- Win32_TSGatewayConnectionAuthorizationPolicy class Remote Desktop Services
- Win32_TSGatewayConnectionAuthorizationPolicy class Remote Desktop Services , described
topic_type:
- apiref
api_name:
- Win32_TSGatewayConnectionAuthorizationPolicy
- Win32_TSGatewayConnectionAuthorizationPolicy.Name
- Win32_TSGatewayConnectionAuthorizationPolicy.Order
- Win32_TSGatewayConnectionAuthorizationPolicy.SmartcardAllowed
- Win32_TSGatewayConnectionAuthorizationPolicy.PasswordAllowed
- Win32_TSGatewayConnectionAuthorizationPolicy.SecureIdAllowed
- Win32_TSGatewayConnectionAuthorizationPolicy.CookieAuthenticationAllowed
- Win32_TSGatewayConnectionAuthorizationPolicy.Enabled
- Win32_TSGatewayConnectionAuthorizationPolicy.IdleTimeout
- Win32_TSGatewayConnectionAuthorizationPolicy.SessionTimeout
- Win32_TSGatewayConnectionAuthorizationPolicy.SessionTimeoutAction
- Win32_TSGatewayConnectionAuthorizationPolicy.DeviceRedirectionType
- Win32_TSGatewayConnectionAuthorizationPolicy.DiskDrivesDisabled
- Win32_TSGatewayConnectionAuthorizationPolicy.PrintersDisabled
- Win32_TSGatewayConnectionAuthorizationPolicy.SerialPortsDisabled
- Win32_TSGatewayConnectionAuthorizationPolicy.ClipboardDisabled
- Win32_TSGatewayConnectionAuthorizationPolicy.PlugAndPlayDevicesDisabled
- Win32_TSGatewayConnectionAuthorizationPolicy.UserGroupNames
- Win32_TSGatewayConnectionAuthorizationPolicy.ComputerGroupNames
- Win32_TSGatewayConnectionAuthorizationPolicy.HasNapAttributes
- Win32_TSGatewayConnectionAuthorizationPolicy.AllowOnlySDRServers
api_location:
- AagWmi.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Win32\_TSGatewayConnectionAuthorizationPolicy class

Describes a Remote Desktop connection authorization policy (RD CAP). RD CAPs are used to determine whether a user is allowed to connect to the Remote Desktop Gateway (RD Gateway) server.

## Syntax

``` syntax
[dynamic, provider("AAGProvider"), AMENDMENT]
class Win32_TSGatewayConnectionAuthorizationPolicy
{
  string  Name;
  uint32  Order;
  boolean SmartcardAllowed;
  boolean PasswordAllowed;
  boolean SecureIdAllowed;
  boolean CookieAuthenticationAllowed;
  boolean Enabled;
  uint32  IdleTimeout;
  uint32  SessionTimeout;
  uint32  SessionTimeoutAction;
  uint32  DeviceRedirectionType;
  boolean DiskDrivesDisabled;
  boolean PrintersDisabled;
  boolean SerialPortsDisabled;
  boolean ClipboardDisabled;
  boolean PlugAndPlayDevicesDisabled;
  string  UserGroupNames;
  string  ComputerGroupNames;
  boolean HasNapAttributes;
  boolean AllowOnlySDRServers;
};
```

## Members

The **Win32\_TSGatewayConnectionAuthorizationPolicy** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Win32\_TSGatewayConnectionAuthorizationPolicy** class has these methods.



| Method                                                                                                                | Description                                                                                                                                                                     |
|:----------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddComputerGroupNames**](addcomputergroupnames-win32-tsgatewayconnectionauthorizationpolicy.md)                   | Adds the specified computer group names to the **ComputerGroupNames** property.<br/>                                                                                      |
| [**AddUserGroupNames**](addusergroupnames-win32-tsgatewayconnectionauthorizationpolicy.md)                           | Adds the specified user group names to the **UserGroupNames** property.<br/>                                                                                              |
| [**Create**](create-win32-tsgatewayconnectionauthorizationpolicy.md)                                                 | Creates an RD CAP.<br/>                                                                                                                                                   |
| [**Delete**](delete-win32-tsgatewayconnectionauthorizationpolicy.md)                                                 | Deletes the current RD CAP.<br/>                                                                                                                                          |
| [**DisableClipboard**](disableclipboard-win32-tsgatewayconnectionauthorizationpolicy.md)                             | Sets the **ClipboardDisabled** property.<br/>                                                                                                                             |
| [**DisableDiskDrives**](disablediskdrives-win32-tsgatewayconnectionauthorizationpolicy.md)                           | Sets the **DiskDrivesDisabled** property.<br/>                                                                                                                            |
| [**DisablePlugAndPlayDevices**](disableplugandplaydevices-win32-tsgatewayconnectionauthorizationpolicy.md)           | Sets the **PlugAndPlayDevicesDisabled** property.<br/>                                                                                                                    |
| [**DisablePrinters**](disableprinters-win32-tsgatewayconnectionauthorizationpolicy.md)                               | Sets the **PrintersDisabled** property.<br/>                                                                                                                              |
| [**DisableSerialPorts**](disableserialports-win32-tsgatewayconnectionauthorizationpolicy.md)                         | Sets the **SerialPortsDisabled** property.<br/>                                                                                                                           |
| [**EnableAllowOnlySDRServers**](win32-tsgatewayconnectionauthorizationpolicy-enableallowonlysdrservers.md)           | Used to toggle the **AllowOnlySDRServers** property<br/> **Windows Server 2008:** This method is not available before Windows Server 2008 R2.<br/>                  |
| [**MoveDown**](movedown-win32-tsgatewayconnectionauthorizationpolicy.md)                                             | Moves the current RD CAP one position down in the list.<br/>                                                                                                              |
| [**MoveUp**](moveup-win32-tsgatewayconnectionauthorizationpolicy.md)                                                 | Moves the current RD CAP one position up in the list.<br/>                                                                                                                |
| [**RemoveComputerGroupNames**](removecomputergroupnames-win32-tsgatewayconnectionauthorizationpolicy.md)             | Removes the specified computer group names from the **ComputerGroupNames** property.<br/>                                                                                 |
| [**RemoveUserGroupNames**](removeusergroupnames-win32-tsgatewayconnectionauthorizationpolicy.md)                     | Removes specified user group names from the **UserGroupNames** property.<br/>                                                                                             |
| [**SetComputerGroupNames**](setcomputergroupnames-win32-tsgatewayconnectionauthorizationpolicy.md)                   | Sets the **ComputerGroupNames** property.<br/>                                                                                                                            |
| [**SetCookieAuthenticationAllowed**](setcookieauthenticationallowed-win32-tsgatewayconnectionauthorizationpolicy.md) | Sets the **CookieAuthenticationAllowed** property.<br/> **Windows Server 2008:** This method is not available.<br/>                                                 |
| [**SetDeviceRedirectionType**](setdeviceredirectiontype-win32-tsgatewayconnectionauthorizationpolicy.md)             | Sets the **DeviceRedirectionType** property.<br/>                                                                                                                         |
| [**SetEnabled**](setenabled-win32-tsgatewayconnectionauthorizationpolicy.md)                                         | Enables or disables the current RD CAP.<br/>                                                                                                                              |
| [**SetIdleTimeout**](setidletimeout-win32-tsgatewayconnectionauthorizationpolicy.md)                                 | Sets the **IdleTimeout** property.<br/> **Windows Server 2008:** This method is not available before Windows Server 2008 R2.<br/>                                   |
| [**SetName**](setname-win32-tsgatewayconnectionauthorizationpolicy.md)                                               | Sets a new name for this RD CAP. This method ensures that names will be unique.<br/>                                                                                      |
| [**SetPasswordAllowed**](setpasswordallowed-win32-tsgatewayconnectionauthorizationpolicy.md)                         | Sets the **PasswordAllowed** property.<br/>                                                                                                                               |
| [**SetSecureIdAllowed**](setsecureidallowed-win32-tsgatewayconnectionauthorizationpolicy.md)                         | Sets the **SecureIdAllowed** property.<br/> **Windows Server 2008:** This method is reserved for future use.<br/>                                                   |
| [**SetSessionTimeout**](setsessiontimeout-win32-tsgatewayconnectionauthorizationpolicy.md)                           | Sets the **SessionTimeout** and **SessionTimeoutAction** properties.<br/> **Windows Server 2008:** This method is not available before Windows Server 2008 R2.<br/> |
| [**SetSmartcardAllowed**](setsmartcardallowed-win32-tsgatewayconnectionauthorizationpolicy.md)                       | Sets the **SmartcardAllowed** property.<br/>                                                                                                                              |
| [**SetUserGroupNames**](setusergroupnames-win32-tsgatewayconnectionauthorizationpolicy.md)                           | Sets the **UserGroupNames** property.<br/>                                                                                                                                |
| [**Update**](update-win32-tsgatewayconnectionauthorizationpolicy.md)                                                 | Updates the current RD CAP.<br/>                                                                                                                                          |



 

### Properties

The **Win32\_TSGatewayConnectionAuthorizationPolicy** class has these properties.

<dl> <dt>

**AllowOnlySDRServers**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether connections allowed only to secure device redirection (SDR) RDS servers. This property can be set using the [**EnableAllowOnlySDRServers**](win32-tsgatewayconnectionauthorizationpolicy-enableallowonlysdrservers.md) method.

**Windows Server 2008:** This property is not available before Windows Server 2008 R2.

</dd> <dt>

**ClipboardDisabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates if clipboard redirection will be disabled. This property has an effect only if the **DeviceRedirectionType** property has a value of "2".

</dd> <dt>

**ComputerGroupNames**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

List of semicolon-separated computer group names. This value can be empty. The names are of the format *Domain\\ComputerGroupName*. If a value is specified, then the client computer must belong to one of these computer groups for the user to access the RD Gateway server.

</dd> <dt>

**CookieAuthenticationAllowed**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates if cookie authentication can be used to connect to the RD Gateway server. This property can be set by using the [**SetCookieAuthenticationAllowed**](setcookieauthenticationallowed-win32-tsgatewayconnectionauthorizationpolicy.md) method.

**Windows Server 2008:** This property is not available.

</dd> <dt>

**DeviceRedirectionType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies which devices will be redirected.

<dt>

0
</dt> <dd>

All devices will be redirected.

</dd> <dt>

1
</dt> <dd>

No devices will be redirected.

</dd> <dt>

2
</dt> <dd>

Specified devices will not be redirected. The **DiskDrivesDisabled**, **PrintersDisabled**, **SerialPortsDisabled**, **ClipboardDisabled**, and **PlugAndPlayDevicesDisabled** properties control which devices will not be redirected.

</dd> </dl>

</dd> <dt>

**DiskDrivesDisabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates if disk drive redirection will be disabled. This property has an effect only if the **DeviceRedirectionType** property has a value of "2".

</dd> <dt>

**Enabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether this RD CAP will be used to evaluate a user for authorization.

</dd> <dt>

**HasNapAttributes**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates if the RD CAP uses Network Access Protection (NAP) attributes.

</dd> <dt>

**IdleTimeout**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The idle timeout value, in minutes. A value of 0 means there is no timeout. This property can be set by using the [**SetIdleTimeout**](setidletimeout-win32-tsgatewayconnectionauthorizationpolicy.md) method.

**Windows Server 2008:** This property is not available.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

Name of the RD CAP.

</dd> <dt>

**Order**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Evaluation order of the RD CAP. The first RD CAP evaluated has a value of "1". The **Order** property can be changed when the [**Create**](create-win32-tsgatewayconnectionauthorizationpolicy.md), [**Delete**](delete-win32-tsgatewayconnectionauthorizationpolicy.md), [**MoveUp**](moveup-win32-tsgatewayconnectionauthorizationpolicy.md), or [**MoveDown**](movedown-win32-tsgatewayconnectionauthorizationpolicy.md) methods are called.

</dd> <dt>

**PasswordAllowed**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates if a password can be used to connect to the RD Gateway server. This property can be changed by using the [**SetPasswordAllowed**](setpasswordallowed-win32-tsgatewayconnectionauthorizationpolicy.md) method.

</dd> <dt>

**PlugAndPlayDevicesDisabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates if redirection of Plug and Play devices will be disabled. This property has an effect only if the **DeviceRedirectionType** property has a value of "2".

</dd> <dt>

**PrintersDisabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates if printer redirection will be disabled. This property has an effect only if the **DeviceRedirectionType** property has a value of "2".

</dd> <dt>

**SecureIdAllowed**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates if a secure identifier can be used to connect to the RD Gateway server.

**Windows Server 2008:** This property is not used.

</dd> <dt>

**SerialPortsDisabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates if serial port redirection will be disabled. This property has an effect only if the **DeviceRedirectionType** property has a value of "2".

</dd> <dt>

**SessionTimeout**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The session timeout value, in minutes. A value of 0 means there is no timeout. This property can be set by using the [**SetSessionTimeout**](setsessiontimeout-win32-tsgatewayconnectionauthorizationpolicy.md) method.

**Windows Server 2008:** This property is not available.

</dd> <dt>

**SessionTimeoutAction**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Specifies the action to be taken in the case of a session timeout. This property can be set by using the [**SetSessionTimeout**](setsessiontimeout-win32-tsgatewayconnectionauthorizationpolicy.md) method.

This can be one of the following values.

**Windows Server 2008:** This property is not available.

<dt>

0
</dt> <dd>

Disconnect the session.

</dd> <dt>

1
</dt> <dd>

Attempt to re-authorize the session.

</dd> </dl>

</dd> <dt>

**SmartcardAllowed**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates if a smart card can be used to connect to the RD Gateway server. This property can be changed by using the [**SetSmartcardAllowed**](setsmartcardallowed-win32-tsgatewayconnectionauthorizationpolicy.md) method.

</dd> <dt>

**UserGroupNames**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

List of semicolon-separated user group names. The names are of the format *Domain\\UserGroupName*. If the user belongs to any of these user groups, the user will be permitted access to the RD Gateway server.

</dd> </dl>

## Remarks

You must be a member of the Administrators group to use this class.

Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Microsoft Windows Software Development Kit (SDK). They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](/windows/desktop/WmiSdk/managed-object-format--mof-).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                           |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                                 |
| MOF<br/>                      | <dl> <dt>TSGateway.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AagWmi.dll</dt> </dl>    |



## See also

<dl> <dt>

[**Win32\_TSGatewayConnection**](win32-tsgatewayconnection.md)
</dt> <dt>

[**Win32\_TSGatewayLoadBalancer**](win32-tsgatewayloadbalancer.md)
</dt> <dt>

[**Win32\_TSGatewayRADIUSServer**](win32-tsgatewayradiusserver.md)
</dt> <dt>

[**Win32\_TSGatewayResourceAuthorizationPolicy**](win32-tsgatewayresourceauthorizationpolicy.md)
</dt> <dt>

[**Win32\_TSGatewayResourceGroup**](win32-tsgatewayresourcegroup.md)
</dt> <dt>

[**Win32\_TSGatewayServerSettings**](win32-tsgatewayserversettings.md)
</dt> </dl>

 

