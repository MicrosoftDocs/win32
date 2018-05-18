---
title: Using LDAP for Password Authentication
description: Determine if multiple users have valid IDs and passwords and if their accounts are enabled.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 'cbce4264-9c37-4c29-ad00-669b1d1de2c6'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-lightweight-directory-services'
ms.tgt_platform: multiple
keywords: ["Using LDAP for Password Authentication LDAP", "Concurrent Binding LDAP", "bind, fast LDAP"]
---

# Using LDAP for Password Authentication

Concurrent bind, also known as fast bind, enables an application to determine if multiple users have valid IDs and passwords and if their accounts are enabled. By using concurrent binding, the application can request multiple bind operations by way of a single LDAP connection.

Unlike a normal LDAP bind, a concurrent bind does not determine a user group association or build a security token; it only determines if the user has a valid ID and password. This enables the concurrent bind to complete in a fraction of the time of a normal bind.

To enable concurrent bind on an LDAP connection, the application sets the [LDAP\_OPT\_FAST\_CONCURRENT\_BIND](session-options.md) session option after the LDAP connection has been initialized, but before any binds are performed. When concurrent binding is enabled for a particular LDAP session, it cannot be disabled without closing the session connection.

Concurrent bind cannot be enabled on an LDAP session if signing or data encryption are enabled. Attempting to enable concurrent bind on sessions with signing or data encryption will fail the [**ldap\_set\_option**](ldap-set-option.md) call and return an [LDAP\_UNWILLING\_TO\_PERFORM](return-values.md) error code.

When concurrent bind is enabled on an LDAP session, only simple bind operations may be performed in that session and all simple binds are fast binds. As a result all subsequent bind requests will not be serialized internally by the LDAP client and the binds will not generate a security token. Any binds performed in this session are performed as anonymous, and because data encryption is not allowed any data sent through this session will appear on the network in an unencrypted form. If the application attempts to use a non-simple bind on a session with concurrent bind enabled, the call will fail and return an [LDAP\_UNWILLING\_TO\_PERFORM](return-values.md) error code.

The following example code shows how to create an LDAP session with concurrent bind enabled.


```C++
ULONG ldap_open_fast_bind_session(LPTSTR pHostName, PLDAP pSession)
{
    ULONG lRtn = LDAP_SUCCESS;
    ULONG version = LDAP_VERSION3;
    
    // Initialize session. LDAP_PORT is the default port, 389.
    pSession = ldap_init(pHostName, LDAP_PORT);
    if (pLS == NULL)
        return LdapGetLastError();

    // Set the version to 3.0 (default version is 2.0).
    lRtn = ldap_set_option(pSession,
                           LDAP_OPT_PROTOCOL_VERSION,
                           (void*)&amp;version);

    // Enable concurrent bind.
    if (lRtn == LDAP_SUCCESS)
        lRtn = ldap_set_option(pSession,
                               LDAP_OPT_FAST_CONCURRENT_BIND,
                               LDAP_OPT_ON);

    // Cleanup on error.
    if (lRtn != LDAP_SUCCESS)
        ldap_unbind(pSession);
    return lRtn;
}
```



 

 




