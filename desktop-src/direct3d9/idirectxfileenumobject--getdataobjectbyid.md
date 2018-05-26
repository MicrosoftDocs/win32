---
Description: Retrieves the data object that has the specified GUID. Deprecated.
ms.assetid: dd079b5c-18e1-4252-aabd-498c24910a08
title: IDirectXFileEnumObjectGetDataObjectById method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IDirectXFileEnumObject::GetDataObjectById method

Retrieves the data object that has the specified GUID. Deprecated.

## Syntax


```C++
HRESULT GetDataObjectById(
  [in]  REFGUID           rguid,
  [out] LPDIRECTXFILEDATA *ppDataObj
);
```



## Parameters

<dl> <dt>

*rguid* \[in\]
</dt> <dd>

Type: **[REFGUID](http://go.microsoft.com/?linkid=9742306)**

Reference to the requested GUID.

</dd> <dt>

*ppDataObj* \[out\]
</dt> <dd>

Type: **[**LPDIRECTXFILEDATA**](idirectxfiledata.md)\***

Address of a pointer to an [**IDirectXFileData**](idirectxfiledata.md) interface, representing the returned file data object.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is DXFILE\_OK. If the method fails, the return value can be one of the following values: DXFILEERR\_BADVALUE, DXFILEERR\_NOTFOUND.

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>DXFile.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3dxof.lib</dt> </dl> |



## See also

<dl> <dt>

[IDirectXFileEnumObject](idirectxfileenumobject.md)
</dt> </dl>

 

 




