---
description: This document describes the design and use of the MSP Base Classes. Use of these classes is not required but most developers will find they simplify the task of building a DirectShow based MSP for TAPI 3s new MSPI.
ms.assetid: 97597dcf-eb18-47aa-b0ed-a43286d5d134
title: TAPI 3 MSP Base Classes
ms.topic: article
ms.date: 05/31/2018
---

# TAPI 3 MSP Base Classes

This document describes the design and use of the MSP Base Classes. Use of these classes is not required, but most developers will find they simplify the task of building a DirectShow-based MSP for TAPI 3's new MSPI.

Source code for the MSP base classes can be found in the Samples directory of the Platform Software Development Kit (SDK).

Familiarity with COM, ATL, DirectShow, and C++ is assumed. The reader must also know the general material in [About the Media Service Provider (MSP)](about-the-media-service-provider-msp-.md) and in [Media Service Provider Interface (MSPI)](media-service-provider-interface-mspi-.md).

ATL 2.1 is required for Windows 2000. Starting with Windows XP, both ATL 2.1 and 3.0 will compile.

MSP Base Class Libraries (available in the SDK):

-   Mspbase.lib
-   Mspid.lib
-   Strmbase.lib
-   Tmuid.lib
    > [!Note]  
    > Dynamic rather than static linking should be used.

     

MSP Base Class Header Files (available in the SDK):

-   Mspaddr.h
-   Mspbase.h
-   Mspcall.h
-   Msplog.h
-   Mspstrm.h
-   Mspterm.h
-   Mspthrd.h
-   Msptmac.h
-   Msptmvc.h
-   Msptrmvc.h
-   Msptrmac.h
-   Msptrmar.h
-   Msputils.h

MSP Base Class Source Files (available in the SDK Samples):

-   Mspaddr.cpp
-   Mspcall.cpp
-   Msplog.cpp
-   Mspstrm.cpp
-   Mspterm.cpp
-   Mspthrd.cpp
-   Msptrmac.cpp
-   Msptrmar.cpp
-   Msptrmvc.cpp
-   Msputils.cpp

 

 



