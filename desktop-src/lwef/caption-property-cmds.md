---
title: Caption Property (Commands Collection Object)
description: Learn about the Caption property of the Command Collection object. Microsoft Agent is deprecated as of Windows 7.
ms.assetid: 7182c21e-1ff0-4dce-9571-534b7576c082
ms.topic: article
ms.date: 05/31/2018
---

# Caption Property (Commands Collection Object)

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Determines the text displayed for a [**Commands**](/windows/desktop/lwef/the-commands-collection-object) object in the character's pop-up menu.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent***.Characters ("***CharacterID***").**[Commands.Caption](caption-property.md) \[ = *string*\]



| Part     | Description                                                              |
|----------|--------------------------------------------------------------------------|
| *string* | A string expression that evaluates to the text displayed as the caption. |



 

</dd> </dl>

## Remarks

Setting the [**Caption**](caption-property.md) property for your [**Commands**](/windows/desktop/lwef/the-commands-collection-object) collection defines how it will appear on the character's pop-up menu when its [**Visible**](visible-property.md) property is set to True and your application is not the input-active client. To specify an access key (unlined mnemonic) for your **Caption**, include an ampersand (&) character before that character.

If you define commands for a [**Commands**](/windows/desktop/lwef/the-commands-collection-object) collection that has a [**Caption**](caption-property.md), you typically also define a **Caption** for its associated **Commands** collection.

 

 
