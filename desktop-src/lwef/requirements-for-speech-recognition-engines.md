---
title: Requirements for Speech Recognition Engines
description: Requirements for Speech Recognition Engines
ms.assetid: 41aca5da-c680-41c1-b070-af291cb0c8e1
ms.topic: article
ms.date: 05/31/2018
---

# Requirements for Speech Recognition Engines

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

A speech recognition engine must also be a fully compliant Command and Control (C&C) engine according to SAPI 4.0. It must support multiple grammars in the binary format described in the specification and allow those grammars to be activated or deactivated in real time.

Note that SAPI 4.0 requires that speech recognition engines support the wide character, Unicode interfaces. However, in supporting these interfaces, the engine should not depend on converting Unicode data to ANSI, as the engine may not function correctly on some systems. For example, a Japanese engine that converts Unicode to ANSI may not work on an English-language Microsoft Windows 95 system.

In addition, to be considered Microsoft Agent-compliant, the engine must return results objects upon the successful recognition of a phrase (through ISRGramNotifySinkW::PhraseFinish). These results objects must support ISRResBasic, as the specification requires. In addition, they should support ISRResScore. Although Microsoft Agent will run with an engine that supports only ISRResBasic, or even with an engine that returns no results objects whatsoever, performance will usually be significantly poorer with such engines. Many applications use the confidence values provided by the engine to control how they respond to various commands.

 

 




