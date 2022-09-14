---
description: The GetCaptureMacType function returns the MAC type of a given capture.
ms.assetid: de0dfb36-df3a-4f6e-b266-09c81dfdc88b
title: GetCaptureMacType function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetCaptureMacType
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# GetCaptureMacType function

The **GetCaptureMacType** function returns the MAC type of a given capture.

## Syntax


```C++
DWORD WINAPI GetCaptureMacType(
  _In_ HCAPTURE hCapture
);
```



## Parameters

<dl> <dt>

*hCapture* \[in\]
</dt> <dd>

Handle to the capture. For information about obtaining the capture handle, see the Remarks section in this **GetCaptureMacType** topic.

</dd> </dl>

## Return value

If the function is successful, the return value is one of the following MAC types.

-   MAC\_TYPE\_UNKNOWN
-   MAC\_TYPE\_ETHERNET
-   MAC\_TYPE\_TOKENRING
-   MAC\_TYPE\_FDDI

If the function is unsuccessful, the return value is an error code.



| Return code                                                                                              | Description                                                 |
|----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| <dl> <dt>**NMERR\_MAC\_TYPE\_UNKNOWN**</dt> </dl> | Network Monitor could not find a known MAC type.<br/> |



 

## Remarks

The handle of the capture can be obtained in several ways, depending on who makes the call. For experts, the handle is specified in the **hCapture** member of the [EXPERTSTARTUPINFO](expertstartupinfo.md) structure. For parsers, the capture handle can be obtained by calling the [GetFrameCaptureHandle](getframecapturehandle.md) function.

[*Experts*](e.md) and [*parsers*](p.md) can call the **GetCaptureMacType** function.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>  |
| Library<br/>                  | <dl> <dt>Nmapi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nmapi.dll</dt> </dl> |



 

 




