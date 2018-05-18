---
Description: 'The fax service is a secure service.'
ms.assetid: '227d7c41-a37c-4c2c-a6be-eaced047ccbf'
title: Fax Client User Access Rights
---

# Fax Client User Access Rights

The fax service is a secure service. In the Microsoft Win32 environment, users must have access rights to successfully call certain fax client functions. The service performs an access check each time a client application calls a fax client function. To check a user's access rights, an application can call the [**FaxAccessCheck**](-mfax-faxaccesscheck.md) function.

If you are using the Microsoft Component Object Model (COM) implementation, your fax client application cannot access this functionality at this time. If a client does not have the access privileges required to perform a specific task, the method or function fails and returns the value HRESULT\_FROM\_WIN32(ERROR\_ACCESS\_DENIED).

The fax service administration application, a Microsoft Management Console (MMC) snap-in component, is available for users to query and modify job access, port access, and global configuration data access privileges.

The following topics contain detailed information about fax access rights.

-   [Specific Fax Access Rights](-mfax-specific-fax-access-rights.md)
-   [Generic Fax Access Rights](-mfax-generic-fax-access-rights.md)
-   [Required Fax Access Rights by Function](-mfax-required-fax-access-rights-by-function.md)

## Related topics

<dl> <dt>

[Fax Port Access Levels](-mfax-fax-port-access-levels.md)
</dt> </dl>

 

 



