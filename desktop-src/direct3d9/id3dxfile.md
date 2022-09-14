---
description: Applications use the methods of the ID3DXFile interface to create instances of the ID3DXFileEnumObject and ID3DXFileSaveObject interfaces, and to register templates.
ms.assetid: 472d45b1-5c03-4417-a005-91f802667919
title: ID3DXFile interface (D3DX9Xof.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXFile
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXFile interface

Applications use the methods of the ID3DXFile interface to create instances of the [**ID3DXFileEnumObject**](id3dxfileenumobject.md) and [**ID3DXFileSaveObject**](id3dxfilesaveobject.md) interfaces, and to register templates.

## Members

The **ID3DXFile** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **ID3DXFile** also has these types of members:

-   [Methods](#methods)

### Methods

The **ID3DXFile** interface has these methods.



| Method                                                            | Description                                                                                                            |
|:------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------|
| [**CreateEnumObject**](id3dxfile--createenumobject.md)           | Creates an enumerator object that will read a .x file.<br/>                                                      |
| [**CreateSaveObject**](id3dxfile--createsaveobject.md)           | Creates a save object that will be used to save data to a .x file.<br/>                                          |
| [**RegisterEnumTemplates**](id3dxfile--registerenumtemplates.md) | Registers custom templates, given an [**ID3DXFileEnumObject**](id3dxfileenumobject.md) enumeration object.<br/> |
| [**RegisterTemplates**](id3dxfile--registertemplates.md)         | Registers custom templates.<br/>                                                                                 |



 

## Remarks

An ID3DXFile object also contains a local template store. This local storage may be added to only with the [**ID3DXFile::RegisterEnumTemplates**](id3dxfile--registerenumtemplates.md) and [**ID3DXFile::RegisterTemplates**](id3dxfile--registertemplates.md) methods.

[**ID3DXFileEnumObject**](id3dxfileenumobject.md) and [**ID3DXFileSaveObject**](id3dxfilesaveobject.md) objects created with [**ID3DXFile::CreateEnumObject**](id3dxfile--createenumobject.md) and [**ID3DXFile::CreateSaveObject**](id3dxfile--createsaveobject.md) also utilize the template store of the parent ID3DXFile object.

The ID3DXFile interface is obtained by calling the [**D3DXFileCreate**](d3dxfilecreate.md) function.

The globally unique identifier (GUID) for the ID3DXFile interface is IID\_ID3DXFile.

The LPD3DXFILE type is defined as a pointer to the ID3DXFile interface.


```
typedef interface ID3DXFile *LPD3DXFILE;
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

 

 
