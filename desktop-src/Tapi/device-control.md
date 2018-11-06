---
Description: Device control at the end-user or server application level requires a relatively small set of basic information.
ms.assetid: 9c787656-93ef-4e0b-9516-8822ae49a83a
title: Device Control
ms.topic: article
ms.date: 05/31/2018
---

# Device Control

Device control at the end-user or server application level requires a relatively small set of basic information. The service provider abstraction layer performs detailed device control. The service providers report required device information to an application through TAPI.

Key device categories include:

-   [Network](network-ovr.md): The transport layer for communications. From an application's point of view, information about the network is typically embedded in the address type, such as LINEADDRESSTYPE\_PHONENUMBER.
-   [Line](line-ovr.md): A connection to a network. This concept is heavily used within TAPI 2.2 (TAPI/C).
-   [Channel](channel-ovr.md): A subdivision of a line. Knowledge of channels is normally not required of an application because the service provider configures how they will appear as addresses.
-   [Address](address-ovr.md): A network location on a network. Each line or channel has one or more associated addresses. The address is a key concept in both TAPI 3.1 (TAPI/COM) and TAPI 2.2 (TAPI/C).
-   [Terminal](terminal-ovr.md): A source or renderer for a particular address and media type.

The service providers report device characteristics to TAPI in response to application queries. Service providers also initiate reports on changes in device state. These changes are then reported to an application based on the notifications requested during initialization.

Basic device characteristics are:

-   [Device Class](device-class-ovr.md)
-   [Device Identifier](device-identifier-ovr.md)
-   [Address Type](address-type-ovr.md)
-   [Address Identifier](address-identifier-ovr.md)
-   [Device Events](device-events-ovr.md)
-   [Media Type](media-type-ovr.md)
-   [Terminal Type](terminal-type-ovr.md)

In addition, the service providers supply information concerning the capacity of a given address to perform various session operations.

Supplemental characteristics may be associated with certain devices, if the service providers support them. A TAPI 2.x application discovers capabilities by using the [**lineGetDevCaps**](https://msdn.microsoft.com/en-us/library/ms735735(v=VS.85).aspx) and [**lineGetAddressCaps**](https://msdn.microsoft.com/en-us/library/ms735674(v=VS.85).aspx) functions. TAPI 3.x applications use the [**ITAddressCapabilities**](/windows/desktop/api/tapi3if/nn-tapi3if-itaddresscapabilities) interface for this purpose.

TAPI 2.x provides a special set of supplemental operations that the service provider may implement for use with phone devices. See [Phone Devices](https://msdn.microsoft.com/en-us/library/ms736591(v=VS.85).aspx).

Extended capabilities are provider-specific and not directly covered by the Microsoft Telephony API. See [Extended Line Functions](https://msdn.microsoft.com/en-us/library/ms734886(v=VS.85).aspx), [Extended Telephony Phone Functions](https://msdn.microsoft.com/en-us/library/ms734891(v=VS.85).aspx), or [Provider-Specific Interfaces](provider-specific-interfaces.md).

Below is a summary of TAPI operations that query service providers on device characteristics and provide data on current state.



| TAPI 2.x functions                                                  | Description                                                                                                    |
|---------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| [**lineGetDevCaps**](https://msdn.microsoft.com/en-us/library/ms735735(v=VS.85).aspx)                   | Queries a specified line device to determine the telephony capabilities of associated addresses.               |
| [**lineGetAddressCaps**](https://msdn.microsoft.com/en-us/library/ms735674(v=VS.85).aspx)           | Queries a specified line device to determine the telephony capabilities of specific address.                   |
| [**lineGetDevConfig**](https://msdn.microsoft.com/en-us/library/ms735739(v=VS.85).aspx)               | Returns an "opaque" data structure that stores the current configuration of a device.                          |
| [**lineSetDevConfig**](https://msdn.microsoft.com/en-us/library/ms736096(v=VS.85).aspx)               | Restores device configuration.                                                                                 |
| [**lineConfigDialog**](https://msdn.microsoft.com/en-us/library/ms735582(v=VS.85).aspx)               | Display a dialog box that allows the user to configure parameters related to the device.                       |
| [**lineGetID**](https://msdn.microsoft.com/en-us/library/ms735751(v=VS.85).aspx)                             | Retrieves a stable device identifier that can be used in further TAPI function calls, or with a different API. |
| [**lineGetLineDevStatus**](https://msdn.microsoft.com/en-us/library/ms735753(v=VS.85).aspx)       | Queries device for current status, such as number of active calls.                                             |
| [**lineSetLineDevStatus**](https://msdn.microsoft.com/en-us/library/ms736098(v=VS.85).aspx)       | Sets device status, such as setting a device as not in service.                                                |
| [**lineGetIcon**](https://msdn.microsoft.com/en-us/library/ms735746(v=VS.85).aspx)                         | Retrieves provider-specific icon for display to the user.                                                      |
| [**lineNegotiateExtVersion**](https://msdn.microsoft.com/en-us/library/ms736003(v=VS.85).aspx) | Allows an application to negotiate an extension version to use with the specified line device.                 |
| [**lineDevSpecific**](https://msdn.microsoft.com/en-us/library/ms735604(v=VS.85).aspx)                 | Gives access to device-specific features.                                                                      |
| [**lineDevSpecificFeature**](https://msdn.microsoft.com/en-us/library/ms735607(v=VS.85).aspx)   | Sends device-specific features to the service provider.                                                        |



 



| TAPI 3.x interfaces or methods                                   | Description                                                                                             |
|------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| [**ITAddressCapabilities**](/windows/desktop/api/tapi3if/nn-tapi3if-itaddresscapabilities)           | Gets information concerning an address's capabilities.                                                  |
| [**ITAMMediaFormat**](https://msdn.microsoft.com/en-us/library/Aa382285(v=VS.85).aspx)                       | Sets and gets DirectShow™ media format.                                                                 |
| [**ITBasicAudioTerminal**](/windows/desktop/api/tapi3if/nn-tapi3if-itbasicaudioterminal)             | Sets and gets standard audio terminal characteristics, such as volume.                                  |
| [**ITMediaSupport**](/windows/desktop/api/tapi3if/nn-tapi3if-itmediasupport)                         | Gets information concerning an address's media support capabilities.                                    |
| [**ITTerminal**](https://msdn.microsoft.com/en-us/library/ms732646(v=VS.85).aspx)                                 | Base interface for the Terminal object. Obtains information such as terminal class and media supported. |
| [**ITTerminalSupport**](https://msdn.microsoft.com/en-us/library/ms733156(v=VS.85).aspx)                   | Gets information on available terminals and creates additional terminals.                               |
| [Provider-Specific Interfaces](provider-specific-interfaces.md) | Service provider dependent.                                                                             |



 

 

 



