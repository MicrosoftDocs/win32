---
title: PS\_DnsServerResourceRecordMX class
description: DNS Server Resource Record MX definition.
audience: developer
ms.assetid: b02c4e5c-b048-4970-ab90-d64a9ed0e032
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DnsServerResourceRecordMX class
- PS_DnsServerResourceRecordMX class, described
topic_type:
- apiref
api_name:
- PS_DnsServerResourceRecordMX
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PS\_DnsServerResourceRecordMX class

DNS Server Resource Record MX definition.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class PS_DnsServerResourceRecordMX
{
};
```

## Members

The **PS\_DnsServerResourceRecordMX** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DnsServerResourceRecordMX** class has these methods.



| Method                                          | Description                                                    |
|:------------------------------------------------|:---------------------------------------------------------------|
| [**Add**](add-ps-dnsserverresourcerecordmx.md) | Add a mail exchanger (MX) resource record to a zone<br/> |



 

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

 

 





