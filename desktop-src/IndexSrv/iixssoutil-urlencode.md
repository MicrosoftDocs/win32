---
Description: Encodes a string using URL encoding using the specified code page.
ms.assetid: 28da29a8-376a-4a67-a4de-dde8992b4852
title: IixssoUtil::URLEncode method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IixssoUtil::URLEncode method

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Encodes a string using URL encoding using the specified code page.

## Syntax


```C++
HRESULT URLEncode(
  [in]          BSTR pwszString,
  [in]          LONG codepage,
  [out, retval] BSTR *ppwszOutput
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

The resulting URL encoded string.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

The URLEncode method is used to work around difficulties with the proper handling of code pages in previous versions of Active Server Pages (ASP).

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| End of client support<br/>    | Windows 7<br/>                                                                 |
| End of server support<br/>    | Windows Server 2008 R2<br/>                                                    |
| DLL<br/>                      | <dl> <dt>Ixsso.dll</dt> </dl> |



## See also

<dl> <dt>

[**IixssoUtil**](iixssoutil.md)
</dt> </dl>

 

 




