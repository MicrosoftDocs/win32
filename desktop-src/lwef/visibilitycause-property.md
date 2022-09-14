---
title: VisibilityCause Property
description: VisibilityCause Property
ms.assetid: 106574ef-af5f-44cf-9efb-9e6da19ebc1f
ms.topic: article
ms.date: 05/31/2018
---

# VisibilityCause Property

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Returns an integer value that specifies what caused the character's visible state.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent*.**Characters("***CharacterID***").VisibilityCause**



| Value | Description                                                                                                  |
|-------|--------------------------------------------------------------------------------------------------------------|
| 0     | The character has not been shown.                                                                            |
| 1     | User hid the character using the command on the character's taskbar icon pop-up menu or using speech input.. |
| 2     | The user showed the character.                                                                               |
| 3     | Your application hid the character.                                                                          |
| 4     | Your application showed the character.                                                                       |
| 5     | Another client application hid the character.                                                                |
| 6     | Another client application showed the character.                                                             |
| 7     | The user hid the character using the command on the character's pop-up menu.                                 |



 

</dd> </dl>

## Remarks

You can use this property to determine what caused the character to move when more than one application is sharing (has loaded) the same character. These values are the same as those returned by the [**Show**](show-event.md) and [**Hide**](hide-event.md) events.

## See Also

[**Hide event**](hide-event.md), [**Show event**](show-event.md), [**Hide method**](hide-method.md), [**Show method**](show-method.md)


 

 




