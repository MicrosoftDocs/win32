---
description: Origin is a general description of where the session started, such as whether it is external or internal to a corporate network. See LINECALLORIGIN\_ Constants for a listing of origins that TAPI supports.
ms.assetid: d9779438-fd08-495a-ae3d-ffad9b543090
title: Origin
ms.topic: article
ms.date: 05/31/2018
---

# Origin

Origin is a general description of where the session started, such as whether it is external or internal to a corporate network. See [LINECALLORIGIN\_ Constants](./linecallorigin--constants.md) for a listing of origins that TAPI supports.

Not all service providers support use of this information.

**TAPI 2.x:** See [**lineGetCallInfo**](/windows/win32/api/tapi/nf-tapi-linegetcallinfo) (**dwOrigin** member of *lpCallInfo*).

**TAPI 3.x:** See [**ITCallInfo::get\_CallInfoLong**](/windows/desktop/api/tapi3if/nf-tapi3if-itcallinfo-get_callinfolong) (**CIL\_ORIGIN** member of [**CALLINFO\_LONG**](/windows/desktop/api/Tapi3if/ne-tapi3if-callinfo_long)).

 

 
