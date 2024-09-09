---
title: EAP Implementation Details
description: Access Points (APs), such as Remote Access Service (RAS), interact with EAP implementations through the use of function calls that must be exported by the third-party EAP DLL.
ms.assetid: 85775c03-7538-41a1-9f83-42e71025a79c
ms.topic: article
ms.date: 06/14/2023
ms.contributor: samyun
---

# EAP Implementation Details

Access Points (APs), such as Remote Access Service (RAS), interact with EAP implementations through the use of function calls that must be exported by the third-party EAP DLL. In other words, EAP is a provider API, meaning that plug-ins or DLLs implement code to become an EAP provider, but must not call the EAP APIs themselves. For example, a programmer of an EAP DLL creates code for an EAP initialization routine and places this code in the EAP predefined function [**RasEapInitialize**](/previous-versions/windows/desktop/legacy/aa363527(v=vs.85)). Then at run-time, the AP connection manager calls the **RasEapInitialize** function, which contains the code, to initialize the EAP implementation.

The following topics detail this interaction:

- [Access Point Initialization of EAP](ras-initialization-of-eap.md)
- [Authentication Protocol Initialization](authentication-protocol-initialization.md)
- [Access Point and Authentication Protocol Interaction](ras-and-authentication-protocol-interaction-during-authentication.md)
- [Completion of the Authentication Session](completion-of-the-authentication-session.md)
