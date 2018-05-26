---
title: PS\_DnsServerForwarder class
description: DNS Server Forwarder definition.
audience: developer
ms.assetid: d584e8f3-8eb2-4376-a45f-6b8e747acccb
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DnsServerForwarder class
- PS_DnsServerForwarder class, described
topic_type:
- apiref
api_name:
- PS_DnsServerForwarder
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PS\_DnsServerForwarder class

DNS Server Forwarder definition.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class PS_DnsServerForwarder
{
};
```

## Members

The **PS\_DnsServerForwarder** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DnsServerForwarder** class has these methods.



| Method                                         | Description                                                                                                                 |
|:-----------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------|
| [**Add**](add-ps-dnsserverforwarder.md)       | Add specified DNS server forwarders to the end of the list.<br/>                                                      |
| [**Get**](get-ps-dnsserverforwarder.md)       | Retrieves DNS Forwarder Settings.<br/>                                                                                |
| [**Remove**](remove-ps-dnsserverforwarder.md) | Remove the specified Forwarders.<br/>                                                                                 |
| [**Set**](set-ps-dnsserverforwarder.md)       | Selects or resets IP address(es) to which the DNS server forwards DNS queries when it cannot solve them locally.<br/> |



 

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

 

 





