---
title: PS\_DAClientDnsConfiguration class
description: Represents all the name resolution configuration for a DirectAccess deployment.
audience: developer
ms.assetid: 601a82cd-1997-422c-ae9e-11f04c075133
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DAClientDnsConfiguration class
- PS_DAClientDnsConfiguration class, described
topic_type:
- apiref
api_name:
- PS_DAClientDnsConfiguration
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PS\_DAClientDnsConfiguration class

Represents all the name resolution configuration for a DirectAccess deployment.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class PS_DAClientDnsConfiguration
{
};
```

## Members

The **PS\_DAClientDnsConfiguration** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DAClientDnsConfiguration** class has these methods.



| Method                                               | Description                                                                                                                                                        |
|:-----------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Add**](add-ps-daclientdnsconfiguration.md)       | This cmdlet adds the specified DNS suffix, DNS server addresses, proxy server set to the NRPT table<br/>                                                     |
| [**Get**](get-ps-daclientdnsconfiguration.md)       | This cmdlet displays all the NRPT table entries and the local name resolution property<br/>                                                                  |
| [**Remove**](remove-ps-daclientdnsconfiguration.md) | This cmdlet removes the NRPT entry corresponding to the specified DNS suffix from the NRPT table<br/>                                                        |
| [**Set**](set-ps-daclientdnsconfiguration.md)       | This cmdlet does the following1. Configures the DNS server and proxy server addresses of an NRPT entry 2. Configures the local name resolution property<br/> |



 

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





