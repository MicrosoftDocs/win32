---
title: IWMPLibrary isIdentical method
description: The isIdentical method returns a value that indicates whether the supplied object is the same as the current one.
ms.assetid: c4eebc46-6a5f-4f9a-8cd4-7421b156670c
keywords:
- isIdentical method Windows Media Player
- isIdentical method Windows Media Player , IWMPLibrary interface
- IWMPLibrary interface Windows Media Player , isIdentical method
topic_type:
- apiref
api_name:
- IWMPLibrary.isIdentical
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPLibrary::isIdentical method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **isIdentical** method returns a value that indicates whether the supplied object is the same as the current one.

## Syntax


```CSharp
public System.Boolean isIdentical(
  IWMPLibrary pIWMPLibrary
);
```


```VB

Public Function isIdentical( _
  ByVal pIWMPLibrary As IWMPLibrary _
) As System.Boolean
Implements IWMPLibrary.isIdentical
```





## Parameters

<dl> <dt>

*pIWMPLibrary* \[in\]
</dt> <dd>

A **WMPLib.IWMPLibrary** interface that represents the object to compare with current one.

</dd> </dl>

## Return value

A **System.Boolean** that is the result of the comparison. The value **true** indicates that the objects are the same.

## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 11.<br/>                                                                                    |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPLibrary Interface (VB and C#)**](iwmplibrary--vb-and-c.md)
</dt> </dl>

 

 





