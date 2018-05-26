---
Description: The resource manager runs as a trusted service in a single process. All requests for smart card access are made to the resource manager, which routes them to the reader that contains the targeted card.
ms.assetid: 4a62588a-14d9-43dc-9572-25a9cbcd0efd
title: Resource Manager Implementation
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Resource Manager Implementation

The [*resource manager*](security.r_gly#-security-resource-manager-gly) runs as a trusted service in a single process. All requests for [*smart card*](security.s_gly#-security-smart-card-gly) access are made to the resource manager, which routes them to the [*reader*](security.r_gly#-security-reader-gly) that contains the targeted card.

Smart cards are often used in conjunction with security and personal privacy. Wherever possible, the resource manager uses the security mechanisms existing within the underlying operating system when accessing a reader or smart card.

 

 



