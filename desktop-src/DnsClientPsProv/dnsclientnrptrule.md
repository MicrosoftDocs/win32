---
title: DnsClientNrptRule class
description: DNS Client Name Resolution Policy Table entry.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '930af913-c764-409f-bcf7-7136a351014d'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-client'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DnsClientNrptRule class", "DnsClientNrptRule class, described"]
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
- DnsClientPSProvider.dll
api_type:
- DllExport
---

# DnsClientNrptRule class

DNS Client Name Resolution Policy Table entry.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsClientPSProvider"), AMENDMENT]
class DnsClientNrptRule
{
  uint32  Version;
  string  Namespace[];
  string  Name;
  string  DisplayName;
  boolean DnsSecEnabled;
  boolean DnsSecValidationRequired;
  boolean DnsSecQueryIPsecRequired;
  string  DnsSecQueryIPsecEncryption;
  boolean DirectAccessEnabled;
  string  IPsecCARestriction;
  string  DirectAccessDnsServers[];
  boolean DirectAccessQueryIPsecRequired;
  string  DirectAccessQueryIPsecEncryption;
  string  DirectAccessProxyType;
  string  DirectAccessProxyName;
  string  NameServers[];
  string  NameEncoding;
  string  Comment;
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

The DNS Servers which will be queried when DA is enabled.

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

The proxy server to be used when connecting to Internet.

</dd> <dt>

**DirectAccessProxyType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The proxy server type to be used when connecting to Internet.

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

Property to control IPsec tunnel encryption settings.

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

Property to tunnel DNS queries over IPsec channel.

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

Property which identifies if DnsSec is enabled on the rule.

</dd> <dt>

**DnsSecQueryIPsecEncryption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Property to control IPsec tunnel encryption settings.

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

Property to tunnel DnsSec queries over IPsec channel.

</dd> <dt>

**DnsSecValidationRequired**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Property to enable AD bit check on DNS responses.

</dd> <dt>

**IPsecCARestriction**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Certificate authority to validate the IPsec channel.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Name which uniquely identifies a rule.

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

The DNS Servers the DNS query is sent to when DA is disabled.

</dd> <dt>

**Namespace**
</dt> <dd> <dl> <dt>

Data type: **string** array
</dt> <dt>

Access type: Read/write
</dt> </dl>

DNS namespace which can be a suffix/prefix/FQDN/Subnet/Any. In order to specify Any, the value must be '.' (dot).

</dd> <dt>

**Version**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The version for NRPT entry.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsClientPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsClientPSProvider.dll</dt> </dl> |



 

 





