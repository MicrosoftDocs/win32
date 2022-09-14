---
title: Ctx Tag
description: Ctx Tag
ms.assetid: 96ceaa98-869d-4c51-a419-882cc9d40ae2
ms.topic: article
ms.date: 05/31/2018
---

# Ctx Tag

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Sets the context of the output text.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

\\**Ctx**=*string*\\



| Part     | Description                                                                                                                                                                                                                                                                                      |
|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *string* | A string specifying the context of the text that follows, which determines how symbols or abbreviations are spoken.<br/> **"Address"**    Addresses and/or phone numbers.<br/> **"E-mail"**    Electronic mail.<br/> **"Unknown"**    (Default) Context is unknown.<br/> |



 

</dd> </dl>

### Remarks

This tag is supported only for TTS-generated output. The range of values for the parameter may vary depending on the installed TTS engine.

 

 





