---
Description: Creates a data object. Deprecated.
ms.assetid: bb0ef2cf-db76-40f6-968f-3599c58459a7
title: IDirectXFileSaveObject::CreateDataObject method
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IDirectXFileSaveObject.CreateDataObject
api_type: 
- COM
api_location: 
- D3dxof.lib
- D3dxof.dll
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

Type: **[REFGUID](https://go.microsoft.com/?linkid=9742306)**

GUID representing the data object's template.

</dd> <dt>

*szName* \[in\]
</dt> <dd>

Type: **[**LPCSTR**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

Pointer to the name of the data object. Specify **NULL** if the object does not have a name.

</dd> <dt>

*pguid* \[in\]
</dt> <dd>

Type: **const [**GUID**](guid.md)\***

Pointer to a GUID representing the data object. Specify **NULL** if the object does not have a GUID.

</dd> <dt>

*cbSize* \[in\]
</dt> <dd>

Type: **[**DWORD**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

Size of the data object, in bytes.

</dd> <dt>

*pvData* \[in\]
</dt> <dd>

Type: **[**LPVOID**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)**

Pointer to a buffer containing all required member's data.

</dd> <dt>

*ppDataObj* \[out, retval\]
</dt> <dd>

Type: **[**LPDIRECTXFILEDATA**](idirectxfiledata.md)\***

Address of a pointer to an [**IDirectXFileData**](idirectxfiledata.md) interface, representing the created file data object.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/en-us/library/Bb401631(v=MSDN.10).aspx)**

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

 

 




