---
title: PS\_VpnSstpProxyRule class
description: Holds the SSTP Proxy configuration functions.
audience: developer
ms.assetid: '5f996a21-5570-472a-8985-21aca44390aa'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["PS_VpnSstpProxyRule class", "PS_VpnSstpProxyRule class, described"]
topic_type:
- apiref
api_name:
- PS_VpnSstpProxyRule
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
---

# PS\_VpnSstpProxyRule class

Holds the SSTP Proxy configuration functions.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class PS_VpnSstpProxyRule
{
};
```

## Members

The **PS\_VpnSstpProxyRule** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_VpnSstpProxyRule** class has these methods.



| Method                                       | Description                                                                  |
|:---------------------------------------------|:-----------------------------------------------------------------------------|
| [**Add**](add-ps-vpnsstpproxyrule.md)       | Adds a tenant ID to gateway mapping.<br/>                              |
| [**Get**](get-ps-vpnsstpproxyrule.md)       | Retrieves the tenant ID to gateway mapping.<br/>                       |
| [**New**](new-ps-vpnsstpproxyrule.md)       | Creates a tenant ID to gateway mapping object.<br/>                    |
| [**Remove**](remove-ps-vpnsstpproxyrule.md) | Removes one or more tenant ID to gateway mappings for SSTP proxy.<br/> |
| [**Set**](set-ps-vpnsstpproxyrule.md)       | Modifies a tenant ID to gateway mapping.<br/>                          |



 

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>Ramgmtpsprovider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





