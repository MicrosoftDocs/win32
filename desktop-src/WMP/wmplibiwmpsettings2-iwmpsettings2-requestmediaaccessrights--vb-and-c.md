---
title: IWMPSettings2 requestMediaAccessRights method
description: The requestMediaAccessRights method requests a specified level of access to the library. | IWMPSettings2 requestMediaAccessRights method
ms.assetid: ea33852c-d1e0-45cf-8954-2a1e2fe51910
keywords:
- requestMediaAccessRights method Windows Media Player
- requestMediaAccessRights method Windows Media Player , IWMPSettings2 interface
- IWMPSettings2 interface Windows Media Player , requestMediaAccessRights method
topic_type:
- apiref
api_name:
- IWMPSettings2.requestMediaAccessRights
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPSettings2::requestMediaAccessRights method

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **requestMediaAccessRights** method requests a specified level of access to the library.

## Syntax


```CSharp
public System.Boolean requestMediaAccessRights(
  System.String bstrDesiredAccess
);
```


```VB

Public Function requestMediaAccessRights( _
  ByVal bstrDesiredAccess As System.String _
) As System.Boolean
Implements IWMPSettings2.requestMediaAccessRights
```





## Parameters

<dl> <dt>

*bstrDesiredAccess* \[in\]
</dt> <dd>

A **System.String** that is one of the following values.



| Value | Description                      |
|-------|----------------------------------|
| none  | Current item access rights only. |
| read  | Read access rights only.         |
| full  | Read/Write access rights.        |



 

</dd> </dl>

## Return value

A **System.Boolean** that indicates whether the requested access rights were granted.

## Remarks

A webpage must first request permission from the user to read information from or write data to the library. Invoking this method prompts the user with a dialog box that requests the specified permission level. This means that certain methods, properties, and events will be inaccessible from code if the appropriate access rights have not been granted. The current access rights level can be retrieved by using **IWMPSettings2.mediaAccessRights**.

Applications running on the user's computer are not required to use this method.

## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                      |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPSettings2 Interface (VB and C#)**](iwmpsettings2--vb-and-c.md)
</dt> <dt>

[**IWMPSettings2.mediaAccessRights (VB and C#)**](wmplibiwmpsettings2-iwmpsettings2-mediaaccessrights--vb-and-c.md)
</dt> </dl>

 

 





