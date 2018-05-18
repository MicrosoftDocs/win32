---
title: DnsClientNrptGlobal class
description: Contains the global settings for the DNS Client Name Resolution Policy table.
audience: developer
ms.assetid: 'e7379e20-5e9d-4ab7-9436-e5d97186522f'
ms.prod: 'windows-server-dev'
ms.technology:
- 'remote-access'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DnsClientNrptGlobal class", "DnsClientNrptGlobal class, described"]
topic_type:
- apiref
api_name:
- DnsClientNrptGlobal
- DnsClientNrptGlobal.EnableDAForAllNetworks
- DnsClientNrptGlobal.SecureNameQueryFallback
- DnsClientNrptGlobal.QueryPolicy
api_location:
- RAMgmtPSProvider.dll
api_type:
- DllExport
---

# DnsClientNrptGlobal class

Contains the global settings for the DNS Client Name Resolution Policy table.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("RAMgmtPSProvider"), AMENDMENT]
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

Describes the DirectAccess rules state.

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

Controls the DNS client query policy.

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

Controls the DNS client name resolution fallback policy.

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



|                                     |                                                                                                 |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                  |
| Namespace<br/>                | Root\\Microsoft\\Windows\\RemoteAccess<br/>                                               |
| MOF<br/>                      | <dl> <dt>RAMgmtPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RAMgmtPSProvider.dll</dt> </dl> |



 

 





