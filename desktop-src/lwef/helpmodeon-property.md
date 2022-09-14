---
title: HelpModeOn Property
description: HelpModeOn Property
ms.assetid: 4a9b5fd3-12e2-489b-8ce0-9b66b01f517a
ms.topic: article
ms.date: 05/31/2018
---

# HelpModeOn Property

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Returns or sets whether context-sensitive Help mode is on for the character.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent.***Characters("***CharacterID***").HelpModeOn** \[ = *boolean*\]



| Part      | Description                                                                                                                                                       |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *boolean* | A Boolean expression specifying whether context-sensitive Help mode is on. **True** Help mode is on. <br/> **False** (Default) Help mode is off.<br/> |



 

</dd> </dl>

## Remarks

When you set this property to **True**, the mouse pointer changes to the context-sensitive Help image when moved over the character or over the pop-up menu for the character. When the user clicks or drags the character or clicks an item in the character's pop-up menu, the server triggers the [**HelpComplete**](helpcomplete-event.md) event and exits Help mode.

In Help mode, the server does not send the [**Click**](click-event.md), [**DragStart**](dragstart-event.md), [**DragComplete**](dragcomplete-event.md), and [**Command**](command-event.md) events, unless you set the [**AutoPopupMenu**](autopopupmenu-property.md) property to **True**. In that case, the server will send the **Click** event (does not exit Help mode), but only for the right mouse button to enable you to display the pop-up menu.

This property applies only to your client application's use of the character; the setting does not affect other clients of the character or other characters of your client application.

## See Also

[**HelpComplete event**](helpcomplete-event.md)


 

 





