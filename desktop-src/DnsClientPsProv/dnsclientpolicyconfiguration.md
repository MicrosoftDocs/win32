---
title: DnsClientPolicyConfiguration class
description: DNS Client Policy Configuration.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d8045d41-1254-45ee-bb50-950233ca3cb1
ms.prod: windows-server-dev
ms.technology:
- dns-client
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsClientPolicyConfiguration class
- DnsClientPolicyConfiguration class, described
topic_type:
- apiref
api_name:
- DnsClientPolicyConfiguration
- DnsClientPolicyConfiguration.Namespace
- DnsClientPolicyConfiguration.DirectAccessEnabled
- DnsClientPolicyConfiguration.QueryPolicy
- DnsClientPolicyConfiguration.SecureNameQueryFallback
- DnsClientPolicyConfiguration.DnsSecIPsecCARestriction
- DnsClientPolicyConfiguration.DnsSecValidationRequired
- DnsClientPolicyConfiguration.DnsSecQueryIPsecRequired
- DnsClientPolicyConfiguration.DnsSecQueryIPsecEncryption
- DnsClientPolicyConfiguration.DirectAccessIPsecCARestriction
- DnsClientPolicyConfiguration.DirectAccessQueryIPsecRequired
- DnsClientPolicyConfiguration.DirectAccessQueryIPsecEncryption
- DnsClientPolicyConfiguration.DirectAccessDnsServers
- DnsClientPolicyConfiguration.DirectAccessProxyType
- DnsClientPolicyConfiguration.DirectAccessProxyName
- DnsClientPolicyConfiguration.NameServers
- DnsClientPolicyConfiguration.NameEncoding
api_location:
- DnsClientPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DnsClientPolicyConfiguration class

