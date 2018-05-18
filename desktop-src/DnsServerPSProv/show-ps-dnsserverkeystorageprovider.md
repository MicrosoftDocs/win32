---
title: Show method of the PS\_DnsServerKeyStorageProvider class
description: Returns the list of key storage providers available on the DNS server.
audience: developer
ms.assetid: '34bca245-5e67-4562-a7d9-6fe42bad667c'
ms.prod: 'windows-server-dev'
ms.technology:
- 'dns-server'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["Show method", "Show method, PS_DnsServerKeyStorageProvider class", "PS_DnsServerKeyStorageProvider class, Show method"]
topic_type:
- apiref
api_name:
- PS_DnsServerKeyStorageProvider.Show
api_location:
- DnsServerPSProvider.dll
api_type:
- COM
---

# Show method of the PS\_DnsServerKeyStorageProvider class

Returns the list of key storage providers available on the DNS server.

## Syntax


```mof
uint32 Show(
  [in]  string ComputerName,
  [out] string cmdletOutput[]
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

Optional DNS server name.

</dd> <dt>

*cmdletOutput* \[out\]
</dt> <dd>

On return, contains an instance of the current object.

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

[**PS\_DnsServerKeyStorageProvider**](ps-dnsserverkeystorageprovider.md)
</dt> </dl>

 

 





