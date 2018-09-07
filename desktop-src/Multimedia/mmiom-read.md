---
title: MMIOM_READ message
description: The MMIOM\_READ message is sent to an I/O procedure by the mmioRead function to request that a specified number of bytes be read from an open file.
ms.assetid: db769a68-f0ac-4a79-931e-6174e438439d
keywords:
- MMIOM_READ message Windows Multimedia
topic_type:
- apiref
api_name:
- MMIOM_READ
api_location:
- Mmsystem.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MMIOM\_READ message

The **MMIOM\_READ** message is sent to an I/O procedure by the [**mmioRead**](https://msdn.microsoft.com/en-us/library/Dd757334(v=VS.85).aspx) function to request that a specified number of bytes be read from an open file.


```C++
MMIOM_READ 
lParam1 = (LPARAM) lBuffer 
lParam2 = (LPARAM) cbRead 
```



## Parameters

<dl> <dt>

<span id="lBuffer"></span><span id="lbuffer"></span><span id="LBUFFER"></span>*lBuffer*
</dt> <dd>

Pointer to the buffer to be filled with data read from the file.

</dd> <dt>

<span id="cbRead"></span><span id="cbread"></span><span id="CBREAD"></span>*cbRead*
</dt> <dd>

Number of bytes to read from file.

</dd> </dl>

## Return Value

Returns the number of bytes actually read from the file. If no more bytes can be read, the return value is 0. If there is an error, the return value is  1.

## Remarks

The I/O procedure is responsible for updating the **lDiskOffset** member of the [**MMIOINFO**](https://msdn.microsoft.com/en-us/library/Dd757322(v=VS.85).aspx) structure to reflect the new file position after the read operation.

## Requirements



|                                     |                                                                                                           |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Mmsystem.h (include Windows.h)</dt> </dl> |



 

 





