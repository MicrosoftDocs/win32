---
title: HelpContextID Property (Command Object)
description: HelpContextID Property
ms.assetid: 9e30e3f7-1d12-4aa1-af0d-5a3b30f57e83
ms.topic: article
ms.date: 05/31/2018
---

# HelpContextID Property (Command Object)

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Returns or sets an associated context number for the [**Command**](/windows/desktop/lwef/the-command-object) object. Used to provide context-sensitive Help for the **Command** object.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent.***Characters("***CharacterID***").Commands("").HelpContextID** \[ = *Number*\]



| Part     | Description                                   |
|----------|-----------------------------------------------|
| *Number* | An integer specifying a valid context number. |



 

</dd> </dl>

## Remarks

If you've created a Windows Help file for your application and set the character's [**HelpFile**](helpfile-property.md) property to the file, Agent automatically calls Help when [**HelpModeOn**](helpmodeon-property.md) is set to **True** and the user selects the command. If you set a context number in the [**HelpContextID**](helpcontextid-property.md), Agent calls Help and searches for the topic identified by the current context number. The current context number is the value of **HelpContextID** for the command.

This property applies only to your client application's use of the character; the setting does not affect other clients of the character or other characters of your client application.

> [!Note]  
> Building a Help file requires the Microsoft Windows Help Compiler.

 

## See Also

[**HelpFile property**](helpfile-property.md)


 

 
