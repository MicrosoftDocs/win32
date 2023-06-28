---
description: The GetTitleParentalLevels method retrieves the parental management levels for the specified title.
ms.assetid: 076808d7-6cb6-4d81-b26d-c7945db298f2
title: GetTitleParentalLevels Method
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# GetTitleParentalLevels Method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `GetTitleParentalLevels` method retrieves the parental management levels for the specified title.

``` syntax
[ iLevels = ] MSWebDVD.GetTitleParentalLevels(iTitle)
```

## Parameters

<dl> <dt>

<span id="iTitle"></span><span id="ititle"></span><span id="ITITLE"></span>*iTitle*
</dt> <dd>

Specifies the title as an Integer.

</dd> </dl>

## Return Value

Returns an integer value whose individual bits indicate which parental management levels (PML) are set in the specified title.

## Remarks

A title may have chapters or even short segments that have a PML different from the overall PML for the title. Use this method to determine all the PMLs that will be encountered when playing a specified title. The returned integer is a set of bit flags that are defined as shown in the table below. Perform a bitwise AND operation on *iLevels* and each possible value. If the operation returns **true**, it means that PML will be encountered at some point in this title.



| Value  | Description          |
|--------|----------------------|
| 0x100  | DVD Parental Level 1 |
| 0x200  | DVD Parental Level 2 |
| 0x400  | DVD Parental Level 3 |
| 0x800  | DVD Parental Level 4 |
| 0x1000 | DVD Parental Level 5 |
| 0x2000 | DVD Parental Level 6 |
| 0x4000 | DVD Parental Level 7 |
| 0x8000 | DVD Parental Level 8 |



 

## See also

<dl> <dt>

[**SelectParentalLevel**](selectparentallevel-method.md)
</dt> <dt>

[**GetPlayerParentalCountry**](getplayerparentalcountry-method.md)
</dt> <dt>

[**GetPlayerParentalLevel**](getplayerparentallevel-method.md)
</dt> <dt>

[**SelectParentalCountry**](selectparentalcountry-method.md)
</dt> </dl>

 

 