DNS Client Policy Configuration.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsClientPSProvider"), AMENDMENT]
class DnsClientPolicyConfiguration
{
  string  Namespace;
  boolean DirectAccessEnabled;
  string  QueryPolicy;
  string  SecureNameQueryFallback;
  string  DnsSecIPsecCARestriction;
  boolean DnsSecValidationRequired;
  boolean DnsSecQueryIPsecRequired;
  string  DnsSecQueryIPsecEncryption;
  string  DirectAccessIPsecCARestriction;
  boolean DirectAccessQueryIPsecRequired;
  string  DirectAccessQueryIPsecEncryption;
  string  DirectAccessDnsServers[];
  string  DirectAccessProxyType;
  string  DirectAccessProxyName;
  string  NameServers[];
  string  NameEncoding;
};
```

## Members

The **DnsClientPolicyConfiguration** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsClientPolicyConfiguration** class has these properties.

<dl> <dt>

**DirectAccessDnsServers**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

The DNS Servers which will be queried when DirectAccess is enabled.

</dd> <dt>

**DirectAccessEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Property which identifies if DirectAccess is enabled.

</dd> <dt>

**DirectAccessIPsecCARestriction**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Certificate authority to validate the IPsec channel for DirectAccess.

</dd> <dt>

**DirectAccessProxyName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The proxy server to be used when connecting to Internet.

</dd> <dt>

**DirectAccessProxyType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The proxy server type to be used when connecting to Internet.

<dt>

<span id="Direct"></span><span id="direct"></span><span id="DIRECT"></span>

**Direct** ("Direct")


</dt> <dd></dd> <dt>

<span id="UseDefault"></span><span id="usedefault"></span><span id="USEDEFAULT"></span>

**UseDefault** ("UseDefault")


</dt> <dd></dd> <dt>

<span id="UseProxyName"></span><span id="useproxyname"></span><span id="USEPROXYNAME"></span>

**UseProxyName** ("UseProxyName")


</dt> <dd></dd> <dt>

<span id="NoProxy"></span><span id="noproxy"></span><span id="NOPROXY"></span>

**NoProxy** ("NoProxy")


</dt> <dd></dd> </dl>

</dd> <dt>

**DirectAccessQueryIPsecEncryption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

IPsec encryption level for DirectAccess.

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

**None** ("None")


</dt> <dd></dd> <dt>

<span id="Low"></span><span id="low"></span><span id="LOW"></span>

**Low** ("Low")


</dt> <dd></dd> <dt>

<span id="Medium"></span><span id="medium"></span><span id="MEDIUM"></span>

**Medium** ("Medium")


</dt> <dd></dd> <dt>

<span id="High"></span><span id="high"></span><span id="HIGH"></span>

**High** ("High")


</dt> <dd></dd> </dl>

</dd> <dt>

**DirectAccessQueryIPsecRequired**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether IPsec is required for DirectAccess.

</dd> <dt>

**DnsSecIPsecCARestriction**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Certificate authority to validate the IPsec channel for DnsSec.

</dd> <dt>

**DnsSecQueryIPsecEncryption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

IPsec encryption level for DnsSec

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

**None** ("None")


</dt> <dd></dd> <dt>

<span id="Low"></span><span id="low"></span><span id="LOW"></span>

**Low** ("Low")


</dt> <dd></dd> <dt>

<span id="Medium"></span><span id="medium"></span><span id="MEDIUM"></span>

**Medium** ("Medium")


</dt> <dd></dd> <dt>

<span id="High"></span><span id="high"></span><span id="HIGH"></span>

**High** ("High")


</dt> <dd></dd> </dl>

</dd> <dt>

**DnsSecQueryIPsecRequired**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether IPsec is required for DnsSec queries.

</dd> <dt>

**DnsSecValidationRequired**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Whether dnssec validation is required or not.

</dd> <dt>

**NameEncoding**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Encoding format for host names in the DNS query.

<dt>

<span id="Disable"></span><span id="disable"></span><span id="DISABLE"></span>

**Disable** ("Disable")


</dt> <dd></dd> <dt>

<span id="Utf8WithMapping"></span><span id="utf8withmapping"></span><span id="UTF8WITHMAPPING"></span>

**Utf8WithMapping** ("Utf8WithMapping")


</dt> <dd></dd> <dt>

<span id="Utf8WithoutMapping"></span><span id="utf8withoutmapping"></span><span id="UTF8WITHOUTMAPPING"></span>

**Utf8WithoutMapping** ("Utf8WithoutMapping")


</dt> <dd></dd> <dt>

<span id="Punycode"></span><span id="punycode"></span><span id="PUNYCODE"></span>

**Punycode** ("Punycode")


</dt> <dd></dd> </dl>

</dd> <dt>

**NameServers**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read-only
</dt> </dl>

Generic Dns Servers

</dd> <dt>

**Namespace**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

DNS namespace which can be a suffix/prefix/FQDN/Subnet.

</dd> <dt>

**QueryPolicy**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Property for controlling DNS Client query policy.

<dt>

<span id="Disable"></span><span id="disable"></span><span id="DISABLE"></span>

**Disable** ("Disable")


</dt> <dd></dd> <dt>

<span id="QueryIPv6Only"></span><span id="queryipv6only"></span><span id="QUERYIPV6ONLY"></span>

**QueryIPv6Only** ("QueryIPv6Only")


</dt> <dd></dd> <dt>

<span id="QueryBoth"></span><span id="queryboth"></span><span id="QUERYBOTH"></span>

**QueryBoth** ("QueryBoth")


</dt> <dd></dd> </dl>

</dd> <dt>

**SecureNameQueryFallback**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Property for controlling DNS Client Name resolution fallback policy.

<dt>

<span id="Disable"></span><span id="disable"></span><span id="DISABLE"></span>

**Disable** ("Disable")


</dt> <dd></dd> <dt>

<span id="FallbackSecure"></span><span id="fallbacksecure"></span><span id="FALLBACKSECURE"></span>

**FallbackSecure** ("FallbackSecure")


</dt> <dd></dd> <dt>

<span id="FallbackUnsecure"></span><span id="fallbackunsecure"></span><span id="FALLBACKUNSECURE"></span>

**FallbackUnsecure** ("FallbackUnsecure")


</dt> <dd></dd> <dt>

<span id="FallbackPrivate"></span><span id="fallbackprivate"></span><span id="FALLBACKPRIVATE"></span>

**FallbackPrivate** ("FallbackPrivate")


</dt> <dd></dd> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsClientPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsClientPSProvider.dll</dt> </dl> |



 

 





