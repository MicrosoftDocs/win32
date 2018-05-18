---
title: IPropertyContainer SetPropSz method
description: Sets the property value for a specified property ID.
ms.assetid: '559226d3-051a-4ef0-9dbb-c5a85633456d'
keywords: ["SetPropSz method Windows Mail (formerly Outlook Express)", "SetPropSz method Windows Mail (formerly Outlook Express) , IPropertyContainer interface", "IPropertyContainer interface Windows Mail (formerly Outlook Express) , SetPropSz method"]
topic_type:
- apiref
api_name:
- IPropertyContainer.SetPropSz
api_location:
- Msoeacct.dll
api_type:
- COM
---

# IPropertyContainer::SetPropSz method

\[**IPropertyContainer::SetPropSz** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Sets the property value for a specified property ID.

## Syntax


```C++
HRESULT SetPropSz(
  [in] DWORD dwPropTag,
  [in] LPSTR psz
);
```



## Parameters

<dl> <dt>

*dwPropTag* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies a **DWORD** that contains the property ID.

</dd> <dt>

*psz* \[in\]
</dt> <dd>

Type: **LPSTR**

Specifies a reference pointer to a string that contains the property value.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                           | Description                                                                                                            |
|-------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                  | Indicates success.<br/>                                                                                          |
| <dl> <dt>**E\_BadPropType**</dt> </dl>         | Indicates that *dwPropTag* specifies an invalid property type.<br/>                                              |
| <dl> <dt>**E\_InvalidBooleanValue**</dt> </dl> | Indicates that an invalid boolean value was passed in. The value must be one or zero.<br/>                       |
| <dl> <dt>**E\_InvalidMinMaxValue**</dt> </dl>  | Indicates that the value of *psz* is out of bounds. <br/>                                                        |
| <dl> <dt>**E\_PropNotFound**</dt> </dl>        | Indicates that *dwPropTag* specifies an invalid property ID. <br/>                                               |
| <dl> <dt>**E\_InvalidPropTag**</dt> </dl>      | Indicates that *dwPropTag* specifies an invalid property ID or that it specifies an unsupported data type. <br/> |



 

## Remarks

The value of *psz* can be **NULL** only for string and binary data types.

The [**IPropertyContainer::SetPropDw**](oe-ipropertycontainer-setpropdw.md) and **IPropertyContainer::SetPropSz** methods are simple helper functions that internally call the base [**IPropertyContainer::SetProp**](oe-ipropertycontainer-setprop.md) method to make setting properties easier when dealing with the most common data types (4 byte numbers and **null**-terminated strings).

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnact.h</dt> </dl>                            |
| IDL<br/>                      | <dl> <dt>Imnact.idl</dt> </dl>                          |
| DLL<br/>                      | <dl> <dt>Msoeacct.dll (version 6.0 or later)</dt> </dl> |



 

 





