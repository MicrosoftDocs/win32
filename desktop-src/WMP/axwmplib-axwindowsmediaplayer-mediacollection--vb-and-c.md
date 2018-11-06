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
ms.topic: article
ms.date: 05/31/2018
---

# AxWindowsMediaPlayer.mediaCollection property

The mediaCollection property gets an **IWMPMediaCollection** interface that provides a way to organize a large collection of media items.

This property is read-only.

## Syntax


```CSharp
public IWMPMediaCollection mediaCollection {get;}
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
<td><pre><code>Public ReadOnly Property mediaCollection As IWMPMediaCollection</code></pre></td>
</tr>
</tbody>
</table>



## Property value

The WMPLib.IWMPMediaCollection interface to a collection of media items.

## Remarks

To retrieve the value of this property, read access to the library is required. For more information, see [Library Access](library-access.md).

## Requirements



|                      |                                                                                                                            |
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

 

 





