---
description: Applications use the methods of the IDirectXFileSaveObject interface to create data objects and to save templates and data objects.
ms.assetid: 7948a7d2-b150-45cf-a1fc-5dca21d74770
title: IDirectXFileSaveObject interface (DXFile.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IDirectXFileSaveObject
api_type: 
- COM
api_location: 
- d3dxof.lib
- d3dxof.dll
---

# IDirectXFileSaveObject interface

Applications use the methods of the IDirectXFileSaveObject interface to create data objects and to save templates and data objects. Note that templates are not required in every file. For example, you could put all templates into a single Microsoft DirectX file rather than duplicating them in every DirectX file. Deprecated.

## Members

The **IDirectXFileSaveObject** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **IDirectXFileSaveObject** also has these types of members:

-   [Methods](#methods)

### Methods

The **IDirectXFileSaveObject** interface has these methods.



| Method                                                               | Description                                                                    |
|:---------------------------------------------------------------------|:-------------------------------------------------------------------------------|
| [**CreateDataObject**](idirectxfilesaveobject--createdataobject.md) | Creates a data object. Deprecated.<br/>                                  |
| [**SaveData**](idirectxfilesaveobject--savedata.md)                 | Saves a data object and its children to a DirectX file. Deprecated.<br/> |
| [**SaveTemplates**](idirectxfilesaveobject--savetemplates.md)       | Saves templates to a DirectX file. Deprecated.<br/>                      |



 

## Remarks

The globally unique identifier (GUID) for the IDirectXFileSaveObject interface is **IID\_IDirectXFileSaveObject**.

The **IDirectXFileSaveObject** interface is obtained by calling the [**IDirectXFile::CreateSaveObject**](idirectxfile--createsaveobject.md) method.

The **LPDIRECTXFILESAVEOBJECT** type is defined as a pointer to this interface.


```
typedef interface IDirectXFileSaveObject *LPDIRECTXFILESAVEOBJECT;
```



## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>DXFile.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3dxof.lib</dt> </dl> |



## See also

<dl> <dt>

[X File Interfaces](dx9-graphics-reference-x-file-interfaces.md)
</dt> </dl>

 

 
