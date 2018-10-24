---
Description: Converts a Microsoft MS-DOS path to a canonicalized URL.
ms.assetid: 1186b970-9ae1-4020-b999-55157cff1741
title: MFCreateURLFromPath function
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MFCreateURLFromPath
api_type: 
- DllExport
api_location: 
- mfplat.dll
---

# MFCreateURLFromPath function

\[This API is not supported and may be altered or unavailable in the future. Instead, Applications should call [UrlCreateFromPath](http://msdn.microsoft.com/en-us/library/bb773773.aspx).\]

Converts a Microsoft MS-DOS path to a canonicalized URL.

## Syntax


```C++
HRESULT MFCreateURLFromPath(
  _In_opt_ LPCWSTR pwszFilePath,
  _Out_    LPWSTR  *ppwszFileURL
);
```



## Parameters

<dl> <dt>

*pwszFilePath* \[in, optional\]
</dt> <dd>

A null-terminated string that contains the path. The maximum length of the string is **INTERNET\_MAX\_URL\_LENGTH**.

</dd> <dt>

*ppwszFileURL* \[out\]
</dt> <dd>

Receives a null-terminated string that contains the URL. The caller must free the string by calling [**CoTaskMemFree**](https://msdn.microsoft.com/en-us/library/ms680722(v=VS.85).aspx).

</dd> </dl>

## Return value

The function returns an **HRESULT**. Possible values include, but are not limited to, those in the following table.



| Return code                                                                             | Description                                                                                                                                                               |
|-----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_FALSE**</dt> </dl> | The string given in the *pwszFilePath* parameter is already in URL format. In this case, *pszFilePath* is simply copied to *ppszFileURL* without modification.<br/> |
| <dl> <dt>**S\_OK**</dt> </dl>    | The function succeeded. <br/>                                                                                                                                       |



 

## Remarks

This function has no associated import library. To call this function, you must use the [**LoadLibrary**](https://msdn.microsoft.com/en-us/library/ms684175(v=VS.85).aspx) and [**GetProcAddress**](https://msdn.microsoft.com/en-us/library/ms683212(v=VS.85).aspx) functions to dynamically link to Mfplat.dll.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| DLL<br/>                      | <dl> <dt>Mfplat.dll</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Functions](media-foundation-functions.md)
</dt> </dl>

 

 




