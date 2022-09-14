---
title: Visible Property (Balloon Object)
description: Learn about the Visible Property of the Balloon object, which returns or sets the visible setting for the word balloon for the specified character.
ms.assetid: cbda7f69-889a-45a0-9549-d27eddfcec57
ms.topic: article
ms.date: 05/31/2018
---

# Visible Property (Balloon Object)

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Returns or sets the visible setting for the word balloon for the specified character.

</dd> <dt>

<span id="Syntax_"></span><span id="syntax_"></span><span id="SYNTAX_"></span>**Syntax** 
</dt> <dd>

*agent***.Characters(**"*CharacterID*"**).Balloon.Visible** \[ = *boolean*\]



| Part      | Description                                                                                                                                                             |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *boolean* | A Boolean expression specifying whether the word balloon is visible.<br/> **True** The balloon is visible.<br/> **False** The balloon is hidden.<br/> |



 

</dd> </dl>

## Remarks

If you follow a [**Speak**](speak-method.md) or [**Think**](think-method.md) call with a statement to attempt to change the balloon's property, it may not affect the balloon's Visible state because the **Speak** or **Think** call gets queued, but the call setting the balloon's visible state does not. Therefore, only set this value when no **Speak** or **Think** calls are in the character's queue.

If you attempt to set this property while the character is speaking, moving, or being dragged, the property setting does not take effect until the preceding operation is completed.

Calling the [**Speak**](speak-method.md) and [**Think**](think-method.md) methods automatically makes the balloon visible, setting the [**Visible**](visible-property.md) property to **True**. If the character's balloon AutoHide property is enabled, the balloon is automatically hidden after the output text is spoken. Clicking or dragging a character that is not currently speaking also automatically hides the balloon even if its AutoHide setting is disabled. You can change the character's AutoHide setting using the balloon's [**Style**](style-property.md) property.

### See Also

[**Style property**](style-property.md)


 

 





