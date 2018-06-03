---
title: PS\_DnsServerResourceRecordPtr class
description: DNS Server Resource Record Pointer definition.
audience: developer
ms.assetid: 84cc7ebd-a9d4-420e-a2a7-a2dce546f669
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- PS_DnsServerResourceRecordPtr class
- PS_DnsServerResourceRecordPtr class, described
topic_type:
- apiref
api_name:
- PS_DnsServerResourceRecordPtr
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PS\_DnsServerResourceRecordPtr class

DNS Server Resource Record Pointer definition.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class PS_DnsServerResourceRecordPtr
{
};
```

## Members

The **PS\_DnsServerResourceRecordPtr** class has these types of members:

-   [Methods](#methods)

### Methods

The **PS\_DnsServerResourceRecordPtr** class has these methods.



| Method                                           | Description                                                       |
|:-------------------------------------------------|:------------------------------------------------------------------|
| [**Add**](add-ps-dnsserverresourcerecordptr.md) | Adds a pointer (PTR) resource record to a reverse zone<br/> |



 

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

 

 





