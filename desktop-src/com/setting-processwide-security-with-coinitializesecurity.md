---
title: Setting Process-Wide Security with CoInitializeSecurity
description: The CoInitializeSecurity function allows you to control complex security scenarios by setting security for an application programmatically.
ms.assetid: 20b66868-fb9a-489f-97a2-59a8a825c8d9
ms.topic: article
ms.date: 05/31/2018
---

# Setting Process-Wide Security with CoInitializeSecurity

The [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity) function allows you to control complex security scenarios by setting security for an application programmatically. This topic describes scenarios when you might use **CoInitializeSecurity** and provides some details on how you use it.

There are several reasons why you might want to use [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity) to set process-wide security within your program. For example, although you can set the authentication level and the access permissions for the application using dcomcnfg.exe, the default impersonation level for the computer might not be the one you want for your process. The only way to change this setting for your process is to call **CoInitializeSecurity**.

If you want to use the Schannel security provider, you must specify it as an authentication service in a call to [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity).

Another common scenario in which you might set process-wide security programmatically is when you would like to set default security for the entire process but you have one or more objects within that process that expose interfaces with special security requirements. In this case, you can call [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity) to set security for the process, allowing COM to handle most of the security checks, and you can call other methods to set security for the objects with special security needs. Calling these methods and functions is described in [Setting Security at the Interface Proxy Level](setting-security-at-the-interface-proxy-level.md).

If your application has very specialized security requirements, such as allowing certain groups access to different objects depending on the time of day, you might want to handle all of your security programmatically, ensuring that COM does no automatic checking for you at all. To do this, you must call [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity), setting the *dwAuthnLevel* parameter to none and the *pVoid* parameter to **NULL**. If you have your own security package you would also need to register it in the *pAuthnSvc* parameter. Then you can handle all of your own security programmatically through calls to the proxy-level interface and functions described in [Setting Security at the Interface Proxy Level](setting-security-at-the-interface-proxy-level.md).

[**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity) offers a rich set of capabilities. If you call **CoInitializeSecurity**, the registry values are ignored and the security initialization values you pass in to the call are used instead. Depending on the result you want, the first parameter, *pVoid*, can point to three different types of values: a [**SECURITY\_DESCRIPTOR**](/windows/desktop/api/winnt/ns-winnt-security_descriptor) , an [**IAccessControl**](/windows/desktop/api/IAccess/nn-iaccess-iaccesscontrol) object, or a pointer to an AppID. In most cases, you will use Windows functions to create a **SECURITY\_DESCRIPTOR** that *pVoid* will point to.

However, *pVoid* can also point to an [**IAccessControl**](/windows/desktop/api/IAccess/nn-iaccess-iaccesscontrol) object.

To indicate to [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity) that you are passing an [**IAccessControl**](/windows/desktop/api/IAccess/nn-iaccess-iaccesscontrol) object to *pVoid*, you must pass the EOAC\_ACCESS\_CONTROL value to the *dwCapabilities* parameter. Since **CoInitializeSecurity** caches the results of access checks, the access control list must not be changed after calling **CoInitializeSecurity**.

Another type of value you can pass to the *pVoid* parameter is a pointer to a GUID, which is the AppID of your application. If *pVoid* is a pointer to an AppID, you must specify EOAC\_APPID in the *pCapabilities* parameter so that the function knows what value to expect in *pVoid*. If *pVoid* points to an AppID, [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity) uses only the registry for authentication values and ignores all other parameters to **CoInitializeSecurity**.

## Related topics

<dl> <dt>

[Setting Process-Wide Security](setting-processwide-security.md)
</dt> </dl>

 

 