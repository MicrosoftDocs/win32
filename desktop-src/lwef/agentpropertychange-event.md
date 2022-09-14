---
title: AgentPropertyChange Event
description: AgentPropertyChange Event
ms.assetid: 56607e9c-99eb-42c1-987a-0f2bc3f82d75
ms.topic: article
ms.date: 05/31/2018
---

# AgentPropertyChange Event

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Occurs when the user changes a property in the Advanced Character Options window.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

**Sub** *agent.***AgentPropertyChange**

</dd> </dl>

### Remarks

This event indicates when the user has changed and applied any property included in the Advanced Character Option window.

In your code for this handling this event, you can query for the specific property settings of [AudioOutput](the-audiooutput-object.md) or [SpeechInput](the-speechinput-object.md) objects.

### See Also

[**DefaultCharacterChange event**](defaultcharacterchange-event.md)


 

 




