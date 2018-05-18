---
title: DnsServerResourceRecordRt class
description: Represents an route through (RT) resource record on a DNS server.
audience: developer
ms.assetid: 'ac0911d0-7b1f-4b3f-aa3b-044d50d92c9a'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DnsServerResourceRecordRt class", "DnsServerResourceRecordRt class, described"]
topic_type:
- apiref
api_name:
- DnsServerResourceRecordRt
- DnsServerResourceRecordRt.Preference
- DnsServerResourceRecordRt.IntermediateHost
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
---

# DnsServerResourceRecordRt class

Represents an route through (RT) resource record on a DNS server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerResourceRecordRt : DnsServerResourceRecordData
{
  uint16 Preference;
  string IntermediateHost;
};
```

## Members

The **DnsServerResourceRecordRt** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerResourceRecordRt** class has these properties.

<dl> <dt>

**IntermediateHost**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The IP address of the intermediate host specified by the RT resource record.

</dd> <dt>

**Preference**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Indicates the preference setting of the RT resource record.

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

[**DnsServerResourceRecordData**](dnsserverresourcerecorddata.md)
</dt> <dt>

[DnsServerPSProvider Provider](dns-server-classes.md)
</dt> </dl>

 

 





