---
title: IWMPClosedCaption2 getSAMILangName method
description: The getSAMILangName method returns the name of a language supported by the current SAMI file.
ms.assetid: 52aaf1cc-89ef-4c4c-af43-3f88dc4a9539
keywords:
- getSAMILangName method Windows Media Player
- getSAMILangName method Windows Media Player , IWMPClosedCaption2 interface
- IWMPClosedCaption2 interface Windows Media Player , getSAMILangName method
topic_type:
- apiref
api_name:
- IWMPClosedCaption2.getSAMILangName
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPClosedCaption2::getSAMILangName method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **getSAMILangName** method returns the name of a language supported by the current SAMI file.

## Syntax


```CSharp
public System.String getSAMILangName(
  System.Int32 nIndex
);
```


```VB

Public Function getSAMILangName( _
  ByVal nIndex As System.Int32 _
) As System.String
Implements IWMPClosedCaption2.getSAMILangName
```





## Parameters

<dl> <dt>

*nIndex* \[in\]
</dt> <dd>

**A System.Int32** that is the zero-based index of the language name to retrieve.

</dd> </dl>

## Return value

A **System.String** that is the name of the language as specified in the SAMI file.

## Remarks

The languages in a SAMI file are indexed in the order shown in the file, starting with zero.

This method returns a zero-length string ("") unless a digital media file is open (AxWindowsMediaPlayer.openState is equal to 13).

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
</dt> </dl>

 

 





