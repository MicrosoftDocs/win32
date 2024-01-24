---
description: Applications use the methods of the IDirectXFileObject interface to retrieve information about Microsoft DirectX file objects. Deprecated.
ms.assetid: 015d2c4e-4a25-40da-b88a-bad0c4e20e09
title: IDirectXFileObject interface (DXFile.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IDirectXFileObject
api_type: 
- COM
api_location: 
- d3dxof.lib
- d3dxof.dll
---

# IDirectXFileObject interface

Applications use the methods of the IDirectXFileObject interface to retrieve information about Microsoft DirectX file objects. Deprecated.

## Members

The **IDirectXFileObject** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **IDirectXFileObject** also has these types of members:

-   [Methods](#methods)

### Methods

The **IDirectXFileObject** interface has these methods.



| Method                                         | Description                                                                                   |
|:-----------------------------------------------|:----------------------------------------------------------------------------------------------|
| [**GetId**](idirectxfileobject--getid.md)     | Retrieves a pointer to the GUID that identifies a DirectX file object. Deprecated.<br/> |
| [**GetName**](idirectxfileobject--getname.md) | Retrieves a pointer to a DirectX file object's name. Deprecated.<br/>                   |



 

## Remarks

The GUID for the IDirectXFileObject interface is IID\_IDirectXFileObject.

The LPDIRECTXFILEOBJECT type is defined as a pointer to this interface.


```
typedef interface IDirectXFileObject *LPDIRECTXFILEOBJECT;
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

 

 
