---
title: Mrk Tag
description: Mrk Tag
ms.assetid: 1bc04853-f919-4f6f-90c2-21ac836bb1e4
ms.topic: article
ms.date: 05/31/2018
---

# Mrk Tag

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Defines a bookmark in the spoken text.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

**\\Mrk=***number***\\**



| Part     | Description                                        |
|----------|----------------------------------------------------|
| *number* | A Long integer value that identifies the bookmark. |



 

</dd> </dl>

### Remarks

When the server processes a bookmark, it generates a bookmark event. You must specify a number greater than zero (0) and not equal to 2147483647 or 2147483646.

 

 




