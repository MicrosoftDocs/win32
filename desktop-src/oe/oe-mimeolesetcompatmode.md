---
title: MimeOleSetCompatMode function
description: Do not use. Sets the MIMEOLE compatibility mode.
ms.assetid: 0b60fd9e-b3ac-405a-bb5e-b7160aeb358b
keywords:
- MimeOleSetCompatMode function Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MimeOleSetCompatMode
api_location:
- Inetcomm.dll
api_type:
- DllExport
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MimeOleSetCompatMode function

Do not use. Sets the MIMEOLE compatibility mode.

## Syntax


```C++
HRESULT MimeOleSetCompatMode(
  _In_ DWORD dwMode
);
```



## Parameters

<dl> <dt>

*dwMode* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies the compatibility mode.



| Value                                                                                                                                                                                                                                                  | Meaning                                                    |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------|
| <span id="MIMEOLE_COMPAT_OE5"></span><span id="mimeole_compat_oe5"></span><dl> <dt>**MIMEOLE\_COMPAT\_OE5**</dt> <dt>0x00000001</dt> </dl>          | Backward compatibility to Outlook Express 5.0. <br/> |
| <span id="MIMEOLE_COMPAT_MLANG2"></span><span id="mimeole_compat_mlang2"></span><dl> <dt>**MIMEOLE\_COMPAT\_MLANG2**</dt> <dt>0x00000002</dt> </dl> | Base multiple language support. <br/>                |



 

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                          | Description                       |
|--------------------------------------------------------------------------------------|-----------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl> | Always returns S\_OK. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





