---
title: Determining Your Security Needs
description: How you set up COM security for your application depends on what kind of security your application needs. There are several common situations that determine what you should do.
ms.assetid: db5c9adb-b04b-4621-b738-2959cac40985
ms.topic: article
ms.date: 05/31/2018
---

# Determining Your Security Needs

How you set up COM security for your application depends on what kind of security your application needs. There are several common situations that determine what you should do.

If you decide to use the COM security defaults, you do not have to do anythingâ€”COM handles it all. For information on what these default settings are, see [COM Security Defaults](com-security-defaults.md).

You can also prevent any remote calls into your machine by disabling DCOM altogether (COM between remote computers). For more information, see [Setting System-Wide Security Using DCOMCNFG](setting-machine-wide-security-using-dcomcnfg.md).

For legacy or new applications, you can set process-wide security in the registry. For more information, see [Setting Processwide Security Through the Registry](setting-processwide-security-through-the-registry.md).

You can also override default security settings for calls to certain interfaces in the process while setting default security for the remainder of the process (to allow COM to handle the general cases). For more information, see [Setting Security at the Interface Proxy Level](setting-security-at-the-interface-proxy-level.md).

For complex security requirements, you can handle all security programmatically rather than allowing COM to handle it for you. To do this, call [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity) to disable automatic authentication, and then control all the security settings by setting security on a per-interface proxy basis. For more information, see [Setting Processwide Security with CoInitializeSecurity](setting-processwide-security-with-coinitializesecurity.md) and [Setting Security at the Interface Proxy Level](setting-security-at-the-interface-proxy-level.md).

In some scenarios, you might want to turn off security completely. You might decide that your application does not need any security, or you might want to disable security during development time so that you can enable security features individually. To learn how to disable COM security, see [Turning Off Security](turning-off-security.md).

Security in COM relies on authentication services administered by security packages. NTLMSSP works well for many applications but does not provide the more robust security offered by other packages. Therefore, COM supports the Schannel security package and the Kerberos v5 security protocol. For more details on using these security packages, see [COM and Security Packages](com-and-security-packages.md).

## Related topics

<dl> <dt>

[Security in COM](security-in-com.md)
</dt> </dl>

 

 




