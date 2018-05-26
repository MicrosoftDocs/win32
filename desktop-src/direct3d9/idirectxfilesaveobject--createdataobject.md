---
Description: Creates a data object. Deprecated.
ms.assetid: bb0ef2cf-db76-40f6-968f-3599c58459a7
title: IDirectXFileSaveObjectCreateDataObject method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IDirectXFileSaveObject::CreateDataObject method

Creates a data object. Deprecated.

## Syntax


```C++
HRESULT CreateDataObject(
  [in]                REFGUID           rguidTemplate,
  [in]                LPCSTR            szName,
  [in]          const GUID              *pguid,
  [in]                DWORD             cbSize,
  [in]                LPVOID            pvData,
  [out, retval]       LPDIRECTXFILEDATA *ppDataObj
);
```



## Parameters

<dl> <dt>

*rguidTemplate* \[in\]
</dt> <dd>

Type: **[REFGUID](http://go.microsoft.com/?linkid=9742306)**

GUID representing the data object's template.

</dd> <dt>

*szName* \[in\]
</dt> <dd>

Type: **[**LPCSTR**](winprog.windows_data_types)**

Pointer to the name of the data object. Specify **NULL** if the object does not have a name.

</dd> <dt>

*pguid* \[in\]
</dt> <dd>

Type: **const [**GUID**](guid.md)\***

Pointer to a GUID representing the data object. Specify **NULL** if the object does not have a GUID.

</dd> <dt>

*cbSize* \[in\]
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

Size of the data object, in bytes.

</dd> <dt>

*pvData* \[in\]
</dt> <dd>

Type: **[**LPVOID**](winprog.windows_data_types)**

Pointer to a buffer containing all required member's data.

</dd> <dt>

*ppDataObj* \[out, retval\]
</dt> <dd>

Type: **[**LPDIRECTXFILEDATA**](idirectxfiledata.md)\***

Address of a pointer to an [**IDirectXFileData**](idirectxfiledata.md) interface, representing the created file data object.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is DXFILE\_OK. If the method fails, the return value can be one of the following values.DXFILEERR\_BADALLOC DXFILEERR\_BADVALUE

## Remarks

If a data reference object will reference the data object, either the szName or pguid parameter must be non-**NULL**.

Save any templates by using the [**IDirectXFileSaveObject::SaveTemplates**](idirectxfilesaveobject--savetemplates.md) method before saving the data created by this method. Save the created data by using the [**IDirectXFileSaveObject::SaveData**](idirectxfilesaveobject--savedata.md) method.

If you need to save optional data, use the [**IDirectXFileData::AddDataObject**](idirectxfiledata--adddataobject.md) method after using this method and before using [**IDirectXFileSaveObject::SaveData**](idirectxfilesaveobject--savedata.md). If the object has child objects, add them before calling **IDirectXFileSaveObject::SaveData**.

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>DXFile.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3dxof.lib</dt> </dl> |



## See also

<dl> <dt>

[IDirectXFileSaveObject](idirectxfilesaveobject.md)
</dt> <dt>

[**IDirectXFileData::AddDataObject**](idirectxfiledata--adddataobject.md)
</dt> <dt>

[**IDirectXFileSaveObject::SaveData**](idirectxfilesaveobject--savedata.md)
</dt> <dt>

[**IDirectXFileSaveObject::SaveTemplates**](idirectxfilesaveobject--savetemplates.md)
</dt> </dl>

 

 




