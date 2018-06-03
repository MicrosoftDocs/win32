---
title: Add method of the PS\_DnsClientNrptRule class
description: Adds a rule to Name Resolution Policy Table.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 573b82cb-500e-4a46-8fc6-952bc8267c78
ms.prod: windows-server-dev
ms.technology:
- dns-client
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- Add method
- Add method, PS_DnsClientNrptRule class
- PS_DnsClientNrptRule class, Add method
topic_type:
- apiref
api_name:
- PS_DnsClientNrptRule.Add
api_location:
- DnsClientPSProvider.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Add method of the PS\_DnsClientNrptRule class

Adds a rule to Name Resolution Policy Table.

## Syntax


```mof
uint32 Add(
  [in]  string            GpoName,
  [in]  string            DANameServers[],
  [in]  boolean           DAIPsecRequired,
  [in]  string            DAIPsecEncryptionType,
  [in]  string            DAProxyServerName,
  [in]  boolean           DnsSecEnable,
  [in]  boolean           DnsSecIPsecRequired,
  [in]  string            DnsSecIPsecEncryptionType,
  [in]  string            NameServers[],
  [in]  string            NameEncoding,
  [in]  string            Namespace[],
  [in]  string            Server,
  [in]  string            DAProxyType,
  [in]  boolean           DnsSecValidationRequired,
  [in]  boolean           DAEnable,
  [in]  string            IPsecTrustAuthority,
  [in]  string            Comment,
  [in]  string            DisplayName,
  [in]  boolean           PassThru,
  [out] DnsClientNrptRule cmdletOutput
);
```



## Parameters

<dl> <dt>

*GpoName* \[in\]
</dt> <dd>

Name of GPO, if not specified the default GPO on the domain.

</dd> <dt>

*DANameServers* \[in\]
</dt> <dd>

The DNS servers which will be queried when Direct Access is enabled.

</dd> <dt>

*DAIPsecRequired* \[in\]
</dt> <dd>

Property for controlling whether IPsec is required or not for DA.

</dd> <dt>

*DAIPsecEncryptionType* \[in\]
</dt> <dd>

Property for controlling IPsec encryption type for DA.

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


</dt> <dd></dd> </dl> </dd> <dt>

*DAProxyServerName* \[in\]
</dt> <dd>

The proxy server to be used when connecting to the Internet.

</dd> <dt>

*DnsSecEnable* \[in\]
</dt> <dd>

Property which identifies if DNSSEC is enabled on the rule.

</dd> <dt>

*DnsSecIPsecRequired* \[in\]
</dt> <dd>

Property to tunnel DNS queries over IPsec channel.

</dd> <dt>

*DnsSecIPsecEncryptionType* \[in\]
</dt> <dd>

Property to control Ipsec tunnel encryption settings.

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


</dt> <dd></dd> </dl> </dd> <dt>

*NameServers* \[in\]
</dt> <dd>

The DNS servers the DNS query is sent to when DA is disabled.

</dd> <dt>

*NameEncoding* \[in\]
</dt> <dd>

Encoding format for host names in the DNS query.

</dd> <dt>

*Namespace* \[in\]
</dt> <dd>

DNS namespace which can be a suffix/prefix/FQDN/subnet/any. In order to specify any, the value must be .(dot)

</dd> <dt>

*Server* \[in\]
</dt> <dd>

Server hosting the GPO.

</dd> <dt>

*DAProxyType* \[in\]
</dt> <dd>

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


</dt> <dd></dd> </dl> </dd> <dt>

*DnsSecValidationRequired* \[in\]
</dt> <dd>

Property for controlling whether Dnssec validation is required or not.

</dd> <dt>

*DAEnable* \[in\]
</dt> <dd>

Property for controlling DirectAccess rules state.

</dd> <dt>

*IPsecTrustAuthority* \[in\]
</dt> <dd>

Certification authority to validate the IPsec channel.

</dd> <dt>

*Comment* \[in\]
</dt> <dd>

Stores admin notes.

</dd> <dt>

*DisplayName* \[in\]
</dt> <dd>

An optional friendly name for the Name Resolution Policy Table rule.

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Specifies if result of the cmdlet should be displayed

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

A [**DnsClientNrptRule**](ps-dnsclientnrptrule.md) object containing all the properties of DNS client NRPT rule.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsClientPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsClientPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DnsClientNrptRule**](ps-dnsclientnrptrule.md)
</dt> </dl>

 

 





