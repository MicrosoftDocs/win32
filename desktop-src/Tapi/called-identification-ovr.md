---
description: Called identification identifies the original destination address for a session. In situations where a session was redirected, forwarded, or transferred, this will be different than the connected identification.
ms.assetid: a03286eb-83a9-4170-b514-e8899fd04c74
title: Called Identification
ms.topic: article
ms.date: 05/31/2018
---

# Called Identification

Called identification identifies the original destination address for a session. In situations where a session was redirected, forwarded, or transferred, this will be different than the [connected identification](connected-identification-ovr.md).

Not all service providers support use of this information.

**TAPI 2.x:** See [**lineGetCallInfo**](/windows/win32/api/tapi/nf-tapi-linegetcallinfo) (**dwCalledIDFlags**, **dwCalledIDSize**, **dwCalledIDOffset**, **dwCalledIDNameSize**, **dwCalledIDNameOffset**, and **dwCalledIDAddressType** members of *lpCallInfo*).

**TAPI 3.x:** See [**ITCallInfo::get\_CallInfoLong**](/windows/desktop/api/tapi3if/nf-tapi3if-itcallinfo-get_callinfolong) (**CIL\_CALLEDIDADDRESSTYPE** member of [**CALLINFO\_LONG**](/windows/desktop/api/Tapi3if/ne-tapi3if-callinfo_long)), [**ITCallInfo::get\_CallInfoString**](/windows/desktop/api/tapi3if/nf-tapi3if-itcallinfo-get_callinfostring) (**CIS\_CALLEDIDNAME** and **CIS\_CALLEDIDNAME** members of [**CALLINFO\_STRING**](/windows/desktop/api/Tapi3if/ne-tapi3if-callinfo_string)).

 

 
