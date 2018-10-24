---
Description: A service provider is required to create one or more call handles (variables of type HDRVCALL) whenever TAPI calls one of the following functions.
ms.assetid: 0a9d9afd-9786-4d9e-b0a2-12c9a1e13887
title: Pending Call Handles
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Pending Call Handles

A service provider is required to create one or more call handles (variables of type [HDRVCALL](hdrvline.md)) whenever TAPI calls one of these functions: [**TSPI\_lineMakeCall**](https://msdn.microsoft.com/en-us/library/ms725576(v=VS.85).aspx), [**TSPI\_lineCompleteTransfer**](https://msdn.microsoft.com/en-us/library/ms725535(v=VS.85).aspx), [**TSPI\_lineForward**](https://msdn.microsoft.com/en-us/library/ms725546(v=VS.85).aspx), [**TSPI\_linePickup**](https://msdn.microsoft.com/en-us/library/ms725585(v=VS.85).aspx), [**TSPI\_linePrepareAddToConference**](https://msdn.microsoft.com/en-us/library/ms725586(v=VS.85).aspx), [**TSPI\_lineSetupConference**](https://msdn.microsoft.com/en-us/library/ms725608(v=VS.85).aspx), [**TSPI\_lineSetupTransfer**](https://msdn.microsoft.com/en-us/library/ms725609(v=VS.85).aspx), and [**TSPI\_lineUnpark**](https://msdn.microsoft.com/en-us/library/ms725613(v=VS.85).aspx). When a service provider receives such a call, the service provider must set the variable supplied by TAPI to the value of the handle before returning from the call. TAPI considers this "pending call handle" to be tentatively valid. When the service provider actually creates the call, it must call the [**ASYNC\_COMPLETION**](https://msdn.microsoft.com/en-us/library/ms725180(v=VS.85).aspx) callback to formally validate the handle.

If TAPI calls the [**TSPI\_lineCloseCall**](https://msdn.microsoft.com/en-us/library/ms725532(v=VS.85).aspx) function before the service provider formally validates a pending call handle, the service provider must stop all further processing associated with the call handle and call the [**ASYNC\_COMPLETION**](https://msdn.microsoft.com/en-us/library/ms725180(v=VS.85).aspx) callback function using the error value LINEERR\_OPERATIONFAILED.

 

 



