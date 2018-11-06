---
title: ITTSBufNotifySinkW
description: ITTSBufNotifySinkW
ms.assetid: 00f4a529-2db1-4cad-9340-ed95999448f7
ms.topic: article
ms.date: 05/31/2018
---

# ITTSBufNotifySinkW

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

The engine must call out through **BookMark**. During preprocessing of speech output, Microsoft Agent code inserts bookmarks between "words" and uses the arrival of those bookmarks to drive the pacing of text in the word balloon. While SAPI does not require anything more than the arrival of those bookmarks at some time before the end of the utterance, the bookmarks must be returned in a relatively timely fashion to support Microsoft Agent.

Note that there is no strict concept of "word" in some languages, such as Japanese. Microsoft Agent's [**Speak**](speak-method.md) method defines a "word" as a connected string of symbols that has a meaning and pronunciation in isolation. Microsoft Agent uses fairly simple parsing code to determine what a "word" is: it looks for symbols separated by white space. Thus, there are three "words" in the English string "The 101 Dalmatians": "the", "one hundred and one", and "Dalmatians". Text included in the Microsoft Agent Map tag is treated as a single "word" for display purposes.

 

 




