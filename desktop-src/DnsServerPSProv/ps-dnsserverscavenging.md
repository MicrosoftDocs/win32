---
title: PS\_DnsServerScavenging class
description: DNS Server Scavaging definition.
audience: developer
ms.assetid: cf2c9450-86d7-463f-868a-e4c1eb6c63dd
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DnsServerScavenging class
- PS_DnsServerScavenging class, described
topic_type:
- apiref
api_name:
- PS_DnsServerScavenging
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PS\_DnsServerScavenging class

DNS Server Scavaging definition.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class PS_DnsServerScavenging
{
};
```

## Members

The **PS\_DnsServerScavenging** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DnsServerScavenging** class has these methods.



| Method                                        | Description                                                                                                           |
|:----------------------------------------------|:----------------------------------------------------------------------------------------------------------------------|
| [**Get**](get-ps-dnsserverscavenging.md)     | Retrieves DNS aging and scavenging settings<br/>                                                                |
| [**Set**](set-ps-dnsserverscavenging.md)     | Sets scavenging settings on the Server.<br/>                                                                    |
| [**Start**](start-ps-dnsserverscavenging.md) | Notifies a DNS server to attempt an immediate search for stale resource records in a specified DNS server.<br/> |



 

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

 

 





