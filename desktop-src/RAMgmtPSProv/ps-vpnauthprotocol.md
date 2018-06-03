---
title: PS\_VpnAuthProtocol class
description: Refers to various VPN authentication protocols.
audience: developer
ms.assetid: d086ef02-d7d6-4da3-ba77-77ddff8d75af
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_VpnAuthProtocol class
- PS_VpnAuthProtocol class, described
topic_type:
- apiref
api_name:
- PS_VpnAuthProtocol
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PS\_VpnAuthProtocol class

Refers to various VPN authentication protocols.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class PS_VpnAuthProtocol
{
};
```

## Members

The **PS\_VpnAuthProtocol** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_VpnAuthProtocol** class has these methods.



| Method                                | Description                                                                                     |
|:--------------------------------------|:------------------------------------------------------------------------------------------------|
| [**Get**](get-ps-vpnauthprotocol.md) | This cmdlet is used to get retrieve VPN authentication parameters.<br/>                   |
| [**Set**](set-ps-vpnauthprotocol.md) | Updates the authentication method of an incoming S2S VPN interface of a RRAS server.<br/> |



 

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





