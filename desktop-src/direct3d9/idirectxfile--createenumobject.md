---
Description: Creates an enumerator object. Deprecated.
ms.assetid: 9e72bb2f-143e-4690-baef-ccded21572ec
title: IDirectXFileCreateEnumObject method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IDirectXFile::CreateEnumObject method

Creates an enumerator object. Deprecated.

## Syntax


```C++
HRESULT CreateEnumObject(
  [in]          LPVOID                  pvSource,
  [in]          DXFILELOADOPTIONS       dwLoadOptions,
  [out, retval] LPDIRECTXFILEENUMOBJECT *ppEnumObj
);
```



## Parameters

<dl> <dt>

*pvSource* \[in\]
</dt> <dd>

Type: **[**LPVOID**](winprog.windows_data_types)**

Pointer to data whose contents depend on the value of dwLoadOptions

</dd> <dt>

*dwLoadOptions* \[in\]
</dt> <dd>

Type: **[**DXFILELOADOPTIONS**](dxfile.md)**

Value that specifies the source of the data. This value can be one of the DXFILELOAD\_xxx flags in [DXFILE Constants](dxfile.md).

</dd> <dt>

*ppEnumObj* \[out, retval\]
</dt> <dd>

Type: **[**LPDIRECTXFILEENUMOBJECT**](idirectxfileenumobject.md)\***

Address of a pointer to an [**IDirectXFileEnumObject**](idirectxfileenumobject.md) interface, representing the created enumerator object.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is DXFILE\_OK. If the method fails, the return value can be one of the following: DXFILEERR\_BADALLOC, DXFILEERR\_BADFILEFLOATSIZE, DXFILEERR\_BADFILETYPE, DXFILEERR\_BADFILEVERSION, DXFILEERR\_BADRESOURCE, DXFILEERR\_BADVALUE, DXFILEERR\_FILENOTFOUND, DXFILEERR\_RESOURCENOTFOUND, DXFILEERR\_URLNOTFOUND.

## Remarks

After using this method, use one of the IDirectXFileEnumObject methods to retrieve a data object.

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>DXFile.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3dxof.lib</dt> </dl> |



## See also

<dl> <dt>

[IDirectXFile](idirectxfile.md)
</dt> </dl>

 

 




