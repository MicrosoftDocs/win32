---
description: When an application redirects a session, TAPI retains identification information about the location that redirected the session and the location to which it was redirected.
ms.assetid: 08484b38-7c97-4acc-921e-0f566b2d3415
title: Redirect Identification
ms.topic: article
ms.date: 05/31/2018
---

# Redirect Identification

When an application [redirects](redirect-ovr.md) a session, TAPI retains identification information about the location that redirected the session and the location to which it was redirected.

"Redirecting" refers to the location that invoked the redirect operation. "Redirection" identifies the new destination for the session.

Not all service providers support use of this information.

**TAPI 2.x:  **[**lineGetCallInfo**](/windows/win32/api/tapi/nf-tapi-linegetcallinfo), **dwRedirectionIDSize**, **dwRedirectionIDOffset**, **dwRedirectionIDNameSize**, **dwRedirectionIDNameOffset**, **dwRedirectingIDSize**, **dwRedirectingIDOffset**, **dwRedirectingIDNameSize**, and **dwRedirectingIDNameOffset** members of [**LINECALLINFO**](/windows/win32/api/tapi/ns-tapi-linecallinfo)

**TAPI 3.x:  **[**ITCallInfo::get\_CallInfoString**](/windows/desktop/api/tapi3if/nf-tapi3if-itcallinfo-get_callinfostring)called with the **CIS\_REDIRECTIONIDNAME**, **CIS\_REDIRECTIONIDNUMBER**, **CIS\_REDIRECTINGIDNAME**, or **CIS\_REDIRECTINGIDNUMBER** member of [**CALLINFO\_STRING**](/windows/desktop/api/Tapi3if/ne-tapi3if-callinfo_string)

 

 
