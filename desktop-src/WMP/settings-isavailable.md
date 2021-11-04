---
title: Settings.isAvailable
description: The isAvailable property indicates whether a specified type of information is available or a specified action can be performed. | Settings.isAvailable
ms.assetid: 89403125-545c-482b-a27e-6fee06abe247
keywords:
- Settings.isAvailable Windows Media Player
topic_type:
- apiref
api_name:
- Settings.isAvailable
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Settings.isAvailable

The **isAvailable** property indicates whether a specified type of information is available or a specified action can be performed.

## Syntax

player.settings.isAvailable( name )

## Parameters

*name*

String containing one of the following values.



| String             | Description                                                    |
|--------------------|----------------------------------------------------------------|
| AutoStart          | Determines whether the autoStart property can be set.          |
| Balance            | Determines whether the balance property can be set.            |
| BaseURL            | Determines whether the baseURL property can be set.            |
| DefaultFrame       | Determines whether the defaultFrame property can be set.       |
| EnableErrorDialogs | Determines whether the enableErrorDialogs property can be set. |
| GetMode            | Determines whether the getMode method can be called.           |
| InvokeURLs         | Determines whether the invokeURLs property can be set.         |
| Mute               | Determines whether the mute property can be set.               |
| PlayCount          | Determines whether the playCount property can be set.          |
| Rate               | Determines whether the rate property can be set.               |
| SetMode            | Determines whether the setMode method can be called.           |
| Volume             | Determines whether the volume property can be set.             |



 

## Return Values

This method returns a **Boolean** value.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player version 7.0 or later.<br/>                              |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**Settings Object**](settings-object.md)
</dt> </dl>

 

 





