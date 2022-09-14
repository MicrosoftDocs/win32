---
title: Publishing COM+ Services
description: COM-based services provide an application-proxy in the form of a Windows installer (MSI) package.
ms.assetid: 38200a22-bea5-4967-a51a-e777b34f299d
ms.tgt_platform: multiple
keywords:
- Publishing COM+ Services
- Active Directory, using, publishing a service, COM+ services
ms.topic: article
ms.date: 05/31/2018
---

# Publishing COM+ Services

COM-based services provide an application-proxy in the form of a Windows installer (MSI) package. This .msi file contains the server name to be used and other required elements, such as proxy/stubs and type libraries required for marshalling. The Component Services snap-in auto-generate these application proxies for COM+ Server applications.

The application proxies are published into policy objects in Active Directory using the Group Policy Editor. No special intervention is required in the client application. The computer/user account on the client computer must be in an OU configured to use the policy object in which the application proxies are published. The COM binder automatically locates the server by means of the directory when the client establishes an instance of the objects concerned.

 

 




