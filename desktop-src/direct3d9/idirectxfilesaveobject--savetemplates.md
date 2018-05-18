---
Description: 'Saves templates to a DirectX file. Deprecated.'
ms.assetid: '7a45565a-8c04-4fa1-a424-294b847d3a2f'
title: 'IDirectXFileSaveObject::SaveTemplates method'
---

# IDirectXFileSaveObject::SaveTemplates method

Saves templates to a DirectX file. Deprecated.

## Syntax


```C++
HRESULT SaveTemplates(
  [in]       DWORD cTemplates,
  [in] const GUID  **ppguidTemplates
);
```



## Parameters

<dl> <dt>

*cTemplates* \[in\]
</dt> <dd>

Type: **[**DWORD**](winprog.windows_data_types)**

Total number of templates to save.

</dd> <dt>

*ppguidTemplates* \[in\]
</dt> <dd>

Type: **const [**GUID**](guid.md)\*\***

Address of a pointer to an array of the GUIDs for all templates to save.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If the method succeeds, the return value is DXFILE\_OK. If the method fails, the return value can be DXFILEERR\_BADVALUE.

## Remarks

The following code fragment provides an example call to **IDirectXFileSaveObject::SaveTemplates** and example contents for the array to which ppguidTemplates points.


```
IDirectXFileSaveObject * pDXFileSaveObject;
    
const GUID *aIds[] = {
    &amp;DXFILEOBJ_SimpleData,
    &amp;DXFILEOBJ_ArrayData,
    &amp;DXFILEOBJ_RestrictedData};
    
hr = pDXFileSaveObject->SaveTemplates(3, aIds);
```



After using this method to save the templates, use the [**IDirectXFileSaveObject::CreateDataObject**](idirectxfilesaveobject--createdataobject.md) method to create a data object.

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>DXFile.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3dxof.lib</dt> </dl> |



## See also

<dl> <dt>

[IDirectXFileSaveObject](idirectxfilesaveobject.md)
</dt> <dt>

[**IDirectXFileSaveObject::CreateDataObject**](idirectxfilesaveobject--createdataobject.md)
</dt> </dl>

 

 




