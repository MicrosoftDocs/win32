---
title: DnsServerResourceRecordAtma class
description: DNS Server Resource Record ATMA.
audience: developer
ms.assetid: d3ca01ff-1d4e-413e-89f0-a75e39af5d18
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerResourceRecordAtma class
- DnsServerResourceRecordAtma class, described
topic_type:
- apiref
api_name:
- DnsServerResourceRecordAtma
- DnsServerResourceRecordAtma.AddressType
- DnsServerResourceRecordAtma.Address
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DnsServerResourceRecordAtma class

DNS Server Resource Record ATMA.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerResourceRecordAtma : DnsServerResourceRecordData
{
  string AddressType;
  string Address;
};
```

## Members

The **DnsServerResourceRecordAtma** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerResourceRecordAtma** class has these properties.

<dl> <dt>

**Address**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Address

</dd> <dt>

**AddressType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Address Type

The possible values are.

<dt>

<span id="E164"></span><span id="e164"></span>

**E164** ("E164")


</dt> <dd></dd> <dt>

<span id="AESA"></span><span id="aesa"></span>

**AESA** ("AESA")


</dt> <dd></dd> </dl>

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

 

 





