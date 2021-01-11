---
description: When you set an authentication level for an application, you determine what degree of authentication is performed when clients call into the application.
ms.assetid: a59935de-6b8f-4c0a-8479-e30bc0509698
title: Setting an Authentication Level for a Server Application
ms.topic: article
ms.date: 05/31/2018
---

# Setting an Authentication Level for a Server Application

When you set an authentication level for an application, you determine what degree of authentication is performed when clients call into the application. Higher authentication levels provide greater security and data integrity, although usually with some performance degradation. For more information, see [Client Authentication](client-authentication.md).

**To select an authentication level for a server application**

1.  Right-click the COM+ application for which you are setting authentication, and then click **Properties**.

2.  In the application properties dialog box, click the **Security** tab.

3.  In the **Authentication level for calls** box, select the appropriate level. The levels are as follows, ordered from lowest to highest security:

    -   **None**. No authentication occurs.
    -   **Connect**. Authenticates credentials only when the connection is made.
    -   **Call**. Authenticates credentials at the beginning of every call.
    -   **Packet**. Authenticates credentials and verifies that all call data is received. This is the default setting for COM+ server applications.
    -   **Packet Integrity**. Authenticates credentials and verifies that no call data has been modified in transit.
    -   **Packet Privacy**. Authenticates credentials and encrypts the packet, including the data and the sender's identity and signature.

4.  Click **OK**.

## Related topics

<dl> <dt>

[Enabling Authentication for a Library Application](enabling-authentication-for-a-library-application.md)
</dt> </dl>

 

 



