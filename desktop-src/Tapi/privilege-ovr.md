---
description: Privilege refers to whether an application owns or is monitoring the session.
ms.assetid: 0c02a88a-370f-4eb9-ba64-07a382bd2e87
title: Privilege
ms.topic: article
ms.date: 05/31/2018
---

# Privilege

Privilege refers to whether an application owns or is monitoring the session. If the application owns the session, it is allowed to perform a variety of session operations. If the application is only monitoring, it will receive state messages and it can access session information, but any attempt to perform most operations will result in an error.

During initialization, an application tells TAPI which privilege level it requires on which addresses. TAPI offers incoming sessions only to applications that have registered for either owner or owner and monitor privilege.

An application's privilege on a session it creates is always owner.

**TAPI 2.x:** See [**lineGetCallStatus**](/windows/win32/api/tapi/nf-tapi-linegetcallstatus), **dwCallPrivilege** member of [**LINECALLSTATUS**](/windows/win32/api/tapi/ns-tapi-linecallstatus), [**lineSetCallPrivilege**](/windows/win32/api/tapi/nf-tapi-linesetcallprivilege).

**TAPI 3.x:** See [**ITCallInfo::get\_Privilege**](/windows/desktop/api/tapi3if/nf-tapi3if-itcallinfo-get_privilege), [**ITCallInfo::get\_CallInfoLong**](/windows/desktop/api/tapi3if/nf-tapi3if-itcallinfo-get_callinfolong), called with the **CIL\_NUMBEROFOWNERS** or **CIL\_NUMBEROFMONITORS** member of [**CALLINFO\_LONG**](/windows/desktop/api/Tapi3if/ne-tapi3if-callinfo_long).

 

 
