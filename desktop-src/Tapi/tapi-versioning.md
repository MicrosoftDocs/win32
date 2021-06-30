---
description: Learn about TAPI versioning. Over time, different versions of TAPI, applications, and service providers may be produced.
ms.assetid: 35fea8f9-307e-4429-b4ec-ffb5c62c2610
title: TAPI Versioning
ms.topic: article
ms.date: 05/31/2018
---

# TAPI Versioning

Over time, different versions of TAPI, applications, and service providers may be produced. These new versions can make new definitions, such as for new features, new members in data structures, and new bit fields. Version numbers are therefore necessary to indicate how to interpret various data structures.

To allow optimal interoperability of different versions of applications, versions of TAPI itself, and versions of service providers by different vendors, Microsoft Telephony provides a simple version negotiation mechanism for applications. There are two different versions that TAPI and the telephony service provider need to agree on for each line device. The first is the version negotiated with TAPI and the telephony service provider (TSP) Basic and Supplementary Telephony, referred to as the TAPI interface version. The other is for provider-specific extensions, if any, and is referred to as the extension version. The format of the data structures and data types used by TAPI's Basic and Supplementary features is defined by the TAPI version, while the extension version determines the format of data structures defined by the vendor-specific extensions.

The [**lineNegotiateAPIVersion**](/windows/desktop/api/Tapi/nf-tapi-linenegotiateapiversion) function negotiates a TAPI version and [**lineNegotiateExtVersion**](/windows/desktop/api/Tapi/nf-tapi-linenegotiateextversion) negotiates the TSP extension version. A single TSP could be capable of handling more than one version, and an application must "fall back" to using an older version if using an older TSP. In **lineNegotiateAPIVersion** the *dwApiVersion* parameter defaults to a value according to version, as follows.



| TAPI version | Default value |
|--------------|---------------|
| 1.3          | 0x00010003    |
| 1.4          | 0x00010004    |
| 2.0          | 0x00020000    |
| 2.1          | 0x00020001    |
| 2.2          | 0x00020002    |



 

However, TAPI makes this much easier as long as the TSP itself is using a newer version than the application. If the TSP is indeed newer, then TAPI is capable of translating "down" to the application's version. For example, TAPI 2.0 TSPs do not need to be specifically capable of dealing with TAPI version 1.4. If a TAPI 1.4 application is run, TAPI converts all TAPI 2.0 structures and messages into TAPI 1.4 equivalents, or as close as possible. If there is no close approximation in TAPI 1.4, then all TAPI 2.0-specific information will be lost.

The precise meaning of an extension version is provider-specific. To use a TSP that supports extensions, consult the provider's documentation.

There are a number of versions of TAPI. While most of these versions involved changes to the TAPI and Telephony Service Provider Interface (TSPI) documentation sets, there are other implications for each version, namely, architectural differences, operating system variations, redistributables, and TSP development issues.



| TAPI version        | Distribution                                                   |
|---------------------|----------------------------------------------------------------|
| 1.0 – 1.2           | Beta versions that should not be used any longer.              |
| [1.4](tapi-1-4.md) | Included in Windows 95.                                        |
| [1.5](tapi-1-5.md) | Included in Windows CE 1.0.                                    |
| [2.0](tapi-2-0.md) | Included in Windows NT 4.0 with SP3.                           |
| [2.1](tapi-2-1.md) | Included in Windows NT 4.0 with SP4 and Windows 98.            |
| [2.2](tapi-2-2.md) | Included in Windows Server 2003, Windows XP, and Windows 2000. |



 

 

 



