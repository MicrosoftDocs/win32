---
title: IixssoUtil TruncateToWhitespace method
description: Truncates a string at a white-space character. Script writers can call this method to display short forms of the value of long properties like the contents of the Description property without truncating in the middle of a word.
ms.assetid: '9f070c3d-1d72-4842-b893-2c3c6c17b494'
keywords: ["TruncateToWhitespace method Indexing Service", "TruncateToWhitespace method Indexing Service , IixssoUtil interface", "IixssoUtil interface Indexing Service , TruncateToWhitespace method"]
topic_type:
- apiref
api_name:
- IixssoUtil.TruncateToWhitespace
api_location:
- Ixsso.dll
api_type:
- COM
---

# IixssoUtil::TruncateToWhitespace method

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Truncates a string at a white-space character. Script writers can call this method to display short forms of the value of long properties like the contents of the Description property without truncating in the middle of a word.

## Syntax


```C++
HRESULT TruncateToWhitespace(
  [in]          BSTR pwszString,
  [in]          LONG cchLen,
  [out, retval] BSTR *ppwszOutput
);
```



## Parameters

<dl> <dt>

*pwszString* \[in\]
</dt> <dd>

The string to be truncated.

</dd> <dt>

*cchLen* \[in\]
</dt> <dd>

The maximum length of the string.

</dd> <dt>

*ppwszOutput* \[out, retval\]
</dt> <dd>

The truncated string.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

The space checking of this method doesn't work well with NLS; however it works well in ANSI. There is no equivalent routine for Asian languages.

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

 

 





