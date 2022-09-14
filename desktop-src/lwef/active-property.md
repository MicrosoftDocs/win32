---
title: Active Property
description: Active Property
ms.assetid: 76ada073-782a-4355-b4e8-42dd84d0139b
ms.topic: article
ms.date: 05/31/2018
---

# Active Property

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Returns whether your application is the active client of the character and whether the character is topmost.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent.***Characters****("***CharacterID***").Active** \[ = *State*\]



| Part    | Description                                                                                                                                                                                                |
|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *state* | An integer expression specifying the state of your client application. 0 Not the active client.<br/> 1 The active client. <br/> 2 The input-active client. (The topmost character.)<br/> |



 

</dd> </dl>

## Remarks

When multiple client applications share the same character, the active client of the character receives mouse input (for example, Microsoft Agent control [**Click**](click-event.md) or [DragStart](dragstart-event.md) events). Similarly, when multiple characters are displayed, the active client of the topmost character (also known as the input-active client) receives Command events.

You can use the [**Activate**](activate-method.md)method to set whether your application is the active client of the character or to make your application the input active client (which also makes the character topmost).

## See Also

[****Activate** method**](activate-method.md)


 

 





