---
title: PS\_DnsServerResourceRecordAging class
description: Class to \ 0034;age \ 0034; different resource records of DnsServer.
audience: developer
ms.assetid: 0394d9b6-ff54-422a-ac6e-5dedfb7ecfd5
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DnsServerResourceRecordAging class
- PS_DnsServerResourceRecordAging class, described
topic_type:
- apiref
api_name:
- PS_DnsServerResourceRecordAging
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# PS\_DnsServerResourceRecordAging class

Class to "age" different resource records of DnsServer.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class PS_DnsServerResourceRecordAging
{
};
```

## Members

The **PS\_DnsServerResourceRecordAging** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DnsServerResourceRecordAging** class has these methods.



| Method                                             | Description                        |
|:---------------------------------------------------|:-----------------------------------|
| [**Set**](set-ps-dnsserverresourcerecordaging.md) | Ages RRs under a node.,<br/> |



 

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

 

 





