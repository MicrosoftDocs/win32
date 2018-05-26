---
title: IMimePropertySet SetOption method
description: Sets the value of an option.
ms.assetid: 2d3292c3-af56-421d-8f30-8041a0e1dbe3
keywords:
- SetOption method Windows Mail (formerly Outlook Express)
- SetOption method Windows Mail (formerly Outlook Express) , IMimePropertySet interface
- IMimePropertySet interface Windows Mail (formerly Outlook Express) , SetOption method
topic_type:
- apiref
api_name:
- IMimePropertySet.SetOption
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

# IMimePropertySet::SetOption method

Sets the value of an option.

## Syntax


```C++
HRESULT SetOption(
  [in] const TYPEDID        oid,
  [in]       LPCPROPVARIANT pValue
);
```



## Parameters

<dl> <dt>

*oid* \[in\]
</dt> <dd>

Type: **const TYPEDID**

Specifies the option ID.

</dd> <dt>

*pValue* \[in\]
</dt> <dd>

Type: **LPCPROPVARIANT**

Specifies a pointer to a [PROPVARIANT](https://msdn.microsoft.com/library/windows/desktop/aa380072) structure that contains the value to set for the option. The client must set the correct member in this structure according to the [VARTYPE](https://msdn.microsoft.com/library/windows/desktop/ms221127) of the option.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                                    | Description                                                                                             |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                           | Indicates success.<br/>                                                                           |
| <dl> <dt>**E\_FAIL**</dt> </dl>                         | Indicates that an unknown error has occurred.<br/>                                                |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                   | Indicates that *pValue* is **NULL**. <br/>                                                        |
| <dl> <dt>**MIME\_E\_INVALID\_OPTION\_VALUE**</dt> </dl> | Indicates that *pValue* is not valid for the option being set. <br/>                              |
| <dl> <dt>**MIME\_E\_INVALID\_OPTION\_ID**</dt> </dl>    | Indicates that *oid* is not a valid [**IMimePropertySet**](oe-imimepropertyset.md) option. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





