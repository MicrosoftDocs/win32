---
title: DefaultCommand Property
description: DefaultCommand Property
ms.assetid: ba4d51fc-7178-4dbb-9ae5-f1991f40aad6
ms.topic: article
ms.date: 05/31/2018
---

# DefaultCommand Property

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Returns or sets the default command of the [**Commands**](/windows/desktop/lwef/the-commands-collection-object) object.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent.***Characters** **("***CharacterID***").Commands.DefaultCommand** \[ = *string*\]



| Part     | Description                                                                         |
|----------|-------------------------------------------------------------------------------------|
| *string* | A string value identifying the name (ID) of the [**Command**](/windows/desktop/lwef/the-command-object). |



 

</dd> </dl>

## Remarks

This property enables you to set a [**Command**](/windows/desktop/lwef/the-command-object) in your [**Commands**](/windows/desktop/lwef/the-commands-collection-object) collection as the default command, rendering it bold. This does not actually change command handling or double-click events.

This property applies only to your client application's use of the character; the setting does not affect other clients of the character or other characters of your client application.

 

 