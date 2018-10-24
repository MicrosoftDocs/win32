---
title: IWMPControls3 getLanguageName method
description: The getLanguageName method returns the name of the audio language with the specified locale identifier (LCID).
ms.assetid: a0651e8d-0ba1-4fff-93f0-fe097231723e
keywords:
- getLanguageName method Windows Media Player
- getLanguageName method Windows Media Player , IWMPControls3 interface
- IWMPControls3 interface Windows Media Player , getLanguageName method
topic_type:
- apiref
api_name:
- IWMPControls3.getLanguageName
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IWMPControls3::getLanguageName method

The **getLanguageName** method returns the name of the audio language with the specified locale identifier (LCID).

## Syntax


```CSharp
public System.String getLanguageName(
  System.Int32 lLangID
);
```

<span codelanguage="VisualBasic"></span>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>VB</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>Public Function getLanguageName( _
  ByVal lLangID As System.Int32 _
) As System.String
Implements IWMPControls3.getLanguageName</code></pre></td>
</tr>
</tbody>
</table>



## Parameters

<dl> <dt>

*lLangID* \[in\]
</dt> <dd>

A **System.Int32** that is the LCID.

</dd> </dl>

## Return value

A **System.String** that is the name of the audio language.

## Remarks

An LCID uniquely identifies a particular language dialect, called a locale.

For Windows Media-based content, properties and methods related to language selection support only a single output.

## Requirements



|                      |                                                                                                                        |
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

[**IWMPControls3.getAudioLanguageID (VB and C#)**](wmplibiwmpcontrols3-iwmpcontrols3-getaudiolanguageid--vb-and-c.md)
</dt> </dl>

 

 





