---
Description: This topic describes the DOT4\_DRIVER\_CMD structure.
ms.assetid: 7F099F7E-6E1F-499A-AF09-80B20429B892
title: DOT4\_DRIVER\_CMD structure
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DOT4\_DRIVER\_CMD structure

This topic describes the **DOT4\_DRIVER\_CMD** structure.

## Syntax


```C++
typedef struct _DOT4_DRIVER_CMD {
  CHANNEL_HANDLE hChannelHandle;
  ULONG          ulSize;
  ULONG          ulOffset;
  ULONG          ulTimeout;
} DOT4_DRIVER_CMD, *PDOT4_DRIVER_CMD;
```



## Members

<dl> <dt>

**hChannelHandle**
</dt> <dd>

Specifies the handle to the channel.

</dd> <dt>

**ulSize**
</dt> <dd>

Specifies the length of the request.

</dd> <dt>

**ulOffset**
</dt> <dd>

Specifies the offset into the buffer.

</dd> <dt>

**ulTimeout**
</dt> <dd>

Specifies the timeout of the operation. Can be INFINITE.

</dd> </dl>

## Requirements



|                   |                                                                                      |
|-------------------|--------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>D4drvif.h</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20DOT4_DRIVER_CMD%20structure%20%20RELEASE:%20%285/12/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/en-us/default.aspx. "Send comments about this topic to Microsoft")




