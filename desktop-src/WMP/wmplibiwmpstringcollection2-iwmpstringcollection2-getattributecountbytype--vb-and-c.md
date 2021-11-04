---
title: IWMPStringCollection2 getAttributeCountByType method
description: The getAttributeCountByType method returns the number of attributes associated with the specified string collection index, attribute name, and language.
ms.assetid: 30312039-3676-4322-b6f6-fb86098bf578
keywords:
- getAttributeCountByType method Windows Media Player
- getAttributeCountByType method Windows Media Player , IWMPStringCollection2 interface
- IWMPStringCollection2 interface Windows Media Player , getAttributeCountByType method
topic_type:
- apiref
api_name:
- IWMPStringCollection2.getAttributeCountByType
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPStringCollection2::getAttributeCountByType method

The **getAttributeCountByType** method returns the number of attributes associated with the specified string collection index, attribute name, and language.

## Syntax


```CSharp
public System.Int32 getAttributeCountByType(
  System.Int32 lCollectionIndex,
  System.String bstrType,
  System.String bstrLanguage
);
```


```VB

Public Function getAttributeCountByType( _
  ByVal lCollectionIndex As System.Int32, _
  ByVal bstrType As System.String, _
  ByVal bstrLanguage As System.String _
) As System.Int32
Implements IWMPStringCollection2.getAttributeCountByType
```





## Parameters

<dl> <dt>

*lCollectionIndex* \[in\]
</dt> <dd>

The **System.Int32** specifying the zero-based index of the string collection item from which to get the attribute.

</dd> <dt>

*bstrType* \[in\]
</dt> <dd>

The **System.String** that is the name of the attribute.

</dd> <dt>

*bstrLanguage* \[in\]
</dt> <dd>

The **System.String** that is the name of the language. If the value is set to null or to a zero-length string (""), the current locale string is used. Otherwise, the value must be a valid RFC 1766 language string such as "en-us".

</dd> </dl>

## Return value

The **System.Int32** that is the count.

## Remarks

This method is used to discover the number of attributes corresponding to a particular attribute name for a given **StringCollection** item. Index numbers can then be passed to the fourth parameter of the **getItemInfoByType** method.

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
</dt> <dt>

[**IWMPStringCollection2.getItemInfoByType (VB and C#)**](wmplibiwmpstringcollection2-iwmpstringcollection2-getiteminfobytype--vb-and-c.md)
</dt> </dl>

 

 





