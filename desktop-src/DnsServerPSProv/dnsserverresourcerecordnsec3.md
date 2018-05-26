---
title: DnsServerResourceRecordNSec3 class
description: DNS Server Resource Record Data NSEC3.
audience: developer
ms.assetid: 97ef7286-e43d-4f4f-9f4d-4acc5c1d3d3c
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerResourceRecordNSec3 class
- DnsServerResourceRecordNSec3 class, described
topic_type:
- apiref
api_name:
- DnsServerResourceRecordNSec3
- DnsServerResourceRecordNSec3.HashAlgorithm
- DnsServerResourceRecordNSec3.OptOut
- DnsServerResourceRecordNSec3.Iterations
- DnsServerResourceRecordNSec3.Salt
- DnsServerResourceRecordNSec3.NextHashedOwnerName
- DnsServerResourceRecordNSec3.CoveredRecordTypes
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DnsServerResourceRecordNSec3 class

DNS Server Resource Record Data NSEC3.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerResourceRecordNSec3 : DnsServerResourceRecordData
{
  String  HashAlgorithm;
  boolean OptOut;
  uint16  Iterations;
  string  Salt;
  string  NextHashedOwnerName;
  string  CoveredRecordTypes[];
};
```

## Members

The **DnsServerResourceRecordNSec3** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerResourceRecordNSec3** class has these properties.

<dl> <dt>

**CoveredRecordTypes**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The covered records in this record set.

</dd> <dt>

**HashAlgorithm**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Crypto algorithm using which the key was generated.

The possible values are.

<dt>



 ("RsaSha1")


</dt> <dd></dd> </dl>

</dd> <dt>

**Iterations**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

NSEC3 iterations.

</dd> <dt>

**NextHashedOwnerName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

NSEC3 hash.

</dd> <dt>

**OptOut**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

If OptOut is enabled. true if enabled and false otherwise.

</dd> <dt>

**Salt**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

NSEC3 Salt.

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

 

 





