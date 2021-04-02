---
description: Provides a mechanism for controlling access to securable objects.
ms.assetid: 5923cb4c-f663-40d2-989a-07d71ac475db
title: Mandatory Integrity Control
ms.topic: article
ms.date: 05/31/2018
---

# Mandatory Integrity Control

Mandatory Integrity Control (MIC) provides a mechanism for controlling access to securable objects. This mechanism is in addition to discretionary access control and evaluates access before access checks against an object's [*discretionary access control list*](/windows/desktop/SecGloss/d-gly) (DACL) are evaluated.

MIC uses integrity levels and mandatory policy to evaluate access. [*Security principals*](/windows/desktop/SecGloss/s-gly) and securable objects are assigned integrity levels that determine their levels of protection or access. For example, a principal with a low integrity level cannot write to an object with a medium integrity level, even if that object's DACL allows write access to the principal.

Windows defines four integrity levels: low, medium, high, and system. Standard users receive medium, elevated users receive high. Processes you start and objects you create receive your integrity level (medium or high) or low if the executable file's level is low; system services receive system integrity. Objects that lack an integrity label are treated as medium by the operating system; this prevents low-integrity code from modifying unlabeled objects. Additionally, Windows ensures that processes running with a low integrity level cannot obtain access to a process which is associated with an app container.

## Integrity Labels

Integrity labels specify the integrity levels of securable objects and security principals. Integrity labels are represented by [*integrity SIDs*](/windows/desktop/SecGloss/i-gly). The integrity SID for a securable object is stored in its [*system access control list*](/windows/desktop/SecGloss/s-gly) (SACL). The SACL contains a [**SYSTEM\_MANDATORY\_LABEL\_ACE**](/windows/desktop/api/Winnt/ns-winnt-system_mandatory_label_ace) [*access control entry*](/windows/desktop/SecGloss/a-gly) (ACE) that in turn contains the integrity SID. Any object without an integrity SID is treated as if it had medium integrity.

The integrity SID for a security principal is stored in its access token. An access token may contain one or more integrity SIDs.

For detailed information about the defined integrity SIDs, see [Well-known SIDs](well-known-sids.md).

## Process Creation

When a user attempts to launch an executable file, the new process is created with the minimum of the user integrity level and the file integrity level. This means that the new process will never execute with higher integrity than the executable file. If the administrator user executes a low integrity program, the token for the new process functions with the low integrity level. This helps protect a user who launches untrustworthy code from malicious acts performed by that code. The user data, which is at the typical user integrity level, is write-protected against this new process.

## Mandatory Policy

The [**SYSTEM\_MANDATORY\_LABEL\_ACE**](/windows/desktop/api/Winnt/ns-winnt-system_mandatory_label_ace) ACE in the SACL of a securable object contains an access mask that specifies the access that principals with integrity levels lower than the object are granted. The values defined for this access mask are **SYSTEM\_MANDATORY\_LABEL\_NO\_WRITE\_UP**, **SYSTEM\_MANDATORY\_LABEL\_NO\_READ\_UP**, and **SYSTEM\_MANDATORY\_LABEL\_NO\_EXECUTE\_UP**. By default, the system creates every object with an access mask of **SYSTEM\_MANDATORY\_LABEL\_NO\_WRITE\_UP**.

Every access token also specifies a mandatory policy that is set by the [*Local Security Authority*](/windows/desktop/SecGloss/l-gly) (LSA) when the token is created. This policy is specified by a [**TOKEN\_MANDATORY\_POLICY**](/windows/desktop/api/Winnt/ns-winnt-token_mandatory_policy) structure associated with the token. This structure can be queried by calling the [**GetTokenInformation**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-gettokeninformation) function with the value of the *TokenInformationClass* parameter set to **TokenMandatoryPolicy**.

 

 
