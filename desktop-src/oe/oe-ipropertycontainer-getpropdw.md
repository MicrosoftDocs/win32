---
title: IPropertyContainer GetPropDw method
description: Retrieves the data and size for a specified property ID.
ms.assetid: '7fc1d14c-9e93-433d-b785-c7ba1181228c'
keywords: ["GetPropDw method Windows Mail (formerly Outlook Express)", "GetPropDw method Windows Mail (formerly Outlook Express) , IPropertyContainer interface", "IPropertyContainer interface Windows Mail (formerly Outlook Express) , GetPropDw method"]
topic_type:
- apiref
api_name:
- IPropertyContainer.GetPropDw
api_location:
- Msoeacct.dll
api_type:
- COM
---

# IPropertyContainer::GetPropDw method

\[**IPropertyContainer::GetPropDw** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Retrieves the data and size for a specified property ID.

## Syntax


```C++
HRESULT GetPropDw(
  [in]  DWORD dwPropTag,
  [out] DWORD *pdw
);
```



## Parameters

<dl> <dt>

*dwPropTag* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies a **DWORD** that contains the property ID.

</dd> <dt>

*pdw* \[out\]
</dt> <dd>

Type: **DWORD\***

Receives a reference pointer to a **DWORD** that contains the property value.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                          | Description                                                                                                                                     |
|------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                 | Indicates success. <br/>                                                                                                                  |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>        | Indicates that an attempt to allocate memory failed. <br/>                                                                                |
| <dl> <dt>**E\_NoPropData**</dt> </dl>         | Indicates that the specified property contains invalid data or that the property has not been set and does not have a default value.<br/> |
| <dl> <dt>**E\_PropNotFound**</dt> </dl>       | Indicates that *dwPropTag* specifies an invalid property ID.<br/>                                                                         |
| <dl> <dt>**E\_InvalidPropTag**</dt> </dl>     | Indicates that *dwPropTag* specifies an invalid property ID or that it specifies an unsupported data type.<br/>                           |
| <dl> <dt>**E\_InvalidPropertySet**</dt> </dl> | Indicates that the internal property set is invalid. <br/>                                                                                |



 

## Remarks

The **IPropertyContainer::GetPropDw** and [**IPropertyContainer::GetPropSz**](oe-ipropertycontainer-getpropsz.md) methods are simple helper functions that internally call the base [**IPropertyContainer::GetProp**](oe-ipropertycontainer-getprop.md) method to make property retrieval easier when dealing with the most common data types (4 byte numbers and null-terminated strings).

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnact.h</dt> </dl>                            |
| IDL<br/>                      | <dl> <dt>Imnact.idl</dt> </dl>                          |
| DLL<br/>                      | <dl> <dt>Msoeacct.dll (version 6.0 or later)</dt> </dl> |



 

 





