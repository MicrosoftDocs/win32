---
description: Applications use the methods of the IDirectXFileDataReference interface to support data reference objects.
ms.assetid: e0f6046f-36d9-4a13-9a0c-0738ebb2e569
title: IDirectXFileDataReference interface (DXFile.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IDirectXFileDataReference
api_type: 
- COM
api_location: 
- d3dxof.lib
- d3dxof.dll
---

# IDirectXFileDataReference interface

Applications use the methods of the IDirectXFileDataReference interface to support data reference objects. A data reference object refers to a data object that is defined earlier in the file. This enables you to use the same object multiple times without repeating it in the file. Deprecated.

## Members

The **IDirectXFileDataReference** interface inherits from [**IDirectXFileObject**](idirectxfileobject.md). **IDirectXFileDataReference** also has these types of members:

-   [Methods](#methods)

### Methods

The **IDirectXFileDataReference** interface has these methods.



| Method                                                | Description                                      |
|:------------------------------------------------------|:-------------------------------------------------|
| [**Resolve**](idirectxfiledatareference--resolve.md) | Resolves data references. Deprecated.<br/> |



 

## Remarks

After you have determined that an object is a data reference object, use the [**IDirectXFileDataReference::Resolve**](idirectxfiledatareference--resolve.md) method to retrieve the referenced object defined earlier in the file. For information about how to identify a data reference object, see the [**IDirectXFileData**](idirectxfiledata.md) interface.

The GUID for the IDirectXFileDataReference interface is IID\_IDirectXFileDataReference.

The LPDIRECTXFILEDataReference type is defined as a pointer to this interface.


```
typedef interface IDirectXFileDataReference *LPDIRECTXFILEDATAREFERENCE;
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

 

 




