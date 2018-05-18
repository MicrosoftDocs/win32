---
title: GetByBrief method of the PS\_DnsServerSetting class
description: Retrieve DNS server settings.
audience: developer
ms.assetid: '88d3918d-7d43-448a-9bf2-f956e478f5b7'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetByBrief method", "GetByBrief method, PS_DnsServerSetting class", "PS_DnsServerSetting class, GetByBrief method"]
topic_type:
- apiref
api_name:
- PS_DnsServerSetting.GetByBrief
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# GetByBrief method of the PS\_DnsServerSetting class

Retrieve DNS server settings.

## Syntax


```mof
uint32 GetByBrief(
  [in]  string                ComputerName,
  [out] DnsServerSettingBrief cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

Receives an embedded instance of the [**DnsServerSetting**](dnsserversetting.md) class.

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**PS\_DnsServerSetting**](ps-dnsserversetting.md)
</dt> </dl>

 

 





