---
title: Port and Register I/O Routines
description: Port and Register I/O Routines
ms.assetid: 9A0991E3-CC7A-4129-AB8E-76732D917D2F
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Port and Register I/O Routines

## 

This section lists the port and register I/O routines supplied by the Storport driver.

## In this section



| Topic                                                                                       | Description                                                                                                                                                                                                                          |
|---------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**StorPortGetDeviceBase**](storportgetdevicebase.md)<br/>                           | The **StorPortGetDeviceBase** routine maps an I/O address to system address space. <br/>                                                                                                                                       |
| [**StorPortFreeDeviceBase**](storportfreedevicebase.md)<br/>                         | **StorPortFreeDeviceBase** frees a range of device I/O memory that was mapped by [**StorPortGetDeviceBase**](storportgetdevicebase.md).<br/>                                                                                  |
| [**StorPortReadPortBufferUchar**](storportreadportbufferuchar.md)<br/>               | The **StorPortReadPortBufferUchar** routine reads a value from a specified port address <br/>                                                                                                                                  |
| [**StorPortReadPortBufferUlong**](storportreadportbufferulong.md)<br/>               | The **StorPortReadPortBufferUlong** routine reads a value from a specified port address. <br/>                                                                                                                                 |
| [**StorPortReadPortBufferUshort**](storportreadportbufferushort.md)<br/>             | The **StorPortReadPortBufferUshort** routine reads a value from a specified port address. <br/>                                                                                                                                |
| [**StorPortReadPortUchar**](storportreadportuchar.md)<br/>                           | The **StorPortReadPortUchar** routine reads a value from a specified port address <br/>                                                                                                                                        |
| [**StorPortReadPortUlong**](storportreadportulong.md)<br/>                           | The **StorPortReadPortUlong** routine reads a value from a specified port address. <br/>                                                                                                                                       |
| [**StorPortReadPortUshort**](storportreadportushort.md)<br/>                         | The **StorPortReadPortUshort** routine reads a value from a specified port address. <br/>                                                                                                                                      |
| [**StorPortReadRegisterBufferUchar**](storportreadregisterbufferuchar.md)<br/>       | The **StorPortReadRegisterBufferUchar** routine reads a value from a specified register address. <br/>                                                                                                                         |
| [**StorPortReadRegisterBufferUlong**](storportreadregisterbufferulong.md)<br/>       | The **StorPortReadRegisterBufferUlong** routine reads a value from a specified register address. <br/>                                                                                                                         |
| [**StorPortReadRegisterBufferUlong64**](storportreadregisterbufferulong64.md)<br/>   | This **StorPortReadRegisterBufferUlong64** routine reads a number of **ULONG64** values from the specified 64-bit register address into a buffer. <br/>                                                                        |
| [**StorPortReadRegisterBufferUshort**](storportreadregisterbufferushort.md)<br/>     | The **StorPortReadRegisterBufferUshort** routine reads a value from a specified register address. <br/>                                                                                                                        |
| [**StorPortReadRegisterUchar**](storportreadregisteruchar.md)<br/>                   | The **StorPortReadRegisterUchar** routine reads a value from a specified register address. <br/>                                                                                                                               |
| [**StorPortReadRegisterUlong**](storportreadregisterulong.md)<br/>                   | The **StorPortReadRegisterUlong** routine reads a value from a specified register address. <br/>                                                                                                                               |
| [**StorPortReadRegisterUlong64**](storportreadregisterulong64.md)<br/>               | The **StorPortReadRegisterUlong64** routine reads a 64-bit value from a specified 64-bit register address.<br/>                                                                                                                |
| [**StorPortReadRegisterUshort**](storportreadregisterushort.md)<br/>                 | The **StorPortReadRegisterUshort** routine reads a value from a specified register address. <br/>                                                                                                                              |
| [**StorPortValidateRange**](storportvalidaterange.md)<br/>                           | The **StorPortValidateRange** routine determines whether a specified range of I/O addresses is in use by another adapter. This routine is obsolete in Windows NT 4.0 and later operating systems. <br/>                        |
| [**StorPortUpdateAdapterMaxIO**](storportupdateadaptermaxio.md)<br/>                 | This function can be called by a miniport to update the maximum IO's supported by an adapter. This function is valid during HwInitialize/HwPassiveInitRoutine callback and has effect only during adapter initialization.<br/> |
| [**StorPortWritePortBufferUchar**](storportwriteportbufferuchar.md)<br/>             | The **StorPortWritePortBufferUchar** routine writes a value to a specified register address. <br/>                                                                                                                             |
| [**StorPortWritePortBufferUlong**](storportwriteportbufferulong.md)<br/>             | The **StorPortWritePortBufferUlong** routine writes a value to a specified register address. <br/>                                                                                                                             |
| [**StorPortWritePortBufferUshort**](storportwriteportbufferushort.md)<br/>           | The **StorPortWritePortBufferUshort** routine writes a value to a specified register address. <br/>                                                                                                                            |
| [**StorPortWritePortUchar**](storportwriteportuchar.md)<br/>                         | The **StorPortWritePortUchar** routine writes a value to a specified register address. <br/>                                                                                                                                   |
| [**StorPortWritePortUlong**](storportwriteportulong.md)<br/>                         | The **StorPortWritePortUlong** routine writes a value to a specified register address. <br/>                                                                                                                                   |
| [**StorPortWritePortUshort**](storportwriteportushort.md)<br/>                       | The **StorPortWritePortUshort** routine writes a value to a specified register address. <br/>                                                                                                                                  |
| [**StorPortWriteRegisterBufferUchar**](storportwriteregisterbufferuchar.md)<br/>     | The **StorPortWriteRegisterBufferUchar** routine transfers a given number of unsigned bytes from a buffer to the HBA. <br/>                                                                                                    |
| [**StorPortWriteRegisterBufferUlong**](storportwriteregisterbufferulong.md)<br/>     | The **StorPortWriteRegisterBufferUlong** routine transfers a given number of ULONG values from a buffer to the HBA.<br/>                                                                                                       |
| [**StorPortWriteRegisterBufferUlong64**](storportwriteregisterbufferulong64.md)<br/> | This **StorPortWriteRegisterBufferUlong64** routine writes a number of **ULONG64** values from a the specified 64-bit register address. <br/>                                                                                  |
| [**StorPortWriteRegisterBufferUshort**](storportwriteregisterbufferushort.md)<br/>   | The **StorPortWriteRegisterBufferUshort** routine transfers a given number of USHORT values from a buffer to the HBA.<br/>                                                                                                     |
| [**StorPortWriteRegisterUchar**](storportwriteregisteruchar.md)<br/>                 | The **StorPortWriteRegisterBufferUshort** routine transfers a given number of character values from a buffer to the indicated HBA register address.<br/>                                                                       |
| [**StorPortWriteRegisterUlong**](storportwriteregisterulong.md)<br/>                 | The **StorPortWriteRegisterUlong** routine transfers a ULONG value to the indicated HBA register address.<br/>                                                                                                                 |
| [**StorPortWriteRegisterUlong64**](storportwriteregisterulong64.md)<br/>             | This **StorPortWriteRegisterUlong64** routine writes a **ULONG64** value to the specified register address.<br/>                                                                                                               |
| [**StorPortWriteRegisterUshort**](storportwriteregisterushort.md)<br/>               | The **StorPortWriteRegisterUshort** routine transfers a ULONG value to the indicated HBA register address.<br/>                                                                                                                |



 

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20Port%20and%20Register%20I/O%20Routines%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





