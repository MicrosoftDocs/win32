---
title: DnsServerRecordRequest class
description: Counts DNS server requests for the specified record type.
audience: developer
ms.assetid: ecda7f95-d06a-4867-a267-db89aee2dba8
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerRecordRequest class
- DnsServerRecordRequest class, described
topic_type:
- apiref
api_name:
- DnsServerRecordRequest
- DnsServerRecordRequest.RecordType
- DnsServerRecordRequest.Request
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DnsServerRecordRequest class

Counts DNS server requests for the specified record type.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerRecordRequest
{
  string RecordType;
  uint32 Request;
};
```

## Members

The **DnsServerRecordRequest** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerRecordRequest** class has these properties.

<dl> <dt>

**RecordType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The record type for which to count DNS server requests.

</dd> <dt>

**Request**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of WINS lookup requests received by the server for the specified record type.

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

 

 





