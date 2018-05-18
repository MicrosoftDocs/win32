---
title: RemoteAccessLoadBalancer class
description: Remote Access Load Balancing configuration.
audience: developer
ms.assetid: 'c1c49050-38ae-49a7-80f2-d99d4596afd3'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["RemoteAccessLoadBalancer class", "RemoteAccessLoadBalancer class, described"]
topic_type:
- apiref
api_name:
- RemoteAccessLoadBalancer
- RemoteAccessLoadBalancer.NlbNodeStatus
- RemoteAccessLoadBalancer.ThirdPartyLoadBalancer
- RemoteAccessLoadBalancer.InternetVirtualIPAddress
- RemoteAccessLoadBalancer.InternalVirtualIPAddress
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
---

# RemoteAccessLoadBalancer class

Remote Access Load Balancing configuration

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class RemoteAccessLoadBalancer
{
  RemoteAccessLoadBalancerNode NlbNodeStatus[];
  string                       ThirdPartyLoadBalancer;
  string                       InternetVirtualIPAddress[];
  string                       InternalVirtualIPAddress[];
};
```

## Members

The **RemoteAccessLoadBalancer** class has these types of members:

-   [Properties](#properties)

### Properties

The **RemoteAccessLoadBalancer** class has these properties.

<dl> <dt>

**InternalVirtualIPAddress**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

An array of the Virtual IP addresses of the intranet interface

</dd> <dt>

**InternetVirtualIPAddress**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

An array of the Virtual IP addresses of the internet interface

</dd> <dt>

**NlbNodeStatus**
</dt> <dd> <dl> <dt>

Data type: **RemoteAccessLoadBalancerNode** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**EmbeddedInstance**](https://msdn.microsoft.com/library/aa393650) ("[**RemoteAccessLoadBalancerNode**](remoteaccessloadbalancernode.md)")
</dt> </dl>

An array of [**RemoteAccessLoadBalancerNode**](remoteaccessloadbalancernode.md) embedded instances

</dd> <dt>

**ThirdPartyLoadBalancer**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

External load balancer state

The possible values are.

<dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>

**Enabled** ("Enabled")


</dt> <dd></dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** ("Disabled")


</dt> <dd></dd> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





