---
title: Win32_TSGatewayResourceGroup class
description: Describes a resource group, which maps a set of resources (computer names) to a single entity.
ms.assetid: 5715a2ea-9bbc-4704-835e-ba6d93a72368
ms.tgt_platform: multiple
keywords:
- Win32_TSGatewayResourceGroup class Remote Desktop Services
- Win32_TSGatewayResourceGroup class Remote Desktop Services , described
topic_type:
- apiref
api_name:
- Win32_TSGatewayResourceGroup
- Win32_TSGatewayResourceGroup.Name
- Win32_TSGatewayResourceGroup.Description
- Win32_TSGatewayResourceGroup.AssociatedRAPs
- Win32_TSGatewayResourceGroup.Resources
api_location:
- AagWmi.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Win32\_TSGatewayResourceGroup class

Describes a resource group, which maps a set of resources (computer names) to a single entity.

## Syntax

``` syntax
[dynamic, provider("AAGProvider"), AMENDMENT]
class Win32_TSGatewayResourceGroup
{
  string Name;
  string Description;
  string AssociatedRAPs;
  string Resources;
};
```

## Members

The **Win32\_TSGatewayResourceGroup** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Win32\_TSGatewayResourceGroup** class has these methods.



| Method                                                                  | Description                                                                           |
|:------------------------------------------------------------------------|:--------------------------------------------------------------------------------------|
| [**AddResources**](addresources-win32-tsgatewayresourcegroup.md)       | Adds resources to the **Resources** property for this resource group.<br/>      |
| [**Create**](create-win32-tsgatewayresourcegroup.md)                   | Creates a resource group.<br/>                                                  |
| [**Delete**](delete-win32-tsgatewayresourcegroup.md)                   | Deletes this resource group.<br/>                                               |
| [**RemoveResources**](removeresources-win32-tsgatewayresourcegroup.md) | Deletes resources from the **Resources** property for this resource group.<br/> |
| [**SetDescription**](setdescription-win32-tsgatewayresourcegroup.md)   | Sets the **Description** property for this resource group.<br/>                 |
| [**SetName**](setname-win32-tsgatewayresourcegroup.md)                 | Sets the **Name** property for this resource group.<br/>                        |
| [**SetResources**](setresources-win32-tsgatewayresourcegroup.md)       | Sets the **Resources** property for this resource group.<br/>                   |
| [**Update**](update-win32-tsgatewayresourcegroup.md)                   | Updates this resource group.<br/>                                               |



 

### Properties

The **Win32\_TSGatewayResourceGroup** class has these properties.

<dl> <dt>

**AssociatedRAPs**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Semicolon-separated list of Remote Desktop Services resource authorization policies (RD RAPs) that are associated with this resource group.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Description of the resource group. This property can be changed with the [**SetDescription**](setdescription-win32-tsgatewayresourcegroup.md) method.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

Name of the resource group. This property can be changed with the [**SetName**](setname-win32-tsgatewayresourcegroup.md) method.

</dd> <dt>

**Resources**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Semicolon-separated list of resources in this resource group. An "\*" means all resources. This property can be changed with the [**SetResources**](setresources-win32-tsgatewayresourcegroup.md), [**AddResources**](addresources-win32-tsgatewayresourcegroup.md), [**RemoveResources**](removeresources-win32-tsgatewayresourcegroup.md), and [**Update**](update-win32-tsgatewayresourcegroup.md) methods.

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

[**Win32\_TSGatewayResourceAuthorizationPolicy**](win32-tsgatewayresourceauthorizationpolicy.md)
</dt> <dt>

[**Win32\_TSGatewayServerSettings**](win32-tsgatewayserversettings.md)
</dt> </dl>

 

