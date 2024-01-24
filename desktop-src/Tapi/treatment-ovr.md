---
description: Treatment refers to the handling of an incoming session that has not yet been answered or has been put on hold, such as music. Please see LINECALLTREATMENT\_ Constants for a list of treatments defined by TAPI.
ms.assetid: 0b8d1023-374a-4937-b39c-04043423eb47
title: Treatment
ms.topic: article
ms.date: 05/31/2018
---

# Treatment

Treatment refers to the handling of an incoming session that has not yet been answered or has been put on hold, such as music. Please see [LINECALLTREATMENT\_ Constants](./linecalltreatment--constants.md) for a list of treatments defined by TAPI.

Not all service providers support use of this information.

**TAPI 2.x:  **[**lineGetCallInfo**](/windows/win32/api/tapi/nf-tapi-linegetcallinfo) (**dwCallTreatment** member of *lpCallInfo*)

**TAPI 3.x:  **[**ITCallInfo::get\_CallInfoLong**](/windows/desktop/api/tapi3if/nf-tapi3if-itcallinfo-get_callinfolong) (**CIL\_CALLTREATMENT** member of [**CALLINFO\_LONG**](/windows/desktop/api/Tapi3if/ne-tapi3if-callinfo_long))

 

 
