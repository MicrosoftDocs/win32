---
Description: This topic provides information on what's new in the Fax Service for Windows XP.
ms.assetid: 66bccf4e-85b3-4341-bc62-e9054018b532
title: What's New in Windows XP and Windows Server 2003
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# What's New in Windows XP and Windows Server 2003

This topic provides information on what's new in the Fax Service for Windows XP.

The Fax Service for Windows XP includes the [Fax Service Extended COM Implementation](-mfax-about-the-fax-service-extended-com-api.md), an extended Component Object Model (COM) API. This API gives you full access to old and new fax features through standard COM interfaces. Through the extended COM, fax administrators have better control of the service, particularly through scripting.

The security model for the fax service has been improved. It includes more specific access rights, and features easier administration.

Beginning with Windows Server 2003, fax service providers (FSPs) and Routing Extensions are loaded into a provider subsystem with the [NetworkService](http://msdn.microsoft.com/library/en-us/dllproc/base/networkservice_account.asp) security account, rather than the [LocalSystem](http://msdn.microsoft.com/library/en-us/dllproc/base/localsystem_account.asp) security account. For more information, see [Fax Service Provider and Routing Extension Hosting and Security](-mfax-fax-service-provider-and-routing-extension-hosting-and-security.md).

The Fax Service provides an extensible Microsoft Management Console (MMC) Administration console for UI customization, as described in the [MMC Snap-in Extensibility Guide](-mfax-mmc-snap-in-extensibility-guide.md).

The [Fax Extension Configuration API](-mfax-about-the-fax-extension-configuration-api.md) allows you to persistently store FSP and Routing Extension configurations without having to write directly to the Fax Service registry.

Other new features:

-   Archives for sent and received faxes.
-   Activity logging, which is useful for reporting and billing purposes.
-   Outbound routing, which allows an administrator to define which devices are used for outbound faxes to each country/region code and area code.
-   Outgoing fax priority settings.
-   Inbound routing, which sends incoming faxes to email addresses using Simple Mail Transport Protocol (SMTP).
-   Support for new types of receipts (delivery notifications), including message boxes and SMTP-based email receipts.

 

 



