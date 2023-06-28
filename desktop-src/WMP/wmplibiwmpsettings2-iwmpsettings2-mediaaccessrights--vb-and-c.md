---
title: IWMPSettings2 mediaAccessRights property
description: The mediaAccessRights property gets a value indicating the permissions currently granted for library access.
ms.assetid: c4289a2c-e343-405d-9bf5-0e97f6617916
keywords:
- mediaAccessRights property Windows Media Player
- mediaAccessRights property Windows Media Player , IWMPSettings2 interface
- IWMPSettings2 interface Windows Media Player , mediaAccessRights property
topic_type:
- apiref
api_name:
- IWMPSettings2.mediaAccessRights
- IWMPSettings2.get_mediaAccessRights
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# IWMPSettings2::mediaAccessRights property

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **mediaAccessRights** property gets a value indicating the permissions currently granted for library access.

This property is read-only.

## Syntax


```CSharp
public System.String mediaAccessRights {get;}
```


```VB

Public ReadOnly Property mediaAccessRights As System.String
```





## Property value

A **System.String** that is one of the following values.



| Value | Description                      |
|-------|----------------------------------|
| none  | Current item access rights only. |
| read  | Read access rights only.         |
| full  | Read/Write access rights.        |



 

## Remarks

A webpage must first request permission from the user to read information from or write data to the library. This means that certain methods, properties, and events will be inaccessible from code if the appropriate access rights have not been granted. To obtain access rights, the application calls **IWMPSettings2.get\_requestMediaAccessRights**, passing a parameter that specifies the desired access rights level.

Applications running on the user's computer always have full access rights.

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

[**IWMPSettings2.requestMediaAccessRights (VB and C#)**](wmplibiwmpsettings2-iwmpsettings2-requestmediaaccessrights--vb-and-c.md)
</dt> </dl>

 

 





