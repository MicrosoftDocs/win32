---
description: Applications use the methods of the ID3DXFileSaveData interface to add data objects as children of a .x file data node.
ms.assetid: ab5bdd9a-496a-4ae1-b93a-fe5856bd97d4
title: ID3DXFileSaveData interface (D3DX9Xof.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXFileSaveData
api_type: 
- COM
api_location: 
- d3dx9.lib
- d3dx9.dll
---

# ID3DXFileSaveData interface

Applications use the methods of the ID3DXFileSaveData interface to add data objects as children of a .x file data node.

## Members

The **ID3DXFileSaveData** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **ID3DXFileSaveData** also has these types of members:

-   [Methods](#methods)

### Methods

The **ID3DXFileSaveData** interface has these methods.



| Method                                                          | Description                                                                                                                                |
|:----------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------|
| [**AddDataObject**](id3dxfilesavedata--adddataobject.md)       | Adds a data object as a child of the **ID3DXFileSaveData** file data node.<br/>                                                      |
| [**AddDataReference**](id3dxfilesavedata--adddatareference.md) | Adds a data reference as a child of this **ID3DXFileSaveData** file data node. The data reference points to a file data object.<br/> |
| [**GetId**](id3dxfilesavedata--getid.md)                       | Retrieves the GUID of this **ID3DXFileSaveData** file data node.<br/>                                                                |
| [**GetName**](id3dxfilesavedata--getname.md)                   | Retrieves the name of this **ID3DXFileSaveData** file data node.<br/>                                                                |
| [**GetSave**](id3dxfilesavedata--getsave.md)                   | Retrieves a pointer to this [**ID3DXFileSaveObject**](id3dxfilesaveobject.md) file data node.<br/>                                  |
| [**GetType**](id3dxfilesavedata--gettype.md)                   | Retrieves the template ID of this file data node.<br/>                                                                               |



 

## Remarks

The GUID for the ID3DXFileSaveObject interface is IID\_ID3DXFileSaveObject.

The LPD3DXFileSaveData type is defined as a pointer to this interface.


```
typedef interface ID3DXFileSaveData *LPD3DXFILESAVEDATA;
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

 

 
