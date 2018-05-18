---
title: StorPortGetPfns routine
description: The StorPortGetPfns routine can be called when a miniport needs to retreive PFNs associated with a MDL for a SRB.
ms.assetid: 'F9E69501-4889-4A1B-8942-C6D4406474DE'
keywords: ["StorPortGetPfns routine Storage Devices"]
topic_type:
- apiref
api_name:
- StorPortGetPfns
api_location:
- Storport.h
api_type:
- HeaderDef
---

# StorPortGetPfns routine

\[Some information relates to pre-released product which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.\]

The **StorPortGetPfns** routine can be called when a miniport needs to retreive PFNs associated with a MDL for a SRB

## Syntax


```C++
ULONG StorPortGetPfns(
  _In_  PVOID               HwDeviceExtension,
  _In_  PSCSI_REQUEST_BLOCK Srb,
  _In_  PVOID               Mdl,
  _Out_ PVOID*              Pfns,
  _Out_ ULONG*              PfnCount,
  _Out_ ULONG*              StartingOffset
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

A pointer to the hardware device extension. This is a per HBA storage area that the port driver allocates and initializes on behalf of the miniport driver.

</dd> <dt>

*Srb* \[in\]
</dt> <dd>

A pointer to the source SCSI request block (SRB).

</dd> <dt>

*Mdl* \[in\]
</dt> <dd>

A pointer to the MDL for which Pfns are requested. Only MDLs obtained using **StorPortGetOriginalMdl** or **StorPortGetDataInBufferMdl** are supported.

</dd> <dt>

*Pfns* \[out\]
</dt> <dd>

A pointer to the beginning of the array of physical page numbers that are associated with the MDL. Callers must NOT modify or update or free the list.

</dd> <dt>

*PfnCount* \[out\]
</dt> <dd>

Specifies the number of PFNs in the array.

</dd> <dt>

*StartingOffset* \[out\]
</dt> <dd>

Specifies the byte offset within the initial page of the buffer described by the given MDL.

</dd> </dl>

## Return value

**StorPortGetPfns** returns one of the following status codes:



| Return code                                                                                                     | Description                                                                       |
|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| <dl> <dt>**STOR\_STATUS\_NOT\_IMPLEMENTED**</dt> </dl>   | This function is not implemented on the active operating system.<br/>       |
| <dl> <dt>**STOR\_STATUS\_SUCCESS**</dt> </dl>            | The list items were removed successfully or the list is already empty.<br/> |
| <dl> <dt>**STOR\_STATUS\_INVALID\_PARAMETER**</dt> </dl> | A pointer to one of the parameters is **NULL**.<br/>                        |



 

## Remarks

Miniport drivers usually store HBA-specific information in this extension, such as the state of the HBA and the mapped access ranges for the HBA. This area is available to the miniport driver in the **DeviceExtension-&gt;HwDeviceExtension** member of the device object for the HBA immediately after the miniport driver calls [**StorPortInitialize**](storportinitialize.md). The port driver frees this memory when it removes the device.

Starting in Windows 8, the *Srb* parameter may point to either [**SCSI\_REQUEST\_BLOCK**](scsi-request-block.md) or [**STORAGE\_REQUEST\_BLOCK**](storage-request-block.md).

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Header<br/>          | <dl> <dt>Storport.h</dt> </dl>                                                   |



## See also

<dl> <dt>

[**StorPortGetDataInBufferMdl**](https://msdn.microsoft.com/library/windows/hardware/jj553718)
</dt> <dt>

[**StorPortGetOriginalMdl**](https://msdn.microsoft.com/library/windows/hardware/ff567093)
</dt> <dt>

[**StorPortInitialize**](storportinitialize.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortGetPfns%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






