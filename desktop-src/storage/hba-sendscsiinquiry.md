---
title: HBA\_SendScsiInquiry routine
description: The HBA\_SendScsiInquiry routine sends a SCSI inquiry command to the indicated remote port.
ms.assetid: 6239f9b5-99e9-4ed7-b2a8-863c1784692b
keywords:
- HBA_SendScsiInquiry routine Storage Devices
topic_type:
- apiref
api_name:
- HBA_SendScsiInquiry
api_location:
- Hbaapi.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# HBA\_SendScsiInquiry routine

The **HBA\_SendScsiInquiry** routine sends a SCSI inquiry command to the indicated remote port.

## Syntax


```C++
HBA_STATUS HBA_API HBA_SendScsiInquiry(
  _In_  HBA_HANDLE handle,
  _In_  HBA_WWN    portWWN,
  _In_  HBA_UINT64 fcLUN,
  _In_  HBA_UINT8  EVPD,
  _In_  HBA_UINT32 PageCode,
  _Out_ void       *pRspBuffer,
  _In_  HBA_UINT32 pRespBufferSize,
  _Out_ void       *pSenseBuffer,
  _In_  HBA_UINT32 SenseBufferSize
);
```



## Parameters

<dl> <dt>

*handle* \[in\]
</dt> <dd>

Contains a value returned by the routine [**HBA\_OpenAdapter**](hba-openadapter.md) that identifies the HBA on which the target port is located.

</dd> <dt>

*portWWN* \[in\]
</dt> <dd>

Contains a 64-bit worldwide name (WWN) that uniquely identifies the remote target port to which the SCSI inquiry command is sent. For a discussion of worldwide names, see the T11 committee's *Fibre Channel HBA API* specification.

</dd> <dt>

*fcLUN* \[in\]
</dt> <dd>

Indicates the fibre channel logical unit number of the logical unit to which the SCSI inquiry command is sent.

</dd> <dt>

*EVPD* \[in\]
</dt> <dd>

Indicates, when 0, that the inquiry command retrieves the standard SCSI inquiry data. When this member is set to 1, it indicates the inquiry command retrieves the vital product data (VPD) specified by *PageCode*.

</dd> <dt>

*PageCode* \[in\]
</dt> <dd>

Indicates the VPD page code to retrieve when *EVPD* is set to 1. If *EVPD* is not set to 1, *PageCode* is ignored.

</dd> <dt>

*pRspBuffer* \[out\]
</dt> <dd>

Pointer to a buffer that receives the output data of the SCSI inquiry command.

</dd> <dt>

*pRespBufferSize* \[in\]
</dt> <dd>

Indicates the size, in bytes, of the buffer at *pRspBuffer*.

</dd> <dt>

*pSenseBuffer* \[out\]
</dt> <dd>

Pointer to a buffer that receives the SCSI sense data.

</dd> <dt>

*SenseBufferSize* \[in\]
</dt> <dd>

On input, indicates the size, in bytes, of the buffer at *pSenseBuffer*. On output, this member indicates the number of bytes of sense data returned.

</dd> </dl>

## Return value

The **HBA\_SendScsiInquiry** routine returns a value of type [HBA\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff557233) that indicates the status of the HBA. In particular, **HBA\_SendScsiInquiry** returns one of the following values.



| Return code                                                                                                        | Description                                                                                                                 |
|--------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**HBA\_STATUS\_OK**</dt> </dl>                     | Returned if the complete payload of a reply to the SCSI inquiry command was successfully retrieved. <br/>             |
| <dl> <dt>**HBA\_STATUS\_ERROR\_NOT\_A\_TARGET**</dt> </dl>  | Returned if the specified remote port specified by *portWWN* does not have SCSI target functionality.<br/>            |
| <dl> <dt>**HBA\_STATUS\_ERROR\_TARGET\_BUSY**</dt> </dl>    | Returned if the SCSI inquiry command could not be delivered without causing a SCSI overlapped command condition.<br/> |
| <dl> <dt>**HBA\_STATUS\_SCSI\_CHECK\_CONDITION**</dt> </dl> | Returned if a SCSI check condition occurred and SCSI send data is provided in the buffer at *pSenseBuffer*.<br/>      |
| <dl> <dt>**HBA\_STATUS\_ERROR**</dt> </dl>                  | Returned if an unspecified error occurred that prevented the execution of the SCSI inquiry command. <br/>             |



 

## Requirements



|                            |                                                                                                        |
|----------------------------|--------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                     |
| Header<br/>          | <dl> <dt>Hbaapi.h (include Hbaapi.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Hbaapi.lib</dt> </dl>                  |
| DLL<br/>             | <dl> <dt>Hbaapi.dll</dt> </dl>                  |



## See also

<dl> <dt>

[**HBA\_OpenAdapter**](hba-openadapter.md)
</dt> <dt>

[HBA\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff557233)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HBA_SendScsiInquiry%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






