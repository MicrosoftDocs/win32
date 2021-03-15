---
title: Player.DomainChange event
description: The DomainChange event occurs when the DVD domain changes. | Player.DomainChange event
ms.assetid: 01965492-276e-4d30-99eb-767e0776b423
keywords:
- DomainChange event Windows Media Player
- DomainChange event Windows Media Player , Player class
- Player class Windows Media Player , DomainChange event
topic_type:
- apiref
api_name:
- Player.DomainChange
api_location:
- wmp.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# Player.DomainChange event

The **DomainChange** event occurs when the DVD domain changes.

## Syntax


```JScript
Player.DomainChange(
  strDomain
)
```



## Parameters

<dl> <dt>

*strDomain* 
</dt> <dd>

**String** indicating the new domain. Contains one of the following values.



| String            | Description                                                          |
|-------------------|----------------------------------------------------------------------|
| firstplay         | Performing default initialization of a DVD disc.                     |
| videoManagerMenu  | Displaying menus for whole disc. Also known as Root Menu or topMenu. |
| videoTitleSetMenu | Displaying menus for current title set. Also known as titleMenu.     |
| title             | Displaying the current title.                                        |
| stop              | The DVD Navigator is in the DVD Stop domain.                         |



 

</dd> </dl>

## Return value

This event does not return a value.

## Remarks

The value of event parameters is specified by Windows Media Player, and can be accessed or passed to a method in an imported JScript file using the parameter name given. This parameter name must be typed exactly as shown, including capitalization.

**Windows Media Player 10 Mobile:** This event is not supported.

## Requirements



|                    |                                                                                    |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player for Windows XP or later.<br/>                           |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**DVD Object**](dvd-object.md)
</dt> <dt>

[**Player Object**](player-object.md)
</dt> </dl>

 

 





