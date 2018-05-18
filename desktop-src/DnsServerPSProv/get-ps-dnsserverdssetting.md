---
title: Get method of the PS\_DnsServerDsSetting class
description: Retrieves DNS Server AD Settings.
audience: developer
ms.assetid: '2e3d3fd9-2120-45ae-a77d-b17f05e70c7a'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Get method", "Get method, PS_DnsServerDsSetting class", "PS_DnsServerDsSetting class, Get method"]
topic_type:
- apiref
api_name:
- PS_DnsServerDsSetting.Get
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# Get method of the PS\_DnsServerDsSetting class

Retrieves DNS Server AD Settings.

## Syntax


```mof
uint32 Get(
  [in]  string             ComputerName,
  [out] DnsServerDsSetting cmdletOutput
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

Specifies the remote computer on which to execute the command

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

An embedded instance of the [**DnsServerDsSetting**](dnsserverdssetting.md) class.

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

[**PS\_DnsServerDsSetting**](ps-dnsserverdssetting.md)
</dt> </dl>

 

 





