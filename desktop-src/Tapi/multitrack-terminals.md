---
description: TAPI 3.1 introduces the notion of a multitrack terminal, a terminal that, in essence, is a collection of &\#0034;track&\#0034; terminals.
ms.assetid: '8dd6f792-a29e-40fd-9f5b-ee5525028c2e'
title: Multitrack Terminals
ms.topic: article
ms.date: 05/31/2018
---

# Multitrack Terminals

TAPI 3.1 introduces the notion of a multitrack terminal, a terminal that, in essence, is a collection of "track" terminals. Multitrack terminals ease the programmer's load in situations where multiple media streams are involved in a communications session.

The [File Recording Terminal](file-playback-terminal-and-file-recording-terminal.md) is an example of a multitrack terminal. It consists of "tracks," where each "track" is a terminal corresponding to a stream in the recorded file.

A [track terminal](track-terminals.md) can be another multitrack terminal or a single-track terminal. A single-track terminal is a terminal that does not have any track terminals. A single-track terminal is a terminal in the TAPI 3 sense of the word.

For more information about multitrack terminals, see the following topics:

-   [About Multitrack Terminals](about-multitrack-terminals.md)
-   [Default Terminal Selection Mechanism](default-terminal-selection-mechanism.md)
-   [Manual Terminal Selection](manual-terminal-selection.md)
-   [Using Multitrack Terminals and the Default Selection Mechanism](using-multitrack-terminals-and-the-default-selection-mechanism.md)

 

 



