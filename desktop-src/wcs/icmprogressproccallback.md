---
title: ICMProgressProcCallback callback function
description: The ICMProgressProcCallback function is an application-supplied callback function that reports progress and permits the application to cancel color processing.
ms.assetid: 4e0bfa4c-f0eb-4776-98d6-90d9adf71bee
keywords:
- ICMProgressProcCallback callback function Windows Color System
topic_type:
- apiref
api_name:
- ICMProgressProcCallback
api_location:
- Icm.h
api_type:
- UserDefined


ms.topic: article
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# ICMProgressProcCallback callback function

The **ICMProgressProcCallback** function is an application-supplied callback function that reports progress and permits the application to cancel color processing.

## Syntax


```C++
BOOL WINAPI ICMProgressProcCallback(
   ULONG  ulMax,
   ULONG  ulCurrent,
   LPARAM ulCallbackData
);
```



## Parameters

<dl> <dt>

*ulMax* 
</dt> <dd>

Specifies the maximum value of the progress counter (used to estimate completion of the bitmap processing).

</dd> <dt>

*ulCurrent* 
</dt> <dd>

Specifies the current value of the progress counter (when divided by the maximum value, provides a rough estimate of percentage of completion).

</dd> <dt>

*ulCallbackData* 
</dt> <dd>

Specifies the data which is passed by the application to an ICM2 function, which then passes it on to the callback function. Such data can be used, for example, to identify the bitmap and process about which progress is being reported.

</dd> </dl>

## Return value

This function returns **TRUE** to continue bitmap processing. The return value is **FALSE** to cancel processing. If processing is canceled, the calling function returns zero to indicate failure, although its output buffer may be partially filled.

## Remarks

The name of this callback function is supplied by the application. A number of WCS functions, including [**TranslateBitmapBits**](/windows/win32/api/icm/nf-icm-translatebitmapbits) and [**CheckBitmapBits**](/windows/win32/api/icm/nf-icm-checkbitmapbits), call this function periodically.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Icm.h</dt> </dl> |



## See also

<dl> <dt>

[Basic color management concepts](basic-color-management-concepts.md)
</dt> <dt>

[Functions](functions.md)
</dt> <dt>

[**TranslateBitmapBits**](/windows/win32/api/icm/nf-icm-translatebitmapbits)
</dt> <dt>

[**CheckBitmapBits**](/windows/win32/api/icm/nf-icm-checkbitmapbits)
</dt> </dl>
