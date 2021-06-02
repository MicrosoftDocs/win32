---
description: Writing a secure provider requires considering how the provider is hosted, how the provider handles impersonation, and ensuring that users are checked for access rights to data.
ms.assetid: 9a8b7730-cbb8-48fa-8a8f-8e551f00d20b
ms.tgt_platform: multiple
title: Securing Your Provider
ms.topic: article
ms.date: 05/31/2018
---

# Securing Your Provider

Writing a secure provider requires considering how the provider is hosted, how the provider handles impersonation, and ensuring that users are checked for access rights to data. You can secure the data in your provider namespace by requiring that data be encrypted authentication before sending it over a network. For more information, see [Requiring an Encrypted Connection to a Namespace](requiring-an-encrypted-connection-to-a-namespace.md).

If a user has **FULL\_WRITE** access in any namespace, then the user can create cross-namespace subscriptions for data in a namespace in which the user is restricted. Because a provider can be loaded into any namespace and be executing in any security context, the provider should perform its own access checks to ensure that only authorized users are allowed access to data or to execute methods. For more information, see [Performing Access Checks](performing-access-checks.md).

The following topics discuss provider security:

-   [Provider Hosting and Security](provider-hosting-and-security.md)
-   [Performing Access Checks](performing-access-checks.md)
-   [Registry Keys for Controlling Provider Security](registry-keys-for-controlling-provider-security-.md)
-   [Access to WMI Namespaces](access-to-wmi-namespaces.md)
-   [Impersonating a Client](impersonating-a-client.md)

The following topics discuss how clients and scripts interact with provider security:

-   [Setting Authentication in WMI](setting-authentication-in-wmi.md)
-   [Connecting Between Different Operating Systems](/windows/desktop/WmiSdk/troubleshooting-a-remote-wmi-connection)
-   [Setting the Default Process Security Level Using VBScript](setting-the-default-process-security-level-using-vbscript.md)
-   [Setting Client Application Process Security](setting-client-application-process-security.md)

## Related topics

<dl> <dt>

[Maintaining WMI Security](maintaining-wmi-security.md)
</dt> <dt>

[Using WMI](using-wmi.md)
</dt> </dl>

 

 
