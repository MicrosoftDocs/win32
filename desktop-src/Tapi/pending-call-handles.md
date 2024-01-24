---
description: A service provider is required to create one or more call handles (variables of type HDRVCALL) whenever TAPI calls one of the following functions.
ms.assetid: 0a9d9afd-9786-4d9e-b0a2-12c9a1e13887
title: Pending Call Handles
ms.topic: article
ms.date: 05/31/2018
---

# Pending Call Handles

A service provider is required to create one or more call handles (variables of type [HDRVCALL](hdrvline.md)) whenever TAPI calls one of these functions: [**TSPI\_lineMakeCall**](/windows/win32/api/tspi/nf-tspi-tspi_linemakecall), [**TSPI\_lineCompleteTransfer**](/windows/win32/api/tspi/nf-tspi-tspi_linecompletetransfer), [**TSPI\_lineForward**](/windows/win32/api/tspi/nf-tspi-tspi_lineforward), [**TSPI\_linePickup**](/windows/win32/api/tspi/nf-tspi-tspi_linepickup), [**TSPI\_linePrepareAddToConference**](/windows/win32/api/tspi/nf-tspi-tspi_lineprepareaddtoconference), [**TSPI\_lineSetupConference**](/windows/win32/api/tspi/nf-tspi-tspi_linesetupconference), [**TSPI\_lineSetupTransfer**](/windows/win32/api/tspi/nf-tspi-tspi_linesetuptransfer), and [**TSPI\_lineUnpark**](/windows/win32/api/tspi/nf-tspi-tspi_lineunpark). When a service provider receives such a call, the service provider must set the variable supplied by TAPI to the value of the handle before returning from the call. TAPI considers this "pending call handle" to be tentatively valid. When the service provider actually creates the call, it must call the [**ASYNC\_COMPLETION**](/windows/win32/api/tspi/nc-tspi-async_completion) callback to formally validate the handle.

If TAPI calls the [**TSPI\_lineCloseCall**](/windows/win32/api/tspi/nf-tspi-tspi_lineclosecall) function before the service provider formally validates a pending call handle, the service provider must stop all further processing associated with the call handle and call the [**ASYNC\_COMPLETION**](/windows/win32/api/tspi/nc-tspi-async_completion) callback function using the error value LINEERR\_OPERATIONFAILED.

 

 
