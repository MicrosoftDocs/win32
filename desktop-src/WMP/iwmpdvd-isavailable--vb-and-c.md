---
title: IWMPDVD.isAvailable (VB and C )
description: The isAvailable property (the get\_isAvailable method in C\ ) gets a value that indicates whether a specified type of information is available or a specified action can be performed.
ms.assetid: 55690783-df2f-473d-a6f2-a4907b7e8a78
keywords:
- IWMPDVD.isAvailable (VB and C ) Windows Media Player
topic_type:
- apiref
api_name:
- IWMPDVD.isAvailable (VB and C )
api_location:
- Interop.WMPLib.dll
api_type:
- Assembly
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPDVD.isAvailable (VB and C#)

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **isAvailable** property (the **get\_isAvailable** method in C#) gets a value that indicates whether a specified type of information is available or a specified action can be performed.


```
[Visual Basic]
ReadOnly Property isAvailable(
  bstrItem As System.String
) As System.Boolean
```




```
[C#]
System.Boolean get_isAvailable (
  System.String bstrItem
)
```



## Parameters

*bstrItem*

A System.String that is one of the following values.



| Value      | Description                                                                                   |
|------------|-----------------------------------------------------------------------------------------------|
| back       | Discovers whether the **IWMPDVD.back** method is available.                                   |
| dvd        | Discovers whether the DVD is loaded.                                                          |
| dvdDecoder | Discovers whether the DVD decoder is installed on system.                                     |
| resume     | Discovers whether the **IWMPDVD.resume** method is available.                                 |
| titleMenu  | Discovers whether the **IWMPDVD.titleMenu** method is available.                              |
| topMenu    | Discovers whether the **IWMPDVD.topMenu** method is available. Commonly called the root menu. |



 

## Property Value

**System.Boolean**

A **System.Boolean** that indicates whether a specified type of information is available or a specified action can be performed.

## Remarks

The DVD features of Windows Media Player will not work on computers that do not have a DVD decoder installed. You can determine whether a decoder is available by calling the **isAvailable** property (the **get\_isAvailable** method in C#) and passing in the **System.String** value "dvdDecoder".

Every DVD is authored differently. The methods available during DVD playback and navigation depend on how the DVD is authored.

## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                      |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPDVD Interface (VB and C#)**](iwmpdvd--vb-and-c.md)
</dt> <dt>

[**IWMPDVD.back (VB and C#)**](wmplibiwmpdvd-iwmpdvd-back--vb-and-c.md)
</dt> <dt>

[**IWMPDVD.resume (VB and C#)**](wmplibiwmpdvd-iwmpdvd-resume--vb-and-c.md)
</dt> <dt>

[**IWMPDVD.titleMenu (VB and C#)**](wmplibiwmpdvd-iwmpdvd-titlemenu--vb-and-c.md)
</dt> <dt>

[**IWMPDVD.topMenu (VB and C#)**](wmplibiwmpdvd-iwmpdvd-topmenu--vb-and-c.md)
</dt> </dl>

 

 





