---
title: PS\_DnsServerConditionalForwarder class
description: DNS Server Conditional Forwarder definition.
audience: developer
ms.assetid: fa1b42eb-dab7-446f-9d6d-caf89a8e778d
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DnsServerConditionalForwarder class
- PS_DnsServerConditionalForwarder class, described
topic_type:
- apiref
api_name:
- PS_DnsServerConditionalForwarder
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PS\_DnsServerConditionalForwarder class

DNS Server Conditional Forwarder definition.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class PS_DnsServerConditionalForwarder
{
};
```

## Members

The **PS\_DnsServerConditionalForwarder** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DnsServerConditionalForwarder** class has these methods.



| Method                                                                                            | Description                                                |
|:--------------------------------------------------------------------------------------------------|:-----------------------------------------------------------|
| [**AddByADForwardLookupZone**](addbyadforwardlookupzone-ps-dnsserverconditionalforwarder.md)     | Adds a DNS conditional forwarder zone.<br/>          |
| [**AddByFileForwardLookupZone**](addbyfileforwardlookupzone-ps-dnsserverconditionalforwarder.md) | Adds a DNS conditional forwarder zone.<br/>          |
| [**SetByADZone**](setbyadzone-ps-dnsserverconditionalforwarder.md)                               | Sets DNS server Conditional Forwarder settings.<br/> |
| [**SetByParameters**](setbyparameters-ps-dnsserverconditionalforwarder.md)                       | Sets DNS server Conditional Forwarder settings.<br/> |



 

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

 

 





