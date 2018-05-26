---
Description: Creates a save object. Deprecated.
ms.assetid: 50a7dbde-1dd4-4aae-a9ab-97d6f99618c0
title: IDirectXFileCreateSaveObject method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IDirectXFile::CreateSaveObject method

Creates a save object. Deprecated.

## Syntax


```C++
HRESULT CreateSaveObject(
  [in]          LPCSTR                  szFileName,
  [in]          DXFILEFORMAT            dwFileFormat,
  [out, retval] LPDIRECTXFILESAVEOBJECT *ppSaveObj
);
```



## Parameters

<dl> <dt>

*szFileName* \[in\]
</dt> <dd>

Type: **[**LPCSTR**](winprog.windows_data_types)**

Pointer to the name of the file to use for saving data.

</dd> <dt>

*dwFileFormat* \[in\]
</dt> <dd>

Type: **[**DXFILEFORMAT**](dxfile.md)**

Indicates the format to use when saving the DirectX file. This value can be one of the DXFILEFORMAT\_xxx flags in [DXFILE Constants](dxfile.md). For more information, see Remarks.

</dd> <dt>

*ppSaveObj* \[out, retval\]
</dt> <dd>

Type: **[**LPDIRECTXFILESAVEOBJECT**](idirectxfilesaveobject.md)\***

Address of a pointer to an [**IDirectXFileSaveObject**](idirectxfilesaveobject.md) interface, representing the created save object.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is DXFILE\_OK. If the method fails, the return value can be one of the following: DXFILEERR\_BADALLOC, DXFILEERR\_BADFILE, DXFILEERR\_BADVALUE.

## Remarks

After using this method, use methods of the [**IDirectXFileSaveObject**](idirectxfilesaveobject.md) interface to create data objects and to save templates or data.

The default value for the file format is DXFILEFORMAT\_BINARY. The file format values can be combined in a logical OR to create compressed text or compressed binary files. If a file is specified as both binary (0) and text (1), it will be saved as a text file because the value will be indistinguishable from the text file format value (0 + 1 = 1). If you indicate that the file format should be text and compressed, the file will first be written out as text and then compressed. However, compressed text files are not as efficient as binary text files, so in most cases you will want to indicate binary and compressed. Setting a file to be compressed without specifying a format will result in a binary, compressed file.

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>DXFile.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3dxof.lib</dt> </dl> |



## See also

<dl> <dt>

[IDirectXFile](idirectxfile.md)
</dt> <dt>

[**IDirectXFileSaveObject**](idirectxfilesaveobject.md)
</dt> </dl>

 

 




