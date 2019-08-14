---
Description: This document outlines the interfaces that provide methods that allow an MSP to interact with the Microsoft Telephony environment and allow a TAPI 3 application to use an MSPs media controls.
ms.assetid: e67d4941-ce0f-48b9-8099-b62659ad33e0
title: Media Service Provider Interface (MSPI) Reference
ms.topic: article
ms.date: 05/31/2018
---

# Media Service Provider Interface (MSPI) Reference

This document outlines the interfaces that provide methods that allow an MSP to interact with the Microsoft Telephony environment and allow a TAPI 3 application to use an MSP's media controls.



| Media Service Provider Interface interfaces      | Description                                                                                                                                                                            | Required? |
|--------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| [**ITMSPAddress**](/windows/desktop/api/msp/nn-msp-itmspaddress)             | Exposed only to TAPI. Main MSP interface for the TAPI DLL. TAPI 3 calls **CoCreateInstance** on this interface to create the MSP object.                                               | Yes       |
| [**ITStream**](https://msdn.microsoft.com/en-us/library/ms732390(v=VS.85).aspx)                     | Exposed to applications. Provides methods that allow an application to retrieve information on a stream, to start, pause, or stop it, and to select or unselect terminals on a stream. | Yes       |
| [**ITStreamControl**](https://msdn.microsoft.com/en-us/library/ms732393(v=VS.85).aspx)       | Exposed to applications. Provides methods that allow an application to create or remove streams.                                                                                       | Yes       |
| [**IEnumStream**](/windows/desktop/api/tapi3if/nn-tapi3if-ienumstream)               | Exposed to applications. Enumerator interface for [**ITStream**](https://msdn.microsoft.com/en-us/library/ms732390(v=VS.85).aspx).                                                                                                        | Yes       |
| [**ITSubStream**](https://msdn.microsoft.com/en-us/library/ms732440(v=VS.85).aspx)               | Exposed to applications. Provides methods that allow an application to retrieve information on a substream, to start, pause, or stop it, and to select or unselect terminals.          | Optional  |
| [**ITSubStreamControl**](https://msdn.microsoft.com/en-us/library/ms732442(v=VS.85).aspx) | Exposed to applications. Provides methods that allow an application to create or remove substreams.                                                                                    | Optional  |
| [**IEnumSubStream**](/windows/desktop/api/tapi3if/nn-tapi3if-ienumsubstream)         | Exposed to applications. Enumerator interface for [**ITSubStream**](https://msdn.microsoft.com/en-us/library/ms732440(v=VS.85).aspx).                                                                                                  | Optional  |
| [**ITTerminal**](https://msdn.microsoft.com/en-us/library/ms732646(v=VS.85).aspx)                 | Exposed to applications. Gets information on the [Terminal object](terminal-object.md), such as terminal call and media supported.                                                    | Yes       |
| [**ITTerminalSupport**](https://msdn.microsoft.com/en-us/library/ms733156(v=VS.85).aspx)   | Exposed to applications. Provides methods to query on available terminals and create additional terminals.                                                                             | Yes       |
| [**ITTerminalSupport2**](/windows/desktop/api/tapi3if/nn-tapi3if-itterminalsupport2) | Exposed to applications. Retrieves information about pluggable terminal classes and superclasses; derives from the [**ITTerminalSupport**](https://msdn.microsoft.com/en-us/library/ms733156(v=VS.85).aspx) interface.           | Yes       |



 

## Media Service Provider Interface Types

-   [**MSP\_ADDRESS\_EVENT**](/windows/win32/api/msp/ne-msp-msp_address_event)
-   [**MSP\_CALL\_EVENT**](/windows/win32/api/msp/ne-msp-msp_call_event)
-   [**MSP\_EVENT**](/windows/win32/api/msp/ne-msp-msp_event)
-   [**MSP\_EVENT\_INFO**](/windows/win32/api/msp/ns-msp-msp_event_info)

## Related topics

<dl> <dt>

[Media Service Provider Interface (MSPI)](media-service-provider-interface-mspi-.md)
</dt> </dl>

 

 



