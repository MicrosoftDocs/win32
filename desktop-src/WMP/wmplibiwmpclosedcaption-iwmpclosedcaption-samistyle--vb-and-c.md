---
title: IWMPClosedCaption SAMIStyle property
description: The SAMIStyle property gets or sets the closed captioning style.
ms.assetid: 0b1f92c6-b659-4ade-90c8-62a06e475f5c
keywords:
- SAMIStyle property Windows Media Player
- SAMIStyle property Windows Media Player , IWMPClosedCaption interface
- IWMPClosedCaption interface Windows Media Player , SAMIStyle property
topic_type:
- apiref
api_name:
- IWMPClosedCaption.SAMIStyle
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPClosedCaption::SAMIStyle property

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **SAMIStyle** property gets or sets the closed captioning style.

## Syntax


```CSharp
public System.String SAMIStyle {get; set;}
```


```VB

Public Property SAMIStyle As System.String
```





## Property value

The **System.String** that is the name specified in the style identifier of a SAMI file.

## Remarks

A SAMI file can contain several format style definitions. SAMI styles are defined between the &lt;STYLE&gt; and </STYLE> tags in the SAMI file. A style is defined with a text string preceded by a \# character. For example:


```
#Emphasis1 {Name: Big Bold Italic; font-size: 14pt; text-align: center;
            color: blue; font-family: sans-serif; font-weight: bold;
            font-style: italic;}
```



This specifies a style that produces a particular font.

If no SAMI style is specified, the first style defined in the SAMI file is used by default.

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

[**IWMPClosedCaption2 Interface (VB and C#)**](iwmpclosedcaption2--vb-and-c.md)
</dt> </dl>

 

 





