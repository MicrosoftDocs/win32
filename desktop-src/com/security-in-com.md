---
title: Security in COM
description: Security in COM is firmly based on the security provided by Windows and the underlying RPC security mechanisms.
ms.assetid: c9f6d06c-da24-48ea-908a-2462c33f7ee3
ms.topic: article
ms.date: 05/31/2018
---

# Security in COM

Security in COM is firmly based on the security provided by Windows and the underlying RPC security mechanisms. COM security relies on *authentication* (the process of verifying a caller's identity) and *authorization* (the process of determining whether a caller is authorized to do what it is asking to do). There are two main types of security in COM: *activation security* and *call security*. Activation security determines whether a client can launch a server at all. After a server has been launched, you can use call security to control access to a server's objects.

In this security model, servers manage and help protect objects, clients get access to objects through servers, and servers can attempt access while impersonating the client.

The system implements the Kerberos v5 authentication protocol and the Schannel security package. It also includes features such as delegate-level impersonation, mutual authentication, the ability to set authentication levels for an AppID in the registry, and cloaking. Using COM security, you can implement objects that can perform privileged operations without compromising security.

Because there is a wide range of COM security features available, it is helpful to initially determine what kind of security your application needs. For most applications, setting an acceptable level of security can be a painless process, but you can also use COM security to support very complex security scenarios.

You can set security processwide, either by using Dcomcnfg.exe to set the registry or by calling [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity). Two primary interfaces, [**IClientSecurity**](/windows/desktop/api/ObjIdl/nn-objidl-iclientsecurity) and [**IServerSecurity**](/windows/win32/api/objidlbase/nn-objidlbase-iserversecurity) (and associated helper functions), allow you to set call-level security within your program.

To learn more about COM security, see the following topics:

-   [Determining Your Security Needs](determining-your-security-needs.md)
-   [COM Security Defaults](com-security-defaults.md)
-   [Activation Security](activation-security.md)
-   [Security Values](security-values.md)
-   [Setting Security for COM Applications](setting-security-for-com-applications.md)
-   [Enabling COM Security Using DCOMCNFG](enabling-com-security-using-dcomcnfg.md)
-   [Turning Off Security](turning-off-security.md)
-   [Server-Side Security](server-side-security.md)
-   [Security Blanket Negotiation](security-blanket-negotiation.md)
-   [COM and Security Packages](com-and-security-packages.md)
-   [DCOM Security Enhancements in Windows XP Service Pack 2 and Windows Server 2003 Service Pack 1](dcom-security-enhancements-in-windows-xp-service-pack-2-and-windows-server-2003-service-pack-1.md)
-   [Access Control Lists for COM](access-control-lists-for-com.md)
-   [The COM Elevation Moniker](the-com-elevation-moniker.md)

 

 