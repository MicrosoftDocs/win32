---
title: PS\_VpnUser class
description: Indicates the user policy operations performed on VPN user.
audience: developer
ms.assetid: 376927b2-b234-4ebc-8760-d7faf5e8eb6c
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_VpnUser class
- PS_VpnUser class, described
topic_type:
- apiref
api_name:
- PS_VpnUser
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PS\_VpnUser class

Indicates the user policy operations performed on VPN user

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class PS_VpnUser
{
};
```

## Members

The **PS\_VpnUser** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_VpnUser** class has these methods.



| Method                                                          | Description                                                                                                                     |
|:----------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------|
| [**DisconnectByHostIP**](disconnectbyhostip-ps-vpnuser.md)     | This cmdlet disconnects a VPN connection originated by a specific user or originating from a specific client machine<br/> |
| [**DisconnectByUserName**](disconnectbyusername-ps-vpnuser.md) | This cmdlet disconnects a VPN connection originated by a specific user or originating from a specific client machine<br/> |



 

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





