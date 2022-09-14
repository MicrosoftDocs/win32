---
title: Unload Method
description: Unload Method
ms.assetid: 2ffaeea6-ff24-48b2-bc99-eba429434a30
ms.topic: article
ms.date: 05/31/2018
---

# Unload Method

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Unloads the character data for the specified character.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent***.Characters.Unload "***CharacterID***"**

</dd> </dl>

## Remarks

Use this method when you no longer need a character, to free up memory used to store information about the character. If you access the character again, use the [**Load**](load-method.md) method.

This method does not return a [**Request**](/windows/desktop/lwef/the-request-object) object.

 

 