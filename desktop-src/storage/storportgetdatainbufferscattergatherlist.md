---
title: StorPortGetDataInBufferScatterGatherList routine
description: Returns the scatter-gather list associated with the input data buffer of a SCSI request block (SRB).
ms.assetid: 015592AE-4AF6-48C8-BF79-6B22A6FCAB98
keywords:
- StorPortGetDataInBufferScatterGatherList routine Storage Devices
topic_type:
- apiref
api_name:
- StorPortGetDataInBufferScatterGatherList
api_location:
- Storport.lib
- Storport.dll
api_type:
- LibDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# StorPortGetDataInBufferScatterGatherList routine

Returns the scatter-gather list associated with the input data buffer of a SCSI request block (SRB).

## Syntax


```C++
ULONG StorPortGetDataInBufferScatterGatherList(
  _In_  PVOID                     HwDeviceExtension,
  _In_  PSCSI_REQUEST_BLOCK       Srb,
  _Out_ PSTOR_SCATTER_GATHER_LIST *SgList
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

A pointer to the hardware device extension for the host bus adapter (HBA).

</dd> <dt>

*Srb* \[in\]
</dt> <dd>

The request block to containing the input data buffer for the scatter-gather list.

</dd> <dt>

*SgList* \[out\]
</dt> <dd>

A pointer to an scatter-gather list structure address to receive the scatter-gather list for the input data buffer in *Srb*.

</dd> </dl>

## Return value

A status value indicating the result of the notification. This can be one of these values:



| Return code                                                                                                     | Description                                                             |
|-----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| <dl> <dt>**STOR\_STATUS\_SUCCESS**</dt> </dl>            | The scatter-gather list for *Srb* was successfully returned.<br/> |
| <dl> <dt>**STOR\_STATUS\_INVALID\_PARAMETER**</dt> </dl> | The pointer value in *SgList* is NULL.<br/>                       |



 

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Version<br/>         | Available starting with Windows 8.<br/>                                                                                           |
| Header<br/>          | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| Library<br/>         | <dl> <dt>Storport.lib</dt> </dl>                                                 |
| IRQL<br/>            | Any<br/>                                                                                                                          |



## See also

<dl> <dt>

[**StorPortGetDataInBufferMdl**](storportgetdatainbuffermdl.md)
</dt> <dt>

[**StorPortGetDataInBufferSystemAddress**](storportgetdatainbuffersystemaddress.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortGetDataInBufferScatterGatherList%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






