---
description: Saves a data object and its children to a DirectX file. Deprecated.
ms.assetid: 18bd5ef6-9e17-4c21-bc14-373de8df9ffb
title: IDirectXFileSaveObject::SaveData method (DXFile.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IDirectXFileSaveObject.SaveData
api_type: 
- COM
api_location: 
- D3dxof.lib
- D3dxof.dll
---

# IDirectXFileSaveObject::SaveData method

Saves a data object and its children to a DirectX file. Deprecated.

## Syntax


```C++
HRESULT SaveData(
  [in] LPDIRECTXFILEDATA pDataObj
);
```



## Parameters

<dl> <dt>

*pDataObj* \[in\]
</dt> <dd>

Type: **[**LPDIRECTXFILEDATA**](idirectxfiledata.md)**

Pointer to an [**IDirectXFileData**](idirectxfiledata.md) interface, representing the file data object to save.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is DXFILE\_OK. If the method fails, the return value can be one of the following values: DXFILEERR\_BADARRAYSIZE, DXFILEERR\_BADVALUE.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>DXFile.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3dxof.lib</dt> </dl> |



## See also

<dl> <dt>

[IDirectXFileSaveObject](idirectxfilesaveobject.md)
</dt> </dl>

 

 




