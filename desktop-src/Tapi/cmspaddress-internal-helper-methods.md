---
Description: The following list contains the internal CMSP address methods.
ms.assetid: 2016a776-1464-46b5-96b9-b045834f9e38
title: CMSPAddress Internal Helper Methods
ms.topic: reference
ms.date: 05/31/2018
---

# CMSPAddress Internal Helper Methods



| CMSPAddress internal helper methods                                        | Description                                                                                                                                                                                                                                                                  |
|----------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetStaticTerminals**](/windows/desktop/api/Mspaddr/nf-mspaddr-cmspaddress-getstaticterminals)               | Called by [**get\_StaticTerminals**](https://msdn.microsoft.com/en-us/library/ms733180(v=VS.85).aspx) and [**EnumerateStaticTerminals**](https://msdn.microsoft.com/en-us/library/ms733174(v=VS.85).aspx) to get an array of static terminals that can be used on this address.                                     |
| [**GetDynamicTerminalClasses**](/windows/desktop/api/Mspaddr/nf-mspaddr-cmspaddress-getdynamicterminalclasses) | Called by [**get\_DynamicTerminalClasses**](https://msdn.microsoft.com/en-us/library/ms733178(v=VS.85).aspx) and [**EnumerateDynamicTerminalClasses**](https://msdn.microsoft.com/en-us/library/ms733173(v=VS.85).aspx) to get an array of dynamic terminal classes that can be used on this address. |
| [**UpdateTerminalList**](/windows/desktop/api/Mspaddr/nf-mspaddr-cmspaddress-updateterminallist)               | Populates the MSP's list of static terminals.                                                                                                                                                                                                                                |
| [**ReceiveTSPAddressData**](/windows/desktop/api/Mspaddr/nf-mspaddr-cmspaddress-receivetspaddressdata)         | Called when a TSP data message is intended to be processed by the address rather than by a specific call.                                                                                                                                                                    |



 

## Related topics

<dl> <dt>

[**CMSPAddress**](/windows/desktop/api/Mspaddr/nl-mspaddr-cmspaddress)
</dt> </dl>

 

 



