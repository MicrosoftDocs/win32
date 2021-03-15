---
description: Creates a save object that will be used to save data to a .x file.
ms.assetid: da064e83-605f-4c86-985d-9a0961c18e01
title: ID3DXFile::CreateSaveObject method (D3DX9Xof.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ID3DXFile.CreateSaveObject
api_type: 
- COM
api_location: 
- D3dx9.lib
- D3dx9.dll
---

# ID3DXFile::CreateSaveObject method

Creates a save object that will be used to save data to a .x file.

## Syntax


```C++
HRESULT CreateSaveObject(
  [in]  LPCVOID               pData,
  [in]  D3DXF_FILESAVEOPTIONS flags,
  [in]  D3DXF_FILEFORMAT      dwFileFormat,
  [out] ID3DXFileSaveObject   **ppSaveObj
);
```



## Parameters

<dl> <dt>

*pData* \[in\]
</dt> <dd>

Type: **[**LPCVOID**](../winprog/windows-data-types.md)**

Pointer to the name of the file to use for saving data.

</dd> <dt>

*flags* \[in\]
</dt> <dd>

Type: **[D3DXF\_FILESAVEOPTIONS](d3dxf.md)**

Value that specifies the name of the file to which data is to be saved. This value can be one of the [File Save Options](d3dxf.md) flags.

</dd> <dt>

*dwFileFormat* \[in\]
</dt> <dd>

Type: **[D3DXF\_FILEFORMAT](d3dxf.md)**

Indicates the format to use when saving the .x file. This value can be one of the [File Formats](d3dxf.md) flags. For more information, see Remarks.

</dd> <dt>

*ppSaveObj* \[out\]
</dt> <dd>

Type: **[**ID3DXFileSaveObject**](id3dxfilesaveobject.md)\*\***

Address of a pointer to an [**ID3DXFileSaveObject**](id3dxfilesaveobject.md) interface, representing the created save object.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is S\_OK. If the method fails, the return value can be one of the following: D3DXFERR\_BADVALUE, D3DXFERR\_PARSEERROR.

## Remarks

After using this method, use methods of the [**ID3DXFileSaveObject**](id3dxfilesaveobject.md) interface to create data objects and to save templates or data.

For the saved file format *dwFileFormat*, one of the binary, legacy binary, or text flags in [File Formats](d3dxf.md) must be specified. The file can be compressed by using the optional D3DXF\_FILEFORMAT\_COMPRESSED flag.

The file format values can be combined in a logical OR to create compressed text or compressed binary files. If you indicate that the file format should be text and compressed, the file will be written out first as text and then compressed. However, compressed text files are not as efficient as binary text files; in most cases, therefore, you will want to indicate binary and compressed.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>D3DX9Xof.h</dt> </dl> |
| Library<br/> | <dl> <dt>D3dx9.lib</dt> </dl>  |



## See also

<dl> <dt>

[ID3DXFile](id3dxfile.md)
</dt> <dt>

[**ID3DXFileSaveObject**](id3dxfilesaveobject.md)
</dt> </dl>

 

 
