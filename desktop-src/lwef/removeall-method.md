---
title: RemoveAll Method
description: RemoveAll Method
ms.assetid: 233f8d65-36ec-4c83-8c91-59d406edd70a
ms.topic: article
ms.date: 05/31/2018
---

# RemoveAll Method

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Removes all [**Command**](/windows/desktop/lwef/the-command-object) objects from the [**Commands**](/windows/desktop/lwef/the-commands-collection-object) collection.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent***.Characters ("***CharacterID***").Commands.RemoveAll**

</dd> </dl>

## Remarks

When a [**Command**](/windows/desktop/lwef/the-command-object) object is removed from the collection, it no longer appears when the character's pop-up menu is displayed or in the Commands Window when your client application is input-active.

## See Also

[**Remove method**](remove-method.md)


 

 