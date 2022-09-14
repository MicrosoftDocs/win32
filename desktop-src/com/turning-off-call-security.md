---
title: Turning Off Call Security
description: Call security determines whether a client has permission to call a server's methods. There are two ways to disable call security One involves using Dcomcnfg.exe to modify the registry, and the other requires calls to CoInitializeSecurity.
ms.assetid: 7ce162d0-20e0-4385-ad9f-472f2c17b060
ms.topic: article
ms.date: 05/31/2018
---

# Turning Off Call Security

Call security determines whether a client has permission to call a server's methods. There are two ways to disable call security: One involves using Dcomcnfg.exe to modify the registry, and the other requires calls to [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity).

-   [Turning Off Call Security Using DCOMCNFG](#turning-off-call-security-using-dcomcnfg)
-   [Turning Off Call Security Programmatically](#turning-off-call-security-programmatically)
-   [Related topics](#related-topics)

## Turning Off Call Security Using DCOMCNFG

Call security can most easily be turned off by using Dcomcnfg.exe to modify the registry. However, using Dcomcnfg.exe to turn security off will work only if both the client and the server do not call [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity). This is because when **CoInitializeSecurity** is called, DCOM ignores the registry settings and uses the values supplied to **CoInitializeSecurity** instead.

To turn off security with Dcomcnfg.exe, both the client and the server must set their Authentication Levels to None. The following steps must be completed:

1.  Run Dcomcnfg.exe.
2.  On the **Applications** page, select the application that represents the server. Click the **Properties** button (or double-click the selected application).
3.  Click the **General** tab.
4.  From the **Default Authentication Level** list box, select **(None)**.
5.  Click the **Apply** button to apply changes; however, changes are not applied to any running instances of the application.
6.  If the client appears on the list on the *Applications* page, repeat steps 2 through 5, choosing the client instead of the server for step 2. Then click the **OK** button. If the client is not on the list, you can do one of the following three things:
    -   You can set the client's Authentication Level to None on a computer-wide basis by using Dcomcnfg.exe. (See the warning and the procedure below.)
    -   You can set the client's authentication level to None programmatically.
    -   You can create an [AppID](appid-key.md) key for the client to indicate an authentication level of None. (See [Setting Process-Wide Security Through the Registry](setting-processwide-security-through-the-registry.md).)

To set the Authentication Level to None on a computer-wide basis:

> [!Note]  
> Setting the computer-wide Authentication Level to None is extremely unsecure.

 

1.  Run Dcomcnfg.exe.
2.  Choose the **Default Properties** tab.
3.  From the **Default Authentication Level** list box, choose **(None)**.
4.  Click the **OK** button.

## Turning Off Call Security Programmatically

To turn call security off programmatically, both the client and the server must call **CoInitializeSecurity**, setting the authentication level in the *dwAuthnLevel* parameter to RPC\_C\_AUTHN\_LEVEL\_NONE.

## Related topics

<dl> <dt>

[Turning Off Activation Security](turning-off-activation-security.md)
</dt> </dl>

 

 




