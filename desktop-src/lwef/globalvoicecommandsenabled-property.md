---
title: GlobalVoiceCommandsEnabled Property
description: GlobalVoiceCommandsEnabled Property
ms.assetid: d4f74019-fa33-41fc-abe7-01791ff188f0
ms.topic: article
ms.date: 05/31/2018
---

# GlobalVoiceCommandsEnabled Property

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Returns or sets whether voice is enabled for Agent's global commands.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent.***Characters("***CharacterID***").Commands.GlobalVoiceCommandsEnabled**

\[ = *boolean*\]



| Part      | Description                                                                                                                                                                                                            |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *boolean* | A Boolean expression that indicates whether voice parameters for Agent's global commands are enabled. **True** (Default) Voice parameters are enabled. <br/> **False** Voice parameters are disabled.<br/> |



 

</dd> </dl>

## Remarks

Microsoft Agent automatically adds voice parameters (grammar) for opening and closing the Voice Commands Window and for showing and hiding the character. If you set **GlobalVoiceCommandsEnabled** to **False**, Agent disables any voice parameters for these commands as well as the voice parameters for the [**Caption**](caption-property.md) of other client's [**Commands**](/windows/desktop/lwef/the-commands-collection-object) objects. This enables you to eliminate these from your client's current active grammar. However, because this potentially blocks voice access to other clients, reset this property to **True** after processing the user's voice input.

Disabling the property does not affect the character's pop-up menu. The global commands added by the server will still appear. You cannot remove them from the pop-up menu.

 

