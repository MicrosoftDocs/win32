---
title: ActiveClientChange Event
description: ActiveClientChange Event
ms.assetid: 617b40e6-cafb-463e-8b36-2a12c468d3ae
ms.topic: article
ms.date: 05/31/2018
---

# ActiveClientChange Event

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Occurs when the active client of the character changes.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

**Sub** *agent.*ActiveClientChange (ByVal *CharacterID*, ByVal *Active* **)**



| Part          | Description                                                                                                                                                                                                                                                        |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *CharacterID* | Returns the ID of the character for which the event occurred.                                                                                                                                                                                                      |
| *Active*      | A Boolean value that indicates whether the client became active or not active. **True** The client application became the active client of the character. <br/> **False** The client application is no longer the active client of the character.<br/> |



 

</dd> </dl>

### Remarks

When multiple client applications share the same character, the active client of the character receives mouse input (for example, Microsoft Agent control click or drag events). Similarly, when multiple characters are displayed, the active client of the topmost character (also known as the input-active client) receives [Command](command-event.md) events.

When the active client of a character changes, this event passes back the ID of that character and **True** if your application has become the active client of the character or **False** if it is no longer the active client of the character.

A client application may receive this event when the user selects a client application's entry in character's pop-up menu or by voice command, when the client application changes its active status, or when another client application quits its connection to Agent. Agent sends this event only to the client applications that are directly affected; that either become the active client or stop being the active client.

### See Also

[****ActivateInput** event**](activateinput-event.md), [****Active** property**](active-property.md), [****DeactivateInput** event**](deactivateinput-event.md), [****Activate** method**](activate-method.md)


 

 





