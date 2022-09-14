---
title: StartService method of the MicrosoftDNS_Server class
description: The StartService method starts the DNS Server.
ms.assetid: f6343a34-9d1b-4f82-897e-289650af6be9
keywords:
- StartService method DNS
- StartService method DNS , MicrosoftDNS_Server class
- MicrosoftDNS_Server class DNS , StartService method
topic_type:
- apiref
api_name:
- MicrosoftDNS_Server.StartService
api_location:
- Root\MicrosoftDNS
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# StartService method of the MicrosoftDNS\_Server class

The **StartService** method starts the DNS Server.

## Syntax


```mof
uint32 StartService();
```



## Parameters

This method has no parameters.

## Return value

ERROR\_SUCCESS indicates the service was successfully started. Any other value is an error code.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                   |
| Namespace<br/>                | Root\\MicrosoftDNS<br/>                                                          |
| MOF<br/>                      | <dl> <dt>Dnsprov.mof</dt> </dl> |



## See also

<dl> <dt>

[**MicrosoftDNS\_Server**](microsoftdns-server.md)
</dt> <dt>

[**StopService Method of the MicrosoftDNS\_Server Class**](microsoftdns-server-stopservice.md)
</dt> <dt>

[**StartScavenging Method of the MicrosoftDNS\_Server Class**](microsoftdns-server-startscavenging.md)
</dt> <dt>

[**GetDistinguishedName Method of the MicrosoftDNS\_Server Class**](microsoftdns-server-getdistinguishedname.md)
</dt> </dl>

 

 





