---
title: CardEnumFiles function
description: Receives an array of the names of files available in a specified directory of a smart card.
ms.assetid: e3d868d7-b160-4c67-a57b-54c0fc1e0152
keywords:
- CardEnumFiles function Security
topic_type:
- apiref
api_name:
- CardEnumFiles
api_location:
- Cardmod.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CardEnumFiles function

This topic is not current. For the most current information about the Smart Card API, see [Smart Card Minidriver Specification](http://go.microsoft.com/fwlink/p/?linkid=178045).

The **CardEnumFiles** function, defined by a smart card module, receives an array of the names of files available in a specified directory of a [*smart card*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-smart-card-gly).

## Syntax


```C++
DWORD WINAPI CardEnumFiles(
  _In_  PCARD_DATA pCardData,
  _In_  LPSTR      pszDirectoryName,
  _Out_ LPSTR      *pmszFileNames,
  _Out_ LPDWORD    pdwcbFileName,
  _In_  DWORD      dwFlags
);
```



## Parameters

<dl> <dt>

*pCardData* \[in\]
</dt> <dd>

A pointer to a [**CARD\_DATA**](card-data.md) structure received from a call to the [**CardAcquireContext**](cardacquirecontext.md) function.

</dd> <dt>

*pszDirectoryName* \[in\]
</dt> <dd>

A pointer to a null-terminated string that contains the name of the directory that contains the files to enumerate.

</dd> <dt>

*pmszFileNames* \[out\]
</dt> <dd>

A pointer to a buffer that, on output, contains an array of null-terminated strings that specify the names of the files in the directory specified by the *pszDirectory* parameter.

This buffer is allocated by the smart card module and freed by the caller. When you have finished using the buffer, free it by calling the [**PFN\_CSP\_FREE**](pfn-csp-free.md) function.

</dd> <dt>

*pdwcbFileName* \[out\]
</dt> <dd>

A pointer to a **DWORD** value that, on output, specifies the size, in bytes, of the *pmszFileNames* buffer.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Reserved. This parameter must be set to zero.

</dd> </dl>

## Return value

If the function succeeds, the function returns zero.

If the function fails, it returns a nonzero error value or one of the following possible error values.



| Return code/value                                                                                                                                                                        | Description                                                          |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| <dl> <dt>**SCARD\_E\_INVALID\_PARAMETER**</dt> <dt>2148532228 (0x80100004)</dt> </dl> | The *dwFlags* parameter contains a value other than zero.<br/> |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Cardmod.h</dt> </dl> |



## See also

<dl> <dt>

[Microsoft Base Smart Card Cryptographic Service Provider](microsoft-base-smart-card-cryptographic-service-provider.md)
</dt> <dt>

[**CARD\_DATA**](card-data.md)
</dt> <dt>

[**CardAcquireContext**](cardacquirecontext.md)
</dt> <dt>

[**CardCreateDirectory**](cardcreatedirectory.md)
</dt> <dt>

[**CardCreateFile**](cardcreatefile.md)
</dt> </dl>

 

 





