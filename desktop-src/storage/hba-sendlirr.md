---
title: HBA\_SendLIRR routine
description: The HBA\_SendLIRR routine registers or de-registers a local (source) port to receive link incident records (LIR) from a remote (destination) port.
ms.assetid: 2e38d297-1e26-4605-a242-3f0180ac0360
keywords:
- HBA_SendLIRR routine Storage Devices
topic_type:
- apiref
api_name:
- HBA_SendLIRR
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

# HBA\_SendLIRR routine

The **HBA\_SendLIRR** routine registers or de-registers a local (source) port to receive link incident records (LIR) from a remote (destination) port.

## Syntax


```C++
HBA_STATUS HBA_API HBA_SendLIRR(
  _In_    HBA_HANDLE Handle,
  _In_    HBA_WWN    SourceWWN,
  _In_    HBA_WWN    DestWWN,
  _In_    HBA_UINT8  Function,
  _In_    HBA_UINT8  Type,
  _Out_   void       *pRspBuffer,
  _Inout_ HBA_UINT32 *RspBufferSize
);
```



## Parameters

<dl> <dt>

*Handle* \[in\]
</dt> <dd>

Contains a value returned by the routine [**HBA\_OpenAdapter**](hba-openadapter.md) that identifies the HBA through which to send the LIR request.

</dd> <dt>

*SourceWWN* \[in\]
</dt> <dd>

Contains the worldwide name (WWN) of the local port from which to issue the command and which will receive link incident records from the destination port referenced by *DestWWN*. For a definition of worldwide names, see the T11 committee's specification for *Fibre Channel HBA API*.

</dd> <dt>

*DestWWN* \[in\]
</dt> <dd>

Contains the WWN of the remote destination port that will report link incident records to the source port. For a definition of worldwide names, see the T11 committee's specification for *Fibre Channel HBA API*.

</dd> <dt>

*Function* \[in\]
</dt> <dd>

Specifies the action to take. This member either registers a source port to receive link incident records and specifies the mode of registration, or it de-registers a source port that is already registered. This member must have one of the following values.



| Value in Hexadecimal | Meaning                                                                                                                                                                                                                                                                   |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x0<br/>       | Reserved.<br/>                                                                                                                                                                                                                                                      |
| 0x01<br/>      | Indicates that the registration is conditional. The source port is added to the registration list for records with the format indicated in *Type* and receives link incident records of that type only if no other ports are receiving records for that type. <br/> |
| 0x02<br/>      | Indicates that the source port is always added to the registration list for records with the format indicated in *Type*. <br/>                                                                                                                                      |
| 0x03<br/>      | Reserved. <br/>                                                                                                                                                                                                                                                     |
| 0xff<br/>      | Indicates that the source port is removed from the registration list for records with the format indicated in *Type* and no longer receives link incident records of that format type. <br/>                                                                        |



 

For further explanation of the available registration modes, see the T11 committee's *Fibre Channel Framing and Signaling* specification.

</dd> <dt>

*Type* \[in\]
</dt> <dd>

Specifies the type of records whose delivery is affected by the link incident record request (LIRR). When 0, the LIRR governs the delivery of common link incident records, so if the source port is registering to receive records, then the source port is added to the destination port's registration list for common link incident records. If the source port is de-registering, then it is removed from that list.

If *Type* is nonzero, then it specifies the format type of the records for which the source port is registering or de-registering. For a list of the types of formats and their corresponding values, see the FC-4 type codes table in the T11 committee's *Fibre Channel Framing and Signaling* specification.

</dd> <dt>

*pRspBuffer* \[out\]
</dt> <dd>

Pointer to a buffer that receives the payload data of the response to the LIRR, if the LIRR succeeds. If the destination port rejects the request, this buffer holds the link service reject (LS\_RJT) payload data. If the amount of returned data exceeds the buffer size specified in *RspBufferSize*, the data is truncated to the buffer size*.* The payload data is in big-endian format (higher order bytes are in lower addresses).

</dd> <dt>

*RspBufferSize* \[in, out\]
</dt> <dd>

On input, indicates the size, in bytes, of the buffer at *pRspBuffer*. On output, this member indicates the size, in bytes, of the response data. Eight bytes is sufficient for any response.

</dd> </dl>

## Return value

The **HBA\_ScsiReportLUNsV2** routine returns a value of type [HBA\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff557233) that indicates the status of the HBA. In particular, **HBA\_ScsiReportLUNsV2** returns one of the following values.



| Return code                                                                                                       | Description                                                                                                                                                           |
|-------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**HBA\_STATUS\_OK**</dt> </dl>                    | Returned if the LIRR succeeded and payload data was successfully retrieved. <br/>                                                                               |
| <dl> <dt>**HBA\_STATUS\_ERROR\_ILLEGAL\_WWN**</dt> </dl>   | Returned if the HBA referenced by *handle* does not contain a port with a name that matches *SourceWWN*. <br/>                                                  |
| <dl> <dt>**HBA\_STATUS\_ERROR\_NOT\_SUPPORTED**</dt> </dl> | Returned if the local HBA referenced by *handle* does not support link incident reporting.<br/>                                                                 |
| <dl> <dt>**HBA\_STATUS\_ERROR\_ELS\_REJECT**</dt> </dl>    | Returned if the destination port referenced by *DestWWN* rejected the request node identification information data (RNID) that identifies the source HBA. <br/> |
| <dl> <dt>**HBA\_STATUS\_ERROR**</dt> </dl>                 | Returned if an unspecified error occurred that prevented the execution of the LIR request. <br/>                                                                |



 

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HBA_SendLIRR%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






