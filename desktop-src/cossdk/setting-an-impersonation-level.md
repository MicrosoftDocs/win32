---
description: When you set an impersonation level for an application, you determine what degree of authority the application grants other applications to use its identity when it calls them.
ms.assetid: 5b5b2c2d-dc3d-4edd-9e13-e6cb13022ceb
title: Setting an Impersonation Level
ms.topic: article
ms.date: 05/31/2018
---

# Setting an Impersonation Level

When you set an impersonation level for an application, you determine what degree of authority the application grants other applications to use its identity when it calls them. You can set this only for COM+ server applications—library applications run under the identity of the hosting process and use the impersonation level that it specifies. For more detail, see [Impersonation Levels](/windows/desktop/com/impersonation-levels).

**To select an impersonation level**

1.  Right-click the COM+ application for which you are setting impersonation, and then click **Properties**.

2.  In the application properties dialog box, click the **Security** tab.

3.  In the **Impersonation level** box, select the appropriate level. The levels are as follows, ordered from granting least to greatest authority:

    -   **Anonymous**. The client is anonymous to the server. The server can impersonate the client, but the impersonation token (a local credential) does not contain any information about the client.
    -   **Identify**. The server can obtain the client's identity and can impersonate the client to do ACL checks.
    -   **Impersonate**. The server can impersonate the client while acting on its behalf, although with restrictions. The server can access resources on the same computer as the client. If the server is on the same computer as the client, it can access network resources as the client. If the server is on a computer different from the client, it can access only resources that are on the same computer as the server. This is the default setting for COM+ server applications.
    -   **Delegate**. The server can impersonate the client while acting on its behalf, whether on the same computer as the client. During impersonation, the client's credentials (both those with local and those with network validity) can be passed to any number of machines.

4.  Click **OK**.

## Related topics

<dl> <dt>

[Configuring Role-Based Security](configuring-role-based-security.md)
</dt> <dt>

[Configuring the Software Restriction Policy](configuring-the-software-restriction-policy.md)
</dt> <dt>

[Enabling Authentication for a Library Application](enabling-authentication-for-a-library-application.md)
</dt> <dt>

[Setting an Authentication Level for a Server Application](setting-an-authentication-level-for-a-server-application.md)
</dt> </dl>

 

 
