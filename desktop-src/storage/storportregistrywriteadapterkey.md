---
title: StorPortRegistryWriteAdapterKey routine
description: The StorPortRegistryWriteAdapterKey routine is called by the miniport driver to write the hardware or device registry adapter keys located in registry at HKLM/CurrentControlSet/Enum/ Instance path /DeviceParameters/...
ms.assetid: D995FB36-177A-44BF-9326-EB2820DB0962
keywords:
- StorPortRegistryWriteAdapterKey routine Storage Devices
topic_type:
- apiref
api_name:
- StorPortRegistryWriteAdapterKey
api_location:
- Storport.lib
- Storport.dll
api_type:
- LibDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# StorPortRegistryWriteAdapterKey routine

The **StorPortRegistryWriteAdapterKey** routine is called by the miniport driver to write the hardware or device registry adapter keys located in registry at HKLM/CurrentControlSet/Enum/&lt;Instance path&gt;/DeviceParameters/... these keys are written at in the [**INF DDInstall.HW Section**](https://msdn.microsoft.com/library/windows/hardware/ff547330).

## Syntax


```C++
STORPORT_STATUS StorPortRegistryWriteAdapterKey(
  _In_     PVOID  HwDeviceExtension,
  _In_opt_ PCWSTR SubKeyName,
  _In_     PCWSTR ValueName,
  _In_     ULONG  ValueType,
  _In_     PVOID  ValueData,
  _In_     ULONG  ValueDataLength
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

A pointer to the hardware device extension. This is a per HBA storage area that the port driver allocates and initializes on behalf of the miniport driver. Miniport drivers usually store HBA-specific information in this extension, such as the state of the HBA and the mapped access ranges for the HBA. This area is available to the miniport driver immediately after the miniport driver calls [**StorPortInitialize**](storportinitialize.md). The port driver frees this memory when it removes the device. The miniport driver must be running at IRQL PASSIVE\_LEVEL when it calls this routine.

</dd> <dt>

*SubKeyName* \[in, optional\]
</dt> <dd>

The miniport subkey.

</dd> <dt>

*ValueName* \[in\]
</dt> <dd>

The name of the Value under the key.

</dd> <dt>

*ValueType* \[in\]
</dt> <dd>

One of the following registry data types.



| Type                                         | Meaning                                                                         |
|----------------------------------------------|---------------------------------------------------------------------------------|
| REG\_SZ<br/>                           | Unicode null-terminated string.<br/>                                      |
| REG\_EXPAND\_SZ<br/>                   | Unicode null-terminated string with environment variable references.<br/> |
| REG\_BINARY<br/>                       | Binary data.<br/>                                                         |
| REG\_DWORD<br/>                        | 32-bit double word.<br/>                                                  |
| REG\_DWORD\_LITTLE\_ENDIAN<br/>        | 32-bit double word with a little-endian format.<br/>                      |
| REG\_DWORD\_BIG\_ENDIAN<br/>           | 32-bit double word with a big-endian format.<br/>                         |
| REG\_LINK<br/>                         | Unicode string that specifies a symbolic link.<br/>                       |
| REG\_MULTI\_SZ<br/>                    | Multiple Unicode strings.<br/>                                            |
| REG\_RESOURCE\_LIST<br/>               | Resource list in the resource map.<br/>                                   |
| REG\_FULL\_RESOURCE\_DESCRIPTOR<br/>   | Resource list in the hardware description.<br/>                           |
| REG\_RESOURCE\_REQUIREMENTS\_LIST<br/> | Resource requirement list.<br/>                                           |
| REG\_QWORD<br/>                        | 64-bit quadlet number.<br/>                                               |
| REG\_QWORD\_LITTLE\_ENDIAN<br/>        | 64-bit quadlet number with a little-endian format.<br/>                   |



 

</dd> <dt>

*ValueData* \[in\]
</dt> <dd>

Pointer to a the data that contains the registry data to be written. The data is converted from UNICODE to a NULL-terminated ASCII string.

</dd> <dt>

*ValueDataLength* \[in\]
</dt> <dd>

Specifies the size of the data pointed to by *ValueData*.

</dd> </dl>

## Return value

Returns STOR\_STATUS\_SUCCESS when the operation is successful, otherwise the appropriate error code.

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Header<br/>          | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| Library<br/>         | <dl> <dt>Storport.lib</dt> </dl>                                                 |
| IRQL<br/>            | PASSIVE\_LEVEL<br/>                                                                                                               |



## See also

<dl> <dt>

[**StorPortInitialize**](storportinitialize.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortRegistryWriteAdapterKey%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






