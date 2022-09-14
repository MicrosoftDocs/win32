---
description: The following list contains the CMSPCAllBase members.
ms.assetid: a3193639-e0c4-4851-a879-551eca8023f9
title: CMSPCallBase Members
ms.topic: article
ms.date: 05/31/2018
---

# CMSPCallBase Members



| Member type                   | Name             | Description                                                                                                                                                                                                                                                                                                                                       |
|-------------------------------|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IUnknown                      | \*m\_pFTM        | Pointer to the free threaded marshaller.                                                                                                                                                                                                                                                                                                          |
| CMSPAddress\*                 | \*m\_pMSPAddress | The pointer to the MSP address object. It is used to get the default terminals if the application doesn't select any. It also carries a refcount (via [**MSPAddressAddRef**](/windows/desktop/api/Mspaddr/nf-mspaddr-cmspaddress-mspaddressaddref), not AddRef) so that the aggregated address will not go away while the call is still alive, but TAPI 3's address is not AddRef'ed. |
| MSP\_HANDLE                   | \*m\_htCall      | The handle to TAPI3's call. Used to fire call events.                                                                                                                                                                                                                                                                                             |
| DWORD                         | m\_dwMediaType   | Bitmask of the media types on this call.                                                                                                                                                                                                                                                                                                          |
| CMSPArray <ITStream \*> | m\_Streams       | The list of stream objects in the call.                                                                                                                                                                                                                                                                                                           |
| CMSPCritSection               | m\_lock          | The lock that protects the stream lists.                                                                                                                                                                                                                                                                                                          |



 

## Related topics

<dl> <dt>

[**CMSPCallBase**](/windows/desktop/api/Mspcall/nl-mspcall-cmspcallbase)
</dt> </dl>

 

 



