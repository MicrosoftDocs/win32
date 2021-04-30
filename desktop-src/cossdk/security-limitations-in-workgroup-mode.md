---
description: Security Limitations in Workgroup Mode
ms.assetid: 05c0aba7-b94b-49d4-a0fc-1ff0a23550b3
title: Security Limitations in Workgroup Mode
ms.topic: article
ms.date: 05/31/2018
---

# Security Limitations in Workgroup Mode

The [Message Queuing](/previous-versions/windows/desktop/legacy/ms711472(v=vs.85)) workgroup configuration does not permit the COM+ queued components service to support application security. If you've installed Message Queuing with the workgroup configuration, you must [disable security](specifying-the-authentication-protocol.md) on each queued application accessed in this configuration by selecting **Do not authenticate messages** on the **Queuing** tab for the COM+ application's **Properties** dialog, using the Component Services administrative tool. This should be done only on a trusted network and must be done at both client and server if the application has already been exported.

 

 



