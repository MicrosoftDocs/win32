---
Description: The ModifyFrame function alters an existing frame with new data.
ms.assetid: ebd248e4-b248-4f4a-8b94-a6d1c331d12a
title: ModifyFrame function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ModifyFrame function

The **ModifyFrame** function alters an existing frame with new data.

## Syntax


```C++
HFRAME WINAPI ModifyFrame(
  _In_  HCAPTURE hCapture,
  _In_  DWORD    FrameNumber,
  _In_  LPBYTE   FrameData,
  _In_  DWORD    FrameLength,
  _Out_ __int64  TimeStamp
);
```



## Parameters

<dl> <dt>

*hCapture* \[in\]
</dt> <dd>

Handle to the capture. For information about obtaining the capture handle, see the Remarks section of this **ModifyFrame** topic.

</dd> <dt>

*FrameNumber* \[in\]
</dt> <dd>

Frame index number.

</dd> <dt>

*FrameData* \[in\]
</dt> <dd>

Pointer to an array of bytes that contain the new frame data.

</dd> <dt>

*FrameLength* \[in\]
</dt> <dd>

Length of the new data, in bytes.

</dd> <dt>

*TimeStamp* \[out\]
</dt> <dd>

Time stamp indicating when the frame was modified.

</dd> </dl>

## Return value

If the function is successful, the return value is a handle to a new frame.

If the function is unsuccessful, the return value is **NULL**.

## Remarks

If the call is successful, the **ModifyFrame** function destroys the original frame.

[*Experts*](https://www.bing.com/search?q=*Experts*) and [*parsers*](https://www.bing.com/search?q=*parsers*) can call the **ModifyFrame** function.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>  |
| Library<br/>                  | <dl> <dt>Nmapi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nmapi.dll</dt> </dl> |



 

 




