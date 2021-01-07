---
description: The lexicon, or list of possible words used by a particular recognizer's language model, is contained in one or more dictionaries.
ms.assetid: e975a75f-ab88-4164-afc8-3b817988504d
title: Dictionaries and Phrase lists
ms.topic: article
ms.date: 05/31/2018
---

# Dictionaries and Phrase lists

The lexicon, or list of possible words used by a particular recognizer's language model, is contained in one or more dictionaries. The recognizer searches all dictionaries available on the system when compiling recognition matches. You can use the Microsoft Speech APIs (SAPI) to modify some of these dictionaries.

A phrase list provides another means of modifying the recognizer's vocabulary. Adding words to a phrase list extends the vocabulary; adding words and then constraining the recognizer to use only the phrase list (as opposed to the phrase list and the dictionaries) restricts the vocabulary.

Previous releases of the Tablet PC Technology APIs relied on the concept of word lists. Word lists are almost identical to phrase lists and are used for the same purpose when working directly with a [**RecognizerContext**](inkrecognizercontext-class.md) object in an application that is ink enabled. For more details about where and when to use word lists, see [Setting Context for Ink-Enabled Controls](setting-context-for-ink-enabled-controls.md).

When the size of the list with which you want to extend the lexicon exceeds 100,000 words, we recommend that you use a dictionary instead of a word list or phrase list.

 

 



