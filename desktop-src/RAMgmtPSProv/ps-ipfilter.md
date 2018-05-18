---
title: PS\_IPFilter class
description: Manages IP filter actions for a Border Gateway Protocol (BGP) router interface.
audience: developer
ms.assetid: '254f2a89-b576-498f-9869-ae6d65879112'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["PS_IPFilter class", "PS_IPFilter class, described"]
topic_type:
- apiref
api_name:
- PS_IPFilter
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
---

# PS\_IPFilter class

Manages IP filter actions for a Border Gateway Protocol (BGP) router interface.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class PS_IPFilter
{
};
```

## Members

The **PS\_IPFilter** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_IPFilter** class has these methods.



| Method                               | Description                                                                 |
|:-------------------------------------|:----------------------------------------------------------------------------|
| [**Add**](add-ps-ipfilter.md)       | Adds an IP filter to a BGP router interface.<br/>                     |
| [**Get**](get-ps-ipfilter.md)       | Retrieves the IP filters for the specified BGP router interface.<br/> |
| [**Remove**](remove-ps-ipfilter.md) | Removes an IP filter from a BGP routing interface.<br/>               |
| [**Set**](set-ps-ipfilter.md)       | Updates the filtering action of an IP filter for a BGP router.<br/>   |



 

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                               |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





