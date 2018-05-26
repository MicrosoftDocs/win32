---
title: HBA\_SendSRL routine
description: The HBA\_SendSRL routine issues a scan remote loop (SRL) request through the specified HBA to a specified domain controller.
ms.assetid: 455ff9c9-89d5-4c79-8b01-f0d731ac8d5a
keywords:
- HBA_SendSRL routine Storage Devices
topic_type:
- apiref
api_name:
- HBA_SendSRL
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

# HBA\_SendSRL routine

The **HBA\_SendSRL** routine issues a scan remote loop (SRL) request through the specified HBA to a specified domain controller.

## Syntax


```C++
HBA_STATUS HBA_API HBA_SendSRL(
  _In_    HBA_HANDLE handle,
  _In_    HBA_WWN    hbaPortWWN,
  _In_    HBA_WWN    wwn,
  _In_    HBA_UINT32 domain,
  _Out_   void       *pRspBuffer,
  _Inout_ HBA_UINT32 *pRspBufferSize
);
```



## Parameters

<dl> <dt>

*handle* \[in\]
</dt> <dd>

Contains a value returned by the routine [**HBA\_OpenAdapter**](hba-openadapter.md) that identifies the HBA through which the request is sent.

</dd> <dt>

*hbaPortWWN* \[in\]
</dt> <dd>

Contains a 64-bit worldwide name (WWN) that uniquely identifies the port through which the SRL request is sent. For a discussion of worldwide names, see the T11 committee's *Fibre Channel HBA API* specification.

</dd> <dt>

*wwn* \[in\]
</dt> <dd>

Contains a 64-bit WWN that uniquely identifies the FL\_Port port that is associated with the loop that is scanned. The SRL request is sent to this port. If this member is **NULL**, it is ignored, and the SRL request is sent to the domain controller that is associated with the loop. The domain controller is identified by the value in *domain.*

</dd> <dt>

*domain* \[in\]
</dt> <dd>

Indicates the number of the domain controller associated with the loops to scan. If *wwn* is nonzero, this member is ignored.

</dd> <dt>

*pRspBuffer* \[out\]
</dt> <dd>

Pointer to a buffer that receives the output data of the SRL request.

</dd> <dt>

*pRspBufferSize* \[in, out\]
</dt> <dd>

On input, indicates the size, in bytes, of the buffer at *pRspBuffer*. On output, this member contains the number of bytes of data retrieved in *pRspBuffer*. If the buffer is not large enough to receive all of the response data, the data is truncated to the size of the buffer. Eight bytes is sufficient buffer space for any response.

</dd> </dl>

## Return value

The **HBA\_SendSRL** routine returns a value of type [HBA\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff557233) that indicates the status of the HBA. In particular, **HBA\_SendSRL** returns one of the following values.



| Return code                                                                                                     | Description                                                                                                                                                                                                        |
|-----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**HBA\_STATUS\_OK**</dt> </dl>                  | Returned if the complete payload of a reply to the SRL request was successfully retrieved. <br/>                                                                                                             |
| <dl> <dt>**HBA\_STATUS\_ERROR\_ILLEGAL\_WWN**</dt> </dl> | Returned if the HBA referenced by *handle* does not contain a port with a name that matches *hbaPortWWN*. <br/>                                                                                              |
| <dl> <dt>**HBA\_STATUS\_ERROR\_ELS\_REJECT**</dt> </dl>  | Returned if the destination port referenced by *wwn,* or the domain controller referenced by *domain,* rejected the request node identification information data (RNID) that identifies the source HBA.<br/> |
| <dl> <dt>**HBA\_STATUS\_ERROR**</dt> </dl>               | Returned if an unspecified error occurred that prevented the execution of the SRL request. <br/>                                                                                                             |



 

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HBA_SendSRL%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






