---
description: A Telephony Service Provider (TSPI) handles device-specific controls for communications programming.
ms.assetid: da54e219-9adb-4a12-baab-52f2b2fb7c66
title: Telephony Service Provider Interface (TSPI)
ms.topic: article
ms.date: 05/31/2018
---

# Telephony Service Provider Interface (TSPI)

A Telephony Service Provider (TSPI) handles device-specific controls for communications programming. A TSP must conform to the Telephony Service Provider (TSPI) in order to function as a service provider within the Microsoft Telephony environment. TSPI defines the external functions exposed by a telephony service provider supplied with communications equipment.

A TSP author must be familiar with the material in [Microsoft Telephony Overview](./microsoft-telephony-overview.md), which covers general telephony architecture and provides an overview of material common to several telephony APIs. For example, this section contains a list of session control operations, such as Park, with descriptions of each operation and jumps to related TAPI 2.2, TAPI 3, and TSPI programming elements.

The following overviews cover material specific to the needs of a TSP author. Please note that the most difficult parts of writing a TSP are device-and operating-system-specific details, which are outside the scope of this document.

The TSPI overview is divided into the following sections:

-   [General Programming Considerations](/previous-versions/windows/desktop/legacy/ms725196(v=vs.85)) covers DLL requirements, proper handling of versions, error checks performed by TAPI, a summary of how TSPI functions correspond to TAPI 2.2 (TAPI/C) functions, and a discussion of levels of service as expressed in TSPI.
-   The [Life Cycle of a Telephony Service Provider](life-cycle-of-a-telephony-service-provider.md) contains a high-level summary of a TSP's operational phases.
-   [Device Access](/previous-versions/windows/desktop/legacy/ms725183(v=vs.85)) covers the basics of how a TSP exposes device information and controls to TAPI.
-   [Session Access](/previous-versions/windows/desktop/legacy/ms725266(v=vs.85)) covers what TAPI expects of a TSP during a communications session.
-   [Media Access](/previous-versions/windows/desktop/legacy/ms725240(v=vs.85)) provides a limited set of controls over media streams. Much finer control is possible through use of a media service provider, and service provider authors should use this API whenever feasible. The TSPI provides for communications between a TSP/MSP pair.
-   [Phone Devices](/previous-versions/windows/desktop/legacy/ms725257(v=vs.85)) covers the supplemental information and operations exposed if a TSP handles phone set control. These operations are optional.
-   [The Telephony Service Provider UI DLL Interface](the-telephony-service-provider-ui-dll-interface.md) cover special functions that can be implemented to allow a user to directly set many aspects of a TSP's functionality.

Please see the [TSPI Reference](tspi-reference.md) for details of the TSPI programming elements.

 

 
