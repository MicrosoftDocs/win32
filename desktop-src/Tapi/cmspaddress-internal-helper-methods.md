---
description: The following list contains the internal CMSP address methods.
ms.assetid: 2016a776-1464-46b5-96b9-b045834f9e38
title: CMSPAddress Internal Helper Methods
ms.topic: reference
ms.date: 05/31/2018
---

# CMSPAddress Internal Helper Methods



| CMSPAddress internal helper methods                                        | Description                                                                                                                                                                                                                                                                  |
|----------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetStaticTerminals**](/windows/desktop/api/Mspaddr/nf-mspaddr-cmspaddress-getstaticterminals)               | Called by [**get\_StaticTerminals**](/windows/win32/api/tapi3if/nf-tapi3if-itterminalsupport-get_staticterminals) and [**EnumerateStaticTerminals**](/windows/win32/api/tapi3if/nf-tapi3if-itterminalsupport-enumeratestaticterminals) to get an array of static terminals that can be used on this address.                                     |
| [**GetDynamicTerminalClasses**](/windows/desktop/api/Mspaddr/nf-mspaddr-cmspaddress-getdynamicterminalclasses) | Called by [**get\_DynamicTerminalClasses**](/windows/win32/api/tapi3if/nf-tapi3if-itterminalsupport-get_dynamicterminalclasses) and [**EnumerateDynamicTerminalClasses**](/windows/win32/api/tapi3if/nf-tapi3if-itterminalsupport-enumeratedynamicterminalclasses) to get an array of dynamic terminal classes that can be used on this address. |
| [**UpdateTerminalList**](/windows/desktop/api/Mspaddr/nf-mspaddr-cmspaddress-updateterminallist)               | Populates the MSP's list of static terminals.                                                                                                                                                                                                                                |
| [**ReceiveTSPAddressData**](/windows/desktop/api/Mspaddr/nf-mspaddr-cmspaddress-receivetspaddressdata)         | Called when a TSP data message is intended to be processed by the address rather than by a specific call.                                                                                                                                                                    |



 

## Related topics

<dl> <dt>

[**CMSPAddress**](/windows/desktop/api/Mspaddr/nl-mspaddr-cmspaddress)
</dt> </dl>

 

 
