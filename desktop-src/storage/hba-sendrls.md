---
title: HBA\_SendRLS routine
description: The HBA\_SendRLS WMI routine sends a read link error status block (RLS) request through the indicated local port to the indicated remote port to retrieve a link error status block associated with the remote port.
ms.assetid: d2349c45-eb88-4584-bbdd-b7c46601a1bc
keywords:
- HBA_SendRLS routine Storage Devices
topic_type:
- apiref
api_name:
- HBA_SendRLS
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

# HBA\_SendRLS routine

The **HBA\_SendRLS** WMI routine sends a read link error status block (RLS) request through the indicated local port to the indicated remote port to retrieve a link error status block associated with the remote port.

## Syntax


```C++
HBA_STATUS HBA_API HBA_SendRLS(
  _In_    HBA_HANDLE HbaHandle,
  _In_    HBA_WWN    HbaPortWWN,
  _In_    HBA_WWN    DestWWN,
  _Out_   void       *pRspBuffer,
  _Inout_ HBA_UINT32 *pRspBufferSize
);
```



## Parameters

<dl> <dt>

*HbaHandle* \[in\]
</dt> <dd>

Contains a value returned by the routine [**HBA\_OpenAdapter**](hba-openadapter.md) that identifies the HBA through which the request is sent.

</dd> <dt>

*HbaPortWWN* \[in\]
</dt> <dd>

Contains a 64-bit worldwide name (WWN) that uniquely identifies the local port through which the request is sent. For a discussion of worldwide names, see the T11 committee's *Fibre Channel HBA API* specification.

</dd> <dt>

*DestWWN* \[in\]
</dt> <dd>

Contains a 64-bit WWN that uniquely identifies the destination port to which the request is sent.

</dd> <dt>

*pRspBuffer* \[out\]
</dt> <dd>

Pointer to a buffer that receives the output data of the RLS request, if the request succeeds. If the destination port rejects the request, this buffer holds the link service reject (LS\_RJT) payload data. If the amount of returned data exceeds the buffer size specified in *pRspBufferSize*, the data is truncated to the buffer size*.* The payload data is in big-endian format (higher order bytes are in lower addresses).

</dd> <dt>

*pRspBufferSize* \[in, out\]
</dt> <dd>

Indicates the size, in bytes, of the buffer at *pRspBuffer*. A size of 28 bytes is sufficient for the largest response.

</dd> </dl>

## Return value

The **HBA\_SendRLS** routine returns a value of type [HBA\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff557233) that indicates the status of the HBA. In particular, **HBA\_SendRLS** returns one of the following values.



| Return code                                                                                                     | Description                                                                                                                                                           |
|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**HBA\_STATUS\_OK**</dt> </dl>                  | Returned if the complete payload of a reply to the RLS request was successfully retrieved. <br/>                                                                |
| <dl> <dt>**HBA\_STATUS\_ERROR\_ILLEGAL\_WWN**</dt> </dl> | Returned if the HBA referenced by *handle* does not contain a port with a name that matches *HbaPortWWN*. <br/>                                                 |
| <dl> <dt>**HBA\_STATUS\_ERROR\_ELS\_REJECT**</dt> </dl>  | Returned if the destination port referenced by *DestWWN* rejected the request node identification information data (RNID) that identifies the source HBA. <br/> |
| <dl> <dt>**HBA\_STATUS\_ERROR**</dt> </dl>               | Returned if an unspecified error occurred that prevented the execution of the RLS request. <br/>                                                                |



 

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HBA_SendRLS%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






