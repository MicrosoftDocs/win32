---
title: IMimeAllocator FreeEnumPropertyArray method
description: Frees any array of ENUMPROPERTY structures.
ms.assetid: 04f951fb-4256-4af0-834b-4f6d5318845b
keywords:
- FreeEnumPropertyArray method Windows Mail (formerly Outlook Express)
- FreeEnumPropertyArray method Windows Mail (formerly Outlook Express) , IMimeAllocator interface
- IMimeAllocator interface Windows Mail (formerly Outlook Express) , FreeEnumPropertyArray method
topic_type:
- apiref
api_name:
- IMimeAllocator.FreeEnumPropertyArray
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

# IMimeAllocator::FreeEnumPropertyArray method

Frees any array of [**ENUMPROPERTY**](oe-enumproperty.md) structures.

## Syntax


```C++
HRESULT FreeEnumPropertyArray(
  [in] ULONG          cProps,
  [in] LPENUMPROPERTY prgProp,
  [in] boolean        fFreeArray
);
```



## Parameters

<dl> <dt>

*cProps* \[in\]
</dt> <dd>

Type: **ULONG**

Specifies a **ULONG** that contains the number of elements in the *prgProp* array.

</dd> <dt>

*prgProp* \[in\]
</dt> <dd>

Type: **LPENUMPROPERTY**

Specifies a pointer to an array of [**ENUMPROPERTY**](oe-enumproperty.md) structures.

</dd> <dt>

*fFreeArray* \[in\]
</dt> <dd>

Type: **boolean**

Specifies whether the pointer to *prgProp* should also be freed.



| Value                                                                                                                                | Meaning                                 |
|--------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| <span id="FALSE"></span><span id="false"></span><dl> <dt>**FALSE**</dt> </dl> | Keep the *prgProp* pointer. <br/> |
| <span id="TRUE"></span><span id="true"></span><dl> <dt>**TRUE**</dt> </dl>    | Free the *prgProp* pointer. <br/> |



 

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



 

 





