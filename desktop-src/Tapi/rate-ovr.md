---
description: The rate or bandwidth of a call specifies the speed of data transmission. Three data points identify rate the current rate the maximum rate for a specified bearer mode and the minimum rate for the bearer mode.
ms.assetid: bc373ac5-a986-483f-a136-60cdc2e2c6b0
title: Rate
ms.topic: article
ms.date: 05/31/2018
---

# Rate

The rate (or bandwidth) of a call specifies the speed of data transmission. Three data points identify rate: the current rate, the maximum rate for a specified bearer mode, and the minimum rate for the bearer mode.

Not all service providers support use of this information.

**TAPI 2.x:  **[**lineSetCallParams**](/windows/win32/api/tapi/nf-tapi-linesetcallparams), [**lineGetCallInfo**](/windows/win32/api/tapi/nf-tapi-linegetcallinfo), **dwMinRate** or **dwMaxRate** member of [**LINECALLINFO**](/windows/win32/api/tapi/ns-tapi-linecallinfo)

**TAPI 3.x:  **[**ITCallInfo::get\_CallInfoLong**](/windows/desktop/api/tapi3if/nf-tapi3if-itcallinfo-get_callinfolong), [**ITCallInfo::put\_CallInfoLong**](/windows/desktop/api/tapi3if/nf-tapi3if-itcallinfo-put_callinfolong), **CIL\_MAXRATE**, **CIL\_MINRATE**, or **CIL\_RATE** member of [**CALLINFO\_LONG**](/windows/desktop/api/Tapi3if/ne-tapi3if-callinfo_long)

**TSPI:  **[**LINE\_CALLINFO**](/previous-versions/windows/desktop/legacy/ms725218(v=vs.85)) message, with *dwParam1* set to LINECALLINFOSTATE\_RATE

 

 
