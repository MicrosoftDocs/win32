---
Description: 'Note  The IDvdControl interface is deprecated. Use IDvdControl2 instread. Sets the parental access level for the current media file.'
ms.assetid: 'ca572d89-b188-442d-884f-0cffa71c2892'
title: 'IDvdControl::ParentalLevelSelect method'
---

# IDvdControl::ParentalLevelSelect method

> [!Note]  
> The **IDvdControl** interface is deprecated. Use [**IDvdControl2**](idvdcontrol2.md) instread.

 

Sets the parental access level for the current media file.

## Syntax


```C++
HRESULT ParentalLevelSelect(
   ULONG ulParentalLevel
);
```



## Parameters

<dl> <dt>

*ulParentalLevel* 
</dt> <dd>

Value that specifies the current media file parental access level. Should be a value from 1 to 8, inclusive. Predefined parental levels are as follows:



| Value | Description                                                                           |
|-------|---------------------------------------------------------------------------------------|
| 1     | The rating is G, General.                                                             |
| 3     | The rating is PG, Parental Guidance Suggested.                                        |
| 4     | The rating is PG-13, Parental Guidance Suggested, not recommended for those under 13. |
| 6     | The rating is R, Restricted.                                                          |
| 7     | The rating is NC-17.                                                                  |



 

</dd> </dl>

## Return value

Returns an **HRESULT** value.

## Remarks

This method returns an error unless the domain is DVD\_DOMAIN\_Stop. For more information, see [**DVD\_DOMAIN**](dvd-domain.md).

This method sets the current user's access level; this access level determines what media files the user can play back. Higher levels can play lower-level content; lower levels can't play higher-level content. For example, adults can watch child-safe content, but children can't watch adult content.

The [DVD Navigator](dvd-navigator-filter.md) filter provides no restriction on setting the parental level. DVD player applications can enforce restrictions on the parental level setting, such as providing password protection for raising the current parental level. Parental management in the DVD Navigator is disabled by default.

To disable parental management, pass 0xffffffff for *ulParentalLevel*. If parental management is disabled, then the player will play the first program chain (PGC) in a parental block regardless of parental IDs.

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Version<br/> | Reference: Dshowh<br/>                                                          |
| DLL<br/>     | <dl> <dt>Quartz.dll</dt> </dl> |



## See also

<dl> <dt>

[Error and Success Codes](error-and-success-codes.md)
</dt> <dt>

[**IDvdControl Interface**](idvdcontrol.md)
</dt> <dt>

[**IDvdControl::ParentalCountrySelect**](idvdcontrol-parentalcountryselect.md)
</dt> </dl>

 

 




