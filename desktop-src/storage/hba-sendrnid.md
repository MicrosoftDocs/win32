---
title: HBA\_SendRNID routine
description: The HBA\_SendRNID routine sends a request for node identification data (RNID) to the indicated HBA, which in turn routes the request through the indicated port or node to the appropriate fabric configuration server.
ms.assetid: c15d74c8-bc04-4d82-a729-6b13f778b8c7
keywords:
- HBA_SendRNID routine Storage Devices
topic_type:
- apiref
api_name:
- HBA_SendRNID
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

# HBA\_SendRNID routine

The **HBA\_SendRNID** routine sends a request for node identification data (RNID) to the indicated HBA, which in turn routes the request through the indicated port or node to the appropriate fabric configuration server.

## Syntax


```C++
HBA_STATUS HBA_API HBA_SendRNID(
  _In_    HBA_HANDLE  HbaHandle,
  _In_    HBA_WWN     Wwn,
  _In_    HBA_WWNTYPE WwnType,
  _Out_   void        *pRspBuffer,
  _Inout_ HBA_UINT32  *RspBufferSize
);
```



## Parameters

<dl> <dt>

*HbaHandle* \[in\]
</dt> <dd>

Contains a value returned by the routine [**HBA\_OpenAdapter**](hba-openadapter.md) that identifies the HBA that will route the command. The HBA routes this command to the appropriate fabric configuration server.

</dd> <dt>

*Wwn* \[in\]
</dt> <dd>

Contains a 64-bit worldwide name (WWN) that uniquely identifies a port or a node from which the RNID command is issued. For a discussion of worldwide names, see the T11 committee's *Fibre Channel HBA API* specification.

</dd> <dt>

*WwnType* \[in\]
</dt> <dd>

Contains an enumerator value of type [**HBA\_wwntype**](hba-wwntype.md) that indicates whether the WWN specified by *Wwn* is a port or a node:

</dd> <dt>

*pRspBuffer* \[out\]
</dt> <dd>

Pointer to a buffer that contains, in big-endian (wire) format, the payload data from the reply to the node identification request.

</dd> <dt>

*RspBufferSize* \[in, out\]
</dt> <dd>

On input, indicates the size, in bytes, of the buffer pointed to by *pRspBuffer*. On return, this member indicates the size, in bytes, of the response data.

</dd> </dl>

## Return value

The **HBA\_SendRNID** routine returns a value of type [HBA\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff557233) that indicates the status of the HBA.

## Remarks

The node identification data request is a common transport (CT) command that queries a fabric configuration server for node identification data. For a complete description of this command, see the sections dealing with node identification requests in the *Fibre Channel Generic Services - 4 (FC-GS-4)* specification published by the ANSI committee.

The **HBA\_SendRNID** library routine serves a purpose very similar to the [**SendRNID**](https://msdn.microsoft.com/library/windows/hardware/ff565459) WMI method.

## Requirements



|                            |                                                                                                        |
|----------------------------|--------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                     |
| Header<br/>          | <dl> <dt>Hbaapi.h (include Hbaapi.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Hbaapi.lib</dt> </dl>                  |
| DLL<br/>             | <dl> <dt>Hbaapi.dll</dt> </dl>                  |



## See also

<dl> <dt>

[**HBA\_SendRNID**](hba-sendrnid.md)
</dt> <dt>

[**SendRNID**](https://msdn.microsoft.com/library/windows/hardware/ff565459)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HBA_SendRNID%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






