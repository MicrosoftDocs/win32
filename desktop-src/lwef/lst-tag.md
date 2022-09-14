---
title: Lst Tag
description: Lst Tag
ms.assetid: 82246675-9aa1-4603-a8f7-a5fd7b3f6be2
ms.topic: article
ms.date: 05/31/2018
---

# Lst Tag

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Repeats last spoken statement for the character.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

\\**Lst**\\

</dd> </dl>

### Remarks

This tag enables a character to repeat its last spoken statement. This tag must appear by itself in the [**Speak**](speak-method.md) method; no other text or parameters can be included. When the spoken text is repeated, any other tags included in the original text are repeated, except for bookmarks. Any .WAV and .LWV files included in the text are also repeated.

 

 




