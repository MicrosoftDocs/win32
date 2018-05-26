---
title: StorPortLogSystemEvent routine
description: The StorPortLogSystemEvent routine gives miniport drivers full access to the capabilities of the Windows kernel event facility, enabling miniport drivers to create event log entries that are truly useful in troubleshooting storage issues.
ms.assetid: 720245ff-8c97-4b8d-8406-f6b712fa74c9
keywords:
- StorPortLogSystemEvent routine Storage Devices
topic_type:
- apiref
api_name:
- StorPortLogSystemEvent
api_location:
- storport.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# StorPortLogSystemEvent routine

The StorPortLogSystemEvent routine gives miniport drivers full access to the capabilities of the Windows kernel event facility, enabling miniport drivers to create event log entries that are truly useful in troubleshooting storage issues. It provides a better alternative to the existing miniport driver event logging function, [**StorPortLogError**](storportlogerror.md).

## Syntax


```C++
ULONG StorPortLogSystemEvent(
  _In_    PVOID                   HwDeviceExtension,
  _Inout_ PSTOR_LOG_EVENT_DETAILS LogDetails,
  _Inout_ PULONG                  MaximumSize
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

A pointer to the hardware device extension. This is a per HBA storage area that the port driver allocates and initializes on behalf of the miniport driver. Miniport drivers usually store HBA-specific information in this extension, such as the state of the HBA and the mapped access ranges for the HBA. This area is available to the miniport immediately after the miniport driver calls [**StorPortInitialize**](storportinitialize.md). The port driver frees this memory when it removes the device.

</dd> <dt>

*LogDetails* \[in, out\]
</dt> <dd>

Information to appear in the system event log entry.

</dd> <dt>

*MaximumSize* \[in, out\]
</dt> <dd>

Variable to receive maximum combined size of miniport's dump data and strings. Only returned if the function fails and returns a STOR\_STATUS\_INVALID\_BUFFER\_SIZE value. This parameter is optional.

</dd> </dl>

## Return value



| Return code                                                                                                          | Description                                                                                                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**STOR\_STATUS\_NOT\_IMPLEMENTED**</dt> </dl>        | This function is not implemented on the active operating system.<br/>                                                                                                                                             |
| <dl> <dt>**STOR\_STATUS\_INVALID\_PARAMETER**</dt> </dl>      | An invalid parameter was passed in.<br/>                                                                                                                                                                          |
| <dl> <dt>**STOR\_STATUS\_INVALID\_IRQL**</dt> </dl>           | The call was made at IRQL &gt; DISPATCH\_LEVEL.<br/>                                                                                                                                                              |
| <dl> <dt>**STOR\_STATUS\_INSUFFICIENT\_RESOURCES**</dt> </dl> | There were insufficient system resources to complete the request.<br/>                                                                                                                                            |
| <dl> <dt>**STOR\_STATUS\_UNSUPPORTED\_VERSION:**</dt> </dl>   | An unsupported (for example, more current) version of the STOR\_LOG\_EVENT\_DETAILS structure was specified. When this is returned, LogDetails-&gt;InterfaceRevision is set to the latest supported version.<br/> |
| <dl> <dt>**STOR\_STATUS\_INVALID\_BUFFER\_SIZE**</dt> </dl>   | The buffers passed to the function were too large. When this value is returned, MaximumSize is set to the maximum combined size of the miniport's dump data and strings.<br/>                                     |
| <dl> <dt>**STOR\_STATUS\_SUCCESS**</dt> </dl>                 | The log operation completed successfully.<br/>                                                                                                                                                                    |



 

## Remarks

To understand how you may use custom error codes to best advantage, see [Storport Error Log Extensions](https://msdn.microsoft.com/library/windows/hardware/ff567554). The StorPortLogSystemEvent routine must be called at IRQL &lt;= DISPATCH\_LEVEL. If you pass in a more recent version of STOR\_LOG\_EVENT\_DETAILS than that supported by this build, this function changes the InterfaceRevision field to the latest supported version and returns STOR\_STATUS\_UNSUPPORTED\_VERSION. The InterfaceRevision field of STOR\_LOG\_EVENT\_DETAILS is a 32-bit value. However, only the three most-significant bytes are used for validation. The low byte is reserved to distinguish between compatible, minor variations of a particular version. For instance, a revision 0x00000101 structure is compatible with a Storport that implements revision 0x00000100 of the interface, although it is possible that some minor, noncritical functionality may be lost. If you specify a combined size of dump data and strings that exceeds the maximum allowed event log entry size, the integer pointed to by MaximumSize is set to the maximum allowed size of miniport dump data and strings, and STOR\_INVALID\_BUFFER\_SIZE is returned. Although this function accepts ULONG values for the path, target, and LUN address specifiers, the values are truncated to UCHAR values because Storport internally only supports 8-bit values for these specifiers.

## Requirements



|                                 |                                                                                                                                         |
|---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/>      | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Header<br/>               | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| DDI compliance rules<br/> | [**StorPortIrql**](https://msdn.microsoft.com/library/windows/hardware/hh454266)                                                                                       |



## See also

<dl> <dt>

[**StorPortLogError**](storportlogerror.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortLogSystemEvent%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






