---
title: IWMPLibraryServices getLibraryByType method
description: The getLibraryByType method returns an IWMPLibrary interface that represents the library that has the specified type and index.
ms.assetid: 2507c764-a2cf-42f9-ad44-eaf040b78891
keywords:
- getLibraryByType method Windows Media Player
- getLibraryByType method Windows Media Player , IWMPLibraryServices interface
- IWMPLibraryServices interface Windows Media Player , getLibraryByType method
topic_type:
- apiref
api_name:
- IWMPLibraryServices.getLibraryByType
api_location:
- Interop.WMPLib.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IWMPLibraryServices::getLibraryByType method

The **getLibraryByType** method returns an **IWMPLibrary** interface that represents the library that has the specified type and index.

## Syntax


```CSharp
public IWMPLibrary getLibraryByType(
  WMPLibraryType wmplt,
  System.Int32 lIndex
);
```


```VB

Public Function getLibraryByType( _
  ByVal wmplt As WMPLibraryType, _
  ByVal lIndex As System.Int32 _
) As IWMPLibrary
Implements IWMPLibraryServices.getLibraryByType
```





## Parameters

<dl> <dt>

*wmplt* \[in\]
</dt> <dd>

A value from the **WMPLib.WMPLibraryType** enumeration that specifies the type of library to retrieve.

</dd> <dt>

*lIndex* \[in\]
</dt> <dd>

A **System.Int32** that is the index of the library to retrieve.

</dd> </dl>

## Return value

A **WMPLib.IWMPLibrary** interface for the library that is returned.

## Remarks

There is only one local library, and disc libraries are available only on data CDs and DVDs that contain media content.

## Requirements



| Requirement | Value |
|----------------------|------------------------------------------------------------------------------------------------------------------------|
| Version<br/>   | Windows Media Player 11.<br/>                                                                                    |
| Namespace<br/> | **WMPLib**<br/>                                                                                                  |
| Assembly<br/>  | <dl> <dt>Interop.WMPLib.dll (Interop.WMPLib.dll.dll)</dt> </dl> |



## See also

<dl> <dt>

[**IWMPLibrary Interface (VB and C#)**](iwmplibrary--vb-and-c.md)
</dt> <dt>

[**IWMPLibraryServices Interface (VB and C#)**](iwmplibraryservices--vb-and-c.md)
</dt> <dt>

[**WMPLibraryType**](/previous-versions/windows/desktop/api/wmp/ne-wmp-wmplibrarytype)
</dt> </dl>

 

 





