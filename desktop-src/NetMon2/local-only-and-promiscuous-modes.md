---
description: Monitors can examine frames in local-only mode or promiscuous mode.
ms.assetid: 4646f5bb-e3e3-4929-91b7-f68c5b70ccb3
title: Local-Only and Promiscuous Modes
ms.topic: article
ms.date: 05/31/2018
---

# Local-Only and Promiscuous Modes

Monitors can examine frames in local-only mode or promiscuous mode.

In local-only mode, the network packet provider (NPP) returns frames that are sent to or from the computer on which the monitor is running, including broadcasts and multicasts directed to the local machine. Although limited to locally directed frames, local-mode is also much less processor intensive.

In promiscuous mode, the monitor can also watch for traffic that is not directed to or from the local computer. Unless the monitor has specified the flag, MCS\_CREATE\_PMODE\_NOT\_REQUIRED, in the [OnLoadingDLL](onloadingdll.md) function, the Monitor Control Service (MCSVC) assumes that the monitor requires promiscuous mode when it loads the monitor DLL.

 

 



