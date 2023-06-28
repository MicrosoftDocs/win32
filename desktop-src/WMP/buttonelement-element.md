---
title: BUTTONELEMENT Element
description: BUTTONELEMENT Element
ms.assetid: 2c1bac51-8aea-4c73-b9b4-4ddbf1e4231b
keywords:
- Windows Media Player skins,BUTTONELEMENT element
- skins,BUTTONELEMENT element
- BUTTONELEMENT element
- reference for skins,BUTTONELEMENT element
- elements,BUTTONELEMENT
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# BUTTONELEMENT Element

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **BUTTONELEMENT** element defines a single button within a parent **BUTTONGROUP** element. It supports the following attributes. Predefined **BUTTONELEMENT** elements are also provided for convenience.

The **BUTTONELEMENT** element supports the following attributes.



| Attribute                                      | Description                                                                                                                                                                                                      |
|------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [cursor](buttonelement-cursor.md)             | Specifies or retrieves the value of the **BUTTONELEMENT** cursor that appears when the mouse is over the **BUTTONELEMENT**.                                                                                      |
| [down](buttonelement-down.md)                 | Specifies or retrieves the up or down value of the **BUTTONELEMENT**.                                                                                                                                            |
| [downToolTip](buttonelement-downtooltip.md)   | Specifies or retrieves the ToolTip text that appears when the mouse is over the **BUTTONELEMENT** and the **BUTTONELEMENT** is in the down state.                                                                |
| [index](buttonelement-index.md)               | Retrieves the index of the **BUTTONELEMENT** within the **BUTTONGROUP**.                                                                                                                                         |
| [mappingColor](buttonelement-mappingcolor.md) | Specifies or retrieves the color key that identifies this **BUTTONELEMENT** in the **BUTTONELEMENT** group.                                                                                                      |
| [sticky](buttonelement-sticky.md)             | Specifies or retrieves a value indicating whether the **BUTTONELEMENT** is sticky. When sticky, a **BUTTONELEMENT** will change states after being clicked and will remain in the new state until clicked again. |
| [upToolTip](buttonelement-uptooltip.md)       | Specifies or retrieves the ToolTip text that appears when the mouse is over the **BUTTONELEMENT** and the **BUTTONELEMENT** is in the up or active state.                                                        |



 

The **BUTTONELEMENT** element supports the following method.



| Method                           | Description                                                            |
|----------------------------------|------------------------------------------------------------------------|
| [click](buttonelement-click.md) | Calls the **onclick** event handler defined for the **BUTTONELEMENT**. |



 

The **BUTTONELEMENT** element can implement the ambient event handlers. For more information, see [Ambient Event Handlers](ambient-event-handlers.md).

The **BUTTONELEMENT** element supports the following ambient attributes: [enabled](ambientattributes-enabled.md) and [tabStop](ambientattributes-tabstop.md).

Predefined effects are normal **EFFECTS** elements with various common attribute settings specified by default. The following predefined **BUTTONELEMENT** elements are available.



| Predefined BUTTONELEMENT         | Description                                                                                               |
|----------------------------------|-----------------------------------------------------------------------------------------------------------|
| [FFWDELEMENT](ffwdelement.md)   | A **BUTTONELEMENT** with a built in **onclick** event handler that calls **player.controls.fastForward**. |
| [NEXTELEMENT](nextelement.md)   | A **BUTTONELEMENT** with a built in **onclick** event handler that calls **player.controls.next**.        |
| [PAUSEELEMENT](pauseelement.md) | A **BUTTONELEMENT** with a built in **onclick** event handler that calls **player.controls.pause**.       |
| [PLAYELEMENT](playerelement.md) | A **BUTTONELEMENT** with a built in **onclick** event handler that calls **player.controls.play**.        |
| [PREVELEMENT](prevelement.md)   | A **BUTTONELEMENT** with a built in **onclick** event handler that calls **player.controls.previous**.    |
| [REWELEMENT](rewelement.md)     | A **BUTTONELEMENT** with a built in **onclick** event handler that calls **player.controls.rewind**.      |
| [STOPELEMENT](stopelement.md)   | A **BUTTONELEMENT** with a built in **onclick** event handler that calls **player.controls.stop**.        |



 

## Related topics

<dl> <dt>

[**Skin Programming Reference**](skin-programming-reference.md)
</dt> </dl>

 

 




