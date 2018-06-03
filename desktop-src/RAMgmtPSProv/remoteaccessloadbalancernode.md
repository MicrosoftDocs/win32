---
title: RemoteAccessLoadBalancerNode class
description: Remote Access Load Balancer Node object.
audience: developer
ms.assetid: 26bb3f41-9ccd-4f94-8413-a39ce37f0a19
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RemoteAccessLoadBalancerNode class
- RemoteAccessLoadBalancerNode class, described
topic_type:
- apiref
api_name:
- RemoteAccessLoadBalancerNode
- RemoteAccessLoadBalancerNode.HostName
- RemoteAccessLoadBalancerNode.StatusCode
- RemoteAccessLoadBalancerNode.VpnIPAddressAssignmentSetting
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# RemoteAccessLoadBalancerNode class

Remote Access Load Balancer Node object

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class RemoteAccessLoadBalancerNode
{
  string                 HostName;
  string                 StatusCode;
  VpnIPAddressAssignment VpnIPAddressAssignmentSetting;
};
```

## Members

The **RemoteAccessLoadBalancerNode** class has these types of members:

-   [Properties](#properties)

### Properties

The **RemoteAccessLoadBalancerNode** class has these properties.

<dl> <dt>

**HostName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the Node

</dd> <dt>

**StatusCode**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The status the Node

The possible values are.

<dt>

<span id="Suspended"></span><span id="suspended"></span><span id="SUSPENDED"></span>

**Suspended** ("Suspended")


</dt> <dd></dd> <dt>

<span id="Stopped"></span><span id="stopped"></span><span id="STOPPED"></span>

**Stopped** ("Stopped")


</dt> <dd></dd> <dt>

<span id="Draining"></span><span id="draining"></span><span id="DRAINING"></span>

**Draining** ("Draining")


</dt> <dd></dd> <dt>

<span id="Converging"></span><span id="converging"></span><span id="CONVERGING"></span>

**Converging** ("Converging")


</dt> <dd></dd> <dt>

<span id="Converged"></span><span id="converged"></span><span id="CONVERGED"></span>

**Converged** ("Converged")


</dt> <dd></dd> <dt>

<span id="Default"></span><span id="default"></span><span id="DEFAULT"></span>

**Default** ("Default")


</dt> <dd></dd> </dl>

</dd> <dt>

**VpnIPAddressAssignmentSetting**
</dt> <dd> <dl> <dt>

Data type: **VpnIPAddressAssignment**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**VpnIPAddressAssignment**](vpnipaddressassignment.md)")
</dt> </dl>

A [**VpnIPAddressAssignment**](vpnipaddressassignment.md) embedded instance

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





