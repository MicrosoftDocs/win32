---
Description: The application must inventory the communications resources available to it, then notify TAPI about which resources it will use and how it will use them.
ms.assetid: 2246c4d2-f8ca-4950-adc6-af9a6e214fe9
title: Resource Inventory
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Resource Inventory

The application must inventory the communications resources available to it, then notify TAPI about which resources it will use and how it will use them. See [Device Control](device-control.md) for additional information on the types of resources and capabilities an application might access.

**TAPI 2.x:** Applications get the number of available lines when [**lineInitializeEx**](https://msdn.microsoft.com/en-us/library/ms735983(v=VS.85).aspx) returns. They can then perform [**lineGetDevCaps**](https://msdn.microsoft.com/en-us/library/ms735735(v=VS.85).aspx) on each line, [**lineGetAddressCaps**](https://msdn.microsoft.com/en-us/library/ms735674(v=VS.85).aspx) for each address, and [**lineOpen**](https://msdn.microsoft.com/en-us/library/ms736005(v=VS.85).aspx) for each line that will be used.

**TAPI 3.x:** Applications use [**ITTAPI::EnumerateAddresses**](/windows/desktop/api/tapi3if/nf-tapi3if-ittapi-enumerateaddresses) or [**ITTAPI::get\_Addresses**](/windows/desktop/api/tapi3if/nf-tapi3if-ittapi-get_addresses) to discover the addresses available. [**ITMediaSupport**](/windows/desktop/api/tapi3if/nn-tapi3if-itmediasupport) and [**ITAddressCapabilities**](/windows/desktop/api/tapi3if/nn-tapi3if-itaddresscapabilities) supply information on communication types possible for each address. If implemented by the service provider, [**ITTerminalSupport**](https://msdn.microsoft.com/en-us/library/ms733156(v=VS.85).aspx) gives an application access to additional information and controls.

 

 



