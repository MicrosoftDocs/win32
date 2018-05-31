---
title: IixssoUtil HTMLEncode method
description: Encodes a string using HTML encoding using the specified code page.
ms.assetid: 6bf4ed00-f1f6-49b3-9e85-017ddd00d245
keywords:
- HTMLEncode method Indexing Service
- HTMLEncode method Indexing Service , IixssoUtil interface
- IixssoUtil interface Indexing Service , HTMLEncode method
topic_type:
- apiref
api_name:
- IixssoUtil.HTMLEncode
api_location:
- Ixsso.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IixssoUtil::HTMLEncode method

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Encodes a string using HTML encoding using the specified code page.

## Syntax


```C++
HRESULT HTMLEncode(
  [in]          BSTR pwszString,
  [in]          LONG codepage,
  [out, retval] BSTR *ppwszOutput
);
```



## Parameters

<dl> <dt>

*pwszString* \[in\]
</dt> <dd>

The string to be encoded.

</dd> <dt>

*codepage* \[in\]
</dt> <dd>

The code page to use for encoding this string.

</dd> <dt>

*ppwszOutput* \[out, retval\]
</dt> <dd>

The resulting HTML encoded string.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

The HTMLEncode method is used to work around difficulties with the proper handling of code pages in previous versions of Active Server Pages (ASP).

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| End of client support<br/>    | Windows 7<br/>                                                                 |
| End of server support<br/>    | Windows Server 2008 R2<br/>                                                    |
| DLL<br/>                      | <dl> <dt>Ixsso.dll</dt> </dl> |



## See also

<dl> <dt>

[**IixssoUtil**](iixssoutil.md)
</dt> </dl>

 

 





