---
title: EAP Installation
description: Vendors implement EAPs, also known as authentication protocols, in dynamic-link libraries (DLLs).
ms.assetid: af10b1e9-45c9-4640-ba79-fc9c23cc3c47
ms.topic: article
ms.date: 05/31/2018
---

# EAP Installation

Vendors implement EAPs, also known as authentication protocols, in dynamic-link libraries (DLLs). A DLL for the authentication protocol must reside on both the client and server computers. For simplicity, the client and server DLLs may be identical; however, this is not a requirement. Also, be aware that the same DLL may support more than one authentication protocol.

The vendor should provide setup software to install and remove the DLL. The setup software should also create the appropriate keys and values for the authentication protocol in the system registry and remove them upon uninstall.

The installation of each EAP DLL should create the following registry key.

**HKEY\_LOCAL\_MACHINE**\\**System**\\**CurrentControlSet**\\**Services**\\**Rasman**\\**PPP**\\**EAP**\\**&lt;eaptypeid&gt;**

In the preceding path, **&lt;eaptypeid&gt;** is the ID of the authentication protocol. The vendor must obtain this ID from the Internet Assigned Numbers Authority (IANA).

For more information and a description of the supported values for this key, see [Authentication Protocol Registry Values](authentication-protocol-registry-values.md).

 

 




