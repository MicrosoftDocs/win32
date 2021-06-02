---
description: Charging information is specific to the ISDN Q.931 standard. Please refer to your service providers documentation on the meaning and use of this data.
ms.assetid: 5032e2cb-486a-4667-9873-bf88365f12cf
title: Charging Information
ms.topic: article
ms.date: 05/31/2018
---

# Charging Information

Charging information is specific to the ISDN Q.931 standard. Please refer to your service provider's documentation on the meaning and use of this data.

Not all service providers support use of this information.

**TAPI 2.x:** See [**lineGetCallInfo**](/windows/win32/api/tapi/nf-tapi-linegetcallinfo) (**dwChargingInfoSize** and **dwChargingInfoOffset** members of *lpCallInfo*).

**TAPI 3.x:** See [**ITCallInfo::get\_CallInfoBuffer**](/windows/desktop/api/tapi3if/nf-tapi3if-itcallinfo-get_callinfobuffer) (**CIB\_CHARGINGINFOBUFFER** member of [**CALLINFO\_BUFFER**](/windows/desktop/api/Tapi3if/ne-tapi3if-callinfo_buffer)).

 

 
