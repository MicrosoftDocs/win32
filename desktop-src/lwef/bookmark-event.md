---
title: Bookmark Event
description: Bookmark Event
ms.assetid: 6733cd4e-2ba0-4cff-b68d-abfea284f748
ms.topic: article
ms.date: 05/31/2018
---

# Bookmark Event

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Occurs when a bookmark in a speech text string that your application defined is activated.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

**Sub** *agent*\_**Bookmark** **(ByVal** *BookmarkID***)**



| Part         | Description                                     |
|--------------|-------------------------------------------------|
| *BookmarkID* | A Long integer identifying the bookmark number. |



 

</dd> </dl>

### Remarks

To specify a bookmark event, use the [**Speak**](speak-method.md) method with a **Mrk** tag in your supplied text. For more information about tags, see Speech Output Tags.

 

 




