---
title: IMimeMessageTree SaveBody method
description: Saves the specified body in the message tree to a stream.
ms.assetid: 28aab8b5-f54c-4726-b4f2-4cc058537735
keywords:
- SaveBody method Windows Mail (formerly Outlook Express)
- SaveBody method Windows Mail (formerly Outlook Express) , IMimeMessageTree interface
- IMimeMessageTree interface Windows Mail (formerly Outlook Express) , SaveBody method
topic_type:
- apiref
api_name:
- IMimeMessageTree.SaveBody
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

# IMimeMessageTree::SaveBody method

Saves the specified body in the message tree to a stream.

## Syntax


```C++
HRESULT SaveBody(
  [in] HBODY   hBody,
  [in] DWORD   dwFlags,
  [in] IStream *pStream
);
```



## Parameters

<dl> <dt>

*hBody* \[in\]
</dt> <dd>

Type: **HBODY**

Specifies a handle to a message body.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies a bitmask. High word of SAVEBODY\_\* is reserved.



| Value                                                                                                                                                                                                                                                 | Meaning                                                                                                                  |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| <span id="SAVEBODY_KEEPBOUNDARY"></span><span id="savebody_keepboundary"></span><dl> <dt>**SAVEBODY\_KEEPBOUNDARY**</dt> <dt>0x00000001</dt> </dl> | Indicates that if the body being saved is a multipart body, the boundary for the multipart should be reused. <br/> |



 

</dd> <dt>

*pStream* \[in\]
</dt> <dd>

Type: **[IStream](http://msdn.microsoft.com/library/stg/stg/istream.asp)\***

Specifies a pointer to the [IStream](http://msdn.microsoft.com/library/stg/stg/istream.asp) object to save the body in.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                             | Description                                                                                        |
|---------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                    | Indicates success.<br/>                                                                      |
| <dl> <dt>**E\_FAIL**</dt> </dl>                  | Indicates that an unknown error has occurred.<br/>                                           |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>            | Indicates that *pStream* is **NULL**. <br/>                                                  |
| <dl> <dt>**MIME\_E\_NO\_DATA**</dt> </dl>        | Indicates that *hBody* is equal to HBODY\_ROOT (0xffffffff) and there is no root body. <br/> |
| <dl> <dt>**MIME\_E\_INVALID\_HANDLE**</dt> </dl> | Indicates that *hBody* is an invalid handle. <br/>                                           |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>           | Indicates that an attempt to allocate memory failed.<br/>                                    |
| <dl> <dt>**STG\_E\_MEDIUMFULL**</dt> </dl>       | Indicates that not enough disk space or memory is available to save the message. <br/>       |



 

## Remarks

If the body specified by *hBody* is a multipart body, all of its children are also saved.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





