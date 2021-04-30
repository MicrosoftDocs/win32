---
description: Device-specific buffers may be part of a service providers implementation of extended operations. The service provider defines the meaning of these buffers.
ms.assetid: 5783f892-ec11-4340-afad-44f2ef55fd18
title: 'Device-specific Buffer'
ms.topic: article
ms.date: 05/31/2018
---

# Device-specific Buffer

Device-specific buffers may be part of a service provider's implementation of extended operations. The service provider defines the meaning of these buffers.

Not all service providers support use of this information.

**TAPI 2.x:** See [**lineGetCallInfo**](/windows/win32/api/tapi/nf-tapi-linegetcallinfo) (**dwDevSpecificSize** and **dwDevSpecificOffset** members of [**LINECALLINFO**](/windows/win32/api/tapi/ns-tapi-linecallinfo)).

**TAPI 3.x:** See [**ITCallInfo::GetCallInfoBuffer**](/windows/desktop/api/tapi3if/nf-tapi3if-itcallinfo-getcallinfobuffer) (**CIB\_DEVSPECIFICBUFFER** member of [**CALLINFO\_BUFFER**](/windows/desktop/api/Tapi3if/ne-tapi3if-callinfo_buffer)).

 

 
