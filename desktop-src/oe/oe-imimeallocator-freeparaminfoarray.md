---
title: IMimeAllocator FreeParamInfoArray method
description: Frees any array of MIMEPARAMINFO structures.
ms.assetid: 'b40de735-a15f-44aa-ac33-917fe6b37b58'
keywords: ["FreeParamInfoArray method Windows Mail (formerly Outlook Express)", "FreeParamInfoArray method Windows Mail (formerly Outlook Express) , IMimeAllocator interface", "IMimeAllocator interface Windows Mail (formerly Outlook Express) , FreeParamInfoArray method"]
topic_type:
- apiref
api_name:
- IMimeAllocator.FreeParamInfoArray
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IMimeAllocator::FreeParamInfoArray method

Frees any array of [**MIMEPARAMINFO**](oe-mimeparaminfo.md) structures.

## Syntax


```C++
HRESULT FreeParamInfoArray(
  [in] ULONG           cParams,
  [in] LPMIMEPARAMINFO prgParam,
  [in] boolean         fFreeArray
);
```



## Parameters

<dl> <dt>

*cParams* \[in\]
</dt> <dd>

Type: **ULONG**

Specifies a **ULONG** that contains the number of elements in the *prgParam* array.

</dd> <dt>

*prgParam* \[in\]
</dt> <dd>

Type: **LPMIMEPARAMINFO**

Specifies a pointer to an array of [**MIMEPARAMINFO**](oe-mimeparaminfo.md) structures.

</dd> <dt>

*fFreeArray* \[in\]
</dt> <dd>

Type: **boolean**

Specifies whether the pointer to *prgParam* should also be freed.



| Value                                                                                                                                | Meaning                                  |
|--------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------|
| <span id="FALSE"></span><span id="false"></span><dl> <dt>**FALSE**</dt> </dl> | Keep the *prgParam* pointer. <br/> |
| <span id="TRUE"></span><span id="true"></span><dl> <dt>**TRUE**</dt> </dl>    | Free the *prgParam* pointer. <br/> |



 

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
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





