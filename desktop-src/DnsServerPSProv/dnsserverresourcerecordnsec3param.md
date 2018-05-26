---
title: DnsServerResourceRecordNSec3Param class
description: DNS Server Resource Record Data NSEC3PARAM.
audience: developer
ms.assetid: 3e112073-beef-41f5-9f22-a5a6798266da
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerResourceRecordNSec3Param class
- DnsServerResourceRecordNSec3Param class, described
topic_type:
- apiref
api_name:
- DnsServerResourceRecordNSec3Param
- DnsServerResourceRecordNSec3Param.HashAlgorithm
- DnsServerResourceRecordNSec3Param.Iterations
- DnsServerResourceRecordNSec3Param.Salt
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DnsServerResourceRecordNSec3Param class

DNS Server Resource Record Data NSEC3PARAM.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerResourceRecordNSec3Param : DnsServerResourceRecordData
{
  string HashAlgorithm;
  uint16 Iterations;
  string Salt;
};
```

## Members

The **DnsServerResourceRecordNSec3Param** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerResourceRecordNSec3Param** class has these properties.

<dl> <dt>

**HashAlgorithm**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Crypto algorithm using which the key was generated.

The possible values are.

<dt>

<span id="RsaSha1"></span><span id="rsasha1"></span><span id="RSASHA1"></span>

**RsaSha1** ("RsaSha1")


</dt> <dd></dd> <dt>

<span id="RsaSha1NSec3"></span><span id="rsasha1nsec3"></span><span id="RSASHA1NSEC3"></span>

**RsaSha1NSec3** ("RsaSha1NSec3")


</dt> <dd></dd> <dt>

<span id="RsaSha256"></span><span id="rsasha256"></span><span id="RSASHA256"></span>

**RsaSha256** ("RsaSha256")


</dt> <dd></dd> <dt>

<span id="RsaSha512"></span><span id="rsasha512"></span><span id="RSASHA512"></span>

**RsaSha512** ("RsaSha512")


</dt> <dd></dd> <dt>

<span id="ECDsaP256Sha256"></span><span id="ecdsap256sha256"></span><span id="ECDSAP256SHA256"></span>

**ECDsaP256Sha256** ("ECDsaP256Sha256")


</dt> <dd></dd> <dt>

<span id="ECDsaP384Sha384"></span><span id="ecdsap384sha384"></span><span id="ECDSAP384SHA384"></span>

**ECDsaP384Sha384** ("ECDsaP384Sha384")


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

 

 





