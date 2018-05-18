---
title: StorPortGetOriginalMdl routine
description: The StorPortGetOriginalMdl routine returns the MDL associated with the given SRB.
ms.assetid: '48042e9d-ed83-4326-931d-ded753deb1a7'
keywords: ["StorPortGetOriginalMdl routine Storage Devices"]
topic_type:
- apiref
api_name:
- StorPortGetOriginalMdl
api_location:
- storport.h
api_type:
- HeaderDef
---

# StorPortGetOriginalMdl routine

The **StorPortGetOriginalMdl** routine returns the MDL associated with the given SRB.

## Syntax


```C++
ULONG StorPortGetOriginalMdl(
  _In_  PVOID               HwDeviceExtension,
  _In_  PSCSI_REQUEST_BLOCK Srb,
  _Out_ PVOID               *Mdl
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

A pointer to a [**SCSI\_REQUEST\_BLOCK**](scsi-request-block.md) structure.

</dd> <dt>

*Mdl* \[out\]
</dt> <dd>

A pointer to receive the MDL.

</dd> </dl>

## Return value

StorPortGetOriginalMdl returns one of the following status codes:



| Return code                                                                                                     | Description                                                                 |
|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| <dl> <dt>**STOR\_STATUS\_NOT\_IMPLEMENTED**</dt> </dl>   | This function is not implemented on the active operating system.<br/> |
| <dl> <dt>**STOR\_STATUS\_SUCCESS**</dt> </dl>            | Indicates that the MDL was obtained successfully.<br/>                |
| <dl> <dt>**STOR\_STATUS\_INVALID\_PARAMETER**</dt> </dl> | The pointer in *Mdl* receiving the SRB's MDL is **NULL**.<br/>        |



 

## Remarks

Starting in Windows 8, the *Srb* parameter may point to either [**SCSI\_REQUEST\_BLOCK**](scsi-request-block.md) or [**STORAGE\_REQUEST\_BLOCK**](storage-request-block.md). If the function identifier in the **Function** field of *Srb* is **SRB\_FUNCTION\_STORAGE\_REQUEST\_BLOCK**, the SRB is a **STORAGE\_REQUEST\_BLOCK** request structure.

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Header<br/>          | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |



## See also

<dl> <dt>

[**SCSI\_REQUEST\_BLOCK**](scsi-request-block.md)
</dt> <dt>

[**STORAGE\_REQUEST\_BLOCK**](storage-request-block.md)
</dt> <dt>

[**StorPortGetSystemAddress**](storportgetsystemaddress.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortGetOriginalMdl%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






