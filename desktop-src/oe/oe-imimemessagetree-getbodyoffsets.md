---
title: IMimeMessageTree GetBodyOffsets method
description: Gets the offsets for the specified body.
ms.assetid: 5746186f-e407-4f25-a9f5-fb66beede4ef
keywords:
- GetBodyOffsets method Windows Mail (formerly Outlook Express)
- GetBodyOffsets method Windows Mail (formerly Outlook Express) , IMimeMessageTree interface
- IMimeMessageTree interface Windows Mail (formerly Outlook Express) , GetBodyOffsets method
topic_type:
- apiref
api_name:
- IMimeMessageTree.GetBodyOffsets
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

# IMimeMessageTree::GetBodyOffsets method

Gets the offsets for the specified body.

## Syntax


```C++
HRESULT GetBodyOffsets(
  [in]      HBODY         hBody,
  [in, out] LPBODYOFFSETS pOffsets
);
```



## Parameters

<dl> <dt>

*hBody* \[in\]
</dt> <dd>

Type: **HBODY**

Specifies the handle of the body. Use HBODY\_ROOT (0xffffffff) to indicate the root body.

</dd> <dt>

*pOffsets* \[in, out\]
</dt> <dd>

Type: **LPBODYOFFSETS**

Receives a pointer to the [**BODYOFFSETS**](oe-bodyoffsets.md) structure for the specified body.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                             | Description                                                                                        |
|---------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                    | Indicates success.<br/>                                                                      |
| <dl> <dt>**E\_FAIL**</dt> </dl>                  | Indicates that an unknown error has occurred.<br/>                                           |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>            | Indicates that *hBody* or *pOffsets* is **NULL**. <br/>                                      |
| <dl> <dt>**MIME\_E\_NO\_DATA**</dt> </dl>        | Indicates that *hBody* is equal to HBODY\_ROOT (0xffffffff) and there is no root body. <br/> |
| <dl> <dt>**MIME\_E\_INVALID\_HANDLE**</dt> </dl> | Indicates that *hBody* is an invalid handle. <br/>                                           |



 

## Remarks

This method is equivalent to:

pMessageTree-&gt;[**BindToObject**](oe-imimemessagetree-bindtoobject.md)(*hBody*, IID\_IMimeBody, (LPVOID \*)&pBody);

pBody-&gt;[**GetOffsets**](oe-imimebody-getoffsets.md)(*pOffsets*);

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





