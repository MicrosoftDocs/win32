---
title: VoiceCaption Property (Command Object)
description: VoiceCaption Property
ms.assetid: 97a3015c-6c39-42d5-b6bd-7563bd444b38
ms.topic: article
ms.date: 05/31/2018
---

# VoiceCaption Property (Command Object)

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Sets or returns the text displayed for the [**Command**](/windows/desktop/lwef/the-command-object) object in the Voice Commands Window.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent.***Characters("***CharacterID***").Commands("***Name***").VoiceCaption** \[ = *string*\]



| Part     | Description                                               |
|----------|-----------------------------------------------------------|
| *string* | A string expression that evaluates to the text displayed. |



 

</dd> </dl>

## Remarks

If you define a [**Command**](/windows/desktop/lwef/the-command-object) object in a [**Commands**](https://www.bing.com/search?q=**Commands**) collection and set its [**Voice**](voice-property.md) property, you will typically also set its [**VoiceCaption**](voicecaption-property.md) property. This text will appear in the Voice Commands Window when your client application is input-active and the character is visible. If this property is not set, the setting for the [**Caption**](caption-property.md) property determines the text displayed. When neither the **VoiceCaption** nor **Caption** property is set, the command does not appear in the Voice Commands Window.

### See Also

[**Caption property**](caption-property.md)


 

 
