---
description: The connected identification identifies the party that was actually connected to. This may be different from the called identification if the call was diverted.
ms.assetid: 3f9ba728-8e78-4f1f-a0c1-76799fd62c9d
title: Connected Identification
ms.topic: article
ms.date: 05/31/2018
---

# Connected Identification

The connected identification identifies the party that was actually connected to. This may be different from the called identification if the call was diverted.

Not all service providers support use of this information.

**TAPI 2.x:** See [**lineGetCallInfo**](/windows/win32/api/tapi/nf-tapi-linegetcallinfo) (**dwConnectedIDFlags**, **dwConnectedIDSize**, **dwConnectedIDOffset**, **dwConnectedIDNameSize**, and **dwConnectedIDNameOffset** members of *lpCallInfo*).

**TAPI 3.x:** See [**ITCallInfo::get\_CallInfoString**](/windows/desktop/api/tapi3if/nf-tapi3if-itcallinfo-get_callinfostring) (**CIL\_CONNECTEDIDNAME** member of [**CALLINFO\_STRING**](/windows/desktop/api/Tapi3if/ne-tapi3if-callinfo_string)).

 

 
