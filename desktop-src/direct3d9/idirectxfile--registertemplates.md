---
description: Registers custom templates. Deprecated.
ms.assetid: f9b24800-83a5-45bf-b19f-b247c88a2c2c
title: IDirectXFile::RegisterTemplates method (DXFile.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IDirectXFile.RegisterTemplates
api_type: 
- COM
api_location: 
- D3dxof.lib
- D3dxof.dll
---

# IDirectXFile::RegisterTemplates method

Registers custom templates. Deprecated.

## Syntax


```C++
HRESULT RegisterTemplates(
  [in] LPVOID pvData,
  [in] DWORD  cbSize
);
```



## Parameters

<dl> <dt>

*pvData* \[in\]
</dt> <dd>

Type: **[**LPVOID**](../winprog/windows-data-types.md)**

Pointer to a buffer consisting of a DirectX file in text or binary format that contains templates.

</dd> <dt>

*cbSize* \[in\]
</dt> <dd>

Type: **[**DWORD**](../winprog/windows-data-types.md)**

Size of the buffer pointed to by pvData, in bytes.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is DXFILE\_OK. If the method fails, the return value can be one of the following values: DXFILEERR\_BADFILEFLOATSIZE, DXFILEERR\_BADFILETYPE, DXFILEERR\_BADFILEVERSION, DXFILEERR\_BADVALUE, DXFILEERR\_PARSEERROR.

## Remarks

The following code fragment provides an example call to **RegisterTemplates** And example contents for the buffer to which pvData points.


```
    TIDirectXFile * pDXFile;
    char *szTemplates = "xof 0303txt 0032\
        template SimpleData { \
            <2b934580-9e9a-11cf-ab39-0020af71e433> \
            DWORD item1;DWORD item2;DWORD item3;} \
        template ArrayData { \
            <2b934581-9e9a-11cf-ab39-0020af71e433> \
            DWORD cItems; array DWORD aItem[2][cItems]; [...] } \
        template RestrictedData { \
            <2b934582-9e9a-11cf-ab39-0020af71e433> \
            DWORD item; [SimpleData]}";
    hr = pDXFile->RegisterTemplates(szTemplates, strlen(szTemplates));
    
    
```



All templates must specify a name and a Universally Unique Identifier (UUID).

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>DXFile.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3dxof.lib</dt> </dl> |



## See also

<dl> <dt>

[IDirectXFile](idirectxfile.md)
</dt> </dl>

 

 
