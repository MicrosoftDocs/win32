---
description: CMSPAddress Pure Virtual Methods - These methods must be overridden by derived classes.
ms.assetid: 68402cff-effd-4a2b-b9f9-f13f233b1555
title: CMSPAddress Pure Virtual Methods
ms.topic: reference
ms.date: 05/31/2018
---

# CMSPAddress Pure Virtual Methods

These methods must be overridden by derived classes.



| CMSPAddress pure virtual methods                           | Description                                                                                                                                                                            |
|------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**MSPAddressAddRef**](/windows/desktop/api/Mspaddr/nf-mspaddr-cmspaddress-mspaddressaddref)   | Private AddRef method for the address.                                                                                                                                                 |
| [**MSPAddressRelease**](/windows/desktop/api/Mspaddr/nf-mspaddr-cmspaddress-mspaddressrelease) | Private Release method for the address.                                                                                                                                                |
| [**CreateMSPCall**](/windows/desktop/api/msp/nf-msp-itmspaddress-createmspcall)        | Called by TAPI to create a call object. The implementation in the derived class should simply call the [**CreateMSPCallHelper**](/windows/desktop/api/Mspaddr/nf-mspaddr-createmspcallhelper) function.        |
| [**ShutdownMSPCall**](/windows/desktop/api/msp/nf-msp-itmspaddress-shutdownmspcall)    | Called by TAPI to shut down a call object. The implementation in the derived class should simply call the [**ShutdownMSPCallHelper**](/windows/desktop/api/Mspaddr/nf-mspaddr-shutdownmspcallhelper) function. |
| [**GetCallMediaTypes**](/windows/desktop/api/Mspaddr/nf-mspaddr-cmspaddress-getcallmediatypes) | Gets media types supported by the MSP.                                                                                                                                                 |



 

## Related topics

<dl> <dt>

[**CMSPAddress**](/windows/desktop/api/Mspaddr/nl-mspaddr-cmspaddress)
</dt> </dl>

 

 



