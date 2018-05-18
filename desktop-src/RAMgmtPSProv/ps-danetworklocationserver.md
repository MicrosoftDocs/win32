---
title: PS\_DANetworkLocationServer class
description: Represents the Network Location Server configuration of the DirectAccess.
audience: developer
ms.assetid: 'd88c1075-804b-49f6-9bc0-29197c8f10a4'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["PS_DANetworkLocationServer class", "PS_DANetworkLocationServer class, described"]
topic_type:
- apiref
api_name:
- PS_DANetworkLocationServer
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
---

# PS\_DANetworkLocationServer class

Represents the Network Location Server configuration of the DirectAccess.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class PS_DANetworkLocationServer
{
};
```

## Members

The **PS\_DANetworkLocationServer** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DANetworkLocationServer** class has these methods.



| Method                                                                        | Description                                                                                                                                                    |
|:------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Get**](get-ps-danetworklocationserver.md)                                 | This cmdlet displays the detailed Network Location Server configuration<br/>                                                                             |
| [**SetByExternalServer**](setbyexternalserver-ps-danetworklocationserver.md) | This cmdlet is used to configure the Network Location Server. It can be present on the DirectAccess server or on some other highly available server<br/> |
| [**SetByOnDAServer**](setbyondaserver-ps-danetworklocationserver.md)         | This cmdlet is used to configure the Network Location Server. It can be present on the DirectAccess server or on some other highly available server<br/> |



 

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





