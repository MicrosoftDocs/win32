---
title: DnsServerWinsStatistics class
description: Represents DNS server statistics related to Windows Internet Name Service (WINS) lookups.
audience: developer
ms.assetid: e9334b0b-38a1-4e46-8ab9-6993bfb37a76
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerWinsStatistics class
- DnsServerWinsStatistics class, described
topic_type:
- apiref
api_name:
- DnsServerWinsStatistics
- DnsServerWinsStatistics.WinsLookups
- DnsServerWinsStatistics.WinsResponses
- DnsServerWinsStatistics.WinsReverseLookups
- DnsServerWinsStatistics.WinsReverseResponses
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DnsServerWinsStatistics class

Represents DNS server statistics related to Windows Internet Name Service (WINS) lookups.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerWinsStatistics
{
  uint32 WinsLookups;
  uint32 WinsResponses;
  uint32 WinsReverseLookups;
  uint32 WinsReverseResponses;
};
```

## Members

The **DnsServerWinsStatistics** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerWinsStatistics** class has these properties.

<dl> <dt>

**WinsLookups**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of WINS lookup requests received by the server.

</dd> <dt>

**WinsResponses**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of WINS responses sent by the server.

</dd> <dt>

**WinsReverseLookups**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of reverse WINS lookup requests received by the server.

</dd> <dt>

**WinsReverseResponses**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of reverse WINS lookup responses sent by the server.

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

 

 





