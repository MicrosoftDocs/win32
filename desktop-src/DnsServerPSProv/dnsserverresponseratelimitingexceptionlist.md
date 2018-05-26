---
title: DnsServerResponseRateLimitingExceptionlist class
description: DNS Server Response Rate Limiting Exceptionlist.
audience: developer
ms.assetid: 353966ea-0012-460e-99ba-0e60273ecd3d
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerResponseRateLimitingExceptionlist class
- DnsServerResponseRateLimitingExceptionlist class, described
topic_type:
- apiref
api_name:
- DnsServerResponseRateLimitingExceptionlist
- DnsServerResponseRateLimitingExceptionlist.Name
- DnsServerResponseRateLimitingExceptionlist.Condition
- DnsServerResponseRateLimitingExceptionlist.ClientSubnet
- DnsServerResponseRateLimitingExceptionlist.Fqdn
- DnsServerResponseRateLimitingExceptionlist.ServerInterfaceIP
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DnsServerResponseRateLimitingExceptionlist class

DNS Server Response Rate Limiting Exceptionlist

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerResponseRateLimitingExceptionlist
{
  string Name;
  string Condition;
  string ClientSubnet;
  string Fqdn;
  string ServerInterfaceIP;
};
```

## Members

The **DnsServerResponseRateLimitingExceptionlist** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerResponseRateLimitingExceptionlist** class has these properties.

<dl> <dt>

**ClientSubnet**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The client subnet.

</dd> <dt>

**Condition**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The condition.

The possible values are.

<dt>

<span id="And"></span><span id="and"></span><span id="AND"></span>

**And** ("And")


</dt> <dd></dd> <dt>

<span id="Or"></span><span id="or"></span><span id="OR"></span>

**Or** ("Or")


</dt> <dd></dd> </dl>

</dd> <dt>

**Fqdn**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The fully-qualified domain name.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The name.

</dd> <dt>

**ServerInterfaceIP**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The server interface IP.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



 

 





