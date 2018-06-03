---
title: IMimeMessageCallback OnWebPageSplitter method
description: Allows the client to specify the HTML used to separate inlined bodies.
ms.assetid: 5a7ac109-2206-42e5-a606-f76cb8979614
keywords:
- OnWebPageSplitter method Windows Mail (formerly Outlook Express)
- OnWebPageSplitter method Windows Mail (formerly Outlook Express) , IMimeMessageCallback interface
- IMimeMessageCallback interface Windows Mail (formerly Outlook Express) , OnWebPageSplitter method
topic_type:
- apiref
api_name:
- IMimeMessageCallback.OnWebPageSplitter
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

# IMimeMessageCallback::OnWebPageSplitter method

\[**IMimeMessageCallback::OnWebPageSplitter** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Allows the client to specify the HTML used to separate inlined bodies. When MimeOLE is rendering a message, this method is called before every body is inlined into the message webpage. The separator HTML should allow the end user to distinguish between multiple bodies in the webpage. The default separator is a horizontal line.

## Syntax


```C++
HRESULT OnWebPageSplitter(
  [in] DWORD   cInlined,
  [in] IStream *ppStream
);
```



## Parameters

<dl> <dt>

*cInlined* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies the number of bodies that have been inlined.

</dd> <dt>

*ppStream* \[in\]
</dt> <dd>

Type: **[IStream](http://msdn.microsoft.com/library/stg/stg/istream.asp)\***

Specifies an IStream into which the client should write HTML.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                               | Description                                                                                                       |
|-------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>      | Valid HTML was written into *ppStream* and should be rendered.<br/>                                         |
| <dl> <dt>**E\_NOTIMPL**</dt> </dl> | Indicates that the client has not implemented this callback method. The default splitter will be used.<br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





