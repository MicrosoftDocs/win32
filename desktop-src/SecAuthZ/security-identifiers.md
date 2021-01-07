---
description: A security identifier (SID) is a unique value of variable length used to identify a trustee.
ms.assetid: 7cb07bcd-70f4-43dd-8382-320fcff151c7
title: Security Identifiers
ms.topic: article
ms.date: 05/31/2018
---

# Security Identifiers

A [*security identifier*](/windows/desktop/SecGloss/s-gly) (SID) is a unique value of variable length used to identify a [trustee](trustees.md). Each account has a unique SID issued by an authority, such as a Windows domain controller, and stored in a security database. Each time a user logs on, the system retrieves the SID for that user from the database and places it in the [*access token*](/windows/desktop/SecGloss/a-gly) for that user. The system uses the SID in the access token to identify the user in all subsequent interactions with Windows security. When a SID has been used as the unique identifier for a user or group, it cannot ever be used again to identify another user or group.

Windows security uses SIDs in the following security elements:

-   In [security descriptors](security-descriptors.md) to identify the owner of an object and primary group
-   In [access control entries](access-control-entries.md), to identify the trustee for whom access is allowed, denied, or audited
-   In [access tokens](access-tokens.md), to identify the user and the groups to which the user belongs

In addition to the uniquely created, domain-specific SIDs assigned to specific users and groups, there are [well-known SIDs](well-known-sids.md) that identify generic groups and generic users. For example, the well-known SIDs, Everyone and World, identify a group that includes all users.

Most applications never need to work with SIDs. Because the names of [well-known SIDs](well-known-sids.md) can vary, you should use the functions to build the SID from predefined constants rather than using the name of the well-known SID. For example, the U.S. English version of the Windows operating system has a well-known SID named "BUILTIN\\Administrators" that might have a different name on international versions of the system. For an example that builds a well-known SID, see [Searching for a SID in an Access Token in C++](searching-for-a-sid-in-an-access-token-in-c--.md).

If you do need to work with SIDs, do not manipulate them directly. Instead, use the following functions.



| Function                                                       | Description                                                                                                                                               |
|----------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AllocateAndInitializeSid**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-allocateandinitializesid)   | Allocates and initializes a SID with the specified number of subauthorities.                                                                              |
| [**ConvertSidToStringSid**](/windows/desktop/api/Sddl/nf-sddl-convertsidtostringsida)         | Converts a SID to a string format suitable for display, storage, or transport.                                                                            |
| [**ConvertStringSidToSid**](/windows/desktop/api/Sddl/nf-sddl-convertstringsidtosida)         | Converts a string-format SID to a valid, functional SID.                                                                                                  |
| [**CopySid**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-copysid)                                     | Copies a source SID to a buffer.                                                                                                                          |
| [**EqualPrefixSid**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-equalprefixsid)                       | Tests two SID prefix values for equality. A SID prefix is the entire SID except for the last subauthority value.                                          |
| [**EqualSid**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-equalsid)                                   | Tests two SIDs for equality. They must match exactly to be considered equal.                                                                              |
| [**FreeSid**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-freesid)                                     | Frees a previously allocated SID by using the [**AllocateAndInitializeSid**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-allocateandinitializesid) function.                                      |
| [**GetLengthSid**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-getlengthsid)                           | Retrieves the length of a SID.                                                                                                                            |
| [**GetSidIdentifierAuthority**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-getsididentifierauthority) | Retrieves a pointer to the identifier authority for a SID.                                                                                                |
| [**GetSidLengthRequired**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-getsidlengthrequired)           | Retrieves the size of the buffer required to store a SID with a specified number of subauthorities.                                                       |
| [**GetSidSubAuthority**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-getsidsubauthority)               | Retrieves a pointer to a specified subauthority in a SID.                                                                                                 |
| [**GetSidSubAuthorityCount**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-getsidsubauthoritycount)     | Retrieves the number of subauthorities in a SID.                                                                                                          |
| [**InitializeSid**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-initializesid)                         | Initializes a [**SID**](/windows/desktop/api/Winnt/ns-winnt-sid) structure.                                                                                                               |
| [**IsValidSid**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-isvalidsid)                               | Tests the validity of a SID by verifying that the revision number is within a known range and that the number of subauthorities is less than the maximum. |
| [**LookupAccountName**](/windows/desktop/api/Winbase/nf-winbase-lookupaccountnamea)                 | Retrieves the SID that corresponds to a specified account name.                                                                                           |
| [**LookupAccountSid**](/windows/desktop/api/Winbase/nf-winbase-lookupaccountsida)                   | Retrieves the account name that corresponds to a specified SID.                                                                                           |



 

 

 
