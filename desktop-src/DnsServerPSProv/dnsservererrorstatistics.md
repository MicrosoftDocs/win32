---
title: DnsServerErrorStatistics class
description: DNS server statistics related to the different types of errors returned by the server.
audience: developer
ms.assetid: '0ffb03fb-e1bb-46fc-bcb4-e834dd228bef'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DnsServerErrorStatistics class", "DnsServerErrorStatistics class, described"]
topic_type:
- apiref
api_name:
- DnsServerErrorStatistics
- DnsServerErrorStatistics.NoError
- DnsServerErrorStatistics.FormError
- DnsServerErrorStatistics.ServFail
- DnsServerErrorStatistics.NxDomain
- DnsServerErrorStatistics.NotImpl
- DnsServerErrorStatistics.Refused
- DnsServerErrorStatistics.YxDomain
- DnsServerErrorStatistics.YxRRSet
- DnsServerErrorStatistics.NxRRSet
- DnsServerErrorStatistics.NotAuthoritative
- DnsServerErrorStatistics.NotZone
- DnsServerErrorStatistics.Max
- DnsServerErrorStatistics.BadSig
- DnsServerErrorStatistics.BadKey
- DnsServerErrorStatistics.BadTime
- DnsServerErrorStatistics.UnknownError
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
---

# DnsServerErrorStatistics class

DNS server statistics related to the different types of errors returned by the server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerErrorStatistics
{
  uint32 NoError;
  uint32 FormError;
  uint32 ServFail;
  uint32 NxDomain;
  uint32 NotImpl;
  uint32 Refused;
  uint32 YxDomain;
  uint32 YxRRSet;
  uint32 NxRRSet;
  uint32 NotAuthoritative;
  uint32 NotZone;
  uint32 Max;
  uint32 BadSig;
  uint32 BadKey;
  uint32 BadTime;
  uint32 UnknownError;
};
```

## Members

The **DnsServerErrorStatistics** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerErrorStatistics** class has these properties.

<dl> <dt>

**BadKey**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of occurrences where the server returned error 0x00000011 due to a bad key being present in the query.

</dd> <dt>

**BadSig**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of occurrences where the server returned error 0x00000010 due to a bad signature being present in the query.

</dd> <dt>

**BadTime**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of occurrences where the server returned error 0x00000012 due to a bad time stamp being present in the query.

</dd> <dt>

**FormError**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of occurrences where the server returned error code 0x00000001 due to a malformed query.

</dd> <dt>

**Max**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of occurrences where the server returned an error code 0x0000000F which is larger than 4 bits and the server needed to introduce the OPT field in the response packet.

</dd> <dt>

**NoError**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of occurrences where the server returned success 0x00000000 and query was successfully responded to.

</dd> <dt>

**NotAuthoritative**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of occurrences where the server returned error code 0x00000009 due to the server not being authoritative for the zone.

</dd> <dt>

**NotImpl**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of occurrences where the server returned error code 0x00000004 due to unimplemented functionality.

</dd> <dt>

**NotZone**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of occurrences where the server returned error 0x0000000A due to the requested zone not being found.

</dd> <dt>

**NxDomain**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of occurrences where the server returned a name error code 0x00000003.

</dd> <dt>

**NxRRSet**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of occurrences where the server returned error code 0x00000008, because the requested resource record did not exist.

</dd> <dt>

**Refused**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of occurrences where the server returned error code 0x00000005 due to policy restrictions.

</dd> <dt>

**ServFail**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of occurrences where the server returned error code 0x00000002 due to a failure in query processing at server.

</dd> <dt>

**UnknownError**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of occurrences where the server returned an error code that was caused by any other reason than those listed above.

</dd> <dt>

**YxDomain**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of occurrences where the server returned error code 0x00000006 due to a domain not being found.

</dd> <dt>

**YxRRSet**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of occurrences where the server returned error code 0x00000007 due to the unexpected existence of a resource record.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[DnsServerPSProvider Provider](dns-server-classes.md)
</dt> </dl>

 

 





