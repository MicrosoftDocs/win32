---
title: DnsClientNrptGlobal class
description: DNS Client Name Resolution Policy Table Global Settings.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: fa69bcd3-bf84-4916-a1d0-2b98615997b0
ms.prod: windows-server-dev
ms.technology:
- dns-client
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsClientNrptGlobal class
- DnsClientNrptGlobal class, described
topic_type:
- apiref
api_name:
- DnsClientNrptGlobal
- DnsClientNrptGlobal.EnableDAForAllNetworks
- DnsClientNrptGlobal.SecureNameQueryFallback
- DnsClientNrptGlobal.QueryPolicy
api_location:
- DnsClientPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DnsClientNrptGlobal class

DNS Client Name Resolution Policy Table Global Settings

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsClientPSProvider"), AMENDMENT]
class DnsClientNrptGlobal
{
  string EnableDAForAllNetworks;
  string SecureNameQueryFallback;
  string QueryPolicy;
};
```

## Members

The **DnsClientNrptGlobal** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsClientNrptGlobal** class has these properties.

<dl> <dt>

**EnableDAForAllNetworks**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Property for controlling DirectAccess rules state

<dt>

<span id="Disable"></span><span id="disable"></span><span id="DISABLE"></span>

**Disable** ("Disable")


</dt> <dd></dd> <dt>

<span id="EnableOnNetworkId"></span><span id="enableonnetworkid"></span><span id="ENABLEONNETWORKID"></span>

**EnableOnNetworkId** ("EnableOnNetworkId")


</dt> <dd></dd> <dt>

<span id="EnableDA"></span><span id="enableda"></span><span id="ENABLEDA"></span>

**EnableDA** ("EnableDA")


</dt> <dd></dd> <dt>

<span id="DisableDA"></span><span id="disableda"></span><span id="DISABLEDA"></span>

**DisableDA** ("DisableDA")


</dt> <dd></dd> </dl>

</dd> <dt>

**QueryPolicy**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Property for controlling DNS Client query policy

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

Access type: Read/write
</dt> </dl>

Property for controlling DNS Client Name resolution fallback policy

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



 

 





