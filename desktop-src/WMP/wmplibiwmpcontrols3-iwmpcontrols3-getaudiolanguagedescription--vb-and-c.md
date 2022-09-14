---
title: IWMPControls3 getAudioLanguageDescription method
description: The getAudioLanguageDescription method returns the description for the audio language corresponding to the specified one-based index.
ms.assetid: bf3db27f-ba14-409e-8942-fe863d6f3670
keywords:
- getAudioLanguageDescription method Windows Media Player
- getAudioLanguageDescription method Windows Media Player , IWMPControls3 interface
- IWMPControls3 interface Windows Media Player , getAudioLanguageDescription method
topic_type:
- apiref
api_name:
- IWMPControls3.getAudioLanguageDescription
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPControls3::getAudioLanguageDescription method

The **getAudioLanguageDescription** method returns the description for the audio language corresponding to the specified one-based index.

## Syntax


```CSharp
public System.String getAudioLanguageDescription(
  System.Int32 lIndex
);
```


```VB

Public Function getAudioLanguageDescription( _
  ByVal lIndex As System.Int32 _
) As System.String
Implements IWMPControls3.getAudioLanguageDescription
```





## Parameters

<dl> <dt>

*lIndex* \[in\]
</dt> <dd>

A **System.Int32** that is the one-based audio language index.

</dd> </dl>

## Return value

A **System.String** that is the description of the audio language.

## Remarks

For Windows Media based content, properties and methods related to language selection support only a single output.

Use the **audioLanguageCount** property to get the number of supported audio languages, and then access an audio language individually by using a one-based index.

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

[**IWMPControls3.audioLanguageCount (VB and C#)**](wmplibiwmpcontrols3-iwmpcontrols3-audiolanguagecount--vb-and-c.md)
</dt> <dt>

[**IWMPControls3.currentAudioLanguageIndex (VB and C#)**](wmplibiwmpcontrols3-iwmpcontrols3-currentaudiolanguageindex--vb-and-c.md)
</dt> <dt>

[**IWMPControls3.currentAudioLanguage (VB and C#)**](wmplibiwmpcontrols3-iwmpcontrols3-currentaudiolanguage--vb-and-c.md)
</dt> <dt>

[**IWMPControls3.getAudioLanguageID (VB and C#)**](wmplibiwmpcontrols3-iwmpcontrols3-getaudiolanguageid--vb-and-c.md)
</dt> <dt>

[**IWMPControls3.getLanguageName (VB and C#)**](wmplibiwmpcontrols3-iwmpcontrols3-getlanguagename--vb-and-c.md)
</dt> </dl>

 

 





