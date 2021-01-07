---
description: An application cannot change the access control list of an object unless the application has the rights to do so.
ms.assetid: 5f710fd8-33de-47c0-a8b2-baf3008c4ed7
title: Access Rights for Access-Token Objects
ms.topic: article
ms.date: 05/31/2018
---

# Access Rights for Access-Token Objects

An application cannot change the access control list of an object unless the application has the rights to do so. These rights are controlled by a security descriptor in the access token for the object. For more information about security, see [Access Control Model](access-control-model.md).

To get or set the [security descriptor](security-descriptors.md) for an [*access token*](/windows/desktop/SecGloss/a-gly), call the [**GetKernelObjectSecurity**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-getkernelobjectsecurity) and [**SetKernelObjectSecurity**](/windows/win32/api/securitybaseapi/nf-securitybaseapi-setkernelobjectsecurity) functions.

When you call the [**OpenProcessToken**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-openprocesstoken) or [**OpenThreadToken**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-openthreadtoken) function to get a handle to an access token, the system checks the requested [access rights](access-rights-and-access-masks.md) against the DACL in the token's security descriptor.

The following are valid access rights for access-token objects:

-   The DELETE, READ\_CONTROL, WRITE\_DAC, and WRITE\_OWNER [standard access rights](standard-access-rights.md). Access tokens do not support the SYNCHRONIZE standard access right.
-   The [ACCESS\_SYSTEM\_SECURITY right](sacl-access-right.md) to get or set the SACL in the object's security descriptor.
-   The specific access rights for access tokens, which are listed in the following table.

    | Value                     | Meaning                                                                                                                                                                                                                                                                           |
    |---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | TOKEN\_ADJUST\_DEFAULT    | Required to change the default owner, primary group, or DACL of an access token.                                                                                                                                                                                                  |
    | TOKEN\_ADJUST\_GROUPS     | Required to adjust the attributes of the groups in an access token.                                                                                                                                                                                                               |
    | TOKEN\_ADJUST\_PRIVILEGES | Required to enable or disable the privileges in an access token.                                                                                                                                                                                                                  |
    | TOKEN\_ADJUST\_SESSIONID  | Required to adjust the session ID of an access token. The SE\_TCB\_NAME privilege is required.                                                                                                                                                                                    |
    | TOKEN\_ASSIGN\_PRIMARY    | Required to attach a [*primary token*](/windows/desktop/SecGloss/p-gly) to a [*process*](/windows/desktop/SecGloss/p-gly). The SE\_ASSIGNPRIMARYTOKEN\_NAME privilege is also required to accomplish this task. |
    | TOKEN\_DUPLICATE          | Required to duplicate an access token.                                                                                                                                                                                                                                            |
    | TOKEN\_EXECUTE            | Combines STANDARD\_RIGHTS\_EXECUTE and TOKEN\_IMPERSONATE.                                                                                                                                                                                                                        |
    | TOKEN\_IMPERSONATE        | Required to attach an impersonation access token to a process.                                                                                                                                                                                                                    |
    | TOKEN\_QUERY              | Required to query an access token.                                                                                                                                                                                                                                                |
    | TOKEN\_QUERY\_SOURCE      | Required to query the source of an access token.                                                                                                                                                                                                                                  |
    | TOKEN\_READ               | Combines STANDARD\_RIGHTS\_READ and TOKEN\_QUERY.                                                                                                                                                                                                                                 |
    | TOKEN\_WRITE              | Combines STANDARD\_RIGHTS\_WRITE, TOKEN\_ADJUST\_PRIVILEGES, TOKEN\_ADJUST\_GROUPS, and TOKEN\_ADJUST\_DEFAULT.                                                                                                                                                                   |
    | TOKEN\_ALL\_ACCESS        | Combines all possible access rights for a token.                                                                                                                                                                                                                                  |

    

     

 

 
