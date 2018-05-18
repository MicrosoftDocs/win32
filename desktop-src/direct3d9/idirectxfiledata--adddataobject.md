---
Description: 'Adds a data object as a child object. Deprecated.'
ms.assetid: '43771dd6-c17f-4376-9b0a-459ba61ff4c5'
title: 'IDirectXFileData::AddDataObject method'
---

# IDirectXFileData::AddDataObject method

Adds a data object as a child object. Deprecated.

## Syntax


```C++
HRESULT AddDataObject(
  [in] LPDIRECTXFILEDATA pDataObj
);
```



## Parameters

<dl> <dt>

*pDataObj* \[in\]
</dt> <dd>

Type: **[**LPDIRECTXFILEDATA**](idirectxfiledata.md)**

Pointer to an [**IDirectXFileData**](idirectxfiledata.md) interface, representing the file data object to add as a child object.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is DXFILE\_OK. If the method fails, the return value can be one of the following values.DXFILEERR\_BADALLOC DXFILEERR\_BADVALUE

## Remarks

Use the [**IDirectXFileSaveObject::CreateDataObject**](idirectxfilesaveobject--createdataobject.md) method to create the [**IDirectXFileData**](idirectxfiledata.md) object before calling this method.

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>DXFile.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3dxof.lib</dt> </dl> |



## See also

<dl> <dt>

[IDirectXFileData](idirectxfiledata.md)
</dt> <dt>

[**IDirectXFileSaveObject::CreateDataObject**](idirectxfilesaveobject--createdataobject.md)
</dt> </dl>

 

 




