---
title: DnsClientNrptRule class
description: Contains a table entry for a DNS client name resolution policy.
audience: developer
ms.assetid: 20034538-2b29-46d3-ad0e-05824e388afd
ms.prod: windows-server-dev
ms.technology:
- remote-access
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsClientNrptRule class
- DnsClientNrptRule class, described
topic_type:
- apiref
api_name:
- DnsClientNrptRule
- DnsClientNrptRule.Version
- DnsClientNrptRule.Namespace
- DnsClientNrptRule.Name
- DnsClientNrptRule.DisplayName
- DnsClientNrptRule.DnsSecEnabled
- DnsClientNrptRule.DnsSecValidationRequired
- DnsClientNrptRule.DnsSecQueryIPsecRequired
- DnsClientNrptRule.DnsSecQueryIPsecEncryption
- DnsClientNrptRule.DirectAccessEnabled
- DnsClientNrptRule.IPsecCARestriction
- DnsClientNrptRule.DirectAccessDnsServers
- DnsClientNrptRule.DirectAccessQueryIPsecRequired
- DnsClientNrptRule.DirectAccessQueryIPsecEncryption
- DnsClientNrptRule.DirectAccessProxyType
- DnsClientNrptRule.DirectAccessProxyName
- DnsClientNrptRule.NameServers
- DnsClientNrptRule.NameEncoding
- DnsClientNrptRule.Comment
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DnsClientNrptRule class

Contains a table entry for a DNS client name resolution policy.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
class DnsClientNrptRule
{
  uint32  Version;
  string  Namespace[];
  string  Name;
  string  DisplayName;
  boolean DnsSecEnabled;
  boolean DnsSecValidationRequired;
  boolean DnsSecQueryIPsecRequired;
  string  DnsSecQueryIPsecEncryption;
  boolean DirectAccessEnabled;
  string  IPsecCARestriction;
  string  DirectAccessDnsServers[];
  boolean DirectAccessQueryIPsecRequired;
  string  DirectAccessQueryIPsecEncryption;
  string  DirectAccessProxyType;
  string  DirectAccessProxyName;
  string  NameServers[];
  string  NameEncoding;
  string  Comment;
};
```

## Members

The **DnsClientNrptRule** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsClientNrptRule** class has these properties.

<dl> <dt>

**Comment**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

A user friendly description of the current rule.

</dd> <dt>

**DirectAccessDnsServers**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The DNS servers which will be queried when DA is enabled.

</dd> <dt>

**DirectAccessEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Property which identifies if DirectAccess is enabled on the rule.

</dd> <dt>

**DirectAccessProxyName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The proxy server to be used when connecting to the Internet.

</dd> <dt>

**DirectAccessProxyType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The proxy server type to be used when connecting to the Internet.

<dt>

<span id="NoProxy"></span><span id="noproxy"></span><span id="NOPROXY"></span>

**NoProxy** ("NoProxy")


</dt> <dd></dd> <dt>

<span id="UseDefault"></span><span id="usedefault"></span><span id="USEDEFAULT"></span>

**UseDefault** ("UseDefault")


</dt> <dd></dd> <dt>

<span id="UseProxyName"></span><span id="useproxyname"></span><span id="USEPROXYNAME"></span>

**UseProxyName** ("UseProxyName")


</dt> <dd></dd> </dl>

</dd> <dt>

**DirectAccessQueryIPsecEncryption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Controls the IPsec tunnel encryption settings.

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

Access type: Read/write
</dt> </dl>

[**true**](https://msdn.microsoft.com/library/dn520573) to tunnel DNS queries over the IPsec channel.

</dd> <dt>

**DisplayName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

An optional friendly name for the NRPT rule.

</dd> <dt>

**DnsSecEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Determines if DNSSEC is enabled on the rule.

</dd> <dt>

**DnsSecQueryIPsecEncryption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Controls the IPsec tunnel encryption settings.

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

Access type: Read/write
</dt> </dl>

**true** to tunnel DNSSEC queries over the IPsec channel.

</dd> <dt>

**DnsSecValidationRequired**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Enables the AD bit check on DNS responses.

</dd> <dt>

**IPsecCARestriction**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The certification authority to validate the IPsec channel.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The name which uniquely identifies a rule.

</dd> <dt>

**NameEncoding**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
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

Access type: Read/write
</dt> </dl>

The DNS servers the DNS query is sent to when DA is disabled.

</dd> <dt>

**Namespace**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

The DNS namespace, which can be a Suffix/Prefix/FQDN/Subnet/Any. In order to specify Any, the value must be .(dot)

</dd> <dt>

**Version**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The version of the Name Resolution Policy Table entry.

</dd> </dl>

## Requirements



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





