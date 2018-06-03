---
title: IMimePropertySet DeleteExcept method
description: Deletes all the properties in the property set, except for a specified set.
ms.assetid: 81665c60-f83d-45f9-9f11-c2b659976b08
keywords:
- DeleteExcept method Windows Mail (formerly Outlook Express)
- DeleteExcept method Windows Mail (formerly Outlook Express) , IMimePropertySet interface
- IMimePropertySet interface Windows Mail (formerly Outlook Express) , DeleteExcept method
topic_type:
- apiref
api_name:
- IMimePropertySet.DeleteExcept
api_location:
- Inetcomm.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IMimePropertySet::DeleteExcept method

Deletes all the properties in the property set, except for a specified set.

## Syntax


```C++
HRESULT DeleteExcept(
  [in] ULONG  cNames,
  [in] LPCSTR *prgszName
);
```



## Parameters

<dl> <dt>

*cNames* \[in\]
</dt> <dd>

Type: **ULONG**

Specifies a **ULONG** that contains the number of elements in the *prgszName* array. A client can pass 0 for this parameter and **NULL** for *prgszName* to delete all properties.

</dd> <dt>

*prgszName* \[in\]
</dt> <dd>

Type: **LPCSTR\***

Specifies a pointer to an array of property names or property IDs to keep.

> [!Note]  
> This is the exception list.

 

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                  | Description                                                                                                                                        |
|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>         | Indicates success. <br/>                                                                                                                     |
| <dl> <dt>**E\_FAIL**</dt> </dl>       | Indicates that an unknown error has occurred. <br/>                                                                                          |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | Indicates that *cNames* is equal to zero and *prgszName* is not **NULL** or *cNames* is greater than zero and *prgszName* is **NULL**. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





