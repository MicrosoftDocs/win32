---
title: IPropertyContainer SetProp method
description: Sets the property value for a specified property ID.
ms.assetid: eeaa0805-c89b-41a1-8acf-bb52c55ff0a9
keywords:
- SetProp method Windows Mail (formerly Outlook Express)
- SetProp method Windows Mail (formerly Outlook Express) , IPropertyContainer interface
- IPropertyContainer interface Windows Mail (formerly Outlook Express) , SetProp method
topic_type:
- apiref
api_name:
- IPropertyContainer.SetProp
api_location:
- Msoeacct.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IPropertyContainer::SetProp method

\[**IPropertyContainer::SetProp** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Sets the property value for a specified property ID.

## Syntax


```C++
HRESULT SetProp(
  [in] DWORD dwPropTag,
  [in] BYTE  *pb,
  [in] ULONG cb
);
```



## Parameters

<dl> <dt>

*dwPropTag* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies a **DWORD** that contains the property ID.

</dd> <dt>

*pb* \[in\]
</dt> <dd>

Type: **BYTE\***

Specifies a reference pointer to a **BYTE** that contains the property value.

</dd> <dt>

*cb* \[in\]
</dt> <dd>

Type: **ULONG**

Specifies a **ULONG** that contains the size (in bytes) of *pb*.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                           | Description                                                                                                            |
|-------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                  | Indicates success.<br/>                                                                                          |
| <dl> <dt>**E\_BadPropType**</dt> </dl>         | Indicates that *dwPropTag* specifies an invalid property type.<br/>                                              |
| <dl> <dt>**E\_BufferSizeMismatch**</dt> </dl>  | Indicates that *cb* specifies the incorrect buffer size for fixed length data types such as a **DWORD**. <br/>   |
| <dl> <dt>**E\_InvalidBooleanValue**</dt> </dl> | Indicates that an invalid Boolean value was passed in. The value must be one or zero.<br/>                       |
| <dl> <dt>**E\_InvalidMinMaxValue**</dt> </dl>  | Indicates that the value of *pb* is out of bounds. <br/>                                                         |
| <dl> <dt>**E\_PropNotFound**</dt> </dl>        | Indicates that *dwPropTag* specifies an invalid property ID. <br/>                                               |
| <dl> <dt>**E\_InvalidPropTag**</dt> </dl>      | Indicates that *dwPropTag* specifies an invalid property ID or that it specifies an unsupported data type. <br/> |



 

## Remarks

The value of *pb* can be **NULL** and the value of *cb* can be zero only for string and binary data types.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnact.h</dt> </dl>                            |
| IDL<br/>                      | <dl> <dt>Imnact.idl</dt> </dl>                          |
| DLL<br/>                      | <dl> <dt>Msoeacct.dll (version 6.0 or later)</dt> </dl> |



 

 





