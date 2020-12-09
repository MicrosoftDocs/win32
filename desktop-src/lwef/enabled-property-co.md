---
title: Enabled Property (Command Object)
description: Enabled Property
ms.assetid: d9dcbdf0-ba35-4ebd-b6f2-f3c8bdfc0431
ms.topic: article
ms.date: 05/31/2018
---

# Enabled Property (Command Object)

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Returns or sets whether the **Command** is enabled in the specified character's pop-up menu.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent***.Characters ("***CharacterID***").Commands("***name***").Enabled** \[ = *boolean*\]



| Part      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *boolean* | A Boolean expression specifying whether the **Command** is enabled.<br/> <dl> <dt><span id="True"></span><span id="true"></span><span id="TRUE"></span>**True**</dt> <dd> The **Command** is enabled.<br/> </dd> <dt><span id="False"></span><span id="false"></span><span id="FALSE"></span>**False**</dt> <dd> The **Command** is disabled.<br/> </dd> </dl> |



 

</dd> </dl>

## Remarks

If the [**Enabled**](enabled-property.md) property is set to **True**, the [**Command**](/windows/desktop/lwef/the-command-object) objects's caption appears as normal text in the character's pop-up menu when the client application is input-active. If the **Enabled** property is **False**, the caption appears as unavailable (disabled) text. A disabled **Command** is also not accessible for voice input.

 

