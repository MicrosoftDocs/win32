---
title: Think Method
description: Think Method
ms.assetid: a188dd47-6af1-429d-af0a-69451f6b495e
ms.topic: article
ms.date: 05/31/2018
---

# Think Method

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Displays the specified text for the specified character in a "thought" word balloon.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent***.Characters ("***CharacterID***").Think** \[*Text*\]



| Part   | Description                                                       |
|--------|-------------------------------------------------------------------|
| *Text* | Optional. A string that specifies the character's thought output. |



 

</dd> </dl>

## Remarks

Like the [**Speak**](speak-method.md) method, the **Think** method is a queued request that displays text in a word balloon, except that the **Think** word balloon differs visually. In addition, the balloon supports only the Bookmark speech control tag (**\\Mrk**) and ignores any other speech control tags. Unlike **Speak**, the **Think** method does not change the character's animation state.

The [**Balloon**](/windows/desktop/lwef/the-balloon-object) object's properties affect the output of both the [**Speak**](speak-method.md) and **Think** methods. For example, the **Balloon** object's [**Enabled**](enabled-property.md) property must be **True** for text to display.

If you declare an object reference and set it to this method, it returns a [**Request**](/windows/desktop/lwef/the-request-object) object. In addition, if the file has not been loaded, the server sets the **Request** object's [**Status**](status-property.md) property to "failed" with an appropriate error code number.

Agent's automatic word breaking in the word balloon breaks words using white-space characters (for example, Space or Tab). However, if it cannot, it may break a word to fit the balloon. In languages like Japanese, Chinese, and Thai where spaces are not used to break words, insert a Unicode zero-width space character (0x200B) between characters to define logical word breaks.

> [!Note]  
> Set the character's language ID before using the [**Speak**](speak-method.md) method to ensure appropriate text display within the word balloon.

 

 

 