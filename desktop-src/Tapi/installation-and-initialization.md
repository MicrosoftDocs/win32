---
description: Installation of a new service provider is highly device- and operating-system-specific, so the details are outside the scope of this SDK.
ms.assetid: 5b48e144-5092-4462-b74c-d3295d23afe1
title: Installation and Initialization
ms.topic: article
ms.date: 05/31/2018
---

# Installation and Initialization

Installation of a new service provider is highly device- and operating-system-specific, so the details are outside the scope of this SDK. Generally speaking, the goal of installation is configuration of the service provider for the current communications environment. This usually involves registry entries and the setting of service dependencies.

Initialization of a telephony service provider starts with version negotiation. See [TSPI Versioning](tspi-versioning.md) for a discussion of version negotiation and current version.

TAPI then calls [**TSPI\_providerInit**](/windows/win32/api/tspi/nf-tspi-tspi_providerinit), which passes the provider a pointer to a callback function used to report on asynchronous functions progress. The TSP returns a count of line and phone devices associated with the current device identifier.

Typically, the next step will be resource inventory, conducted by TAPI invoking [**TSPI\_lineGetDevCaps**](/windows/win32/api/tspi/nf-tspi-tspi_linegetdevcaps) and [**TSPI\_lineGetAddressCaps**](/windows/win32/api/tspi/nf-tspi-tspi_linegetaddresscaps). The service provider is expected to fill in those elements of the data structures involved that pertain to device and session capabilities it supports.

TAPI collects information from the various applications concerning event notification requirements, and instructs the TSP using [**TSPI\_lineSetDefaultMediaDetection**](/windows/win32/api/tspi/nf-tspi-tspi_linesetdefaultmediadetection) to indicate which media types to detect for a line and [**TSPI\_lineSetStatusMessages**](/windows/win32/api/tspi/nf-tspi-tspi_linesetstatusmessages) to indicate which line and address events should be reported.

 

 
