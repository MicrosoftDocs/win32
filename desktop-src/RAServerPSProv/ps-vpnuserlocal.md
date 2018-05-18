---
title: PS\_VpnUserLocal class
description: Refers to the connection stats summary based on accounting data.
audience: developer
ms.assetid: '0bd95bf0-32d2-478f-bcc6-f270dd518505'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["PS_VpnUserLocal class", "PS_VpnUserLocal class, described"]
topic_type:
- apiref
api_name:
- PS_VpnUserLocal
api_location:
- RAServerPSProvider.dll
api_type:
- DllExport
---

# PS\_VpnUserLocal class

Refers to the connection stats summary based on accounting data.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAServerPSProvider"), AMENDMENT]
class PS_VpnUserLocal
{
};
```

## Members

The **PS\_VpnUserLocal** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_VpnUserLocal** class has these methods.



| Method                                                               | Description                               |
|:---------------------------------------------------------------------|:------------------------------------------|
| [**DisconnectByHostIP**](disconnectbyhostip-ps-vpnuserlocal.md)     | Disconnects the specified user<br/> |
| [**DisconnectByUserName**](disconnectbyusername-ps-vpnuserlocal.md) | Disconnects the specified user<br/> |



 

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                    |
| Namespace<br/>                | Root\\microsoft\\windows\\remoteaccess\\server<br/>                                         |
| MOF<br/>                      | <dl> <dt>RAServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAServerPSProvider.dll</dt> </dl> |



 

 





