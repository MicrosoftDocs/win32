---
description: The TSPI specification is very closely related to the specifications for TAPI 2.2 (TAPI/C).
ms.assetid: 2c51f7e3-c741-4736-9611-2327d65b427e
title: Overall Comparison with TAPI
ms.topic: article
ms.date: 05/31/2018
---

# Overall Comparison with TAPI

The TSPI specification is very closely related to the specifications for TAPI 2.2 (TAPI/C). Most of the functions in one have a corresponding function in the other. The usual correspondence is as follows:

-   TSPI functions have the same names as TAPI functions except that they are prepended with "**TSPI\_**". For example, the TAPI function [**lineAccept**](/windows/win32/api/tapi/nf-tapi-lineaccept) corresponds to the TSPI function [**TSPI\_lineAccept**](/windows/win32/api/tspi/nf-tspi-tspi_lineaccept).
-   Procedures that allow asynchronous operation insert a *dwRequestID* parameter of type [DRV\_REQUESTID](drv-requestid.md) as their first parameter. This parameter specifies the value to be returned to indicate asynchronous operation and to report asynchronous completion.
-   *hCall* parameters of type HCALL are replaced with *hdCall* parameters of type [HDRVCALL](hdrvline.md), indicating the service provider's handle for the call.
-   *hLine* parameters of type HLINE are replaced with *hdLine* parameters of -type [HDRVLINE](hdrvline.md), indicating the service provider's handle for the line.
-   *hPhone* parameters of type HPHONE are replaced with *hdPhone* parameters of type [HDRVPHONE](hdrvphone.md), indicating the service provider's handle for the phone.
-   Procedures that create a new call, such as [**TSPI\_lineMakeCall**](/windows/win32/api/tspi/nf-tspi-tspi_linemakecall), replace a single *lphCall* parameter with two parameters: an *htCall* of type [HTAPICALL](htapicall.md) parameter that passes in the TAPI handle for the call, and an *lphdCall* of type LPHDRVCALL that indicates the location to which the service provider must write its new handle for the call. A similar split of parameters occurs in [**TSPI\_lineOpen**](/windows/win32/api/tspi/nf-tspi-tspi_lineopen) and [**TSPI\_phoneOpen**](/windows/win32/api/tspi/nf-tspi-tspi_phoneopen).
-   At the TSPI level, there is no notion of "privilege" associated with device handles. Furthermore, at the API level, each application that has a device or call handle has a different handle, but TAPI merges these into a single handle in the service provider side. As a consequence, the error codes and status messages relating to privilege and number of clients using a device do not appear at the TSPI level.

The set of TAPI functions do not map one to one onto the set of TSPI functions. In particular, functions related to privilege, phone number translation, and interapplication communication are handled by TAPI and have no corresponding function in TSPI. Other functions, such as those used for service-provider configuration and initialization, have no corresponding functions in TAPI.

 

 
