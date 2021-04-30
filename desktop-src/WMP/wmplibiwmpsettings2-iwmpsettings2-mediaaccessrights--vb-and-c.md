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
ms.date: 05/31/2018
---

# IWMPSettings2::mediaAccessRights property

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

 

 





