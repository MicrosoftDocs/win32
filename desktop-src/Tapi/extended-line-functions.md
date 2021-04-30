---
description: Extended line services (or device-specific line services) include all service-provider defined extensions to the API.
ms.assetid: 0f01509e-caa5-4f79-be78-36bd5f23c5d7
title: Extended Line Functions
ms.topic: article
ms.date: 05/31/2018
---

# Extended Line Functions

Extended line services (or device-specific line services) include all service-provider defined extensions to the API. The API defines a mechanism that enables service-provider vendors to extend TAPI using device-specific extensions. The API only defines the extension mechanism, and by doing so provides access to device-specific extensions, but the API does not define their behavior. Behavior is completely defined by the service provider.

TAPI consists of scalar and bit-flag constant definitions, data structures, functions, and messages. Procedures are defined that enable a vendor to extend most of these as follows.

For extensible scalar data constants, a service-provider vendor can define new values in a specified range. As most data constants are **DWORD**s, typically the range 0x00000000 through 0x7FFFFFFF is reserved for common future extensions, while 0x80000000 through 0xFFFFFFFF are available for vendor-specific extensions. The assumption is that a vendor would define values that are natural extensions of the data types defined by the API.

For extensible bit-flag data constants, a service-provider vendor can define new values for specified bits. As most bit-flag constants are **DWORD**s, typically a specific number of the lower bits are reserved for common extensions while the remaining upper bits are available for vendor-specific extensions. Common bit flags are assigned from bit zero up; vendor-specific extensions should be assigned from bit 31 down. This provides maximum flexibility in assigning bit positions to common extensions versus vendor-specific extensions. A vendor is expected to define new values that are natural extensions of the bit flags defined by the API.

Extensible data structures have a variably sized field that is reserved for device-specific use. Being variably sized, the service provider decides the amount of information and the interpretation. A vendor that defines a device-specific field is expected to make these natural extensions of the original data structure defined by the API.

Two functions, [**lineDevSpecific**](/windows/desktop/api/Tapi/nf-tapi-linedevspecific) and [**lineDevSpecificFeature**](/windows/desktop/api/Tapi/nf-tapi-linedevspecificfeature), and two related messages, [**LINE\_DEVSPECIFIC**](line-devspecific.md) and [**LINE\_DEVSPECIFICFEATURE**](line-devspecificfeature.md), provide a vendor-specific extension mechanism. The **lineDevSpecific** function and associated LINE\_DEVSPECIFIC message enable an application to access device-specific line, address, or call features that are unavailable with the Basic or Supplementary Telephony services. The parameter profile of the **lineDevSpecific** function is generic in that little interpretation of the parameters is made by the API. The interpretation of the parameters is defined by the service provider and must be understood by an application that uses them. The parameters are simply passed through TAPI from the application to the service provider. An application that relies on device-specific extensions will not generally work with other service providers; however, applications written to the Basic and Supplementary Telephony services will work with the extended service provider.

For convenience, a more specialized escape function is also provided. It is similar to [**lineDevSpecific**](/windows/desktop/api/Tapi/nf-tapi-linedevspecific), but places interpretation on some of the parameters. This more specialized function is [**lineDevSpecificFeature**](/windows/desktop/api/Tapi/nf-tapi-linedevspecificfeature), a device-specific escape function to allow sending switch features to the switch. The message [**LINE\_DEVSPECIFICFEATURE**](line-devspecificfeature.md) is the device-specific message sent to the application as an indication of features sent to the switch. This function and its associated message allow an application to emulate button presses at the line's feature phone. As feature phones and the meanings of their buttons are vendor-specific, feature invocation using [**lineDevSpecificFeature**](/windows/desktop/api/Tapi/nf-tapi-linedevspecificfeature) is also vendor specific.

As mentioned earlier, there is no central registry for manufacturer identifiers. Instead, a unique identifier generator (EXTIDGEN) is made available.

 

 



