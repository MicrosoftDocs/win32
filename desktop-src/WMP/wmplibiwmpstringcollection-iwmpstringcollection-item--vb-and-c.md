---
title: IWMPStringCollection Item method
description: The Item method returns the string at the specified index.
ms.assetid: 77546cb2-eda5-4bb8-97b9-55270461815f
keywords:
- Item method Windows Media Player
- Item method Windows Media Player , IWMPStringCollection interface
- IWMPStringCollection interface Windows Media Player , Item method
topic_type:
- apiref
api_name:
- IWMPStringCollection.Item
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPStringCollection::Item method

The **Item** method returns the string at the specified index.

## Syntax


```CSharp
public System.String Item(
  System.Int32 lIndex
);
```


```VB

Public Function Item( _
  ByVal lIndex As System.Int32 _
) As System.String
Implements IWMPStringCollection.Item
```





## Parameters

<dl> <dt>

*lIndex* \[in\]
</dt> <dd>

A **System.Int32** that is the index.

</dd> </dl>

## Return value

A **System.String** that is the string at the specified index.

## Remarks

The **IWMPStringCollection** interface is used to retrieve the set of values available for an attribute. For example, the **IWMPMediaCollection.getAttributeStringCollection** method can be used to retrieve an **IWMPStringCollection** interface representing all the values for the Genre attribute within the Audio media type. The **Item** method can then be used to iterate through all of the possible values for the Genre attribute.

To use this method, read access to the library is required. For more information, see [Library Access](library-access.md).

## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 9 Series or later<br/>                                                                      |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPMediaCollection.getAttributeStringCollection (VB and C#)**](wmplibiwmpmediacollection-iwmpmediacollection-getattributestringcollection--vb-and-c.md)
</dt> <dt>

[**IWMPSettings2.mediaAccessRights (VB and C#)**](wmplibiwmpsettings2-iwmpsettings2-mediaaccessrights--vb-and-c.md)
</dt> <dt>

[**IWMPSettings2.requestMediaAccessRights (VB and C#)**](wmplibiwmpsettings2-iwmpsettings2-requestmediaaccessrights--vb-and-c.md)
</dt> <dt>

[**IWMPStringCollection Interface (VB and C#)**](iwmpstringcollection--vb-and-c.md)
</dt> </dl>

 

 





