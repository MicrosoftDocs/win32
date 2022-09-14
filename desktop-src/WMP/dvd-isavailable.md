---
title: DVD.isAvailable
description: The isAvailable property indicates whether a specified type of information is available or a specified action can be performed. | DVD.isAvailable
ms.assetid: ed34a943-b9c3-40a8-8845-b83f16951a3e
keywords:
- DVD.isAvailable Windows Media Player
topic_type:
- apiref
api_name:
- DVD.isAvailable
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# DVD.isAvailable

The **isAvailable** property indicates whether a specified type of information is available or a specified action can be performed.

``` syntax
player.dvd.isAvailable(
        name
        )
```

## Parameters

*name*

**String** containing one of the following values.



| String     | Description                                                                            |
|------------|----------------------------------------------------------------------------------------|
| back       | Determines whether the **back** method is available.                                   |
| dvd        | Determines whether the DVD is loaded.                                                  |
| dvdDecoder | Determines whether the DVD decoder is installed on system.                             |
| resume     | Determines whether the **resume** method is available.                                 |
| titleMenu  | Determines whether the **titleMenu** method is available.                              |
| topMenu    | Determines whether the **topMenu** method is available. Commonly called the root menu. |



 

## Return Values

This method returns a read-only **Boolean** indicating whether the specified parameter is available.

## Remarks

The DVD features of Windows Media Player will not work on computers that do not have third-party DVD decoders installed. You can determine whether a decoder is available by calling **isAvailable**("dvdDecoder").

Every DVD is authored differently. The methods available during DVD playback and navigation depend on how the DVD is authored.

**Windows Media Player 10 Mobile:** This property always returns **false**.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                               |
| Version<br/>                  | Windows Media Player for Windows XP or later<br/>                            |
| DLL<br/>                      | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**DVD Object**](dvd-object.md)
</dt> </dl>

 

 





