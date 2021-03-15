---
description: Creates an enumerator object. Deprecated.
ms.assetid: 9e72bb2f-143e-4690-baef-ccded21572ec
title: IDirectXFile::CreateEnumObject method (DXFile.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IDirectXFile.CreateEnumObject
api_type: 
- COM
api_location: 
- D3dxof.lib
- D3dxof.dll
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

Type: **[**LPVOID**](../winprog/windows-data-types.md)**

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

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is DXFILE\_OK. If the method fails, the return value can be one of the following: DXFILEERR\_BADALLOC, DXFILEERR\_BADFILEFLOATSIZE, DXFILEERR\_BADFILETYPE, DXFILEERR\_BADFILEVERSION, DXFILEERR\_BADRESOURCE, DXFILEERR\_BADVALUE, DXFILEERR\_FILENOTFOUND, DXFILEERR\_RESOURCENOTFOUND, DXFILEERR\_URLNOTFOUND.

## Remarks

After using this method, use one of the IDirectXFileEnumObject methods to retrieve a data object.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>DXFile.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3dxof.lib</dt> </dl> |



## See also

<dl> <dt>

[IDirectXFile](idirectxfile.md)
</dt> </dl>

 

 
