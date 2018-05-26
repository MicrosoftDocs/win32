---
title: DnsServerRecursion class
description: Represents the recursion settings on a DNS server.
audience: developer
ms.assetid: 7ed64a05-b62c-4967-8b0e-64e066e434b8
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerRecursion class
- DnsServerRecursion class, described
topic_type:
- apiref
api_name:
- DnsServerRecursion
- DnsServerRecursion.Timeout
- DnsServerRecursion.RetryInterval
- DnsServerRecursion.AdditionalTimeout
- DnsServerRecursion.Enable
- DnsServerRecursion.SecureResponse
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DnsServerRecursion class

Represents the recursion settings on a DNS server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerRecursion
{
  uint32  Timeout;
  uint32  RetryInterval;
  uint32  AdditionalTimeout;
  boolean Enable;
  boolean SecureResponse;
};
```

## Members

The **DnsServerRecursion** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerRecursion** class has these properties.

<dl> <dt>

**AdditionalTimeout**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The time interval, in seconds, that a DNS server waits as it uses recursion to get resource records from a remote DNS server. We recommend that you limit the value to the range 0x00000000 to 0x0000000F (0 seconds to 15 seconds), inclusive. However, you can use any value. We recommend that you set the default value to 4.

</dd> <dt>

**Enable**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**True** to enable recursion on the DNS server; otherwise, **false**.

</dd> <dt>

**RetryInterval**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The elapsed seconds before a DNS server retries a recursive lookup. If the parameter is undefined or zero, the DNS server retries after three seconds. Valid values range from 1 to 15 seconds.

</dd> <dt>

**SecureResponse**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

**True** for the DNS server to screen DNS records against the zone of authority for the remote server, to prevent cache pollution; otherwise, **false**.

</dd> <dt>

**Timeout**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The number of seconds that a DNS server waits before it stops trying to contact a remote server. The valid value is in the range of 0x1 to 0xFFFFFFFF (1 second to 15 seconds). The default setting is 0xF (15 seconds). We recommend that you increase this value when recursion occurs over a slow link.

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

 

 





