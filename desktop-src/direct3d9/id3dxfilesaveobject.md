---
description: Applications use the methods of the ID3DXFileSaveObject interface to write a .x file to disk, and to add and save data objects and templates.
ms.assetid: 1131c151-fa21-4654-9776-484922d58487
title: ID3DXFileSaveObject interface (D3DX9Xof.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXFileSaveObject
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXFileSaveObject interface

Applications use the methods of the ID3DXFileSaveObject interface to write a .x file to disk, and to add and save data objects and templates.

## Members

The **ID3DXFileSaveObject** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **ID3DXFileSaveObject** also has these types of members:

-   [Methods](#methods)

### Methods

The **ID3DXFileSaveObject** interface has these methods.



| Method                                                      | Description                                                                                                                  |
|:------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------|
| [**AddDataObject**](id3dxfilesaveobject--adddataobject.md) | Adds a data object as a child of the [**ID3DXFileSaveData**](id3dxfilesavedata.md) object.<br/>                       |
| [**GetFile**](id3dxfilesaveobject--getfile.md)             | Gets the [**ID3DXFile**](id3dxfile.md) interface of the object that created this **ID3DXFileSaveObject** object.<br/> |
| [**Save**](id3dxfilesaveobject--save.md)                   | Saves a data object and its children to a .x file on disk.<br/>                                                        |



 

## Remarks

Templates are not required in every file. For example, you could put all templates into a single .x file rather than duplicating them in every .x file.

The ID3DXFileSaveObject interface is obtained by calling the [**ID3DXFile::CreateSaveObject**](id3dxfile--createsaveobject.md) method.

The globally unique identifier (GUID) for the ID3DXFileSaveObject interface is IID\_ID3DXFileSaveObject.

The LPD3DXFILESAVEOBJECT type is defined as a pointer to this interface.


```
typedef interface ID3DXFileSaveObject *LPD3DXFILESAVEOBJECT;
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

 

 
