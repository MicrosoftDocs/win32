---
title: Turning Off Activation Security
description: Turning Off Activation Security
ms.assetid: 3474f8ad-f041-4886-ad39-ff0603c5c69e
ms.topic: article
ms.date: 05/31/2018
---

# Turning Off Activation Security

Normally, activation uses default security settings. However, you can control activation security by specifying a [**COAUTHINFO**](/windows/desktop/api/wtypesbase/ns-wtypesbase-coauthinfo) structure, which is a member of the [**COSERVERINFO**](/windows/win32/api/objidlbase/ns-objidlbase-coserverinfo) structure that is passed to the activation functions. If the client specifies an authentication level of RPC\_C\_AUTHN\_LEVEL\_NONE in the **COAUTHINFO** structure, authentication is not attempted. Otherwise, secure activation is attempted, and if authentication fails, activation fails.

If the client does not specify an explicit [**COAUTHINFO**](/windows/desktop/api/wtypesbase/ns-wtypesbase-coauthinfo) structure and instead sets the pointer to **NULL**, COM will attempt to authenticate the client. If it cannot authenticate the client, COM checks the launch permission security descriptor to see whether there is a **NULL** DACL or an ACL that allows access to Everyone. If this check succeeds, the server is launched. Therefore, even if the client does not specify a **COAUTHINFO**structure, unsecure activation may take place when the server allows it.

> [!Note]  
> To allow unauthenticated network users to run a COM application, the application roles must include the Anonymous user. Starting with Windows Server 2003, by default, the Anonymous user is not included in the Everyone group.

 

Why would a client want to turn off activation security explicitly even though unsecure activation will eventually take place if the server allows it? Because explicitly turning off activation security increases performance when the client does not want or need security checks.

The following things must be done to explicitly turn off activation security:

-   The client must specify an authentication level of RPC\_C\_AUTHN\_LEVEL\_NONE in the [**COAUTHINFO**](/windows/desktop/api/wtypesbase/ns-wtypesbase-coauthinfo) structure that is a member of the [**COSERVERINFO**](/windows/win32/api/objidlbase/ns-objidlbase-coserverinfo) structure supplied to the activation function.
-   The client must specify an impersonation level of RPC\_C\_IMP\_LEVEL\_IMPERSONATE in the [**COAUTHINFO**](/windows/desktop/api/wtypesbase/ns-wtypesbase-coauthinfo) structure that is a member of the [**COSERVERINFO**](/windows/win32/api/objidlbase/ns-objidlbase-coserverinfo) structure supplied to the activation function. If this value is not passed, you will get RPC\_S\_SERVER\_UNAVAILABLE.
-   The server must specify **Everyone** for **Default Launch Permissions**. The recommended way to perform this task is to use Dcomcnfg.exe as follows:
    1.  Run Dcomcnfg.exe.
    2.  On the **Applications** page, select the application that represents the server. Click the **Properties** button (or double-click the selected application).
    3.  On the **Security** property page, click the **Use Custom Launch Permissions** button.
    4.  Click the **Edit** button in the **Launch Permissions** area.
    5.  In the **Registry Value Permissions** dialog box, click the **Add** button.
    6.  Select the entry for **Everyone** in the list box.
    7.  In the **Type of Access** list box, choose **Allow Launch**.
    8.  Click the **OK** button.

> [!Note]  
> In Windows Server 2003, the authentication capability for the COM+ system application includes the value EOAC\_DISABLE\_AAA. This value, which disables activate-as-activator (AAA) activations, is used in the [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity) call when launching the system application. Setting the authentication capability to EOAC\_DISABLE\_AAA allows an application that runs under a privileged account (such as LocalSystem) to help prevent its identity from being used to launch untrusted components.

 

## Related topics

<dl> <dt>

[Turning Off Call Security](turning-off-call-security.md)
</dt> </dl>

 

 