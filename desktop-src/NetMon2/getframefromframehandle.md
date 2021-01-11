---
description: The GetFrameFromFrameHandle function returns a pointer to a frame from a frame handle.
ms.assetid: 790fe5fe-a857-4947-a471-d0538c0f0d61
title: GetFrameFromFrameHandle function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetFrameFromFrameHandle
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# GetFrameFromFrameHandle function

The **GetFrameFromFrameHandle** function returns a pointer to a frame from a frame handle.

## Syntax


```C++
ULPFRAME WINAPI GetFrameFromFrameHandle(
  _In_ HFRAME hFrame
);
```



## Parameters

<dl> <dt>

*hFrame* \[in\]
</dt> <dd>

Handle to the frame.

</dd> </dl>

## Return value

If the function is successful, the return value is a pointer to the frame.

If the function is unsuccessful, the return value is 0.

## Remarks

The **GetFrameFromFrameHandle** function retrieves data that cannot be retrieved by the other helper functions that Network Monitor provides. Use the following functions whenever possible.

<dl>

[**GetFrameDstAddressOffset**](getframedstaddressoffset.md)  
[**GetFrameSrcAddressOffset**](getframesrcaddressoffset.md)  
[**GetFrameCaptureHandle**](getframecapturehandle.md)  
[**GetFrameDestAddress**](getframedestaddress.md)  
[**GetFrameSourceAddress**](getframesourceaddress.md)  
[**GetFrameMacHeaderLength**](getframemacheaderlength.md)  
[**GetFrameLength**](getframelength.md)  
[**GetFrameStoredLength**](getframestoredlength.md)  
[**GetFrameMacType**](getframemactype.md)  
[**GetFrameNumber**](getframenumber.md)  
[**GetFrameTimeStamp**](getframetimestamp.md)  
</dl>

[*Experts*](e.md) and [*parsers*](p.md) can call the **GetFrameFromFrameHandle** function.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>  |
| Library<br/>                  | <dl> <dt>Nmapi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nmapi.dll</dt> </dl> |



 

 




