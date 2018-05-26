---
title: MimeOleGetFileInfoW function
description: Do not use. Returns file information for a supplied Unicode file path string.
ms.assetid: a0c8d10f-6042-45f3-8e80-e509e1983135
keywords:
- MimeOleGetFileInfoW function Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- MimeOleGetFileInfoW
api_location:
- Inetcomm.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MimeOleGetFileInfoW function

Do not use. Returns file information for a supplied Unicode file path string.

## Syntax


```C++
HRESULT MimeOleGetFileInfoW(
  _In_  LPWSTR pszFilePath,
  _Out_ LPWSTR *ppszCntType,
  _Out_ LPWSTR *ppszSubType,
  _Out_ LPWSTR *ppszCntDesc,
  _Out_ LPWSTR *ppszFileName,
  _Out_ LPWSTR *ppszExtension
);
```



## Parameters

<dl> <dt>

*pszFilePath* \[in\]
</dt> <dd>

Type: **LPWSTR**

Specifies an **LPWSTR** that contains the file path.

</dd> <dt>

*ppszCntType* \[out\]
</dt> <dd>

Type: **LPWSTR\***

Receives a pointer to an **LPWSTR** that contains the primary [Content-Type](http://msdn.microsoft.com/library/cdosys/html/48f7ae1c-9dc8-4b2f-8dc1-11c55e62173f.asp).

</dd> <dt>

*ppszSubType* \[out\]
</dt> <dd>

Type: **LPWSTR\***

Receives a pointer to an **LPWSTR** that contains the secondary [Content-Type](http://msdn.microsoft.com/library/cdosys/html/48f7ae1c-9dc8-4b2f-8dc1-11c55e62173f.asp).

</dd> <dt>

*ppszCntDesc* \[out\]
</dt> <dd>

Type: **LPWSTR\***

Receives a pointer to an **LPWSTR** that may contain the following descriptions: SHGFI\_USEFILEATTRIBUTES, SHGFI\_DISPLAYNAME, SHGFI\_TYPENAME. See shellapi.h.

</dd> <dt>

*ppszFileName* \[out\]
</dt> <dd>

Type: **LPWSTR\***

Receives a pointer to an **LPWSTR** that contains the file name.

</dd> <dt>

*ppszExtension* \[out\]
</dt> <dd>

Type: **LPWSTR\***

Receives a pointer to an **LPWSTR** that contains the file name extension.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                 |
|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success. <br/>                              |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that a pointer parameter is **NULL**. <br/> |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an allocation failed. <br/>            |



 

## Remarks

Enter **NULL** for any parameter you do not wish to obtain info for. However, any parameter that is not **NULL** must be a valid pointer.

> [!Note]  
> Both *ppszCntType* and *ppszSubType* must be present and valid to receive info for either one.

 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| Library<br/>                  | <dl> <dt>Inetcomm.lib</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





