---
title: PS\_BgpRoutingPolicyForPeer class
description: Assigns BGP routing policies to BGP peers.
audience: developer
ms.assetid: '69bdf47d-631b-471d-85c9-5ea72bb3673a'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["PS_BgpRoutingPolicyForPeer class", "PS_BgpRoutingPolicyForPeer class, described"]
topic_type:
- apiref
api_name:
- PS_BgpRoutingPolicyForPeer
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
---

# PS\_BgpRoutingPolicyForPeer class

Assigns BGP routing policies to BGP peers.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class PS_BgpRoutingPolicyForPeer
{
};
```

## Members

The **PS\_BgpRoutingPolicyForPeer** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_BgpRoutingPolicyForPeer** class has these methods.



| Method                                              | Description                                                                                  |
|:----------------------------------------------------|:---------------------------------------------------------------------------------------------|
| [**Add**](add-ps-bgproutingpolicyforpeer.md)       | Assigns a set of BGP routing policies to a set of BGP peers.<br/>                      |
| [**Remove**](remove-ps-bgproutingpolicyforpeer.md) | Removes a set of BGP routing policies from a set of BGP peers.<br/>                    |
| [**Set**](set-ps-bgproutingpolicyforpeer.md)       | Updates an existing set of BGP routing policy assignments for a set of BGP peers.<br/> |



 

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                               |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





