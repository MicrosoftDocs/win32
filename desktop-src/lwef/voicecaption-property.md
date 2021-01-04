---
title: VoiceCaption Property (Commands Object)
description: VoiceCaption Property
ms.assetid: 2c4fa175-fc2d-4474-b15f-7e838103a435
ms.topic: article
ms.date: 05/31/2018
---

# VoiceCaption Property (Commands Object)

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Returns or sets the text displayed for the [**Commands**](/windows/desktop/lwef/the-commands-collection-object) object in the Voice Commands Window.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent.***Characters("***CharacterID***").Commands.VoiceCaption** \[ = *string*\]



| Part     | Description                                               |
|----------|-----------------------------------------------------------|
| *string* | A string expression that evaluates to the text displayed. |



 

</dd> </dl>

## Remarks

If you set the [**Voice**](voice-property.md) property of your [**Commands**](/windows/desktop/lwef/the-commands-collection-object) collection, you will typically also set its **VoiceCaption** property. The **VoiceCaption** text setting appears in the Voice Commands Window when your client application is input-active and the character is visible. If this property is not set, the setting for the **Commands** collection's [**Caption**](caption-property.md) property determines the text displayed. When neither the **VoiceCaption** or **Caption** property is set, then commands in the collection appear in the Voice Commands Window under "(undefined command)" when your client application becomes input-active.

The **VoiceCaption** setting also determines the text displayed in the Listening Tip to indicate the commands for which the character listens.

## See Also

[Caption property](caption-property.md)


 

 
