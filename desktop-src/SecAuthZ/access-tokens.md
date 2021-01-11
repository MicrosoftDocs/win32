---
description: An access token is an object that describes the security context of a process or thread.
ms.assetid: 350159c9-2399-427a-ba44-c897a9664299
title: Access Tokens
ms.topic: article
ms.date: 05/31/2018
---

# Access Tokens

An [*access token*](/windows/desktop/SecGloss/a-gly) is an object that describes the [*security context*](/windows/desktop/SecGloss/s-gly) of a [*process*](/windows/desktop/SecGloss/p-gly) or thread. The information in a token includes the identity and privileges of the user account associated with the process or thread. When a user logs on, the system verifies the user's password by comparing it with information stored in a security database. If the password is [*authenticated*](/windows/desktop/SecGloss/a-gly), the system produces an access token. Every process executed on behalf of this user has a copy of this access token.

The system uses an access token to identify the user when a thread interacts with a [securable object](securable-objects.md) or tries to perform a system task that requires privileges. Access tokens contain the following information:

-   The [security identifier](security-identifiers.md) (SID) for the user's account
-   SIDs for the groups of which the user is a member
-   A [*logon SID*](/windows/desktop/SecGloss/l-gly) that identifies the current [*logon session*](/windows/desktop/SecGloss/l-gly)
-   A list of the [privileges](privileges.md) held by either the user or the user's groups
-   An owner SID
-   The SID for the primary group
-   The default [DACL](access-control-lists.md) that the system uses when the user creates a securable object without specifying a [*security descriptor*](/windows/desktop/SecGloss/s-gly)
-   The source of the access token
-   Whether the token is a [*primary*](/windows/desktop/SecGloss/p-gly) or [impersonation](client-impersonation.md) token
-   An optional list of [restricting SIDs](restricted-tokens.md)
-   Current impersonation levels
-   Other statistics

Every process has a [*primary token*](/windows/desktop/SecGloss/p-gly) that describes the [*security context*](/windows/desktop/SecGloss/s-gly) of the user account associated with the process. By default, the system uses the primary token when a thread of the process interacts with a securable object. Moreover, a thread can impersonate a client account. Impersonation allows the thread to interact with securable objects using the client's security context. A thread that is impersonating a client has both a primary token and an [*impersonation token*](/windows/desktop/SecGloss/i-gly).

Use the [**OpenProcessToken**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-openprocesstoken) function to retrieve a handle to the primary token of a process. Use the [**OpenThreadToken**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-openthreadtoken) function to retrieve a handle to the impersonation token of a thread. For more information, see [Impersonation](client-impersonation.md).

You can use the following functions to manipulate access tokens.



| Function                                               | Description                                                                                                                                                            |
|--------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AdjustTokenGroups**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-adjusttokengroups)         | Changes the group information in an access token.                                                                                                                      |
| [**AdjustTokenPrivileges**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-adjusttokenprivileges) | Enables or disables the privileges in an access token. It does not grant new privileges or revoke existing ones.                                                       |
| [**CheckTokenMembership**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-checktokenmembership)   | Determines whether a specified SID is enabled in a specified access token.                                                                                             |
| [**CreateRestrictedToken**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-createrestrictedtoken) | Creates a new token that is a restricted version of an existing token. The restricted token can have disabled SIDs, deleted privileges, and a list of restricted SIDs. |
| [**DuplicateToken**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-duplicatetoken)               | Creates a new impersonation token that duplicates an existing token.                                                                                                   |
| [**DuplicateTokenEx**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-duplicatetokenex)           | Creates a new primary token or impersonation token that duplicates an existing token.                                                                                  |
| [**GetTokenInformation**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-gettokeninformation)     | Retrieves information about a token.                                                                                                                                   |
| [**IsTokenRestricted**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-istokenrestricted)         | Determines whether a token has a list of restricting SIDs.                                                                                                             |
| [**OpenProcessToken**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-openprocesstoken)           | Retrieves a handle to the primary access token for a process.                                                                                                          |
| [**OpenThreadToken**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-openthreadtoken)             | Retrieves a handle to the impersonation access token for a thread.                                                                                                     |
| [**SetThreadToken**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-setthreadtoken)               | Assigns or removes an impersonation token for a thread.                                                                                                                |
| [**SetTokenInformation**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-settokeninformation)     | Changes a token's owner, primary group, or default DACL.                                                                                                               |



 

The access token functions use the following structures to describe the parts of an access token.



| Structure                                            | Description                                                                                           |
|------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| [**TOKEN\_CONTROL**](/windows/desktop/api/Winnt/ns-winnt-token_control)              | Information that identifies an access token.                                                          |
| [**TOKEN\_DEFAULT\_DACL**](/windows/desktop/api/Winnt/ns-winnt-token_default_dacl)   | The default DACL that the system uses in the security descriptors of new objects created by a thread. |
| [**TOKEN\_GROUPS**](/windows/desktop/api/Winnt/ns-winnt-token_groups)                | Specifies the SIDs and attributes of the group SIDs in an access token.                               |
| [**TOKEN\_OWNER**](/windows/desktop/api/Winnt/ns-winnt-token_owner)                  | The default owner SID for the security descriptors of new objects.                                    |
| [**TOKEN\_PRIMARY\_GROUP**](/windows/desktop/api/Winnt/ns-winnt-token_primary_group) | The default primary group SID for the security descriptors of new objects.                            |
| [**TOKEN\_PRIVILEGES**](/windows/desktop/api/Winnt/ns-winnt-token_privileges)        | The privileges associated with an access token. Also determines whether the privileges are enabled.   |
| [**TOKEN\_SOURCE**](/windows/desktop/api/Winnt/ns-winnt-token_source)                | The source of an access token.                                                                        |
| [**TOKEN\_STATISTICS**](/windows/desktop/api/Winnt/ns-winnt-token_statistics)        | Statistics associated with an access token.                                                           |
| [**TOKEN\_USER**](/windows/desktop/api/Winnt/ns-winnt-token_user)                    | The SID of the user associated with an access token.                                                  |



 

The access token functions use the following enumeration types.



| Enumeration type                                             | Specifies                                                                       |
|--------------------------------------------------------------|---------------------------------------------------------------------------------|
| [**TOKEN\_INFORMATION\_CLASS**](/windows/desktop/api/Winnt/ne-winnt-token_information_class) | Identifies the type of information being set or retrieved from an access token. |
| [**TOKEN\_TYPE**](/windows/desktop/api/Winnt/ne-winnt-token_type)                            | Identifies an access token as a primary or impersonation token.                 |



 

 

 
