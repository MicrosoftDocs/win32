---
title: HelpContextID Property (Characters Object)
description: HelpContextID Property
ms.assetid: 7ef190ba-c194-4386-a8d6-d32d902a1c03
ms.topic: article
ms.date: 05/31/2018
---

# HelpContextID Property (Characters Object)

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Returns or sets an associated context number for the character. Used to provide context-sensitive Help for the character.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent.***Characters("***CharacterID***").HelpContextID** \[ = *Number*\]



| Part     | Description                                   |
|----------|-----------------------------------------------|
| *Number* | An integer specifying a valid context number. |



 

</dd> </dl>

## Remarks

To support context-sensitive Help for the character, assign the context number to the character you use for the associated Help topic when you compile your Help file. This property applies only to the client of the character; the setting does not affect other clients of the character or other characters of the client.

If you've created a Windows Help file for your application and set the character's [**HelpFile**](helpfile-property.md) property, Agent automatically calls Help when [**HelpModeOn**](helpmodeon-property.md) is set to **True** and the user clicks the character. If there is a context number in the [**HelpContextID**](helpcontextid-property.md), Agent calls Help and searches for the topic identified by the current context number. The current context number is the value of **HelpContextID** for the character.

> [!Note]  
> Building a Help file requires the Microsoft Windows Help Compiler.

 

## See Also

[**HelpFile property**](helpfile-property.md)


 

 




