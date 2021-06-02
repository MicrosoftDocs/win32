---
description: Parameter flags supply information on a variety of status flags concerning a communications session, such as whether caller identification should be blocked. See LINECALLPARAMFLAGS\_ Constants for a list of flags defined by TAPI.
ms.assetid: 30511328-a310-42b7-a81e-3ef2abf586ed
title: Parameter Flags
ms.topic: article
ms.date: 05/31/2018
---

# Parameter Flags

Parameter flags supply information on a variety of status flags concerning a communications session, such as whether caller identification should be blocked. See [LINECALLPARAMFLAGS\_ Constants](./linecallparamflags--constants.md) for a list of flags defined by TAPI.

Not all service providers support use of this information.

**TAPI 2.x:** See [**lineGetCallInfo**](/windows/win32/api/tapi/nf-tapi-linegetcallinfo) (**dwCallParamFlags** member of *lpCallInfo*).

**TAPI 3.x:** See [**ITCallInfo::get\_CallInfoLong**](/windows/desktop/api/tapi3if/nf-tapi3if-itcallinfo-get_callinfolong) (**CIL\_CALLPARAMSFLAGS** member of [**CALLINFO\_LONG**](/windows/desktop/api/Tapi3if/ne-tapi3if-callinfo_long)).

 

 
