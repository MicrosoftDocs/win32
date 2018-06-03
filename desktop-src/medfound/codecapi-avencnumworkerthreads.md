---
Description: Sets the number of worker threads used by a video encoder.
ms.assetid: E490DF0C-97DE-4375-A4DB-17DA4E782E2D
title: CODECAPI\_AVEncNumWorkerThreads property
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CODECAPI\_AVEncNumWorkerThreads property

Sets the number of worker threads used by a video encoder.

## Data type

**ULONG** (VT\_UI4)

## Property GUID

**CODECAPI\_AVEncNumWorkerThreads**

## Remarks

If the value is zero, the encoder selects the number of threads.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps \| UWP apps\]<br/>                           |
| Header<br/>                   | <dl> <dt>Codecapi.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> <dt>

[**ICodecAPI**](https://msdn.microsoft.com/library/windows/desktop/dd311953)
</dt> </dl>

 

 




