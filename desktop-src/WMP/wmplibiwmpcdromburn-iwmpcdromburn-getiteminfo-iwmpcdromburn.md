---
title: IWMPCdromBurn getItemInfo method
description: The getItemInfo method retrieves the value of the specified attribute for the CD.
ms.assetid: 9ca54ec4-42be-40c1-931e-c3bfcbc2b370
keywords:
- getItemInfo method Windows Media Player
- getItemInfo method Windows Media Player , IWMPCdromBurn interface
- IWMPCdromBurn interface Windows Media Player , getItemInfo method
topic_type:
- apiref
api_name:
- IWMPCdromBurn.getItemInfo
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPCdromBurn::getItemInfo method

The **getItemInfo** method retrieves the value of the specified attribute for the CD.

## Syntax


```CSharp
public System.String getItemInfo(
  System.String bstrItem
);
```


```VB

Public Function getItemInfo( _
  ByVal bstrItem As System.String _
) As System.String
Implements IWMPCdromBurn.getItemInfo
```





## Parameters

<dl> <dt>

*bstrItem* \[in\]
</dt> <dd>

A **System.String** that contains one of the following values.



| Value         | Description                                                                                  |
|---------------|----------------------------------------------------------------------------------------------|
| AvailableTime | Retrieves the time available on the CD, in seconds.                                          |
| Blank         | Retrieves a **System.Boolean** (represented as a string) indicating whether the CD is blank. |
| FreeSpace     | Retrieves the free space on the CD, in bytes.                                                |
| TotalSpace    | Retrieves the total space on the CD, in bytes.                                               |



 

</dd> </dl>

## Return value

A **System.String** that is the value of the specified attribute.

## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 11<br/>                                                                                     |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPCdromBurn Interface (VB and C#)**](iwmpcdromburn--vb-and-c.md)
</dt> </dl>

 

 





