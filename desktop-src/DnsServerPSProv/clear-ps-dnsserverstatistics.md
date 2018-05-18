---
title: Clear method of the PS\_DnsServerStatistics class
description: Clears all DNS server statistics.
audience: developer
ms.assetid: '8fa0d3d4-91e1-406c-9b26-56ba51008c7d'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Clear method", "Clear method, PS_DnsServerStatistics class", "PS_DnsServerStatistics class, Clear method"]
topic_type:
- apiref
api_name:
- PS_DnsServerStatistics.Clear
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# Clear method of the PS\_DnsServerStatistics class

Clears all DNS server statistics.

## Syntax


```mof
uint32 Clear(
  [in] string  ComputerName,
  [in] boolean Force
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command.

</dd> <dt>

*Force* \[in\]
</dt> <dd>

Specifies whether the method performs the operation without prompting for a confirmation.

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

[**PS\_DnsServerStatistics**](ps-dnsserverstatistics.md)
</dt> </dl>

 

 





