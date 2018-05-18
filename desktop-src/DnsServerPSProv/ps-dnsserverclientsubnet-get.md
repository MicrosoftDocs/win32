---
title: Get method of the Ps\_DnsServerClientSubnet class
description: Enumerate the client subnet record data.
audience: developer
ms.assetid: '69BF6F2C-28A1-49CC-893E-E903136B19DB'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Get method", "Get method, Ps_DnsServerClientSubnet class", "Ps_DnsServerClientSubnet class, Get method"]
topic_type:
- apiref
api_name:
- Ps_DnsServerClientSubnet.Get
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# Get method of the Ps\_DnsServerClientSubnet class

Enumerate the client subnet record data

## Syntax


```mof
uint32 Get(
  [in]  string                Name,
  [in]  string                ComputerName,
  [out] DnsServerClientSubnet cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

The name of the client subnet record.

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

The name of the remote computer on which to execute the command.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

When this method returns, this parameter receives an embedded instance of the [**DnsServerClientSubnet**](dnsserverclientsubnet.md) object that represents the retrieved subnet record.

</dd> </dl>

## Return value

If this operation succeeds, this method returns "0"; otherwise, it returns a WMI error code.

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[**Ps\_DnsServerClientSubnet**](ps-dnsserverclientsubnet.md)
</dt> </dl>

 

 





