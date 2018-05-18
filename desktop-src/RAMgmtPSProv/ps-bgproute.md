---
title: PS\_BgpRoute class
description: Retrieves Border Gateway Protocol (BGP) routes from the local BGP routing table.
audience: developer
ms.assetid: '1c94bf45-3b7f-48c8-ab18-8ebbcc0c9b8b'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["PS_BgpRoute class", "PS_BgpRoute class, described"]
topic_type:
- apiref
api_name:
- PS_BgpRoute
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
---

# PS\_BgpRoute class

Retrieves Border Gateway Protocol (BGP) routes from the local BGP routing table.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class PS_BgpRoute
{
};
```

## Members

The **PS\_BgpRoute** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_BgpRoute** class has these methods.



| Method                         | Description                                                                                                 |
|:-------------------------------|:------------------------------------------------------------------------------------------------------------|
| [**Get**](get-ps-bgproute.md) | Retrieves the BGP route information for one or more network prefixes from the BGP routing table.<br/> |



 

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                               |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





