---
description: Saves templates to a DirectX file. Deprecated.
ms.assetid: 7a45565a-8c04-4fa1-a424-294b847d3a2f
title: IDirectXFileSaveObject::SaveTemplates method (DXFile.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IDirectXFileSaveObject.SaveTemplates
api_type: 
- COM
api_location: 
- D3dxof.lib
- D3dxof.dll
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

Type: **[**DWORD**](../winprog/windows-data-types.md)**

Total number of templates to save.

</dd> <dt>

*ppguidTemplates* \[in\]
</dt> <dd>

Type: **const [**GUID**](guid.md)\*\***

Address of a pointer to an array of the GUIDs for all templates to save.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is DXFILE\_OK. If the method fails, the return value can be DXFILEERR\_BADVALUE.

## Remarks

The following code fragment provides an example call to **IDirectXFileSaveObject::SaveTemplates** and example contents for the array to which ppguidTemplates points.


```
IDirectXFileSaveObject * pDXFileSaveObject;
    
const GUID *aIds[] = {
    &DXFILEOBJ_SimpleData,
    &DXFILEOBJ_ArrayData,
    &DXFILEOBJ_RestrictedData};
    
hr = pDXFileSaveObject->SaveTemplates(3, aIds);
```



After using this method to save the templates, use the [**IDirectXFileSaveObject::CreateDataObject**](idirectxfilesaveobject--createdataobject.md) method to create a data object.

## Requirements



| Requirement | Value |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>DXFile.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3dxof.lib</dt> </dl> |



## See also

<dl> <dt>

[IDirectXFileSaveObject](idirectxfilesaveobject.md)
</dt> <dt>

[**IDirectXFileSaveObject::CreateDataObject**](idirectxfilesaveobject--createdataobject.md)
</dt> </dl>

 

 
