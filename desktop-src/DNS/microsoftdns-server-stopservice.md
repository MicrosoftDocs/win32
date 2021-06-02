---
title: StopService method of the MicrosoftDNS_Server class
description: The StopService method stops the DNS Server.
ms.assetid: 80637d5b-e43a-4710-b3ab-eec246587788
keywords:
- StopService method DNS
- StopService method DNS , MicrosoftDNS_Server class
- MicrosoftDNS_Server class DNS , StopService method
topic_type:
- apiref
api_name:
- MicrosoftDNS_Server.StopService
api_location:
- Root\MicrosoftDNS
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# StopService method of the MicrosoftDNS\_Server class

The **StopService** method stops the DNS Server.

## Syntax


```mof
uint32 StopService();
```



## Parameters

This method has no parameters.

## Return value

ERROR\_SUCCESS indicates the service was successfully stopped. Any other value is an error code.

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

[**StartService Method of the MicrosoftDNS\_Server Class**](microsoftdns-server-startservice.md)
</dt> <dt>

[**StartScavenging Method of the MicrosoftDNS\_Server Class**](microsoftdns-server-startscavenging.md)
</dt> <dt>

[**GetDistinguishedName Method of the MicrosoftDNS\_Server Class**](microsoftdns-server-getdistinguishedname.md)
</dt> </dl>

 

 





