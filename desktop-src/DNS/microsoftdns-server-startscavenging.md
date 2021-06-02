---
title: StartScavenging method of the MicrosoftDNS_Server class
description: The StartScavenging method starts scavenging stale records in the zones subjected to scavenging.
ms.assetid: ee1bc0e0-9334-4971-a524-4bb8a9015b5b
keywords:
- StartScavenging method DNS
- StartScavenging method DNS , MicrosoftDNS_Server class
- MicrosoftDNS_Server class DNS , StartScavenging method
topic_type:
- apiref
api_name:
- MicrosoftDNS_Server.StartScavenging
api_location:
- Root\MicrosoftDNS
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# StartScavenging method of the MicrosoftDNS\_Server class

The **StartScavenging** method starts scavenging stale records in the zones subjected to scavenging.

## Syntax


```mof
uint32 StartScavenging();
```



## Parameters

This method has no parameters.

## Return value

ERROR\_SUCCESS indicates the scavenging was successfully started. Any other value is an error code.

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

[**StopService Method of the MicrosoftDNS\_Server Class**](microsoftdns-server-stopservice.md)
</dt> <dt>

[**GetDistinguishedName Method of the MicrosoftDNS\_Server Class**](microsoftdns-server-getdistinguishedname.md)
</dt> </dl>

 

 





