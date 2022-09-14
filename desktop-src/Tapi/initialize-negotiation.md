---
description: The INITIALIZE\_NEGOTIATION datatype is a special value of type DWORD.
ms.assetid: ce978913-47a1-4387-bd1b-1795aaf82dd7
title: INITIALIZE_NEGOTIATION
ms.topic: article
ms.date: 05/31/2018
---

# INITIALIZE\_NEGOTIATION

The **INITIALIZE\_NEGOTIATION** datatype is a special value of type **DWORD**. It can be passed as the *dwDeviceID* parameter in the [**TSPI\_lineNegotiateTSPIVersion**](/windows/win32/api/tspi/nf-tspi-tspi_linenegotiatetspiversion) and [**TSPI\_phoneNegotiateTSPIVersion**](/windows/win32/api/tspi/nf-tspi-tspi_phonenegotiatetspiversion) functions. Doing so indicates that TAPI can negotiate a TSPI interface version number independent of any specific devices.

 

 
