---
title: IImnAccount ValidateProperty method
description: Validates the specified value of a property.
ms.assetid: 7f4097d3-3e98-40c4-9b2f-58ce772a84e7
keywords:
- ValidateProperty method Windows Mail (formerly Outlook Express)
- ValidateProperty method Windows Mail (formerly Outlook Express) , IImnAccount interface
- IImnAccount interface Windows Mail (formerly Outlook Express) , ValidateProperty method
topic_type:
- apiref
api_name:
- IImnAccount.ValidateProperty
api_location:
- Msoeacct.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IImnAccount::ValidateProperty method

\[**IImnAccount::ValidateProperty** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Validates the specified value of a property.

## Syntax


```C++
HRESULT ValidateProperty(
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

Specifies the name of the property.

</dd> <dt>

*pb* \[in\]
</dt> <dd>

Type: **BYTE\***

Specifies a pointer to a **BYTE** that contains the property value to validate.

</dd> <dt>

*cb* \[in\]
</dt> <dd>

Type: **ULONG**

Specifies a **ULONG** that indicates the size of *pb*.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                    | Description                                                              |
|------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>           | Indicates success. <br/>                                           |
| <dl> <dt>**S\_FALSE**</dt> </dl>        | Indicates that the property is not supported for validation. <br/> |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>   | Indicates that *pb* is **NULL**. <br/>                             |
| <dl> <dt>**E\_InvalidValue**</dt> </dl> | Indicates that the property value is invalid. <br/>                |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnact.h</dt> </dl>                            |
| IDL<br/>                      | <dl> <dt>Imnact.idl</dt> </dl>                          |
| DLL<br/>                      | <dl> <dt>Msoeacct.dll (version 6.0 or later)</dt> </dl> |



 

 





