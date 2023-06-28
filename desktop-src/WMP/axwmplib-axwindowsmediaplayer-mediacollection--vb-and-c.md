---
title: AxWindowsMediaPlayer.mediaCollection property
description: The mediaCollection property gets an IWMPMediaCollection interface that provides a way to organize a large collection of media items.
ms.assetid: ec37e1da-a843-4b89-88fc-ec9255baa98a
keywords:
- mediaCollection property Windows Media Player
- mediaCollection property Windows Media Player , AxWindowsMediaPlayer class
- AxWindowsMediaPlayer class Windows Media Player , mediaCollection property
topic_type:
- apiref
api_name:
- AxWindowsMediaPlayer.mediaCollection
api_location:
- AxInterop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# AxWindowsMediaPlayer.mediaCollection property

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The mediaCollection property gets an **IWMPMediaCollection** interface that provides a way to organize a large collection of media items.

This property is read-only.

## Syntax


```CSharp
public IWMPMediaCollection mediaCollection {get;}
```


```VB

Public ReadOnly Property mediaCollection As IWMPMediaCollection
```





## Property value

The WMPLib.IWMPMediaCollection interface to a collection of media items.

## Remarks

To retrieve the value of this property, read access to the library is required. For more information, see [Library Access](library-access.md).

## Requirements



| Requirement | Value |
|----------------------|----------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                          |
| Namespace<br/> | **AxWMPLib**<br/>                                                                                                    |
| Assembly<br/>  | <dl> <dt>AxInterop.WMPLib.dll (AxInterop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**AxWindowsMediaPlayer Object (VB and C#)**](axwindowsmediaplayer-object--vb-and-c.md)
</dt> <dt>

[**IWMPMediaCollection Interface (VB and C#)**](iwmpmediacollection--vb-and-c.md)
</dt> <dt>

[**IWMPSettings2.mediaAccessRights (VB and C#)**](wmplibiwmpsettings2-iwmpsettings2-mediaaccessrights--vb-and-c.md)
</dt> <dt>

[**IWMPSettings2.requestMediaAccessRights (VB and C#)**](wmplibiwmpsettings2-iwmpsettings2-requestmediaaccessrights--vb-and-c.md)
</dt> </dl>

 

 





