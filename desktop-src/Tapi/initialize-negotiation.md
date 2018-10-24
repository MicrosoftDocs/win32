---
Description: The INITIALIZE\_NEGOTIATION datatype is a special value of type DWORD.
ms.assetid: ce978913-47a1-4387-bd1b-1795aaf82dd7
title: INITIALIZE_NEGOTIATION
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# INITIALIZE\_NEGOTIATION

The **INITIALIZE\_NEGOTIATION** datatype is a special value of type **DWORD**. It can be passed as the *dwDeviceID* parameter in the [**TSPI\_lineNegotiateTSPIVersion**](https://msdn.microsoft.com/en-us/library/ms725582(v=VS.85).aspx) and [**TSPI\_phoneNegotiateTSPIVersion**](https://msdn.microsoft.com/en-us/library/ms725940(v=VS.85).aspx) functions. Doing so indicates that TAPI can negotiate a TSPI interface version number independent of any specific devices.

 

 



