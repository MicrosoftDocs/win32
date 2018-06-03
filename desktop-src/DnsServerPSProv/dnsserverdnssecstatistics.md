---
title: DnsServerDnssecStatistics class
description: Represents statistics for the Domain Name System Security Extensions (DNSSEC) signature on a DNS server.
audience: developer
ms.assetid: 383f671c-df55-4119-a779-12bc461897ad
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerDnssecStatistics class
- DnsServerDnssecStatistics class, described
topic_type:
- apiref
api_name:
- DnsServerDnssecStatistics
- DnsServerDnssecStatistics.SuccessfulValidations
- DnsServerDnssecStatistics.FailedValidations
- DnsServerDnssecStatistics.RecursionFailures
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DnsServerDnssecStatistics class

Represents statistics for the Domain Name System Security Extensions (DNSSEC) signature on a DNS server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerDnssecStatistics
{
  uint32 SuccessfulValidations;
  uint32 FailedValidations;
  uint32 RecursionFailures;
};
```

## Members

The **DnsServerDnssecStatistics** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerDnssecStatistics** class has these properties.

<dl> <dt>

**FailedValidations**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times a validation attempt on a DNSSEC signature or DS digest hash failed.

</dd> <dt>

**RecursionFailures**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times a validation attempt for recursive name resolution query failed while fetching DNSSEC data.

</dd> <dt>

**SuccessfulValidations**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times a validation attempt on a DNSSEC signature or DS digest hash succeeded.

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

[DnsServerPSProvider Provider](dns-server-classes.md)
</dt> </dl>

 

 





