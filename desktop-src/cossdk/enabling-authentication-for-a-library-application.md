---
description: Enabling Authentication for a Library Application
ms.assetid: 80c80c14-ceef-4a74-810d-6aa3cc320cef
title: Enabling Authentication for a Library Application
ms.topic: article
ms.date: 05/31/2018
---

# Enabling Authentication for a Library Application

Because COM+ library applications are hosted by other processes, their security requirements may be different from those of server applications. If the library application will be hosted by a browser, it might need to receive unauthenticated callbacks.

To address this need, you can disable authentication so that the hosting process does not perform security checks for callers of the library application. When you disable authentication, calls to the library application effectively go unauthenticated—all calls to it will succeed. For more information, see [Library Application Security](library-application-security.md).

**To enable (or disable) authentication for a library application**

1.  Right-click the COM+ application for which you are enabling or disabling authentication, and then click **Properties**.

2.  In the application properties dialog box, click the **Security** tab.

3.  Under **Authentication**, select the **Enable authentication** check box to enable authentication; clearing the check box will disable authentication.

4.  Click **OK**.

## Related topics

<dl> <dt>

[Setting an Authentication Level for a Server Application](setting-an-authentication-level-for-a-server-application.md)
</dt> </dl>

 

 



