---
title: HelpFile Property
description: HelpFile Property
ms.assetid: 18a5fd9b-4ca7-4701-9993-1e0c55f6e232
ms.topic: article
ms.date: 05/31/2018
---

# HelpFile Property

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Returns or sets the path and filename for a Microsoft Windows context-sensitive Help file supplied by the client application.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent.***Characters("***CharacterID***").Helpfile** \[ = *Filename*\]



| Part       | Description                                                                    |
|------------|--------------------------------------------------------------------------------|
| *Filename* | A string expression specifying the path and filename of the Windows Help file. |



 

</dd> </dl>

## Remarks

If you've created a Windows Help file for your application and set the character's **HelpFile** property, Agent automatically calls Help when [**HelpModeOn**](helpmodeon-property.md) is set to **True** and the user clicks the character or selects a command from its pop-up menu. If you specified a context number in the [**HelpContextID**](helpcontextid-property.md) property of the selected command, Help displays a topic corresponding to the current Help context; otherwise it displays "No Help topic associated with this item."

This property applies only to your client application's use of the character; the setting does not affect other clients of the character or other characters of your client application.

## See Also

[**HelpModeOn property**](helpmodeon-property.md), [**HelpContextID property**](helpcontextid-property.md)


 

 




