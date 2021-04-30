---
description: Policy modules are programs that receive requests from the Certificate Services, evaluate those requests, and specify optional properties of the certificates that are built to fill these requests.
ms.assetid: 23d920ea-af62-42ce-ad48-c7a03ab55fc9
title: Policy Modules
ms.topic: article
ms.date: 05/31/2018
---

# Policy Modules

Policy modules are programs that receive requests from the Certificate Services, evaluate those requests, and specify optional properties of the certificates that are built to fill these requests. A policy module is implemented as a [*dynamic-link library*](../secgloss/d-gly.md) (DLL). A policy module can use the [ICertServerPolicy](/windows/desktop/api/Certif/nn-certif-icertserverpolicy) interface to communicate with Certificate Services. Certificate Services communicates with a policy module by means of direct COM calls or, if the module does not support direct COM calls, by means of Automation.

A policy module may view existing certificate properties and extensions, and it may also view request attributes and properties. In addition, a policy module may set or modify certificate extensions and "NotBefore" and "NotAfter" properties, as well as the [*relative distinguished name*](../secgloss/r-gly.md) (RDN) of a Certificate Subject, subject to certain restrictions. A policy module ultimately issues or denies the [*certificate request*](../secgloss/c-gly.md) or holds it pending.

Before writing a custom policy module, consider using one of the default policy modules. Both the Certificate Services enterprise [*certification authority*](../secgloss/c-gly.md) (CA) and stand-alone CA ship with an appropriate default policy module. Both the enterprise and stand-alone default policy modules issue certificate requests (although the stand-alone default policy is to hold the certificate pending until it is manually issued by an administrator). An enterprise certification authority should use only the Microsoft-provided enterprise policy module.

The enterprise CA requires Active Directory. Additional features of its default policy module include certificate templates, [*access control list*](../secgloss/a-gly.md) (ACL) security on the certificate templates to ensure requests are issued to only those authorized, predefined extensions added to the issued certificate, and support for smart card domain logon certificates.

The default stand-alone CA policy module does not support many of the features of the default enterprise module, but it does support the issuance of smart card certificates. For specific details, as well as the most current capabilities of the default policy module, see the product documentation.

For installations where the default policy module is unacceptable, Certificate Services allows custom policy modules. For more information, see [Writing Custom Policy Modules](writing-custom-modules.md).

 

 
