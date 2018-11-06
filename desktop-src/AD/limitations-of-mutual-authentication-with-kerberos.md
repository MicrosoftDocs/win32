---
title: Limitations of Mutual Authentication with Kerberos
description: Both the client's account and the service's account must be in Windows 2000 native or mixed-mode domains because Kerberos services are not available in downlevel domains.
ms.assetid: 54685e88-b289-4db9-b4cb-f5c22a216a0d
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Limitations of Mutual Authentication with Kerberos

Both the client's account and the service's account must be in Windows 2000 native or mixed-mode domains because Kerberos services are not available in downlevel domains. In addition, both client and service accounts must be in the same forest because the client's KDC uses the global catalog to search for the service principal name.

Both service and client must be running on Windows 2000, otherwise mutual authentication with Kerberos will fail because earlier versions of Windows do not support Kerberos.

Service principal names must include the DNS name of the host server on which the service is running. You must use the DNS name.

 

 




