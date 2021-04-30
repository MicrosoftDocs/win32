---
description: As part of the phone device abstraction defined by TSPI, TAPI and the service provider must first undergo basic initialization.
ms.assetid: cd8bb328-fbd0-409c-8471-34ad4c2c8d93
title: Phone SPI Initialization
ms.topic: article
ms.date: 05/31/2018
---

# Phone SPI Initialization

As part of the phone device abstraction defined by TSPI, TAPI and the service provider must first undergo basic initialization. This basic initialization is accomplished both for the line and phone halves of the interface by the same set of steps. The first of these steps is interface version negotiation. TAPI performs this by calling the [**TSPI\_lineNegotiateTSPIVersion**](/windows/win32/api/tspi/nf-tspi-tspi_linenegotiatetspiversion) function. This function is usually used to negotiate on behalf of an individual line device; different line devices within the same service provider may operate according to different interface versions. TAPI passes a special reserved device identifier value, [**INITIALIZE\_NEGOTIATION**](initialize-negotiation.md), to indicate that it is negotiating an overall interface version for initialization functions that affect the entire service provider, both for lines and phones.

The result of this negotiation is passed to subsequent procedures until a phone device is opened. At that time, the phone device becomes committed to a particular interface version. This interface version is implicit until the phone is closed, and does not need to be passed to subsequent functions that operate on an opened phone.

Following overall interface version negotiation, TAPI calls the [**TSPI\_providerInit**](/windows/win32/api/tspi/nf-tspi-tspi_providerinit) function. This function initializes the service provider, also giving it parameters required for subsequent operation. These parameters include the following:

-   *dwPermanentProviderID*: Specifies the permanent identifier of the service provider being initialized, unique within the service providers on this system.
-   *dwLineDeviceIDBase*: Specifies the lowest device identifier for the line devices supported by this service provider.
-   *dwPhoneDeviceIDBase*: Specifies the lowest device identifier for the phone devices supported by this service provider. Devices of the telephony phone device class are identified by integers starting from zero. This range of identifiers is contiguous across the full range of phone devices. Because there may be multiple service providers managing phone devices in a single system, each service provider gets a contiguous portion of the total range. This parameter tells the service provider the lowest value in its portion of the range. The service provider, rather than TAPI, is responsible for mapping this variable range to its own internal device identifiers. This gives the service-provider vendor sufficient flexibility to use device identifiers in device-specific extensions if it wants. Because the service provider knows what device identifiers appear in TAPI-defined parameters and data structures, it can use consistent device identifiers in device-specific extension parameters and data structures.
-   *dwNumLines*: Specifies how many line devices this service provider supports.
-   *dwNumPhones*: Specifies how many phone devices this service provider supports.
-   *lpfnCompletionProc*: Specifies the procedure the service provider calls to report completion of all asynchronously operating procedures on line and phone devices.

Following [**TSPI\_providerInit**](/windows/win32/api/tspi/nf-tspi-tspi_providerinit), normal operations such as opening phones can be carried out.

 

 
