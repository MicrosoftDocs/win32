---
title: HBA\_SendCTPassThru routine
description: The HBA\_SendCTPassThru routine sends a common transport (CT) pass-through command.
ms.assetid: adfdb968-5ba3-43af-899a-7172c9ecf46c
keywords:
- HBA_SendCTPassThru routine Storage Devices
topic_type:
- apiref
api_name:
- HBA_SendCTPassThru
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

# HBA\_SendCTPassThru routine

The **HBA\_SendCTPassThru** routine sends a common transport (CT) pass-through command.

## Syntax


```C++
HBA_STATUS HBA_API HBA_SendCTPassThru(
  _In_  HBA_HANDLE HbaHandle,
  _In_  void       *pReqBuffer,
  _In_  HBA_UINT32 ReqBufferSize,
  _Out_ void       *pRspBuffer,
  _In_  HBA_UINT32 RspBufferSize
);
```



## Parameters

<dl> <dt>

*HbaHandle* \[in\]
</dt> <dd>

Contains a value returned by the routine [**HBA\_OpenAdapter**](hba-openadapter.md) that identifies the HBA that will route the CT command. The HBA routes the CT command to the server that runs the service requested by the CT command.

</dd> <dt>

*pReqBuffer* \[in\]
</dt> <dd>

Pointer to a buffer that contains the full frame of the common transport command in big-endian (wire) format.

</dd> <dt>

*ReqBufferSize* \[in\]
</dt> <dd>

Indicates the size of the buffer pointed to by *pReqBuffer*:

</dd> <dt>

*pRspBuffer* \[out\]
</dt> <dd>

Pointer to a buffer that contains the payload data from the reply to the common transport command in big-endian (wire) format.

</dd> <dt>

*RspBufferSize* \[in\]
</dt> <dd>

Indicates the size of the buffer pointed to by *pRspBuffer*.

</dd> </dl>

## Return value

The **HBA\_SendCTPassThru** routine returns a value of type [HBA\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff557233) that indicates the status of the HBA. If the HBA successfully delivers the command to the destination service, and the service executes the command and successfully returns the results, the HBA\_SendCTPassThru routine returns a value of HBA\_STATUS\_OK. If the command does not succeed, this routine returns an appropriate error code of type HBA\_STATUS.

## Remarks

The **HBA\_SendCTPassThru** library routine serves a purpose very similar to the [**SendCTPassThru**](https://msdn.microsoft.com/library/windows/hardware/ff565409) WMI method.

A CT command can request services that distribute encryption keys, IP addresses, time stamps, names, aliases, fabric configuration, and security policies. For a complete list of the service types that can be specified in a CT command, see the *Fibre Channel Generic Services - 4 (FC-GS-4)* specification published by the ANSI committee.

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

[**HBA\_SendCTPassThruV2**](hba-sendctpassthruv2.md)
</dt> <dt>

[HBA\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff557233)
</dt> <dt>

[**SendCTPassThru**](https://msdn.microsoft.com/library/windows/hardware/ff565409)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HBA_SendCTPassThru%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






