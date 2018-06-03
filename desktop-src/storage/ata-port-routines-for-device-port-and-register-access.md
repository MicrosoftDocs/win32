---
title: ATA Port Routines for Device Port and Register Access
description: ATA Port Routines for Device Port and Register Access
ms.assetid: 76a12feb-618d-4be6-b248-4a1d653ee699
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ATA Port Routines for Device Port and Register Access

## 

This section covers the ATA port library routines that the miniport driver can use for device port and register access.

> [!Note]  
> The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

This section includes the following routines:

<dl>

[**AtaPortReadPortUchar**](ataportreadportuchar.md)  
[**AtaPortReadPortUshort**](ataportreadportushort.md)  
[**AtaPortReadPortUlong**](ataportreadportulong.md)  
[**AtaPortReadPortBufferUchar**](ataportreadportbufferuchar.md)  
[**AtaPortReadPortBufferUshort**](ataportreadportbufferushort.md)  
[**AtaPortReadPortBufferUlong**](ataportreadportbufferulong.md)  
[**AtaPortReadRegisterUchar**](ataportreadregisteruchar.md)  
[**AtaPortReadRegisterUshort**](ataportreadregisterushort.md)  
[**AtaPortReadRegisterUlong**](ataportreadregisterulong.md)  
[**AtaPortReadRegisterBufferUchar**](ataportreadregisterbufferuchar.md)  
[**AtaPortReadRegisterBufferUshort**](ataportreadregisterbufferushort.md)  
[**AtaPortReadRegisterBufferUlong**](ataportreadregisterbufferulong.md)  
[**AtaPortWritePortUchar**](ataportwriteportuchar.md)  
[**AtaPortWritePortUshort**](ataportwriteportushort.md)  
[**AtaPortWritePortUlong**](ataportwriteportulong.md)  
[**AtaPortWritePortBufferUchar**](ataportwriteportbufferuchar.md)  
[**AtaPortWritePortBufferUshort**](ataportwriteportbufferushort.md)  
[**AtaPortWritePortBufferUlong**](ataportwriteportbufferulong.md)  
[**AtaPortWriteRegisterUchar**](ataportwriteregisteruchar.md)  
[**AtaPortWriteRegisterUshort**](ataportwriteregisterushort.md)  
[**AtaPortWriteRegisterUlong**](ataportwriteregisterulong.md)  
[**AtaPortWriteRegisterBufferUchar**](ataportwriteregisterbufferuchar.md)  
[**AtaPortWriteRegisterBufferUshort**](ataportwriteregisterbufferushort.md)  
[**AtaPortWriteRegisterBufferUlong**](ataportwriteregisterbufferulong.md)  
</dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ATA%20Port%20Routines%20for%20Device%20Port%20and%20Register%20Access%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




