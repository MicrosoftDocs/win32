---
title: Publishing Under a Computer Object
description: Typically, host-based services create SCPs under the computer object for the host computer. Host-based services are services closely tied to a single host computer.
ms.assetid: ecd7d8bc-4714-408a-856c-7cab8360bf81
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Publishing Under a Computer Object

Typically, host-based services create SCPs under the computer object for the host computer. Host-based services are services closely tied to a single host computer.

**To create SCPs under a computer object**

1.  Call the [**GetComputerObjectName**](/windows/desktop/api/secext/nf-secext-getcomputerobjectnamea) function to get the distinguished name (DN) in the directory of the computer object for the local computer.
2.  Use that DN to bind to the computer object and create the SCP.

For more information and a code example, see [How Clients Find and Use a Service Connection Point](how-clients-find-and-use-a-service-connection-point.md).

Be aware that only domain-member computers have valid computer objects in the directory.

To get the DNS or NetBIOS name of the local computer, call the [**GetComputerNameEx**](/windows/desktop/api/sysinfoapi/nf-sysinfoapi-getcomputernameexa) function.

 

 