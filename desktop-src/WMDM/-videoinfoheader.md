---
title: '_VIDEOINFOHEADER structure'
description: The \_VIDEOINFOHEADER structure contains information about a video stream and includes a \_BITMAPINFOHEADER structure that defines the format of an individual frame.
ms.assetid: 5a39d66e-8dbc-4572-8370-14f722b6c906
keywords:
- _VIDEOINFOHEADER structure windows Media Device Manager
topic_type:
- apiref
api_name:
- _VIDEOINFOHEADER
api_location:
- wmdm.idl
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# \_VIDEOINFOHEADER structure

The **\_VIDEOINFOHEADER** structure contains information about a video stream and includes a **\_BITMAPINFOHEADER** structure that defines the format of an individual frame.

## Syntax


```C++
typedef struct _tagVIDEOINFOHEADER {
  RECT             rcSource;
  RECT             rcTarget;
  DWORD            dwBitRate;
  DWORD            dwBitErrorRate;
  REFERENCE_TIME   AvgTimePerFrame;
  BITMAPINFOHEADER bmiHeader;
} _VIDEOINFOHEADER;
```



## Members

<dl> <dt>

**rcSource**
</dt> <dd>

**RECT** structure that specifies the source video window.

</dd> <dt>

**rcTarget**
</dt> <dd>

**RECT** structure that specifies the destination video window.

</dd> <dt>

**dwBitRate**
</dt> <dd>

**DWORD** value that specifies the video stream's approximate data rate, in bits per second.

</dd> <dt>

**dwBitErrorRate**
</dt> <dd>

**DWORD** value that specifies the video stream's data error rate, in bit errors per second.

</dd> <dt>

**AvgTimePerFrame**
</dt> <dd>

**REFERENCE\_TIME** value that specifies the video frame's average display time, in 100-nanosecond units.

</dd> <dt>

**bmiHeader**
</dt> <dd>

Win32 **\_BITMAPINFOHEADER** structure that contains color and dimension information for the video image bitmap.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------|-------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Wmdm.idl</dt> </dl> |



## See also

<dl> <dt>

[**\_BITMAPINFOHEADER**](-bitmapinfoheader.md)
</dt> <dt>

[**Structures**](structures.md)
</dt> </dl>

 

 





