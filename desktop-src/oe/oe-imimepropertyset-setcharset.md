---
title: IMimePropertySet SetCharset method
description: Sets the character set of the property set.
ms.assetid: 61d0bd71-b5f9-4d04-b327-3c0d5990cdd2
keywords:
- SetCharset method Windows Mail (formerly Outlook Express)
- SetCharset method Windows Mail (formerly Outlook Express) , IMimePropertySet interface
- IMimePropertySet interface Windows Mail (formerly Outlook Express) , SetCharset method
topic_type:
- apiref
api_name:
- IMimePropertySet.SetCharset
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

# IMimePropertySet::SetCharset method

Sets the character set of the property set.

## Syntax


```C++
HRESULT SetCharset(
  [in] HCHARSET      hCharset,
  [in] CSETAPPLYTYPE applytype
);
```



## Parameters

<dl> <dt>

*hCharset* \[in\]
</dt> <dd>

Type: **HCHARSET**

Specifies the handle of the character set.

</dd> <dt>

*applytype* \[in\]
</dt> <dd>

Type: **[**CSETAPPLYTYPE**](oe-csetapplytype.md)**

Specifies [**CSETAPPLYTYPE**](oe-csetapplytype.md) value that indicates how to apply *hCharset* to the property set.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                             | Description                                                 |
|---------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                    | Indicates success.<br/>                               |
| <dl> <dt>**E\_FAIL**</dt> </dl>                  | Indicates that an unknown error has occurred.<br/>    |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>            | Indicates that *hCharset* is **NULL**. <br/>          |
| <dl> <dt>**MIME\_E\_INVALID\_HANDLE**</dt> </dl> | Indicates that *hCharset* is an invalid handle. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





