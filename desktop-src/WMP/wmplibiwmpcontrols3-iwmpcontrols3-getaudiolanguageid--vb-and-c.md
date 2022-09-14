---
title: IWMPControls3 getAudioLanguageID method
description: The getAudioLanguageID method returns the locale identifier (LCID) for a specified audio language index.
ms.assetid: 880bbfca-6f69-41ce-a078-467c1939fae5
keywords:
- getAudioLanguageID method Windows Media Player
- getAudioLanguageID method Windows Media Player , IWMPControls3 interface
- IWMPControls3 interface Windows Media Player , getAudioLanguageID method
topic_type:
- apiref
api_name:
- IWMPControls3.getAudioLanguageID
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPControls3::getAudioLanguageID method

The **getAudioLanguageID** method returns the locale identifier (LCID) for a specified audio language index.

## Syntax


```CSharp
public System.Int32 getAudioLanguageID(
  System.Int32 lIndex
);
```


```VB

Public Function getAudioLanguageID( _
  ByVal lIndex As System.Int32 _
) As System.Int32
Implements IWMPControls3.getAudioLanguageID
```





## Parameters

<dl> <dt>

*lIndex* \[in\]
</dt> <dd>

A **System.Int32** that is the one-based index of the audio language.

</dd> </dl>

## Return value

A **System.Int32** that is the LCID.

## Remarks

An LCID uniquely identifies a particular language dialect, called a locale.

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

[**IWMPControls3.currentAudioLanguage (VB and C#)**](wmplibiwmpcontrols3-iwmpcontrols3-currentaudiolanguage--vb-and-c.md)
</dt> <dt>

[**IWMPControls3.currentAudioLanguageIndex (VB and C#)**](wmplibiwmpcontrols3-iwmpcontrols3-currentaudiolanguageindex--vb-and-c.md)
</dt> <dt>

[**IWMPControls3.getAudioLanguageDescription (VB and C#)**](wmplibiwmpcontrols3-iwmpcontrols3-getaudiolanguagedescription--vb-and-c.md)
</dt> <dt>

[**IWMPControls3.getLanguageName (VB and C#)**](wmplibiwmpcontrols3-iwmpcontrols3-getlanguagename--vb-and-c.md)
</dt> </dl>

 

 





