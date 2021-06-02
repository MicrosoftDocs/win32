---
description: SID Components
ms.assetid: 528412e7-c2b6-4ddd-86de-999252972421
title: SID Components
ms.topic: article
ms.date: 05/31/2018
---

# SID Components

A SID value includes components that provide information about the [**SID**](/windows/desktop/api/Winnt/ns-winnt-sid) structure and components that uniquely identify a trustee. A SID consists of the following components:

-   The revision level of the [**SID**](/windows/desktop/api/Winnt/ns-winnt-sid) structure
-   A 48-bit identifier authority value that identifies the authority that issued the SID
-   A variable number of subauthority or [*relative identifier*](/windows/desktop/SecGloss/r-gly) (RID) values that uniquely identify the trustee relative to the authority that issued the SID

The combination of the identifier authority value and the subauthority values ensures that no two SIDs will be the same, even if two different SID-issuing authorities issue the same combination of RID values. Each SID-issuing authority issues a given RID only once.

SIDs are stored in binary format in a [**SID**](/windows/desktop/api/Winnt/ns-winnt-sid) structure. To display a SID, you can call the [**ConvertSidToStringSid**](/windows/desktop/api/Sddl/nf-sddl-convertsidtostringsida) function to convert a binary SID to string format. To convert a SID string back to a valid, functional SID, call the [**ConvertStringSidToSid**](/windows/desktop/api/Sddl/nf-sddl-convertstringsidtosida) function.

These functions use the following standardized string notation for SIDs, which makes it simpler to visualize their components:

S-*R*-*I*-*S*…

In this notation, the literal character "S" identifies the series of digits as a SID, *R* is the revision level, *I* is the identifier-authority value, and *S*… is one or more subauthority values.

The following example uses this notation to display the well-known domain-relative SID of the local Administrators group:

S-1-5-32-544

In this example, the SID has the following components. The constants in parentheses are well-known identifier authority and [*RID*](/windows/desktop/SecGloss/r-gly) values defined in Winnt.h:

-   A revision level of 1
-   An identifier-authority value of 5 (SECURITY\_NT\_AUTHORITY)
-   A first subauthority value of 32 (SECURITY\_BUILTIN\_DOMAIN\_RID)
-   A second subauthority value of 544 (DOMAIN\_ALIAS\_RID\_ADMINS)

 

 
