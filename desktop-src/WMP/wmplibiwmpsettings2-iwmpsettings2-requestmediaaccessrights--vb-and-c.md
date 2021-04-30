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
ms.date: 05/31/2018
---

# IWMPSettings2::requestMediaAccessRights method

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

 

 





