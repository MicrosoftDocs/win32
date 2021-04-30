---
description: The Call ID differs from the Session Identifier in two primary ways the service provider assigns it, and it is the same for every application that handles the session.
ms.assetid: c9d0d43b-3053-4e3e-b442-57942f3448df
title: Call ID
ms.topic: article
ms.date: 05/31/2018
---

# Call ID

The Call ID differs from the [Session Identifier](session-identifier-ovr.md) in two primary ways: the service provider assigns it, and it is the same for every application that handles the session. It cannot be used for ordinary communication with TAPI concerning session operations because it does not match to a particular application.

The Call ID is used in operations such as determining whether a group of session IDs actually refer to one call, as is the case for a conference, or for communications with another application.

Not all service providers support use of this information.

**TAPI 2.x:** See [**lineGetCallInfo**](/windows/win32/api/tapi/nf-tapi-linegetcallinfo) (**dwCallID** member of [**LINECALLINFO**](/windows/win32/api/tapi/ns-tapi-linecallinfo)).

**TAPI 3.x:** See [**ITCallInfo::get\_CallInfoLong**](/windows/desktop/api/tapi3if/nf-tapi3if-itcallinfo-get_callinfolong) (**CIL\_CALLID** member of [**CALLINFO\_LONG**](/windows/desktop/api/Tapi3if/ne-tapi3if-callinfo_long)).

 

 
