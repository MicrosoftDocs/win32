---
description: The compatibility buffer is specific to the ISDN Q.931 standard. Please refer to your service providers documentation on the meaning and use of this data.
ms.assetid: c4c87ca8-fbae-4275-9b69-7b32daf4c18f
title: Compatibility Buffer
ms.topic: article
ms.date: 05/31/2018
---

# Compatibility Buffer

The compatibility buffer is specific to the ISDN Q.931 standard. Please refer to your service provider's documentation on the meaning and use of this data.

Not all service providers support use of this information.

**TAPI 2.x:** See [**lineGetCallInfo**](/windows/win32/api/tapi/nf-tapi-linegetcallinfo) (**dwHighLevelCompSize**, **dwHighLevelCompOffset**, **dwLowLevelCompSize**, and **dwLowLevelCompOffset** members of *lpCallInfo*).

**TAPI 3.x:** See [**ITCallInfo::get\_CallInfoBuffer**](/windows/desktop/api/tapi3if/nf-tapi3if-itcallinfo-get_callinfobuffer) (**CIB\_HIGHLEVELCOMPATIBILITYBUFFER** and **CIB\_LOWLEVELCOMPATIBILITYBUFFER** member of [**CALLINFO\_BUFFER**](/windows/desktop/api/Tapi3if/ne-tapi3if-callinfo_buffer)).

 

 
