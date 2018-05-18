---
title: DnsServerResponseRateLimiting class
description: Describes the DNS server response rate limiting.
audience: developer
ms.assetid: '1e63c432-da32-4a2c-a226-24e086231e2f'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["DnsServerResponseRateLimiting class", "DnsServerResponseRateLimiting class, described"]
topic_type:
- apiref
api_name:
- DnsServerResponseRateLimiting
- DnsServerResponseRateLimiting.ResponsesPerSec
- DnsServerResponseRateLimiting.ErrorsPerSec
- DnsServerResponseRateLimiting.WindowInSec
- DnsServerResponseRateLimiting.IPv4PrefixLength
- DnsServerResponseRateLimiting.IPv6PrefixLength
- DnsServerResponseRateLimiting.LeakRate
- DnsServerResponseRateLimiting.TruncateRate
- DnsServerResponseRateLimiting.MaximumResponsesPerWindow
- DnsServerResponseRateLimiting.Mode
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
---

# DnsServerResponseRateLimiting class

Describes the DNS server response rate limiting.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerResponseRateLimiting
{
  uint32 ResponsesPerSec;
  uint32 ErrorsPerSec;
  uint32 WindowInSec;
  uint32 IPv4PrefixLength;
  uint32 IPv6PrefixLength;
  uint32 LeakRate;
  uint32 TruncateRate;
  uint32 MaximumResponsesPerWindow;
  string Mode;
};
```

## Members

The **DnsServerResponseRateLimiting** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerResponseRateLimiting** class has these properties.

<dl> <dt>

**ErrorsPerSec**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Errors per second.

</dd> <dt>

**IPv4PrefixLength**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

IPv4 prefix length.

</dd> <dt>

**IPv6PrefixLength**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

IPv6 prefix length.

</dd> <dt>

**LeakRate**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The leak rate.

</dd> <dt>

**MaximumResponsesPerWindow**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Maximum responses per window.

</dd> <dt>

**Mode**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The mode.

The possible values are.

<dt>

<span id="LogOnly"></span><span id="logonly"></span><span id="LOGONLY"></span>

**LogOnly** ("LogOnly")


</dt> <dd></dd> <dt>

<span id="Enable"></span><span id="enable"></span><span id="ENABLE"></span>

**Enable** ("Enable")


</dt> <dd></dd> <dt>

<span id="Disable"></span><span id="disable"></span><span id="DISABLE"></span>

**Disable** ("Disable")


</dt> <dd></dd> </dl>

</dd> <dt>

**ResponsesPerSec**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Responses per second.

</dd> <dt>

**TruncateRate**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Truncate rate.

</dd> <dt>

**WindowInSec**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read/write
</dt> </dl>

The window period (in seconds) over which rates are measured and averaged for RRL.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



 

 





