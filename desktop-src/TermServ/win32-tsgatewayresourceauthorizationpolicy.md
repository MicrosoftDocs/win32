---
title: Win32_TSGatewayResourceAuthorizationPolicy class
description: Describes a Remote Desktop resource authorization policy (RD \ 160;RAP). An RD \ 160;RAP is used to decide whether a user is authorized to connect to a specified resource through Remote Desktop Gateway (RD Gateway).
ms.assetid: 284a868d-7856-4a25-ba7b-b4beba8ffffc
ms.tgt_platform: multiple
keywords:
- Win32_TSGatewayResourceAuthorizationPolicy class Remote Desktop Services
- Win32_TSGatewayResourceAuthorizationPolicy class Remote Desktop Services , described
topic_type:
- apiref
api_name:
- Win32_TSGatewayResourceAuthorizationPolicy
- Win32_TSGatewayResourceAuthorizationPolicy.Name
- Win32_TSGatewayResourceAuthorizationPolicy.Description
- Win32_TSGatewayResourceAuthorizationPolicy.Enabled
- Win32_TSGatewayResourceAuthorizationPolicy.ResourceGroupType
- Win32_TSGatewayResourceAuthorizationPolicy.ResourceGroupName
- Win32_TSGatewayResourceAuthorizationPolicy.UserGroupNames
- Win32_TSGatewayResourceAuthorizationPolicy.ProtocolNames
- Win32_TSGatewayResourceAuthorizationPolicy.PortNumbers
api_location:
- AagWmi.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Win32\_TSGatewayResourceAuthorizationPolicy class

Describes a Remote Desktop resource authorization policy (RD RAP). An RD RAP is used to decide whether a user is authorized to connect to a specified resource through Remote Desktop Gateway (RD Gateway).

## Syntax

``` syntax
[dynamic, provider("AAGProvider"), AMENDMENT]
class Win32_TSGatewayResourceAuthorizationPolicy
{
  string  Name;
  string  Description;
  boolean Enabled;
  string  ResourceGroupType;
  string  ResourceGroupName;
  string  UserGroupNames;
  string  ProtocolNames;
  string  PortNumbers;
};
```

## Members

The **Win32\_TSGatewayResourceAuthorizationPolicy** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Win32\_TSGatewayResourceAuthorizationPolicy** class has these methods.



| Method                                                                                          | Description                                                                                                         |
|:------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------|
| [**AddUserGroupNames**](addusergroupnames-win32-tsgatewayresourceauthorizationpolicy.md)       | Adds the specified user group names to the existing user groups in the **UserGroupNames** property.<br/>      |
| [**Create**](create-win32-tsgatewayresourceauthorizationpolicy.md)                             | Creates an RD RAP.<br/>                                                                                       |
| [**Delete**](delete-win32-tsgatewayresourceauthorizationpolicy.md)                             | Deletes the current RD RAP.<br/>                                                                              |
| [**RemoveUserGroupNames**](removeusergroupnames-win32-tsgatewayresourceauthorizationpolicy.md) | Removes the specified user group names from the existing user groups in the **UserGroupNames** property.<br/> |
| [**SetDescription**](setdescription-win32-tsgatewayresourceauthorizationpolicy.md)             | Sets the **Description** property for the RD RAP.<br/>                                                        |
| [**SetEnabled**](setenabled-win32-tsgatewayresourceauthorizationpolicy.md)                     | Enables or disables the RD RAP by setting the **Enabled** property.<br/>                                      |
| [**SetName**](setname-win32-tsgatewayresourceauthorizationpolicy.md)                           | Sets the **Name** property for the RD RAP.<br/>                                                               |
| [**SetPortNumbers**](setportnumbers-win32-tsgatewayresourceauthorizationpolicy.md)             | Sets the **PortNumbers** property for the RD RAP.<br/>                                                        |
| [**SetResourceGroup**](setresourcegroup-win32-tsgatewayresourceauthorizationpolicy.md)         | Sets the **ResourceGroupType** and **ResourceGroupName** properties.<br/>                                     |
| [**SetUserGroupNames**](setusergroupnames-win32-tsgatewayresourceauthorizationpolicy.md)       | Sets the **UserGroupNames** property for the RD RAP.<br/>                                                     |
| [**Update**](update-win32-tsgatewayresourceauthorizationpolicy.md)                             | Updates the current RD RAP.<br/>                                                                              |



 

### Properties

The **Win32\_TSGatewayResourceAuthorizationPolicy** class has these properties.

<dl> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Description of the RD RAP. This property is changed with the [**SetDescription**](setdescription-win32-tsgatewayresourceauthorizationpolicy.md) method.

</dd> <dt>

**Enabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether this RD RAP is enabled. This property is changed with the [**SetEnabled**](setenabled-win32-tsgatewayresourceauthorizationpolicy.md) method.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

Name of the RD RAP. This property is changed with the [**SetName**](setname-win32-tsgatewayresourceauthorizationpolicy.md) method.

</dd> <dt>

**PortNumbers**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

List of semicolon-separated port numbers that are allowed for this policy. To allow any port number, set "\*".

</dd> <dt>

**ProtocolNames**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

List of semicolon-separated protocol names that are enabled for this policy. Names must match the return of the [**GetProtocolName**](getprotocolname-win32-tsgatewayserversettings.md) method of the [**Win32\_TSGatewayServerSettings**](win32-tsgatewayserversettings.md) class.

</dd> <dt>

**ResourceGroupName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Resource group name. This property is changed with the [**SetResourceGroup**](setresourcegroup-win32-tsgatewayresourceauthorizationpolicy.md) method.

</dd> <dt>

**ResourceGroupType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Identifies the type of the resource group. This property is changed with the [**SetResourceGroup**](setresourcegroup-win32-tsgatewayresourceauthorizationpolicy.md) method.

<dt>

"RG"
</dt> <dd>

Resource group.

</dd> <dt>

"CG"
</dt> <dd>

Computer group, as stored in Active Directory Domain Services.

</dd> <dt>

"ALL"
</dt> <dd>

All resources.

</dd> </dl>

</dd> <dt>

**UserGroupNames**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Semicolon-separated list of user group names. If the user belongs to any of these user groups, access will be permitted. This property is changed with the [**SetUserGroupNames**](setusergroupnames-win32-tsgatewayresourceauthorizationpolicy.md), [**AddUserGroupNames**](addusergroupnames-win32-tsgatewayresourceauthorizationpolicy.md), and [**RemoveUserGroupNames**](removeusergroupnames-win32-tsgatewayresourceauthorizationpolicy.md) methods.

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

[**Win32\_TSGatewayConnectionAuthorizationPolicy**](win32-tsgatewayconnectionauthorizationpolicy.md)
</dt> <dt>

[**Win32\_TSGatewayLoadBalancer**](win32-tsgatewayloadbalancer.md)
</dt> <dt>

[**Win32\_TSGatewayRADIUSServer**](win32-tsgatewayradiusserver.md)
</dt> <dt>

[**Win32\_TSGatewayResourceGroup**](win32-tsgatewayresourcegroup.md)
</dt> <dt>

[**Win32\_TSGatewayServerSettings**](win32-tsgatewayserversettings.md)
</dt> </dl>

 

