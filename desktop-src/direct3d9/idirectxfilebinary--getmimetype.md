---
Description: Retrieves the Multipurpose Internet Mail Extensions (MIME) type for the binary data. Deprecated.
ms.assetid: 57c42ace-4313-40d8-9992-eaf12edf3a30
title: IDirectXFileBinary::GetMimeType method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IDirectXFileBinary::GetMimeType method

Retrieves the Multipurpose Internet Mail Extensions (MIME) type for the binary data. Deprecated.

## Syntax


```C++
HRESULT GetMimeType(
  [out] LPCSTR *pszMimeType
);
```



## Parameters

<dl> <dt>

*pszMimeType* \[out\]
</dt> <dd>

Type: **[**LPCSTR**](https://msdn.microsoft.com/en-us/library/Aa383751(v=VS.85).aspx)\***

Address of a pointer to receive the MIME type string.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/en-us/library/Bb401631(v=MSDN.10).aspx)**

If the method succeeds, the return value is DXFILE\_OK. If the method fails, the return value can be DXFILEERR\_BADVALUE.

## Remarks

When there is no MIME type specified in a DirectX file for a binary object, the function will set pszMimeType to **NULL**.

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>DXFile.h</dt> </dl>   |
| Library<br/> | <dl> <dt>D3dxof.lib</dt> </dl> |



## See also

<dl> <dt>

[IDirectXFileBinary](idirectxfilebinary.md)
</dt> </dl>

 

 




