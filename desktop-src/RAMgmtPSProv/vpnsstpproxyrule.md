---
title: VpnSstpProxyRule class
description: Configuration information for the BGP Router admin network.
audience: developer
ms.assetid: 5f996a21-5570-472a-8985-21aca44390aa
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- VpnSstpProxyRule class
- VpnSstpProxyRule class, described
topic_type:
- apiref
api_name:
- VpnSstpProxyRule
- VpnSstpProxyRule.TenantID
- VpnSstpProxyRule.GatewayAddress
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# VpnSstpProxyRule class

Configuration information for the BGP Router admin network

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class VpnSstpProxyRule
{
  string TenantID;
  string GatewayAddress[];
};
```

## Members

The **VpnSstpProxyRule** class has these types of members:

-   [Properties](#properties)

### Properties

The **VpnSstpProxyRule** class has these properties.

<dl> <dt>

**GatewayAddress**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Address of the SSTP gateway

</dd> <dt>

**TenantID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

ID for the tenant

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>Ramgmtpsprovider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





