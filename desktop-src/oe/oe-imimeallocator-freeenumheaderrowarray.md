---
title: IMimeAllocator FreeEnumHeaderRowArray method
description: Frees any array of ENUMHEADERROW structures.
ms.assetid: 28cb5e53-c19f-48e1-9493-057ec9e3bd62
keywords:
- FreeEnumHeaderRowArray method Windows Mail (formerly Outlook Express)
- FreeEnumHeaderRowArray method Windows Mail (formerly Outlook Express) , IMimeAllocator interface
- IMimeAllocator interface Windows Mail (formerly Outlook Express) , FreeEnumHeaderRowArray method
topic_type:
- apiref
api_name:
- IMimeAllocator.FreeEnumHeaderRowArray
api_location:
- Inetcomm.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IMimeAllocator::FreeEnumHeaderRowArray method

Frees any array of [**ENUMHEADERROW**](oe-enumheaderrow.md) structures.

## Syntax


```C++
HRESULT FreeEnumHeaderRowArray(
  [in] ULONG           cRows,
  [in] LPENUMHEADERROW prgRow,
  [in] boolean         fFreeArray
);
```



## Parameters

<dl> <dt>

*cRows* \[in\]
</dt> <dd>

Type: **ULONG**

Specifies a **ULONG** that contains the number of elements in the *prgRow* array.

</dd> <dt>

*prgRow* \[in\]
</dt> <dd>

Type: **LPENUMHEADERROW**

Specifies a pointer to an array of [**ENUMHEADERROW**](oe-enumheaderrow.md) structures.

</dd> <dt>

*fFreeArray* \[in\]
</dt> <dd>

Type: **boolean**

Specifies whether the pointer to *prgRow* should also be freed.



| Value                                                                                                                                | Meaning                                |
|--------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| <span id="FALSE"></span><span id="false"></span><dl> <dt>**FALSE**</dt> </dl> | Keep the *prgRow* pointer. <br/> |
| <span id="TRUE"></span><span id="true"></span><dl> <dt>**TRUE**</dt> </dl>    | Free the *prgRow* pointer. <br/> |



 

</dd> </dl>

## Return value

Type: **HRESULT**

Returns the following value.



| Return code                                                                          | Description                   |
|--------------------------------------------------------------------------------------|-------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | Indicates success.<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





