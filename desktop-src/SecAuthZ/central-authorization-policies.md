---
description: A Central Authorization Policy (CAP) collects the specific authorization rules (CAPRs) into a single policy.
ms.assetid: E3E43D9F-6826-468A-86E9-AC8F9A381FD4
title: Central Authorization Policies
ms.topic: article
ms.date: 05/31/2018
---

# Central Authorization Policies

A Central Authorization Policy (CAP) collects the specific authorization rules (CAPRs) into a single policy. To allow the specific authorization rules (CAPRs) to be combined into the holistic authorization policy of the organization, CAPRs can be referenced together and applied to a set of resources. This is done by collecting multiple (by reference) into a CAP. Once a CAP is defined it can be distributed consumed by resource managers to apply the organizations authorization policy to resources.

A CAP has the following attributes:

-   Collection of CAPRs – a list of references to existing CAPR objects
-   An identifier (Sid)
-   Description
-   Name

A CAP is evaluated during access evaluation for files and folders on which an administrator enables it. During an [**AccessCheck**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-accesscheck) call, the CAP check is logically combined with the discretionary ACL check; this means that in order to obtain access to a file to which the CAP applies, a user needs to have access both according to the CAP (its associated CAPRs) and the discretionary ACL on the file.

Example CAP:

``` syntax
CORPORATE-FINANCE-CAP]
CAPID=S-1-5-3-4-56-45-67-123
Policies=HBI-CAPE;RETENTION-CAPR
```

## CAP Definition

A CAP is created and edited in Active Directory using a new UX in ADAC (or PowerShell) that allows the administrator to create a CAP and specify a set of CAPRs that make up the CAP.

 

 
