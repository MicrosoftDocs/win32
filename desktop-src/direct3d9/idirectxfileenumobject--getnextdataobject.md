---
Description: Retrieves the next top-level object in the DirectX file. Deprecated.
ms.assetid: 91cd3205-5603-4a62-aab2-7ef4adb9e6d1
title: IDirectXFileEnumObjectGetNextDataObject method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IDirectXFileEnumObject::GetNextDataObject method

Retrieves the next top-level object in the DirectX file. Deprecated.

## Syntax


```C++
HRESULT GetNextDataObject(
  [out] LPDIRECTXFILEDATA *ppDataObj
);
```



## Parameters

<dl> <dt>

*ppDataObj* \[out\]
</dt> <dd>

Type: **[**LPDIRECTXFILEDATA**](idirectxfiledata.md)\***

Address of a pointer to an [**IDirectXFileData**](idirectxfiledata.md) interface, representing the returned file data object.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is DXFILE\_OK. If the method fails, the return value can be one of the following values: DXFILEERR\_BADVALUE, DXFILEERR\_NOMOREOBJECTS

## Remarks

Top-level objects are always data objects. Data reference objects and binary objects can only be children of data objects.

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>DXFile.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3dxof.lib</dt> </dl> |



## See also

<dl> <dt>

[IDirectXFileEnumObject](idirectxfileenumobject.md)
</dt> </dl>

 

 




