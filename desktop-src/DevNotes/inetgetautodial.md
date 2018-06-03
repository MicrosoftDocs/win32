---
Description: The InetGetAutodial function returns the autodial settings from the registry.
ms.assetid: e36761da-c050-4844-ad94-efdc77702f6f
title: InetGetAutodial function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
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

This function has no associated import library or header file; you must call it using the [**LoadLibrary**](https://msdn.microsoft.com/windows/desktop/d936b4dd-058c-48e1-834b-b47ef6d8ef65) and [**GetProcAddress**](https://msdn.microsoft.com/windows/desktop/a0d7fc09-f888-4f46-a571-d3719a627597) functions.

## Requirements



|                |                                                                                        |
|----------------|----------------------------------------------------------------------------------------|
| DLL<br/> | <dl> <dt>Inetcfg.dll</dt> </dl> |



 

 




