---
title: Win32_TSGatewayLoadBalancer class
description: Describes a set of Remote Desktop Gateway (RD Gateway) load-balancing servers. These are used to load balance RD Gateway connections across multiple servers.
ms.assetid: aa7e7b77-7233-4c6a-8f41-cc332fa509d5
ms.tgt_platform: multiple
keywords:
- Win32_TSGatewayLoadBalancer class Remote Desktop Services
- Win32_TSGatewayLoadBalancer class Remote Desktop Services , described
topic_type:
- apiref
api_name:
- Win32_TSGatewayLoadBalancer
- Win32_TSGatewayLoadBalancer.Servers
api_location:
- AagWmi.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Win32\_TSGatewayLoadBalancer class

Describes a set of Remote Desktop Gateway (RD Gateway) load-balancing servers. These are used to load balance RD Gateway connections across multiple servers.

## Syntax

``` syntax
[dynamic, provider("AAGProvider"), AMENDMENT]
class Win32_TSGatewayLoadBalancer
{
  string Servers;
};
```

## Members

The **Win32\_TSGatewayLoadBalancer** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Win32\_TSGatewayLoadBalancer** class has these methods.



| Method                                                                             | Description                                                                                                      |
|:-----------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------|
| [**AddServers**](addservers-win32-tsgatewayloadbalancer.md)                       | Adds servers to the **Servers** property.<br/>                                                             |
| [**DeleteAllServers**](deleteallservers-win32-tsgatewayloadbalancer.md)           | Deletes all RD Gateway load-balancing servers participating in the load-balancing farm.<br/>               |
| [**DeleteServers**](deleteservers-win32-tsgatewayloadbalancer.md)                 | Deletes servers from the **Servers** property.<br/>                                                        |
| [**IsLoadBalancingServer**](win32-tsgatewayloadbalancer-isloadbalancingserver.md) | Determines whether the server can perform load balancing.<br/>                                             |
| [**SetServers**](setservers-win32-tsgatewayloadbalancer.md)                       | Sets the **Servers** property with the semicolon-separated list of RD Gateway load-balancing servers.<br/> |



 

### Properties

The **Win32\_TSGatewayLoadBalancer** class has these properties.

<dl> <dt>

**Servers**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

Semicolon-separated list of RD Gateway load-balancing servers. This property can be changed with the [**SetServers**](setservers-win32-tsgatewayloadbalancer.md), [**AddServers**](addservers-win32-tsgatewayloadbalancer.md), [**DeleteServers**](deleteservers-win32-tsgatewayloadbalancer.md), and [**DeleteAllServers**](deleteallservers-win32-tsgatewayloadbalancer.md) methods.

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

[**Win32\_TSGatewayRADIUSServer**](win32-tsgatewayradiusserver.md)
</dt> <dt>

[**Win32\_TSGatewayResourceAuthorizationPolicy**](win32-tsgatewayresourceauthorizationpolicy.md)
</dt> <dt>

[**Win32\_TSGatewayResourceGroup**](win32-tsgatewayresourcegroup.md)
</dt> <dt>

[**Win32\_TSGatewayServerSettings**](win32-tsgatewayserversettings.md)
</dt> </dl>

 

