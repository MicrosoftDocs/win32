---
title: PS\_BgpRoutingPolicy class
description: BGP routing policy management.
audience: developer
ms.assetid: 5ea11549-9f07-4044-959e-2ecb20b3b5bb
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_BgpRoutingPolicy class
- PS_BgpRoutingPolicy class, described
topic_type:
- apiref
api_name:
- PS_BgpRoutingPolicy
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PS\_BgpRoutingPolicy class

BGP routing policy management

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class PS_BgpRoutingPolicy
{
};
```

## Members

The **PS\_BgpRoutingPolicy** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_BgpRoutingPolicy** class has these methods.



| Method                                       | Description                                                                                                 |
|:---------------------------------------------|:------------------------------------------------------------------------------------------------------------|
| [**Add**](add-ps-bgproutingpolicy.md)       | Adds a new BGP routing policy to the policy store.<br/>                                               |
| [**Get**](get-ps-bgproutingpolicy.md)       | Retrieves configuration information from the policy store, for one or more BGP routing policies.<br/> |
| [**Remove**](remove-ps-bgproutingpolicy.md) | Removes one or more BGP routing policies from the policy store.<br/>                                  |
| [**Set**](set-ps-bgproutingpolicy.md)       | Updates a BGP routing policy.<br/>                                                                    |



 

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                               |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





