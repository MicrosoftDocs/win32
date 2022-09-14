---
description: Applications use the methods of the ID3DXFileData interface to build or to access the immediate hierarchy of the data object. Template restrictions determine the hierarchy.
ms.assetid: ce291e2b-b926-4502-8bee-55fe6d6d3267
title: ID3DXFileData interface (D3DX9Xof.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXFileData
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXFileData interface

Applications use the methods of the ID3DXFileData interface to build or to access the immediate hierarchy of the data object. Template restrictions determine the hierarchy.

## Members

The **ID3DXFileData** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **ID3DXFileData** also has these types of members:

-   [Methods](#methods)

### Methods

The **ID3DXFileData** interface has these methods.



| Method                                            | Description                                                                                                          |
|:--------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------|
| [**GetChild**](id3dxfiledata--getchild.md)       | Retrieves a child object in this file data object.<br/>                                                        |
| [**GetChildren**](id3dxfiledata--getchildren.md) | Retrieves the number of children in this file data object.<br/>                                                |
| [**GetEnum**](id3dxfiledata--getenum.md)         | Retrieves the enumeration object in this file data object.<br/>                                                |
| [**GetId**](id3dxfiledata--getid.md)             | Retrieves the GUID of this file data object.<br/>                                                              |
| [**GetName**](id3dxfiledata--getname.md)         | Retrieves the name of this file data object.<br/>                                                              |
| [**GetType**](id3dxfiledata--gettype.md)         | Retrieves the template ID in this file data object.<br/>                                                       |
| [**IsReference**](id3dxfiledata--isreference.md) | Indicates whether this file data object is a reference object that points to another child data object.<br/>   |
| [**Lock**](id3dxfiledata--lock.md)               | Accesses the .x file data.<br/>                                                                                |
| [**Unlock**](id3dxfiledata--unlock.md)           | Ends the lifespan of the *ppData* pointer returned by [**ID3DXFileData::Lock**](id3dxfiledata--lock.md).<br/> |



 

## Remarks

Data types allowed by the template are called optional members. The optional members are not required, but an object might miss important information without them. These optional members are saved as children of the data object. A child can be another data object or a reference to an earlier data object.

The GUID for the ID3DXFileData interface is IID\_ID3DXFileData.

The LPD3DXFILEDATA type is defined as a pointer to this interface.


```
typedef interface ID3DXFileData *LPD3DXFILEDATA;
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

 

 
