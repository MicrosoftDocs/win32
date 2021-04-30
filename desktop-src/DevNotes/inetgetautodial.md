---
description: The InetGetAutodial function returns the autodial settings from the registry.
ms.assetid: e36761da-c050-4844-ad94-efdc77702f6f
title: InetGetAutodial function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- InetGetAutodial
api_type: 
- DllExport
api_location: 
- Inetcfg.dll
---

# InetGetAutodial function

\[This function is unsupported and may be altered or unavailable in future versions of Windows. \]

The **InetGetAutodial** function returns the autodial settings from the registry.

## Syntax


```C++
HRESULT InetGetAutodial(
  _Out_ LPBOOL lpfEnable,
  _Out_ LPSTR  lpszEntryName,
  _In_  DWORD  cbEntryNameSize
);
```



## Parameters

<dl> <dt>

*lpfEnable* \[out\]
</dt> <dd>

Indicates whether autodial is enabled. A value of **TRUE** upon return indicates autodial is enabled.

</dd> <dt>

*lpszEntryName* \[out\]
</dt> <dd>

On return, contains the name of the phone book entry that is set for autodial.

</dd> <dt>

*cbEntryNameSize* \[in\]
</dt> <dd>

Size of the buffer allocated by the caller for the phone book entry name.

</dd> </dl>

## Return value

This function can return one of these values.



| Return code                                                                                                | Description                                                                                                                                               |
|------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**ERROR\_SUCCESS**</dt> </dl>              | The call was successful.<br/>                                                                                                                       |
| <dl> <dt>**ERROR\_BAD\_ARGUMENTS**</dt> </dl>       | *lpfEnable* or *lpszEntryName* contains a **NULL** pointer, or the value of *cbEntryNameSize* is zero.<br/>                                         |
| <dl> <dt>**ERROR\_NOT\_ENOUGH\_MEMORY**</dt> </dl>  | There was insufficient memory to allocate internal buffers.<br/>                                                                                    |
| <dl> <dt>**ERROR\_INSUFFICIENT\_BUFFER**</dt> </dl> | *cbEntryNameSize* does not indicate that the buffer pointed to by *lpszEntryName* is large enough to receive the name of the phone book entry.<br/> |



 

## Remarks

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions.

## Requirements



| Requirement | Value |
|----------------|----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Inetcfg.dll</dt> </dl> |



 

 
