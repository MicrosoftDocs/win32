---
title: Caption Property (Command Object)
description: Caption Property
ms.assetid: 8dcdf3e0-3111-438b-9d39-ba9a36437ad2
ms.topic: article
ms.date: 05/31/2018
---

# Caption Property (Command Object)

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Determines the text displayed for a [**Command**](/windows/desktop/lwef/the-command-object) in the specified character's pop-up menu.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent***.Characters ("***CharacterID***").Commands("***name***").Caption** \[ = *string*\]



| Part     | Description                                                                                  |
|----------|----------------------------------------------------------------------------------------------|
| *string* | A string expression that evaluates to the text displayed as the caption for the **Command**. |



 

</dd> </dl>

## Remarks

To specify an access key (unlined mnemonic) for your **Caption**, include an ampersand (&) character before that character.

If you don't define a **VoiceCaption** for your command, your **Caption** setting will be used.

 

 
