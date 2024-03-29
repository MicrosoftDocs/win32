---
title: IWMPClosedCaption2 SAMILangCount property
description: The SAMILangCount property gets the number of languages supported by the current SAMI file.
ms.assetid: e3c7203d-66cb-49e2-9204-795c0f27248f
keywords:
- SAMILangCount property Windows Media Player
- SAMILangCount property Windows Media Player , IWMPClosedCaption2 interface
- IWMPClosedCaption2 interface Windows Media Player , SAMILangCount property
topic_type:
- apiref
api_name:
- IWMPClosedCaption2.SAMILangCount
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPClosedCaption2::SAMILangCount property

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **SAMILangCount** property gets the number of languages supported by the current SAMI file.

## Syntax


```CSharp
public System.Int32 SAMILangCount {get; set;}
```


```VB

Public ReadOnly Property SAMILangCount As System.Int32
```





## Property value

A **System.Int32** that is the number of languages supported.

## Remarks

This property returns 0 unless a digital media file is open (AxWindowsMediaPlayer.openState is equal to 13).

## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                      |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**Adding Closed Captions to Digital Media**](adding-closed-captions-to-digital-media.md)
</dt> <dt>

[**IWMPClosedCaption Interface (VB and C#)**](iwmpclosedcaption--vb-and-c.md)
</dt> <dt>

[**IWMPClosedCaption.SAMILang (VB and C#)**](wmplibiwmpclosedcaption-iwmpclosedcaption-samilang--vb-and-c.md)
</dt> <dt>

[**IWMPClosedCaption2 Interface (VB and C#)**](iwmpclosedcaption2--vb-and-c.md)
</dt> <dt>

[**IWMPClosedCaption2.getSAMILangName (VB and C#)**](wmplibiwmpclosedcaption2-iwmpclosedcaption2-getsamilangname--vb-and-c.md)
</dt> </dl>

 

 





