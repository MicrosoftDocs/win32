---
title: HBA\_SendRPS routine
description: The HBA\_SendRPS routine sends a read port status block (RPS) request to the indicated agent port or domain controller.
ms.assetid: 6a79896a-0591-40dd-8e2d-6e3796556564
keywords:
- HBA_SendRPS routine Storage Devices
topic_type:
- apiref
api_name:
- HBA_SendRPS
api_location:
- Hbaapi.dll
api_type:
- DllExport
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# HBA\_SendRPS routine

The **HBA\_SendRPS** routine sends a read port status block (RPS) request to the indicated agent port or domain controller.

## Syntax


```C++
HBA_STATUS HBA_API HBA_SendRPS(
  _In_    HBA_HANDLE Handle,
  _In_    HBA_WWN    hbaPortWWN,
  _In_    HBA_WWN    agent_wwn,
  _In_    HBA_UINT32 agent_domain,
  _In_    HBA_WWN    object_wwn,
  _In_    HBA_UINT32 object_port_number,
  _Out_   void       *pRspBuffer,
  _Inout_ HBA_UINT32 *RspBufferSize
);
```



## Parameters

<dl> <dt>

*Handle* \[in\]
</dt> <dd>

Contains a value returned by the routine [**HBA\_OpenAdapter**](hba-openadapter.md) that identifies the local HBA through which the request is sent.

</dd> <dt>

*hbaPortWWN* \[in\]
</dt> <dd>

Contains a 64-bit worldwide name (WWN) that uniquely identifies the local port through which the RPS request is sent. For a discussion of worldwide names, see the T11 committee's *Fibre Channel HBA API* specification.

</dd> <dt>

*agent\_wwn* \[in\]
</dt> <dd>

Contains, when non-**NULL**, a 64-bit WWN that uniquely identifies the port to query for the status of the port referenced by *object\_wwn.* If this member is **NULL**, it is ignored, and the domain controller identified by *agent\_domain* is queried.

</dd> <dt>

*agent\_domain* \[in\]
</dt> <dd>

Contains the domain number for the domain controller to query for the status of the port referenced by *object\_wwn.* If *agent\_wwn* is non-**NULL**, this member is ignored.

</dd> <dt>

*object\_wwn* \[in\]
</dt> <dd>

Contains a 64-bit WWN that uniquely identifies the port for which status information is retrieved. If this member is **NULL**, it is ignored, and status information is retrieved for the port identified by *object\_port\_number*.

</dd> <dt>

*object\_port\_number* \[in\]
</dt> <dd>

Contains the relative port number of the port for which status information is retrieved. The meaning of the relative port number is defined by the hardware vendor that contains the port, and it is the responsibility of the software that receives the status query to interpret this number. If *object\_wwn* is non-**NULL**, this member is ignored.

</dd> <dt>

*pRspBuffer* \[out\]
</dt> <dd>

Pointer to a buffer that receives the results of the RPS request, if the request succeeds. If the destination port or domain controller rejects the request, this buffer holds the link service reject (LS\_RJT) payload data. If the amount of returned data exceeds the buffer size specified in *RspBufferSize*, the data is truncated to the buffer size*.* The payload data is in big-endian format (higher order bytes are in lower addresses).

</dd> <dt>

*RspBufferSize* \[in, out\]
</dt> <dd>

On input, indicates the size, in bytes, of the buffer pointed to by *pRspBuffer*. On return, this member indicates the size, in bytes, of the response data. A buffer size of 56 bytes is sufficient for the largest response.

</dd> </dl>

## Return value

The **HBA\_SendRPS** routine returns a value of type [HBA\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff557233) that indicates the status of the HBA. In particular, **HBA\_SendRPS** returns one of the following values.



| Return code                                                                                                     | Description                                                                                                                                                                                                                     |
|-----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**HBA\_STATUS\_OK**</dt> </dl>                  | Returned if the complete payload of a reply to the RPS request was successfully retrieved. <br/>                                                                                                                          |
| <dl> <dt>**HBA\_STATUS\_ERROR\_ILLEGAL\_WWN**</dt> </dl> | Returned if the HBA referenced by *handle* does not contain a port with a name that matches *hbaPortWWN*. <br/>                                                                                                           |
| <dl> <dt>**HBA\_STATUS\_ERROR\_ELS\_REJECT**</dt> </dl>  | Returned if the destination port referenced by *agent\_wwn* or the domain controller referenced by *agent\_domain* rejected the request node identification information data (RNID) that identifies the source HBA. <br/> |
| <dl> <dt>**HBA\_STATUS\_ERROR**</dt> </dl>               | Returned if an unspecified error occurred that prevented the execution of the RPS request. <br/>                                                                                                                          |



 

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HBA_SendRPS%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






