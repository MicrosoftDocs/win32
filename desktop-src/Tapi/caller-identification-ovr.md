---
description: Caller identification provides information on the calling party when receiving an incoming session. An application typically uses this data as part of a status message to a user.
ms.assetid: aaaa5eae-e917-44a7-b9c5-97ca2d9a4eec
title: Caller Identification
ms.topic: article
ms.date: 05/31/2018
---

# Caller Identification

Caller identification provides information on the calling party when receiving an incoming session. An application typically uses this data as part of a status message to a user.

This information is not always available immediately. An application that wants to use this information and has verified that the service provider supports it should check several times before assuming that the information is not available.

Not all service providers support use of this information.

**TAPI 2.x:** See [**lineGetCallInfo**](/windows/win32/api/tapi/nf-tapi-linegetcallinfo) (**dwCallerIDFlags**, **dwCallerIDSize**, **dwCallerIDOffset**, **dwCallerIDNameSize**, **dwCallerIDNameOffset**, and **dwCallerIDAddressType** members of *lpCallInfo*).

**TAPI 3.x:** See [**ITCallInfo::get\_CallInfoLong**](/windows/desktop/api/tapi3if/nf-tapi3if-itcallinfo-get_callinfolong) (**CIL\_CALLERIDADDRESSTYPE** member of [**CALLINFO\_LONG**](/windows/desktop/api/Tapi3if/ne-tapi3if-callinfo_long)), [**ITCallInfo::get\_CallInfoString**](/windows/desktop/api/tapi3if/nf-tapi3if-itcallinfo-get_callinfostring) (**CIS\_CALLERIDNAME** and **CIS\_CALLERIDNAME** members of [**CALLINFO\_STRING**](/windows/desktop/api/Tapi3if/ne-tapi3if-callinfo_string)).

 

 
