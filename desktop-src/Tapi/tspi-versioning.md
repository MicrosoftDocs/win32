---
description: Over time, different versions of TAPI, applications, and service providers may be produced.
ms.assetid: 994fad0e-5958-4d93-8952-9db2bbe01f44
title: TSPI Versioning
ms.topic: article
ms.date: 05/31/2018
---

# TSPI Versioning

Over time, different versions of TAPI, applications, and service providers may be produced. These new versions can make new definitions, such as for new features, new members in data structures, and new bit fields. Version numbers are therefore necessary to indicate how to interpret various data structures.

To allow optimal interoperability of different versions of applications, versions of TAPI itself, and versions of service providers by different vendors, Microsoft Telephony provides a simple version negotiation mechanism for applications. There are two different versions that need to be agreed on by TAPI and the telephony service provider for each line device. The first is the version number for the Basic and Supplementary Telephony SPI, referred to as the *TSPI interface version*. The other is for provider-specific extensions, if any, and is referred to as the *extension version*. The format of the data structures and datatypes used by TSPI's Basic and Supplementary features is defined by the TSPI version, while the extension version determines the format of data structures defined by the vendor-specific extensions.

These two types of version negotiation are handled by two different procedures: [**TSPI\_lineNegotiateTSPIVersion**](/windows/win32/api/tspi/nf-tspi-tspi_linenegotiatetspiversion) is used to negotiate the TSPI interface version, and [**TSPI\_lineNegotiateExtVersion**](/windows/win32/api/tspi/nf-tspi-tspi_linenegotiateextversion) is used to negotiate the extension version. Extension version negotiation can be skipped if extensions are not wanted. If these ranges input during negotiation overlap, the service provider must return a value within the overlapping portion of the range as the result of the negotiation. Usually, this should be the highest possible value. If the ranges do not overlap, the two parties are incompatible and the function returns an error.

Results of a negotiation simply indicate that the service provider is willing to operate at a particular version number, but do not commit the service provider to doing so. For example, TAPI can renegotiate to determine an ideal version after having negotiated a possible version. The TSPI interface version is only committed when a line is opened using [**TSPI\_lineOpen**](/windows/win32/api/tspi/nf-tspi-tspi_lineopen) and survives until the device is closed. The extension version is committed when the [**TSPI\_lineSelectExtVersion**](/windows/win32/api/tspi/nf-tspi-tspi_lineselectextversion) function is called, and survives until the selection is canceled by selecting extension version zero.

Extension version selection can happen many times, including while an extension version is in effect. Because the service provider is committed to the extension version, its range of supported versions narrows to exactly that extension version. For example, consider a service provider that is normally compatible with extension versions 1.0 through 5.5. If version 3.0 is in effect while a caller attempts to negotiate a version within the range 1.0 to 5.5, the negotiation returns 3.0.

Because TAPI negotiates the version, you can upgrade a service provider to new versions of the interface without requiring that TAPI also be upgraded. Similarly, TAPI can be upgraded, yet still use your older service provider.

 

 
