---
description: The GetCaptureTimeStamp function returns the time and date when the capture started recording frames.
ms.assetid: a7120a7c-5031-4c71-a177-f08c41037b3c
title: GetCaptureTimeStamp function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetCaptureTimeStamp
api_type: 
- DllExport
api_location: 
- Nmapi.dll
---

# GetCaptureTimeStamp function

The **GetCaptureTimeStamp** function returns the time and date when the capture started recording frames.

## Syntax


```C++
LPSYSTEMTIME WINAPI GetCaptureTimeStamp(
  _In_ HCAPTURE hCapture
);
```



## Parameters

<dl> <dt>

*hCapture* \[in\]
</dt> <dd>

Handle to the capture. For information about obtaining the capture handle, see the Remarks section of this **GetCaptureTimeStamp** topic.

</dd> </dl>

## Return value

If the function is successful, the return value is a pointer to a [SYSTEMTIME](/windows/desktop/api/minwinbase/ns-minwinbase-systemtime) structure.

If the function is unsuccessful, the return value is **NULL**.

## Remarks

The **GetCaptureTimeStamp** function returns the time when the Network Packet Provider (NPP) starts collecting data, not when the expert loads the capture for analysis.

Do not overwrite the data in the **SYSTEMTIME** structure. The data is part of the capture. Trying to modify the data causes an access violation.

[*Experts*](e.md) and [*parsers*](p.md) can call the **GetCaptureTimeStamp** function.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>  |
| Library<br/>                  | <dl> <dt>Nmapi.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Nmapi.dll</dt> </dl> |



## See also

<dl> <dt>

[SYSTEMTIME](/windows/desktop/api/minwinbase/ns-minwinbase-systemtime)
</dt> </dl>

 

