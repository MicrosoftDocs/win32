---
title: IPropertyContainer GetProp method
description: Retrieves the data and size for a specified property ID.
ms.assetid: '57a7df20-d100-4091-a43e-5d5902d154b1'
keywords: ["GetProp method Windows Mail (formerly Outlook Express)", "GetProp method Windows Mail (formerly Outlook Express) , IPropertyContainer interface", "IPropertyContainer interface Windows Mail (formerly Outlook Express) , GetProp method"]
topic_type:
- apiref
api_name:
- IPropertyContainer.GetProp
api_location:
- Msoeacct.dll
api_type:
- COM
---

# IPropertyContainer::GetProp method

\[**IPropertyContainer::GetProp** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Retrieves the data and size for a specified property ID.

## Syntax


```C++
HRESULT GetProp(
  [in]  DWORD dwPropTag,
  [out] BYTE  *pb,
  [out] ULONG *pcb
);
```



## Parameters

<dl> <dt>

*dwPropTag* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies a **DWORD** that contains the property ID.

</dd> <dt>

*pb* \[out\]
</dt> <dd>

Type: **BYTE\***

Specifies a reference pointer to a **BYTE** that contains the property value.

</dd> <dt>

*pcb* \[out\]
</dt> <dd>

Type: **ULONG\***

Specifies a reference pointer to a **ULONG** that contains the size (in bytes) of *pb*. If *pb* is **NULL**, then this parameter contains the number of bytes required to store *pb*.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                          | Description                                                                                                                                     |
|------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                 | Indicates success. <br/>                                                                                                                  |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>        | Indicates that an attempt to allocate memory failed. <br/>                                                                                |
| <dl> <dt>**E\_NoPropData**</dt> </dl>         | Indicates that the specified property contains invalid data or that the property has not been set and does not have a default value.<br/> |
| <dl> <dt>**E\_BufferTooSmall**</dt> </dl>     | Indicates that *pcb* does not specify a buffer large enough to store the property value. <br/>                                            |
| <dl> <dt>**E\_PropNotFound**</dt> </dl>       | Indicates that *dwPropTag* specifies an invalid property ID.<br/>                                                                         |
| <dl> <dt>**E\_InvalidPropTag**</dt> </dl>     | Indicates that *dwPropTag* specifies an invalid property ID or that it specifies an unsupported data type.<br/>                           |
| <dl> <dt>**E\_InvalidPropertySet**</dt> </dl> | Indicates that the internal property set is invalid. <br/>                                                                                |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnact.h</dt> </dl>                            |
| IDL<br/>                      | <dl> <dt>Imnact.idl</dt> </dl>                          |
| DLL<br/>                      | <dl> <dt>Msoeacct.dll (version 6.0 or later)</dt> </dl> |



 

 





