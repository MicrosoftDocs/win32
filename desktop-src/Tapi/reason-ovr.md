---
description: The possible reasons for an incoming session, such as that it was transferred, are listed in the LINECALLREASON\_ Constants.
ms.assetid: 94cc1a79-7ce4-47ec-bdd8-ee7f0d9f48ed
title: Reason
ms.topic: article
ms.date: 05/31/2018
---

# Reason

The possible reasons for an incoming session, such as that it was transferred, are listed in the [LINECALLREASON\_ Constants](./linecallreason--constants.md).

Not all service providers support use of this information.

**TAPI 2.x:  **[**lineGetCallInfo**](/windows/win32/api/tapi/nf-tapi-linegetcallinfo) (**dwReason** member of *lpCallInfo*)

**TAPI 3.x:  **[**ITCallInfo::get\_CallInfoLong**](/windows/desktop/api/tapi3if/nf-tapi3if-itcallinfo-get_callinfolong) (**CIL\_REASON** member of [**CALLINFO\_LONG**](/windows/desktop/api/Tapi3if/ne-tapi3if-callinfo_long))

 

 
