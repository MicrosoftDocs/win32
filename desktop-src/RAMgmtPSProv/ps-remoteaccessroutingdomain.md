---
title: PS\_RemoteAccessRoutingDomain class
description: Manages Remote Access settings for routing domain configurations.
audience: developer
ms.assetid: '90d62a31-4eff-459a-a960-f20e439a83ab'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["PS_RemoteAccessRoutingDomain class", "PS_RemoteAccessRoutingDomain class, described"]
topic_type:
- apiref
api_name:
- PS_RemoteAccessRoutingDomain
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
---

# PS\_RemoteAccessRoutingDomain class

Manages Remote Access settings for routing domain configurations.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class PS_RemoteAccessRoutingDomain
{
};
```

## Members

The **PS\_RemoteAccessRoutingDomain** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_RemoteAccessRoutingDomain** class has these methods.



| Method                                                                          | Description                                                                                                                          |
|:--------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------|
| [**Disable**](disable-ps-remoteaccessroutingdomain.md)                         | Disables S2S VPN for the specified routing domain.<br/>                                                                        |
| [**Enable**](enable-ps-remoteaccessroutingdomain.md)                           | Enables site-to-site (S2S) VPN for the specified routing domain.<br/>                                                          |
| [**Get**](get-ps-remoteaccessroutingdomain.md)                                 | Retrieves a VPN routing domain configuration for the specified routing domain, or for all routing domains of the gateway.<br/> |
| [**SetByCustomPolicy**](setbycustompolicy-ps-remoteaccessroutingdomain.md)     | Updates S2S VPN settings for a custom routing domain configuration.<br/>                                                       |
| [**SetByEncryptionType**](setbyencryptiontype-ps-remoteaccessroutingdomain.md) | Updates the S2S VPN settings for the specified encryption type.<br/>                                                           |



 

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                               |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





