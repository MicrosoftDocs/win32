---
title: TapeClassAllocateSrbBuffer routine
description: The TapeClassAllocateSrbBuffer routine allocates an Srb- DataBuffer.
ms.assetid: f6762d9b-5a3d-49a3-b954-48e4e4a9eacb
keywords:
- TapeClassAllocateSrbBuffer routine Storage Devices
topic_type:
- apiref
api_name:
- TapeClassAllocateSrbBuffer
api_location:
- Tape.lib
- Tape.dll
api_type:
- LibDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# TapeClassAllocateSrbBuffer routine

The **TapeClassAllocateSrbBuffer** routine allocates an **Srb-&gt;DataBuffer**.

## Syntax


```C++
BOOLEAN TapeClassAllocateSrbBuffer(
  _Inout_ PSCSI_REQUEST_BLOCK Srb,
  _In_    ULONG               SrbBufferSize
);
```



## Parameters

<dl> <dt>

*Srb* \[in, out\]
</dt> <dd>

Pointer to the SRB.

</dd> <dt>

*SrbBufferSize* \[in\]
</dt> <dd>

Specifies the size, in bytes, of the **DataBuffer** to be allocated.

</dd> </dl>

## Return value

**TapeClassAllocateSrbBuffer** returns **TRUE** if the **DataBuffer** was allocated successfully, and **FALSE** if the buffer was not allocated.

## Remarks

**TapeClassAllocateSrbBuffer** allocates an **Srb-&gt;DataBuffer** from nonpaged memory and initializes the members to zero. If the buffer already exists from an earlier call, it is freed and a new buffer allocated. A tape miniclass driver calls this routine to allocate a **DataBuffer** in a portable way.

## Requirements



|                            |                                                                                                            |
|----------------------------|------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                         |
| Header<br/>          | <dl> <dt>Minitape.h (include Minitape.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Tape.lib</dt> </dl>                        |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20TapeClassAllocateSrbBuffer%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





