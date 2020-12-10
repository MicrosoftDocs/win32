---
title: HelpContextID Property (Commands Collection Object)
description: HelpContextID Property
ms.assetid: 8b8ac1c6-1a34-45f1-a0a6-2ae14ad6adef
ms.topic: article
ms.date: 05/31/2018
---

# HelpContextID Property (Commands Collection Object)

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Returns or sets an associated context number for the [**Commands**](/windows/desktop/lwef/the-commands-collection-object) object. Used to provide context-sensitive Help for the **Commands** object.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent.***Characters("***CharacterID***").Commands("***name***").HelpContextID** \[ = *Number*\]



| Part     | Description                                   |
|----------|-----------------------------------------------|
| *Number* | An integer specifying a valid context number. |



 

</dd> </dl>

## Remarks

If you've created a Windows Help file for your application and set the character's [**HelpFile**](helpfile-property.md) property, Agent automatically calls Help when [**HelpModeOn**](helpmodeon-property.md) is set to **True** and the user selects the [**Commands**](/windows/desktop/lwef/the-commands-collection-object) object. If you set a context number in the **HelpContextID**, Agent calls Help and searches for the topic identified by that context number.

This property applies only to your client application's use of the character; the setting does not affect other clients of the character or other characters of your client application.

> [!Note]  
> Building a Help file requires the Microsoft Windows Help Compiler.

 

## See Also

[**HelpFile property**](helpfile-property.md)


 

 
