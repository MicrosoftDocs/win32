---
title: ICM_COMPRESS_BEGIN message (Vfw.h)
description: The ICM\_COMPRESS\_BEGIN message notifies a video compression driver to prepare to compress data. You can send this message explicitly or by using the ICCompressBegin macro.
ms.assetid: dd1d3a66-c625-4f55-b65a-8545c1c16301
keywords:
- ICM_COMPRESS_BEGIN message Windows Multimedia
topic_type:
- apiref
api_name:
- ICM_COMPRESS_BEGIN
api_location:
- Vfw.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# ICM\_COMPRESS\_BEGIN message

The **ICM\_COMPRESS\_BEGIN** message notifies a video compression driver to prepare to compress data. You can send this message explicitly or by using the [**ICCompressBegin**](/windows/desktop/api/Vfw/nf-vfw-iccompressbegin) macro.


```C++
ICM_COMPRESS_BEGIN 
wParam = (DWORD_PTR) (LPVOID) lpbiInput; 
lParam = (DWORD_PTR) (LPVOID) lpbiOutput; 
```



## Parameters

<dl> <dt>

<span id="lpbiInput"></span><span id="lpbiinput"></span><span id="LPBIINPUT"></span>*lpbiInput*
</dt> <dd>

Pointer to a [**BITMAPINFO**](/windows/win32/api/wingdi/ns-wingdi-bitmapinfo) structure containing the input format.

</dd> <dt>

<span id="lpbiOutput"></span><span id="lpbioutput"></span><span id="LPBIOUTPUT"></span>*lpbiOutput*
</dt> <dd>

Pointer to a [**BITMAPINFO**](/windows/win32/api/wingdi/ns-wingdi-bitmapinfo) structure containing the output format.

</dd> </dl>

## Return Value

Returns ICERR\_OK if the driver supports the specified compression or ICERR\_BADFORMAT if the input or output format is not supported.

## Remarks

The driver should allocate and initialize any tables or memory that it needs for compressing the data formats when it receives the [**ICM\_COMPRESS**](icm-compress.md) message.

VCM saves the settings of the most recent **ICM\_COMPRESS\_BEGIN** message. The **ICM\_COMPRESS\_BEGIN** and [**ICM\_COMPRESS\_END**](icm-compress-end.md) messages do not nest. If your driver receives **ICM\_COMPRESS\_BEGIN** before compression is stopped with **ICM\_COMPRESS\_END**, it should restart compression with new parameters.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                       |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                             |
| Header<br/>                   | <dl> <dt>Vfw.h</dt> </dl> |



## See also

<dl> <dt>

[Video Compression Manager](video-compression-manager.md)
</dt> <dt>

[Video Compression Messages](video-compression-messages.md)
</dt> </dl>

 

