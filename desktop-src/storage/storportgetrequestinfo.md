---
title: StorPortGetRequestInfo routine
description: The StorPortGetRequestInfo routine retrieves the IO request information associated with a SCSI request block (SRB) and returns it in a STOR\_REQUEST\_INFO structure.
ms.assetid: 3B0A25E8-6DBC-4AA9-A0D0-DDB36B402F43
keywords:
- StorPortGetRequestInfo routine Storage Devices
topic_type:
- apiref
api_name:
- StorPortGetRequestInfo
api_location:
- storport.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# StorPortGetRequestInfo routine

The **StorPortGetRequestInfo** routine retrieves the IO request information associated with a SCSI request block (SRB) and returns it in a [**STOR\_REQUEST\_INFO**](stor-request-info.md) structure.

## Syntax


```C++
ULONG StorPortGetRequestInfo(
  _In_  PVOID               HwDeviceExtension,
  _In_  PSCSI_REQUEST_BLOCK Srb,
  _Out_ PSTOR_REQUEST_INFO  RequestInfo
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

A pointer to the SRB to be queried.

</dd> <dt>

*RequestInfo* \[out\]
</dt> <dd>

A pointer to a caller-supplied [**STOR\_REQUEST\_INFO**](stor-request-info.md) structure.

</dd> </dl>

## Return value

The **StorPortGetRequestInfo** routine returns one of these status codes:



| Return code                                                                                                       | Description                                                                                       |
|-------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| <dl> <dt>**STOR\_STATUS\_UNSUPPORTED\_VERSION**</dt> </dl> | The version specified for [**STOR\_REQUEST\_INFO**](stor-request-info.md) is invalid.<br/> |
| <dl> <dt>**STOR\_STATUS\_SUCCESS**</dt> </dl>              | The operation was successful.<br/>                                                          |
| <dl> <dt>**STOR\_STATUS\_INVALID\_PARAMETER**</dt> </dl>   | Either *Srb* or *RequestInfo* is set to NULL.<br/>                                          |



 

## Remarks

The caller of **StorPortGetRequestInfo** must set the **Version** member of *RequestInfo* to STOR\_REQUEST\_INFO\_VER\_1. Otherwise, function will return STOR\_STATUS\_UNSUPPORTED\_VERSION.

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Version<br/>         | Available in Windows 8 and later versions of Windows.<br/>                                                                        |
| Header<br/>          | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| IRQL<br/>            | Any<br/>                                                                                                                          |



## See also

<dl> <dt>

[**STOR\_REQUEST\_INFO**](stor-request-info.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortGetRequestInfo%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






