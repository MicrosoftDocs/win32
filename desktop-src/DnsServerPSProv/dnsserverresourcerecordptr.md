---
title: DnsServerResourceRecordPtr class
description: DNS Server Resource Record PTR.
audience: developer
ms.assetid: 84cc7ebd-a9d4-420e-a2a7-a2dce546f669
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerResourceRecordPtr class
- DnsServerResourceRecordPtr class, described
topic_type:
- apiref
api_name:
- DnsServerResourceRecordPtr
- DnsServerResourceRecordPtr.PtrDomainName
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DnsServerResourceRecordPtr class

DNS Server Resource Record PTR.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerResourceRecordPtr : DnsServerResourceRecordData
{
  string PtrDomainName;
};
```

## Members

The **DnsServerResourceRecordPtr** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerResourceRecordPtr** class has these properties.

<dl> <dt>

**PtrDomainName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

PTR Domain Name.

</dd> </dl>

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

[**DnsServerResourceRecordData**](dnsserverresourcerecorddata.md)
</dt> <dt>

[DnsServerPSProvider Provider](dns-server-classes.md)
</dt> </dl>

 

 





