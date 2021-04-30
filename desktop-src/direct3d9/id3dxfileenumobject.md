---
description: Applications use the methods of the ID3DXFileEnumObject interface to cycle through the child file data objects in the file and to retrieve a child object by its globally unique identifier (GUID) or by its name.
ms.assetid: 23b28f07-5832-4163-953b-615d20e781f6
title: ID3DXFileEnumObject interface (D3DX9Xof.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXFileEnumObject
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXFileEnumObject interface

Applications use the methods of the ID3DXFileEnumObject interface to cycle through the child file data objects in the file and to retrieve a child object by its globally unique identifier (GUID) or by its name.

## Members

The **ID3DXFileEnumObject** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **ID3DXFileEnumObject** also has these types of members:

-   [Methods](#methods)

### Methods

The **ID3DXFileEnumObject** interface has these methods.



| Method                                                                  | Description                                                                |
|:------------------------------------------------------------------------|:---------------------------------------------------------------------------|
| [**GetChild**](id3dxfileenumobject--getchild.md)                       | Retrieves a child object in this file data object.<br/>              |
| [**GetChildren**](id3dxfileenumobject--getchildren.md)                 | Retrieves the number of child objects in this file data object.<br/> |
| [**GetDataObjectById**](id3dxfileenumobject--getdataobjectbyid.md)     | Retrieves the data object that has the specified GUID.<br/>          |
| [**GetDataObjectByName**](id3dxfileenumobject--getdataobjectbyname.md) | Retrieves the data object that has the specified name.<br/>          |
| [**GetFile**](id3dxfileenumobject--getfile.md)                         | Retrieves the [**ID3DXFile**](id3dxfile.md) object.<br/>            |



 

## Remarks

The GUID for the ID3DXFileEnumObject interface is IID\_ID3DXFileEnumObject.

The LPD3DXFILEENUMOBJECT type is defined as a pointer to this interface.


```
typedef interface ID3DXFileEnumObject *LPD3DXFILEENUMOBJECT;
```



## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Xof.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>  |



## See also

<dl> <dt>

[D3DX X File Interfaces](dx9-graphics-reference-d3dx-x-file-interfaces.md)
</dt> </dl>

 

 
