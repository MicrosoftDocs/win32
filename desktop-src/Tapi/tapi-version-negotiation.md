---
description: Over time, different versions may exist for TAPI, applications, and service providers for a line or phone.
ms.assetid: 36a17ae8-31db-4db9-a401-097d47aa26ad
title: TAPI Version Negotiation
ms.topic: article
ms.date: 05/31/2018
---

# TAPI Version Negotiation

Over time, different versions may exist for TAPI, applications, and service providers for a line or phone. New versions may define new features, new fields to data structures, and so on. Version numbers therefore indicate how to interpret various data structures.

To allow optimal interoperability of different versions of applications, versions of TAPI itself, and versions of service providers by different vendors, TAPI provides a simple, two-step version negotiation mechanism for applications. Two different versions must be agreed on by the application, TAPI, and the service provider for each line device. The first is the version number for Basic and Supplementary Telephony and is referred to as the API version. The other is for provider-specific extensions, if any, and is referred to as the extension version. The format of the data structures and datatypes used by TAPI's basic and supplementary features is defined by the API version, while the extension version determines the format of the data structures defined by the vendor-specific extensions.

Version negotiation proceeds in two phases. In the first phase, the API version number is negotiated and the extension identifier associated with any vendor-specific extensions supported on the device is obtained. In the second phase, the extension version is negotiated. If the application does not use any API extensions, it skips the second phase and extensions are not activated by the service provider. If the application does want to use extensions, but the service provider's extensions (the extension identifier) are not recognized by the application, the application should skip the negotiation for extension version as well. Each vendor has its own set of legal (recognized) versions for each set of extension specifications it distributes.

The [**lineNegotiateAPIVersion**](/windows/desktop/api/Tapi/nf-tapi-linenegotiateapiversion) function is used to negotiate the API version number to use. It also retrieves the extension identifier supported by the line device, returning zeros if no extensions are supported. With this function call, the application provides the API version range it is compatible with. TAPI in turn negotiates with the line's service provider to determine which API version range it supports. TAPI next selects a version number (typically, although not necessarily, the highest version number) in the overlapping version range that the application, the DLL, and the service provider have supplied. This number is returned to the application, along with the extension identifier that defines the extensions available from that line's service provider.

If the application wants to use the extensions defined by the returned extension identifier, it must first call [**lineNegotiateExtVersion**](/windows/desktop/api/Tapi/nf-tapi-linenegotiateextversion) to negotiate the extension version. In a similar negotiation phase, the application specifies the already agreed-upon API version and the extension version range it supports. TAPI passes this information to the service provider for the line. The service provider checks the API version and the extension version range against its own, and selects the appropriate extension version number, if one exists.

When the application later calls [**lineGetDevCaps**](/windows/desktop/api/Tapi/nf-tapi-linegetdevcaps), it returns a set of device capabilities for the line that correspond to the results of version negotiation. These include the line's device capabilities consistent with the API version and the line's device-specific capabilities consistent with the extension version. The application must specify both of these version numbers when it opens a line. At that point, the application, the DLL, and the service provider are committed to using the agreed-upon versions. If device-specific extensions are not to be used, the extension version should be specified as zero.

In an environment where multiple applications open the same line device, the first application to open the line device selects the versions for all future applications that want to use the line (service providers do not support multiple versions simultaneously.) Similarly, an application that opens multiple line devices may find it easier to operate all line devices under the same API version number.

Every function that takes a *dwAPIVersion* or similar parameter must set this parameter to either the highest API version supported by the application or the API version negotiated using the [**lineNegotiateAPIVersion**](/windows/desktop/api/Tapi/nf-tapi-linenegotiateapiversion) or [**phoneNegotiateAPIVersion**](/windows/desktop/api/Tapi/nf-tapi-phonenegotiateapiversion) function on a particular device. Use the following table as a guide:



| Function                                                     | Meaning                                                                               |
|--------------------------------------------------------------|---------------------------------------------------------------------------------------|
| [**lineGetAddressCaps**](/windows/desktop/api/Tapi/nf-tapi-linegetaddresscaps)             | Use version returned by [**lineNegotiateAPIVersion**](/windows/desktop/api/Tapi/nf-tapi-linenegotiateapiversion).   |
| [**lineGetCountry**](/windows/desktop/api/Tapi/nf-tapi-linegetcountry)                     | Use highest version supported by the application.                                     |
| [**lineGetDevCaps**](/windows/desktop/api/Tapi/nf-tapi-linegetdevcaps)                     | Use version returned by [**lineNegotiateAPIVersion**](/windows/desktop/api/Tapi/nf-tapi-linenegotiateapiversion).   |
| [**lineGetProviderList**](/windows/desktop/api/Tapi/nf-tapi-linegetproviderlist)           | Use highest version supported by the application.                                     |
| [**lineGetTranslateCaps**](/windows/desktop/api/Tapi/nf-tapi-linegettranslatecaps)         | Use highest version supported by the application.                                     |
| [**lineNegotiateAPIVersion**](/windows/desktop/api/Tapi/nf-tapi-linenegotiateapiversion)   | Use highest version supported by the application.                                     |
| [**lineNegotiateExtVersion**](/windows/desktop/api/Tapi/nf-tapi-linenegotiateextversion)   | Use version returned by [**lineNegotiateAPIVersion**](/windows/desktop/api/Tapi/nf-tapi-linenegotiateapiversion).   |
| [**lineOpen**](/windows/desktop/api/Tapi/nf-tapi-lineopen)                                 | Use version returned by [**lineNegotiateAPIVersion**](/windows/desktop/api/Tapi/nf-tapi-linenegotiateapiversion).   |
| [**lineTranslateAddress**](/windows/desktop/api/Tapi/nf-tapi-linetranslateaddress)         | Use highest version supported by the application.                                     |
| [**lineTranslateDialog**](/windows/desktop/api/Tapi/nf-tapi-linetranslatedialog)           | Use highest version supported by the application.                                     |
| [**phoneGetDevCaps**](/windows/desktop/api/Tapi/nf-tapi-phonegetdevcaps)                   | Use version returned by [**phoneNegotiateAPIVersion**](/windows/desktop/api/Tapi/nf-tapi-phonenegotiateapiversion). |
| [**phoneNegotiateAPIVersion**](/windows/desktop/api/Tapi/nf-tapi-phonenegotiateapiversion) | Use highest version supported by the application.                                     |
| [**phoneNegotiateExtVersion**](/windows/desktop/api/Tapi/nf-tapi-phonenegotiateextversion) | Use version returned by [**phoneNegotiateAPIVersion**](/windows/desktop/api/Tapi/nf-tapi-phonenegotiateapiversion). |
| [**phoneOpen**](/windows/desktop/api/Tapi/nf-tapi-phoneopen)                               | Use version returned by [**phoneNegotiateAPIVersion**](/windows/desktop/api/Tapi/nf-tapi-phonenegotiateapiversion). |



 

> [!IMPORTANT]
> When negotiating an API version, always set the high and low version numbers to the range of versions that your application can support. For example, never use 0x00000000 for the low version or 0xFFFFFFFF for the high because these values require that your application support all versions of TAPI, both past and future.

 

 

 



