---
title: DnsServerResourceRecordAfsdb class
description: DNS Server Resource Record AFSDB.
audience: developer
ms.assetid: 'ad537922-5dda-4dc1-88c5-9d75cf79de33'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DnsServerResourceRecordAfsdb class", "DnsServerResourceRecordAfsdb class, described"]
topic_type:
- apiref
api_name:
- DnsServerResourceRecordAfsdb
- DnsServerResourceRecordAfsdb.SubType
- DnsServerResourceRecordAfsdb.ServerName
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
---

# DnsServerResourceRecordAfsdb class

DNS Server Resource Record AFSDB.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerResourceRecordAfsdb : DnsServerResourceRecordData
{
  uint16 SubType;
  string ServerName;
};
```

## Members

The **DnsServerResourceRecordAfsdb** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerResourceRecordAfsdb** class has these properties.

<dl> <dt>

**ServerName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Server Name

</dd> <dt>

**SubType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Sub type

The possible values are.

<dt>

<span id="1"></span>

**1** (1)


</dt> <dd></dd> <dt>

<span id="2"></span>

**2** (2)


</dt> <dd></dd> </dl>

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

 

 





