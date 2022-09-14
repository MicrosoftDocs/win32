---
description: Applications use the methods of the IDirectXFileData interface to build or to access the immediate hierarchy of the data object.
ms.assetid: 8810162f-76a8-45ba-b069-7910fd611a60
title: IDirectXFileData interface (DXFile.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IDirectXFileData
api_type: 
- COM
api_location: 
- d3dxof.lib
- d3dxof.dll
---

# IDirectXFileData interface

Applications use the methods of the IDirectXFileData interface to build or to access the immediate hierarchy of the data object. Template restrictions determine the hierarchy. Data types allowed by the template are called optional members. The optional members are not required, but an object might miss important information without them. These optional members are saved as children of the data object. The children can be another data object, a reference to an earlier data object, or a binary object. Deprecated.

## Members

The **IDirectXFileData** interface inherits from [**IDirectXFileObject**](idirectxfileobject.md). **IDirectXFileData** also has these types of members:

-   [Methods](#methods)

### Methods

The **IDirectXFileData** interface has these methods.



| Method                                                         | Description                                                                                                               |
|:---------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------|
| [**AddBinaryObject**](idirectxfiledata--addbinaryobject.md)   | Creates a binary object and adds it as a child object. Deprecated.<br/>                                             |
| [**AddDataObject**](idirectxfiledata--adddataobject.md)       | Adds a data object as a child object. Deprecated.<br/>                                                              |
| [**AddDataReference**](idirectxfiledata--adddatareference.md) | Creates and adds a data reference object as a child object. Deprecated.<br/>                                        |
| [**GetData**](idirectxfiledata--getdata.md)                   | Retrieves the data for one of the object's members or the data for all members. Deprecated.<br/>                    |
| [**GetNextObject**](idirectxfiledata--getnextobject.md)       | Retrieves the next child data object, data reference object, or binary object in the DirectX file. Deprecated.<br/> |
| [**GetType**](idirectxfiledata--gettype.md)                   | Retrieves the GUID of the object's template. Deprecated.<br/>                                                       |



 

## Remarks

The GUID for the IDirectXFileData interface is IID\_IDirectXFileData.

The LPDIRECTXFILEDATA type is defined as a pointer to this interface.


```
typedef interface IDirectXFileData *LPDIRECTXFILEDATA;
```



## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>DXFile.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3dxof.lib</dt> </dl> |



## See also

<dl> <dt>

[**IDirectXFileObject**](idirectxfileobject.md)
</dt> <dt>

[X File Interfaces](dx9-graphics-reference-x-file-interfaces.md)
</dt> </dl>

 

 




