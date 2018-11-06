---
title: Remove Method
description: Remove Method
ms.assetid: b50d47b2-a425-4545-8d85-efeae460d2b1
ms.topic: article
ms.date: 05/31/2018
---

# Remove Method

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Removes a [**Command**](https://msdn.microsoft.com/library/windows/desktop/ms696441) object from the [**Commands**](https://msdn.microsoft.com/library/windows/desktop/ms695971) collection.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent***.Characters ("***CharacterID***").Commands.Remove***Name*



| Part   | Description                                                       |
|--------|-------------------------------------------------------------------|
| *Name* | Required. A string value corresponding to the ID for the command. |



 

</dd> </dl>

## Remarks

When a [**Command**](https://msdn.microsoft.com/library/windows/desktop/ms696441) object is removed from the collection, it no longer appears when the character's pop-up menu is displayed or in the Commands Window when your client application is input-active.

## See Also

[**RemoveAll method**](removeall-method.md)


 

 




