---
title: IWMPStringCollection2 getItemInfo method
description: The getItemInfo method returns the string corresponding to the specified string collection item index and name.
ms.assetid: 4a107e85-9eb7-42be-b1f9-8e9e92e6e509
keywords:
- getItemInfo method Windows Media Player
- getItemInfo method Windows Media Player , IWMPStringCollection2 interface
- IWMPStringCollection2 interface Windows Media Player , getItemInfo method
topic_type:
- apiref
api_name:
- IWMPStringCollection2.getItemInfo
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPStringCollection2::getItemInfo method

The **getItemInfo** method returns the string corresponding to the specified string collection item index and name.

## Syntax


```CSharp
public System.String getItemInfo(
  System.Int32 lCollectionIndex,
  System.String bstrItemName
);
```


```VB

Public Function getItemInfo( _
  ByVal lCollectionIndex As System.Int32, _
  ByVal bstrItemName As System.String _
) As System.String
Implements IWMPStringCollection2.getItemInfo
```





## Parameters

<dl> <dt>

*lCollectionIndex* \[in\]
</dt> <dd>

The **System.Int32** specifying the zero-based index of the string collection item from which to get the attribute.

</dd> <dt>

*bstrItemName* \[in\]
</dt> <dd>

The **System.String** that is the attribute name.

</dd> </dl>

## Return value

The **System.String** that is the name of the string collection item. For attributes whose underlying value is **System.Boolean**, it returns the string "true" or "false".

## Remarks

To retrieve attributes with multiple values and attributes with complex values, use the **getItemInfoByType** method.

To use this method, read access to the library is required. For more information, see [Library Access](library-access.md).

## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 11.<br/>                                                                                    |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPStringCollection2 Interface**](iwmpstringcollection2--vb-and-c.md)
</dt> <dt>

[**IWMPStringCollection2.getItemInfoByType (VB and C#)**](wmplibiwmpstringcollection2-iwmpstringcollection2-getiteminfobytype--vb-and-c.md)
</dt> </dl>

 

 





