---
description: The SelectParentalLevel method sets the specified parental level for subsequent playback.
ms.assetid: ffd1e204-6ed2-4190-8635-9f3866d38099
title: SelectParentalLevel Method
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# SelectParentalLevel Method

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `SelectParentalLevel` method sets the specified parental level for subsequent playback.

``` syntax
MSWebDVD.SelectParentalLevel(iLevel, sUserName, sPassword)
```

## Parameters

<dl> <dt>

<span id="iLevel"></span><span id="ilevel"></span><span id="ILEVEL"></span>*iLevel*
</dt> <dd>

Specifies the parental management level as an Integer. To enable the parental management, the *iLevel* parameter must range from 1 through 8. To disable the parental management, set *iLevel* to -1.

</dd> <dt>

<span id="sUserName"></span><span id="susername"></span><span id="SUSERNAME"></span>*sUserName*
</dt> <dd>

Specifies the current user as a String. (Currently ignored.)

</dd> <dt>

<span id="sPassword"></span><span id="spassword"></span><span id="SPASSWORD"></span>*sPassword*
</dt> <dd>

Specifies the password currently stored in the registry as a String.

</dd> </dl>

## Return Value

No return value.

## Remarks

This method sets the access level in the MSWebDVD object, which determines what content the user can play back. Higher levels can play lower-level content but lower levels can't play higher-level content. The exact meaning of the eight DVD parental management levels varies depending on the country/region. In the United States and Canada, the levels are mapped to the Motion Picture Association of America (MPAA) rating categories. Parental management in the DVD Navigator is disabled by default.

## See also

<dl> <dt>

[**SelectParentalCountry**](selectparentalcountry-method.md)
</dt> <dt>

[**NotifyParentalLevelChange**](notifyparentallevelchange-method.md)
</dt> <dt>

[**GetTitleParentalLevels**](gettitleparentallevels-method.md)
</dt> <dt>

[**GetPlayerParentalCountry**](getplayerparentalcountry-method.md)
</dt> <dt>

[**GetPlayerParentalLevel**](getplayerparentallevel-method.md)
</dt> <dt>

[**AcceptParentalLevelChange**](acceptparentallevelchange-method.md)
</dt> </dl>

 

 



