---
Description: There are nine asynchronous operations related to phones.
ms.assetid: b255bdde-1677-401f-b02d-4850e0e98dc4
title: Asynchronous Phone Operations
ms.topic: article
ms.date: 05/31/2018
---

# Asynchronous Phone Operations

There are nine asynchronous operations related to phones. These are initiated by the [**TSPI\_phoneDevSpecific**](https://msdn.microsoft.com/library/ms725925(v=VS.85).aspx), [**TSPI\_phoneSetButtonInfo**](https://msdn.microsoft.com/library/ms725943(v=VS.85).aspx), [**TSPI\_phoneSetData**](https://msdn.microsoft.com/library/ms725944(v=VS.85).aspx), [**TSPI\_phoneSetDisplay**](https://msdn.microsoft.com/library/ms725945(v=VS.85).aspx), [**TSPI\_phoneSetGain**](https://msdn.microsoft.com/library/ms725946(v=VS.85).aspx), [**TSPI\_phoneSetHookSwitch**](https://msdn.microsoft.com/library/ms725947(v=VS.85).aspx), [**TSPI\_phoneSetLamp**](https://msdn.microsoft.com/library/ms725948(v=VS.85).aspx), [**TSPI\_phoneSetRing**](https://msdn.microsoft.com/library/ms725949(v=VS.85).aspx), and [**TSPI\_phoneSetVolume**](https://msdn.microsoft.com/library/ms725951(v=VS.85).aspx) functions. If an application calls the TAPI [**phoneClose**](https://msdn.microsoft.com/library/ms736605(v=VS.85).aspx) function and has the only handle to the phone, TAPI calls the [**TSPI\_phoneClose**](https://msdn.microsoft.com/library/ms725923(v=VS.85).aspx) function to direct the service provider to terminate the asynchronous operations and call the [*Completion\_Proc*](https://msdn.microsoft.com/library/ms725180(v=VS.85).aspx) callback function as appropriate. If the application does not have the only handle to the phone, the service provider receives no notification of the request and any outstanding asynchronous operations remain active.

 

 



