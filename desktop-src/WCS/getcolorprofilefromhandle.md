---
title: GetColorProfileFromHandle function
description: Given a handle to an open color profile, the GetColorProfileFromHandle function will copy the contents of the profile into a buffer supplied by the application.
ms.assetid: 'ff51c6d5-4db2-4b64-a4e3-34a9e502f456'
keywords: ["GetColorProfileFromHandle function Windows Color System"]
topic_type:
- apiref
api_name:
- GetColorProfileFromHandle
api_location:
- mscms.dll
api_type:
- DllExport
---

# GetColorProfileFromHandle function

Given a handle to an open color profile, the **GetColorProfileFromHandle** function will copy the contents of the profile into a buffer supplied by the application. If the handle is a Windows Color System (WCS) handle, then the DMP is returned and the CAMP and GMMP associated with the HPROFILE are ignored.

## Syntax


```C++
BOOL WINAPI GetColorProfileFromHandle(
   HPROFILE hProfile,
   PBYTE    pBuffer,
   PDWORD   pcbSize
);
```



## Parameters

<dl> <dt>

*hProfile* 
</dt> <dd>

Handle to an open color profile. The function determines whether the HPROFILE contains ICC or WCS profile information.

</dd> <dt>

*pBuffer* 
</dt> <dd>

Pointer to buffer to receive raw ICC or DMP profile data. Can be **NULL**. If it is, the size required for the buffer will be stored in the memory location pointed to by *pcbSize*. The buffer can be allocated to the appropriate size, and this function called again with *pBuffer* containing the address of the buffer.

</dd> <dt>

*pcbSize* 
</dt> <dd>

Pointer to a **DWORD** that holds the size of buffer pointed at by *pBuffer*. On return it is filled with size of buffer that was actually used if the function succeeds. If this function is called with *pBuffer* set to **NULL**, this parameter will contain the size of the buffer required.

</dd> </dl>

## Return value

If this function succeeds, the return value is **TRUE**. It returns **FALSE** if the *pBuffer* parameter is **NULL** and the size required for the buffer is copied into *pcbSize.*

If this function fails, the return value is **FALSE**. For extended error information, call **GetLastError**.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Icm.h</dt> </dl>     |
| Library<br/>                  | <dl> <dt>Mscms.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Mscms.dll</dt> </dl> |



## See also

<dl> <dt>

[Basic Color Management Concepts](basic-color-management-concepts.md)
</dt> <dt>

[Functions](functions.md)
</dt> </dl>

 

 





