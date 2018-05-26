---
title: PS\_DnsServerSetting class
description: DNS Server Setting definition.
audience: developer
ms.assetid: 8cc65c8f-14db-4f49-b855-2573336aa13c
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DnsServerSetting class
- PS_DnsServerSetting class, described
topic_type:
- apiref
api_name:
- PS_DnsServerSetting
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PS\_DnsServerSetting class

DNS Server Setting definition.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class PS_DnsServerSetting
{
};
```

## Members

The **PS\_DnsServerSetting** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DnsServerSetting** class has these methods.



| Method                                               | Description                                                                                                                                                                                                                                                                                      |
|:-----------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetByAll**](getbyall-ps-dnsserversetting.md)     | Retrieve DNS server settings.<br/>                                                                                                                                                                                                                                                         |
| [**GetByBrief**](getbybrief-ps-dnsserversetting.md) | Retrieve DNS server settings.<br/>                                                                                                                                                                                                                                                         |
| [**Set**](set-ps-dnsserversetting.md)               | Sets Different DNS server settings: One of the parameters other than RemoteName, Credentials, comments is mandatory. This should also take remote ip address from pipeline from other cmdlets. Hence we may need an additional IP address parameter. This applies to all the cmdlets.<br/> |



 

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

 

 





