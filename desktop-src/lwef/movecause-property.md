---
title: MoveCause Property
description: MoveCause Property
ms.assetid: 8f78a6da-8498-4a39-a4b9-5ab7a43d97f5
ms.topic: article
ms.date: 05/31/2018
---

# MoveCause Property

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Returns an integer value that specifies what caused the character's last move.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent*.**Characters("***CharacterID***").MoveCause**



| Value | Description                                                                                |
|-------|--------------------------------------------------------------------------------------------|
| 0     | The character has not been moved.                                                          |
| 1     | The user moved the character.                                                              |
| 2     | Your application moved the character.                                                      |
| 3     | Another client application moved the character.                                            |
| 4     | The Agent server moved the character to keep it onscreen after a screen resolution change. |



 

</dd> </dl>

## Remarks

You can use this property to determine what caused the character to move, when more than one application is sharing (has loaded) the same character. These values are the same as those returned by the [**Move**](move-event.md) event.

## See Also

[**Move event**](move-event.md), [**MoveTo method**](moveto-method.md)


 

 




