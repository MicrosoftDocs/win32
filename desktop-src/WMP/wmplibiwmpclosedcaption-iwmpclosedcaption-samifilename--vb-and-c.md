---
title: IWMPClosedCaption SAMIFileName property
description: The SAMIFileName property gets or sets the name of a file containing the information needed for closed captioning.
ms.assetid: c3162c5f-9d66-41d4-920c-ed9840742d9d
keywords:
- SAMIFileName property Windows Media Player
- SAMIFileName property Windows Media Player , IWMPClosedCaption interface
- IWMPClosedCaption interface Windows Media Player , SAMIFileName property
topic_type:
- apiref
api_name:
- IWMPClosedCaption.SAMIFileName
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPClosedCaption::SAMIFileName property

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **SAMIFileName** property gets or sets the name of a file containing the information needed for closed captioning.

## Syntax


```CSharp
public System.String SAMIFileName {get; set;}
```


```VB

Public Property SAMIFileName As System.String
```





## Property value

The **System.String** that is the name of the Synchronized Accessible Media Interchange (SAMI) file.

## Remarks

The SAMI file must use an .smi or .sami file name extension.

If you do not set a value using **SAMIFileName**, this property gets a **string** containing the default file name or URL associated with the current media item. This association can occur when a SAMI file is specified by using the *sami* URL parameter, or automatically when the SAMI file has the same name as the digital media file (except for the file name extension). If there is no default SAMI file associated with the current media, this property gets a zero-length string ("").

Once you set a value using **SAMIFileName**, that value persists until you set a new value (or until a new media item is opened using the sami URL parameter). Therefore, you must set a new value for this property before you play each new media item. That way, the new value for **SAMIFileName** will take effect when the next media item is opened (or when **AxWindowsMediaPlayer.close** is called). Specifying a new value for **SAMIFileName** has no effect for the current media.

To cause Windows Media Player to use the default SAMI file associated with a particular media item, set **SAMIFileName** to a zero-length string ("") before you play the next media item.

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

[**AxWindowsMediaPlayer.close**](axwmplib-axwindowsmediaplayer-close.md)
</dt> <dt>

[**IWMPClosedCaption Interface (VB and C#)**](iwmpclosedcaption--vb-and-c.md)
</dt> <dt>

[**IWMPClosedCaption2 Interface (VB and C#)**](iwmpclosedcaption2--vb-and-c.md)
</dt> </dl>

 

 





