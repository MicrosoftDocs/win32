---
description: There are nine asynchronous operations related to phones.
ms.assetid: b255bdde-1677-401f-b02d-4850e0e98dc4
title: Asynchronous Phone Operations
ms.topic: article
ms.date: 05/31/2018
---

# Asynchronous Phone Operations

There are nine asynchronous operations related to phones. These are initiated by the [**TSPI\_phoneDevSpecific**](/windows/win32/api/tspi/nf-tspi-tspi_phonedevspecific), [**TSPI\_phoneSetButtonInfo**](/windows/win32/api/tspi/nf-tspi-tspi_phonesetbuttoninfo), [**TSPI\_phoneSetData**](/windows/win32/api/tspi/nf-tspi-tspi_phonesetdata), [**TSPI\_phoneSetDisplay**](/windows/win32/api/tspi/nf-tspi-tspi_phonesetdisplay), [**TSPI\_phoneSetGain**](/windows/win32/api/tspi/nf-tspi-tspi_phonesetgain), [**TSPI\_phoneSetHookSwitch**](/windows/win32/api/tspi/nf-tspi-tspi_phonesethookswitch), [**TSPI\_phoneSetLamp**](/windows/win32/api/tspi/nf-tspi-tspi_phonesetlamp), [**TSPI\_phoneSetRing**](/windows/win32/api/tspi/nf-tspi-tspi_phonesetring), and [**TSPI\_phoneSetVolume**](/windows/win32/api/tspi/nf-tspi-tspi_phonesetvolume) functions. If an application calls the TAPI [**phoneClose**](/windows/win32/api/tapi/nf-tapi-phoneclose) function and has the only handle to the phone, TAPI calls the [**TSPI\_phoneClose**](/windows/win32/api/tspi/nf-tspi-tspi_phoneclose) function to direct the service provider to terminate the asynchronous operations and call the [*Completion\_Proc*](/windows/win32/api/tspi/nc-tspi-async_completion) callback function as appropriate. If the application does not have the only handle to the phone, the service provider receives no notification of the request and any outstanding asynchronous operations remain active.

 

 
