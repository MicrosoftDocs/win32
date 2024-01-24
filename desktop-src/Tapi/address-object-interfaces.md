---
description: Address objects are entities that can make or receive calls. The related interfaces and methods allow an application to get and set information concerning an address, such as whether the address has caller ID support.
ms.assetid: 6e347e4c-aec3-4bbd-95f3-a68e6e136e11
title: Address Object Interfaces
ms.topic: article
ms.date: 05/31/2018
---

# Address Object Interfaces

[Address objects](address-object.md) are entities that can make or receive calls. The related interfaces and methods allow an application to get and set information concerning an address, such as whether the address has caller ID support.

The [**ITAddressEvent**](/windows/desktop/api/tapi3if/nn-tapi3if-itaddressevent), [**ITAddressTranslationInfo**](/windows/desktop/api/tapi3if/nn-tapi3if-itaddresstranslationinfo), [**ITCallingCard**](/windows/desktop/api/tapi3if/nn-tapi3if-itcallingcard), [**ITForwardInformation**](/windows/desktop/api/tapi3if/nn-tapi3if-itforwardinformation), [**ITLocationInfo**](/windows/desktop/api/tapi3if/nn-tapi3if-itlocationinfo), and [**IEnumAddress**](/windows/desktop/api/tapi3if/nn-tapi3if-ienumaddress) interfaces are not directly exposed on the Address Object, but are tightly related to it and are listed here for reference convenience.



| Interface                                                            | Description                                                                                                                                     |
|----------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ITAddress**](/windows/desktop/api/tapi3if/nn-tapi3if-itaddress)                                       | Acts as base interface for the Address object.                                                                                                  |
| [**ITAddress2**](/windows/desktop/api/tapi3if/nn-tapi3if-itaddress2)                                     | Derives from [**ITAddress**](/windows/desktop/api/tapi3if/nn-tapi3if-itaddress); provides additional methods that support phone devices.                                            |
| [**ITAddressCapabilities**](/windows/desktop/api/tapi3if/nn-tapi3if-itaddresscapabilities)               | Gets information concerning an address's capabilities.                                                                                          |
| [**ITAddressEvent**](/windows/desktop/api/tapi3if/nn-tapi3if-itaddressevent)                             | Provides information concerning address events.                                                                                                 |
| [**ITAddressTranslation**](/windows/desktop/api/tapi3if/nn-tapi3if-itaddresstranslation)                 | Performs address translation.                                                                                                                   |
| [**ITAddressTranslationInfo**](/windows/desktop/api/tapi3if/nn-tapi3if-itaddresstranslationinfo)         | Gets address translation information.                                                                                                           |
| [**ITCallingCard**](/windows/desktop/api/tapi3if/nn-tapi3if-itcallingcard)                               | Provides methods to retrieve calling card information.                                                                                          |
| [**ITForwardInformation**](/windows/desktop/api/tapi3if/nn-tapi3if-itforwardinformation)                 | Provides methods for setting up and implementing call forwarding.                                                                               |
| [**ITLegacyAddressMediaControl**](/windows/desktop/api/tapi3if/nn-tapi3if-itlegacyaddressmediacontrol)   | Supports legacy applications that require direct access to a device and its configuration.                                                      |
| [**ITLegacyAddressMediaControl2**](/windows/desktop/api/Tapi3if/nn-tapi3if-itlegacyaddressmediacontrol2) | Extends [**ITLegacyAddressMediaControl**](/windows/desktop/api/tapi3if/nn-tapi3if-itlegacyaddressmediacontrol) by allowing the configuration of parameters related to line devices. |
| [**ITLocationInfo**](/windows/desktop/api/tapi3if/nn-tapi3if-itlocationinfo)                             | Gets information related to the location of the calling party.                                                                                  |
| [**ITMediaSupport**](/windows/desktop/api/tapi3if/nn-tapi3if-itmediasupport)                             | Gets information concerning an address's media support capabilities.                                                                            |
| [**ITTerminalSupport**](/windows/win32/api/tapi3if/nn-tapi3if-itterminalsupport)                       | Gets information on available terminals and provides a method to create additional terminals.                                                   |
| [**IEnumAddress**](/windows/desktop/api/tapi3if/nn-tapi3if-ienumaddress)                                 | Enumerates [**ITAddress**](/windows/desktop/api/tapi3if/nn-tapi3if-itaddress).                                                                                                      |
| [**IEnumCallingCard**](/windows/desktop/api/tapi3if/nn-tapi3if-ienumcallingcard)                         | Enumerates [**ITCallingCard**](/windows/desktop/api/tapi3if/nn-tapi3if-itcallingcard).                                                                                              |



 

If the address is a [Wave MSP](wave-msp.md) address, the [**ITLegacyWaveSupport**](/windows/desktop/api/tapi3if/nn-tapi3if-itlegacywavesupport) interface is also exposed on the Address object.

 

 
