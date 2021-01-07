---
description: Exit modules receive notifications from the server engine when operations such as the issuance of a certificate occur.
ms.assetid: 5e7ee1f4-7e07-4a08-8e72-89b449804bc2
title: Exit Modules
ms.topic: article
ms.date: 05/31/2018
---

# Exit Modules

Exit modules receive notifications from the server engine when operations such as the issuance of a certificate occur. An exit module is implemented as a [*dynamic-link library*](../secgloss/d-gly.md) (DLL). A typical operation for an exit module is to publish a completed certificate in a specified location (the default enterprise certification authority exit module, for instance, publishes user certificates and [*certificate revocation lists*](../secgloss/c-gly.md) (CRLs) to the Active Directory). An exit module can use the [**ICertServerExit**](/windows/desktop/api/Certif/nn-certif-icertserverexit) interface to communicate with Certificate Services. Certificate Services communicates with an exit module by means of direct COM calls or, if the module does not support direct COM calls, by means of Automation.

An exit module may view existing certificate properties and extensions, and it may also view request attributes and properties. An exit module cannot, however, modify any properties.

Certificate Services provides a default exit module, but you can also create custom exit modules to meet special needs. However, before writing a custom exit module, consider using the default exit module. Moreover, for an enterprise certification authority, the default exit module should always be used, even though you can add additional, custom exit modules. For more information, see [Writing Custom Exit Modules](writing-custom-exit-modules.md).

 

 
