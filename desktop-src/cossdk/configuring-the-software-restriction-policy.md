---
description: Configuring the Software Restriction Policy
ms.assetid: 22c1897a-abb5-4ce9-9d09-21b6aed4f1d8
title: Configuring the Software Restriction Policy
ms.topic: article
ms.date: 05/31/2018
---

# Configuring the Software Restriction Policy

When you explicitly set the software restriction policy trust levels of a COM+ application, you are overriding the default systemwide settings. This is often necessary for COM+ server applications because the systemwide trust level is set the same for all server applications (because they all run in the same file, dllhost.exe). However, when you set the software restriction policy trust level of a COM+ library application, you are affecting the systemwide configuration for that application. For a discussion of how to use the software restriction policy in COM+, see [Using the Software Restriction Policy in COM+](using-the-software-restriction-policy-in-com-.md).

**To set the software restriction policy**

1.  Right-click the COM+ application for which you are setting the software restriction policy, and then click **Properties**.

2.  In the application properties dialog box, click the **Security** tab.

3.  Under **Software Restriction Policy**, select the **Apply software restriction policy** check box; this enables you to set the trust level. Clearing the check box will cause COM+ to use the systemwide configuration of the software restriction policy for the application. This check box corresponds to the SRPEnabled property of the [**Applications**](applications.md) collection.

4.  In the **Restriction Level** box, select the appropriate level. This drop-down box corresponds to the SRPTrustLevel property of the [**Applications**](applications.md) collection. The levels are as follows, ordered from least to most trusted:

    -   **Disallowed**. The application is disallowed from using the full privileges of the user. Components with any trust level can be loaded into it.
    -   **Unrestricted**. The application has unrestricted access to the user's privileges. Only components with an Unrestricted trust level can be loaded into it.

5.  Click **OK**.

## Related topics

<dl> <dt>

[Configuring Role-Based Security](configuring-role-based-security.md)
</dt> <dt>

[Enabling Authentication for a Library Application](enabling-authentication-for-a-library-application.md)
</dt> <dt>

[Setting an Authentication Level for a Server Application](setting-an-authentication-level-for-a-server-application.md)
</dt> <dt>

[Setting an Impersonation Level](setting-an-impersonation-level.md)
</dt> </dl>

 

 



