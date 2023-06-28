---
title: IWMPControls3 audioLanguageCount property
description: The audioLanguageCount property gets the count of supported audio languages.
ms.assetid: 92e2093f-435b-4427-9f85-8c8ae76e0e2d
keywords:
- audioLanguageCount property Windows Media Player
- audioLanguageCount property Windows Media Player , IWMPControls3 interface
- IWMPControls3 interface Windows Media Player , audioLanguageCount property
topic_type:
- apiref
api_name:
- IWMPControls3.audioLanguageCount
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPControls3::audioLanguageCount property

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **audioLanguageCount** property gets the count of supported audio languages.

## Syntax


```CSharp
public System.Int32 audioLanguageCount {get; set;}
```


```VB

Public ReadOnly Property audioLanguageCount As System.Int32
```





## Property value

A **System.Int32** that is the count of supported audio languages.

## Remarks

For Windows Media-based content, properties and methods related to language selection support only a single output.

## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                      |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPControls3 Interface (VB and C#)**](iwmpcontrols3--vb-and-c.md)
</dt> <dt>

[**IWMPControls3.currentAudioLanguage (VB and C#)**](wmplibiwmpcontrols3-iwmpcontrols3-currentaudiolanguage--vb-and-c.md)
</dt> <dt>

[**IWMPControls3.currentAudioLanguageIndex (VB and C#)**](wmplibiwmpcontrols3-iwmpcontrols3-currentaudiolanguageindex--vb-and-c.md)
</dt> <dt>

[**IWMPControls3.getAudioLanguageDescription (VB and C#)**](wmplibiwmpcontrols3-iwmpcontrols3-getaudiolanguagedescription--vb-and-c.md)
</dt> <dt>

[**IWMPControls3.getAudioLanguageID (VB and C#)**](wmplibiwmpcontrols3-iwmpcontrols3-getaudiolanguageid--vb-and-c.md)
</dt> <dt>

[**IWMPControls3.getLanguageName (VB and C#)**](wmplibiwmpcontrols3-iwmpcontrols3-getlanguagename--vb-and-c.md)
</dt> </dl>

 

 





