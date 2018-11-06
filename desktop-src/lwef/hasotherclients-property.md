---
title: HasOtherClients Property
description: HasOtherClients Property
ms.assetid: 5ecc6f42-786b-40a6-8800-9ad0d92edfb2
ms.topic: article
ms.date: 05/31/2018
---

# HasOtherClients Property

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Returns whether the specified character is in use by other applications.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent*.**Characters("***CharacterID***").HasOtherClients**



| Value     | Description                                |
|-----------|--------------------------------------------|
| **True**  | The character has other clients.           |
| **False** | The character does not have other clients. |



 

</dd> </dl>

## Remarks

You can use this property to determine whether your application is the only or last client of the character, when more than one application is sharing (has loaded) the same character.

 

 




