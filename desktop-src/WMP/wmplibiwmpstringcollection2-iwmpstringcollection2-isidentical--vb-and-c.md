---
title: IWMPStringCollection2 isIdentical method
description: The isIdentical method returns a value indicating whether the object represented by the supplied interface is the same as the current one.
ms.assetid: 826e7fd8-88f8-4a2a-9ca0-82a500099272
keywords:
- isIdentical method Windows Media Player
- isIdentical method Windows Media Player , IWMPStringCollection2 interface
- IWMPStringCollection2 interface Windows Media Player , isIdentical method
topic_type:
- apiref
api_name:
- IWMPStringCollection2.isIdentical
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPStringCollection2::isIdentical method

The **isIdentical** method returns a value indicating whether the object represented by the supplied interface is the same as the current one.

## Syntax


```CSharp
public System.Boolean isIdentical(
  IWMPStringCollection2 pIWMPStringCollection2
);
```


```VB

Public Function isIdentical( _
  ByVal pIWMPStringCollection2 As IWMPStringCollection2 _
) As System.Boolean
Implements IWMPStringCollection2.isIdentical
```





## Parameters

<dl> <dt>

*pIWMPStringCollection2* \[in\]
</dt> <dd>

The **WMPLib.IWMPStringCollection2** interface that represents the object to compare with current one.

</dd> </dl>

## Return value

The **System.Boolean** that is the result of the comparison. A value of **true** indicates that the string collection objects are the same.

## Remarks

To use this method, read access to the library is required. For more information, see [Library Access](library-access.md).

## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 11.<br/>                                                                                    |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPStringCollection2 Interface (VB and C#)**](iwmpstringcollection2--vb-and-c.md)
</dt> </dl>

 

 





