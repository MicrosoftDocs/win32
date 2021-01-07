---
description: Extended line services (or device-specific line services) include all service-provider defined extensions to TSPI.
ms.assetid: 23519d23-27bd-422e-b3c4-00e0d0d93f9e
title: Extended Line Services
ms.topic: article
ms.date: 05/31/2018
---

# Extended Line Services

Extended line services (or device-specific line services) include all service-provider defined extensions to TSPI. TSPI defines a mechanism that enables service-provider vendors to extend the Telephony SPI using device-specific extensions. TSPI only defines the extension mechanism, and by doing so provides access to device-specific extensions, but TSPI does not define their behavior. Behavior is completely defined by the service provider.

The Telephony SPI consists of scalar and bit flag constant definitions, data structures, functions, and callback messages. Procedures are defined that enable a vendor to extend most of these as follows.

For extensible scalar data constants, a service-provider vendor can define new values in a specified range. As most data constants are **DWORD**s, typically the range 0x00000000 through 0x7FFFFFFF is reserved for common future extensions, while 0x80000000 through 0xFFFFFFFF are available for vendor-specific extensions. The assumption is that a vendor would define values that are natural extensions of the datatypes defined by TSPI.

For extensible bit flag data constants, a service-provider vendor can define new values for specified bits. As most bit flag constants are **DWORD**s, typically a specific number of the lower bits are reserved for common extensions while the remaining upper bits are available for vendor-specific extensions. Common bit flags are assigned from bit zero up; vendor-specific extensions should be assigned from bit 31 down. This provides maximum flexibility in assigning bit positions to common extensions versus vendor-specific extensions. A vendor is expected to define new values that are natural extensions of the bit flags defined by TSPI.

Extensible data structures have a variably sized field that is reserved for device-specific use. Being variably sized, the service provider decides the amount of information and the interpretation. A vendor that defines a device-specific field is expected to make these natural extensions of the original data structure defined by TSPI.

Two functions, [**TSPI\_lineDevSpecific**](/windows/win32/api/tspi/nf-tspi-tspi_linedevspecific) and [**TSPI\_lineDevSpecificFeature**](/windows/win32/api/tspi/nf-tspi-tspi_linedevspecificfeature), and four related messages, [**LINE\_DEVSPECIFIC**](/previous-versions/windows/desktop/legacy/ms725225(v=vs.85)), [**LINE\_CALLDEVSPECIFIC**](line-calldevspecific.md), [**LINE\_DEVSPECIFICFEATURE**](/previous-versions/windows/desktop/legacy/ms725227(v=vs.85)), and [**LINE\_CALLDEVSPECIFICFEATURE**](line-calldevspecificfeature.md), offer a vendor-specific extension mechanism. The **TSPI\_lineDevSpecific** operation and associated LINE\_DEVSPECIFIC and LINE\_CALLDEVSPECIFIC messages allow the Tapi32.dll client application to access device-specific line, address, or call features that are unavailable in the Basic or Supplementary Telephony services. The parameter profile of the [**TSPI\_lineDevSpecific**](/windows/win32/api/tspi/nf-tspi-tspi_linedevspecific) function is generic in that little interpretation of the parameters is made by TSPI. Device-handle parameters have TSPI-defined meanings and are translated appropriately between the application and the service provider. Generic parameters are simply passed through unmodified. The interpretation of the generic parameters is defined by the service provider and must be understood by any applications that use them. An application that relies on device-specific extensions generally does not work with other service providers. However, applications written entirely to the Basic and Supplementary Telephony services should work with the extended service provider.

The TAPI implementation of the device-specific functions and messages is "pass-through." TAPI does not examine or modify the generic device-specific parameters and buffers, but it does map application-level opaque handle values (used at the TAPI level) to service-provider-level opaque handle values (used at the TSPI level).

Regarding handle translation, the passthrough nature of the generic parts of device-specific extensions has an important consequence. A service provider has no way to relate the handles used at the TSPI level to those at the TAPI level except by passing them through the predefined handle parameters and fields. Any handle put into the generic extension area is untranslated by TAPI as it is passed between application and service provider. The designer of a service-provider extension should generally not define extensions that pass handles in this way.

The appropriate approach when defining a device-specific extension that must refer to specific devices without using handles is to refer to them using their absolute device identification. The device identifier used in opening a line at the TAPI level, for example, is strictly the same value that is used at the TSPI level to open the line. Similarly, a (line device identifier, address identifier) tuple that uniquely identifies an address at the TAPI level uses the same values to identify the same thing at the TSPI level.

For convenience, a more specialized escape function is also provided. It is similar to [**TSPI\_lineDevSpecific**](/windows/win32/api/tspi/nf-tspi-tspi_linedevspecific), but places interpretation on some of the parameters. The [**TSPI\_lineDevSpecificFeature**](/windows/win32/api/tspi/nf-tspi-tspi_linedevspecificfeature) function and associated [**LINE\_DEVSPECIFICFEATURE**](/previous-versions/windows/desktop/legacy/ms725227(v=vs.85)) and [**LINE\_CALLDEVSPECIFICFEATURE**](line-calldevspecificfeature.md) messages allow TAPI to emulate button presses at the line's feature phone. As feature phones and the meanings of their buttons are vendor-specific, feature invocation using **TSPI\_lineDevSpecificFeature** is also vendor specific.

To summarize, the [**TSPI\_lineDevSpecificFeature**](/windows/win32/api/tspi/nf-tspi-tspi_linedevspecificfeature) function is a device-specific escape function to allow sending switch features to the switch. The [**LINE\_CALLDEVSPECIFICFEATURE**](line-calldevspecificfeature.md) message is a device-specific message sent to the application's callback as an indication of call-related features sent to the switch. [**LINE\_DEVSPECIFICFEATURE**](/previous-versions/windows/desktop/legacy/ms725227(v=vs.85)) is a device-specific message sent to the application's callback as an indication of line-related features sent to the switch.

There is no central registry for manufacturer identifiers. Instead a unique identifier generator called Extidgen.exe is made available as part of TSPI. The vendor that designs a set of device-specific extensions uses this utility to obtain a unique identifier for those extensions.

 

 
