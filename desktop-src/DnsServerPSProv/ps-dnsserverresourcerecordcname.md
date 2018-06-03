---
title: PS\_DnsServerResourceRecordCName class
description: DNS Server Resource Record CName definition.
audience: developer
ms.assetid: 49c88598-e184-4c32-8689-b6b297796923
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DnsServerResourceRecordCName class
- PS_DnsServerResourceRecordCName class, described
topic_type:
- apiref
api_name:
- PS_DnsServerResourceRecordCName
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PS\_DnsServerResourceRecordCName class

DNS Server Resource Record CName definition.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class PS_DnsServerResourceRecordCName
{
};
```

## Members

The **PS\_DnsServerResourceRecordCName** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DnsServerResourceRecordCName** class has these methods.



| Method                                             | Description                                                                                         |
|:---------------------------------------------------|:----------------------------------------------------------------------------------------------------|
| [**Add**](add-ps-dnsserverresourcerecordcname.md) | Adds a record for mapping an alias DNS domain name to another primary or canonical name.<br/> |



 

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

 

 





