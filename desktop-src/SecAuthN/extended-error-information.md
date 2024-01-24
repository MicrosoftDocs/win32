---
description: Some security packages support extended error messages that allow the sides of a communication link to communicate any reasons for a failure.
ms.assetid: a15c61f0-03cc-462f-b5c1-8e7f062e9523
title: Extended Error Information
ms.topic: article
ms.date: 05/31/2018
---

# Extended Error Information

Some [*security packages*](/windows/desktop/SecGloss/s-gly) support extended error messages that allow the sides of a communication link to communicate any reasons for a failure. For example, the [*Kerberos protocol*](/windows/desktop/SecGloss/k-gly) could fail because of a time discrepancy between the time of request for a Kerberos ticket and the ticket's time of issue. With information from returned extended error information, a client can resynchronize its clock and generate a new connection message.

A security package setting the SECPKG\_FLAG\_EXTENDED\_ERROR flag in the **fCapabilities** member of a [**SecPkgInfo**](/windows/desktop/api/Sspi/ns-sspi-secpkginfoa) structure indicates that the security package supports extended error messages.

Client applications requiring extended error messages specify the ISC\_REQ\_EXTENDED\_ERROR flag when calling the [**InitializeSecurityContext (General)**](/windows/win32/api/sspi/nf-sspi-initializesecuritycontexta) function. Server applications requiring extended error messages set the ASC\_REQ\_EXTENDED\_ERROR flag when calling [**AcceptSecurityContext (General)**](/windows/win32/api/sspi/nf-sspi-acceptsecuritycontext).

 

 
