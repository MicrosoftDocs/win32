---
title: StorPortRegistryRead routine
description: The StorPortRegistryRead routine reads the registry data for the indicated device and value.
ms.assetid: '16f13973-c1c1-4123-8fa4-20187ec2c204'
keywords: ["StorPortRegistryRead routine Storage Devices"]
topic_type:
- apiref
api_name:
- StorPortRegistryRead
api_location:
- Storport.lib
- Storport.dll
api_type:
- LibDef
---

# StorPortRegistryRead routine

The **StorPortRegistryRead** routine reads the registry data for the indicated device and value.

## Syntax


```C++
BOOLEAN StorPortRegistryRead(
   IN PVOID  HwDeviceExtension,
   IN PUCHAR ValueName,
   IN ULONG  Global,
   IN ULONG  Type,
   IN PUCHAR Buffer,
   IN PULONG BufferLength
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* 
</dt> <dd>

A pointer to the hardware device extension. This is a per HBA storage area that the port driver allocates and initializes on behalf of the miniport driver. Miniport drivers usually store HBA-specific information in this extension, such as the state of the HBA and the mapped access ranges for the HBA. This area is available to the miniport driver immediately after the miniport driver calls [**StorPortInitialize**](storportinitialize.md). The port driver frees this memory when it removes the device. The miniport driver must be running at IRQL PASSIVE\_LEVEL when it calls this routine.

</dd> <dt>

*ValueName* 
</dt> <dd>

Pointer to a UCHAR that specifies the registry value name whose content is to be read.

</dd> <dt>

*Global* 
</dt> <dd>

Indicates, when nonzero, that the port driver reads the contents of the registry value specified by *ValueName* under the Parameters\\Device subkey. The values under the Device key apply to all adapters in the system. When *Global* is zero, the port driver reads the contents of the registry value specified by *ValueName* under the Parameters\\Device(d) subkey, where (d) is a decimal value that corresponds to the port number of a particular adapter. In this case, the data retrieved is adapter-specific.

</dd> <dt>

*Type* 
</dt> <dd>

Indicates the data type of registry value. This parameter must have one of the values in the following table.



| Registry value data type                     | Meaning                                                                                                                                                                                                                                                                                                                                                                   |
|----------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| REG\_NONE<br/>                         | No data type specified. <br/>                                                                                                                                                                                                                                                                                                                                       |
| REG\_SZ<br/>                           | Indicates a **NULL**-terminated Unicode string.<br/>                                                                                                                                                                                                                                                                                                                |
| REG\_EXPAND\_SZ<br/>                   | Indicates a **NULL**-terminated Unicode string that includes environment variables that must be expanded to obtain the complete string. For example, a path name might be stored as the following string: "%USERPROFILE%\\Application Data ".<br/> In this example, the environment variable USERPROFILE must be expanded to obtain the actual pathname.<br/> |
| REG\_BINARY<br/>                       | Indicates a raw binary data.<br/>                                                                                                                                                                                                                                                                                                                                   |
| REG\_DWORD<br/>                        | Indicates a 32-bit double word value.<br/>                                                                                                                                                                                                                                                                                                                          |
| REG\_DWORD\_LITTLE\_ENDIAN<br/>        | Indicates a 32-bit double word value, in little-endian order. This is identical to REG\_DWORD.<br/>                                                                                                                                                                                                                                                                 |
| REG\_DWORD\_BIG\_ENDIAN<br/>           | Indicates a 32-bit double word value, in big-endian order. <br/>                                                                                                                                                                                                                                                                                                    |
| REG\_LINK<br/>                         | Indicates a Unicode string containing a symbolic link. <br/>                                                                                                                                                                                                                                                                                                        |
| REG\_MULTI\_SZ<br/>                    | Indicates a series of **NULL**-terminated strings.<br/>                                                                                                                                                                                                                                                                                                             |
| REG\_RESOURCE\_LIST<br/>               | Indicates that the registry value contains a list of hardware resources, also known as the "hardware resource map", that is stored under the HKEY\_LOCAL\_MACHINE\\HARDWARE\\ResourceMap hive.<br/>                                                                                                                                                                 |
| REG\_FULL\_RESOURCE\_DESCRIPTOR<br/>   | Indicates that the registry value contains a description of hardware resources stored under the HKEY\_LOCAL\_MACHINE\\HARDWARE\\Description hive.<br/>                                                                                                                                                                                                              |
| REG\_RESOURCE\_REQUIREMENTS\_LIST<br/> | Indicates that the registry value contains a list of hardware resource requirements stored under the HKEY\_LOCAL\_MACHINE\\HARDWARE\\ResourceMap tree.<br/>                                                                                                                                                                                                         |
| REG\_QWORD<br/>                        | Indicates that the registry value contains a 64-bit number.<br/>                                                                                                                                                                                                                                                                                                    |
| REG\_QWORD\_LITTLE\_ENDIAN<br/>        | Indicates that the registry value contains a 64-bit number. This is the same data type as REG\_QWORD. <br/>                                                                                                                                                                                                                                                         |



 

</dd> <dt>

*Buffer* 
</dt> <dd>

Pointer to the buffer where the retrieved registry information is to be reported.

</dd> <dt>

*BufferLength* 
</dt> <dd>

Pointer to a ULONG that contains the size, in bytes, of the registry data returned.

</dd> </dl>

## Return value

**StorPortRegistryRead** returns a Boolean value of **TRUE** if the data pointed to by *ValueName* is successfully converted into ASCII and copied into the buffer. This routine returns **FALSE** in the event of an error.

## Remarks

If **StorPortRegistryRead** returns **FALSE** with a nonzero value in the *BufferLength* parameter, the buffer that was passed was too small and the *BufferLength* parameter reflects the correct buffer size that should be used. If the routine returns **FALSE** with the *BufferLength* parameter set to zero, another error has occurred.

The buffer used in this routine is allocated by calling [**StorPortAllocateRegistryBuffer**](storportallocateregistrybuffer.md) and freed by calling [**StorPortFreeRegistryBuffer**](storportfreeregistrybuffer.md).

## Requirements



|                                 |                                                                                                                                         |
|---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/>      | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Header<br/>               | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| Library<br/>              | <dl> <dt>Storport.lib</dt> </dl>                                                 |
| IRQL<br/>                 | PASSIVE\_LEVEL<br/>                                                                                                               |
| DDI compliance rules<br/> | [**StorPortIrql**](https://msdn.microsoft.com/library/windows/hardware/hh454266)                                                                                       |



## See also

<dl> <dt>

[**StorPortAllocateRegistryBuffer**](storportallocateregistrybuffer.md)
</dt> <dt>

[**StorPortFreeRegistryBuffer**](storportfreeregistrybuffer.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortRegistryRead%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






