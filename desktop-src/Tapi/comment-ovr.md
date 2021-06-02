---
description: An application can set a comment during the initiation of a session. Comments are often used for logging purposes.
ms.assetid: 46201166-de07-47b8-8d9a-c8edb7fb6926
title: Comment
ms.topic: article
ms.date: 05/31/2018
---

# Comment

An application can set a comment during the initiation of a session. Comments are often used for logging purposes.

Not all service providers support use of this information.

**TAPI 2.x:** See [**lineGetCallInfo**](/windows/win32/api/tapi/nf-tapi-linegetcallinfo) (**dwCommentSize** and **dwCommentOffset** members of *lpCallInfo*).

**TAPI 3.x:** See [**ITCallInfo::get\_CallInfoString**](/windows/desktop/api/tapi3if/nf-tapi3if-itcallinfo-get_callinfostring) (**CIL\_COMMENT** member of [**CALLINFO\_STRING**](/windows/desktop/api/Tapi3if/ne-tapi3if-callinfo_string)).

 

 
