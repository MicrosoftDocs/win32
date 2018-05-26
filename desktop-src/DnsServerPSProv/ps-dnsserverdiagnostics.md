---
title: PS\_DnsServerDiagnostics class
description: DNS Server Diagnostics definition.
audience: developer
ms.assetid: 0898931e-5531-4eaa-b4ce-2049c9062593
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DnsServerDiagnostics class
- PS_DnsServerDiagnostics class, described
topic_type:
- apiref
api_name:
- PS_DnsServerDiagnostics
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PS\_DnsServerDiagnostics class

DNS Server Diagnostics definition.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class PS_DnsServerDiagnostics
{
};
```

## Members

The **PS\_DnsServerDiagnostics** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DnsServerDiagnostics** class has these methods.



| Method                                                             | Description                                    |
|:-------------------------------------------------------------------|:-----------------------------------------------|
| [**Get**](get-ps-dnsserverdiagnostics.md)                         | Retrieve DNS Event logging details.<br/> |
| [**SetByAll**](setbyall-ps-dnsserverdiagnostics.md)               | Sets debug and logging parameters.<br/>  |
| [**SetByLogLevel**](setbyloglevel-ps-dnsserverdiagnostics.md)     | Sets debug and logging parameters.<br/>  |
| [**SetByParameters**](setbyparameters-ps-dnsserverdiagnostics.md) | Sets debug and logging parameters.<br/>  |



 

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[DnsServerPSProvider Provider](dns-server-classes.md)
</dt> </dl>

 

 





