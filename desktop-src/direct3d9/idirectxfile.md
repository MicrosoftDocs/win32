---
description: Applications use the methods of the IDirectXFile interface to create instances of the IDirectXFileEnumObject and IDirectXFileSaveObject interfaces, and to register templates. Deprecated.
ms.assetid: c4e800dc-72a9-4b91-9c89-ee76764b1bb9
title: IDirectXFile interface (DXFile.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IDirectXFile
api_type: 
- COM
api_location: 
- d3dxof.lib
- d3dxof.dll
---

# IDirectXFile interface

Applications use the methods of the IDirectXFile interface to create instances of the [**IDirectXFileEnumObject**](idirectxfileenumobject.md) and [**IDirectXFileSaveObject**](idirectxfilesaveobject.md) interfaces, and to register templates. Deprecated.

## Members

The **IDirectXFile** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **IDirectXFile** also has these types of members:

-   [Methods](#methods)

### Methods

The **IDirectXFile** interface has these methods.



| Method                                                       | Description                                          |
|:-------------------------------------------------------------|:-----------------------------------------------------|
| [**CreateEnumObject**](idirectxfile--createenumobject.md)   | Creates an enumerator object. Deprecated.<br/> |
| [**CreateSaveObject**](idirectxfile--createsaveobject.md)   | Creates a save object. Deprecated.<br/>        |
| [**RegisterTemplates**](idirectxfile--registertemplates.md) | Registers custom templates. Deprecated.<br/>   |



 

## Remarks

The globally unique identifier (GUID) for the IDirectXFile interface is IID\_IDirectXFile.

The IDirectXFile interface is obtained by calling the [**DirectXFileCreate**](directxfilecreate.md) function.

The LPDIRECTXFILE type is defined as a pointer to this interface.


```
typedef interface IDirectXFile *LPDIRECTXFILE;
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

 

 
