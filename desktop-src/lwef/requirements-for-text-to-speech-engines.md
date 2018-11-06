---
title: Requirements for Text-To-Speech Engines
description: Requirements for Text-To-Speech Engines
ms.assetid: 21d19949-c9b4-4d9c-9684-6d15162f7a7d
ms.topic: article
ms.date: 05/31/2018
---

# Requirements for Text-To-Speech Engines

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

The engine must be fully SAPI 4.0-compliant. In addition, the engine must also support the following SAPI interfaces for tagged text and bookmark notifications. These interfaces enable Microsoft Agent to pace the output of text to a character's word balloon and lip-sync the character's mouth (or equivalent) with the spoken words.

-   [ITTSCentralW](ittscentralw.md)
-   [ITTSNotifySinkW](ittsnotifysinkw.md)
-   [ITTSBufNotifySinkW](ittsbufnotifysinkw.md)
-   [ITTSAttributesW](ittsattributesw.md)

 

 




