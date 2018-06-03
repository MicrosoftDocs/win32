---
title: HBA\_GetFcpTargetMappingV2 routine
description: The HBA\_GetFcpTargetMappingV2 routine retrieves the mappings between operating system and fibre channel protocol (FCP) identifiers for a set of targets that the HBA can enumerate on the indicated port.
ms.assetid: 970475d7-dd81-4189-bd2b-2a22c4f732dc
keywords:
- HBA_GetFcpTargetMappingV2 routine Storage Devices
topic_type:
- apiref
api_name:
- HBA_GetFcpTargetMappingV2
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

# HBA\_GetFcpTargetMappingV2 routine

The **HBA\_GetFcpTargetMappingV2** routine retrieves the mappings between operating system and fibre channel protocol (FCP) identifiers for a set of targets that the HBA can enumerate on the indicated port.

## Syntax


```C++
HBA_STATUS HBA_API HBA_GetFcpTargetMappingV2(
  _In_    HBA_HANDLE             HbaHandle,
  _In_    HBA_WWN                HbaPortWWN,
  _Inout_ HBA_FCPTARGETMAPPINGV2 *Mapping
);
```



## Parameters

<dl> <dt>

*HbaHandle* \[in\]
</dt> <dd>

Contains a value returned by the routine [**HBA\_OpenAdapter**](hba-openadapter.md) that identifies the HBA to query for the target mappings. The HBA returns mappings for the targets that it can enumerate on the port specified by *HbaPortWWN*.

</dd> <dt>

*HbaPortWWN* \[in\]
</dt> <dd>

Contains a 64-bit worldwide name (WWN) that uniquely identifies the fibre channel port on which the targets are enumerated. For a discussion of worldwide names, see the T11 committee's *Fibre Channel HBA API* specification.

</dd> <dt>

*Mapping* \[in, out\]
</dt> <dd>

Pointer to a structure of type [**HBA\_FCPTargetMappingV2**](hba-fcptargetmappingv2.md) that contains an array of bindings between operating system and FCP identifiers for a set of target devices. These mappings are maintained by the HBA referenced by *HbaHandle*. On input, the **NumberOfEntries** member of HBA\_FCPTargetMappingV2 should contain a number of mappings that fit in the output buffer. On output, the **NumberOfEntries** contains the number of mappings requested, or the full set of mappings, whichever is smaller. The value in **NumberOfEntries** contains the number of mappings returned even when an error occurred due to insufficient buffer space.

</dd> </dl>

## Return value

The **HBA\_GetFcpTargetMappingV2** routine returns a value of type [HBA\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff557233) that indicates the status of the HBA. In particular, **HBA\_GetFcpTargetMappingV2** returns one of the following qualifiers.



| Return code                                                                                                       | Description                                                                                                    |
|-------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**HBA\_STATUS\_OK**</dt> </dl>                    | Returned if all mapping were successfully retrieved. <br/>                                               |
| <dl> <dt>**HBA\_STATUS\_ERROR\_MORE\_DATA**</dt> </dl>     | Returned if the buffer space is insufficient to hold all of the mapping information. <br/>               |
| <dl> <dt>**HBA\_STATUS\_ERROR\_ILLEGAL\_WWN**</dt> </dl>   | Returned if the HBA referenced by *HbaHandle* does not contain a port with a name of *HbaPortWWN.* <br/> |
| <dl> <dt>**HBA\_STATUS\_ERROR\_NOT\_SUPPORTED**</dt> </dl> | Returned if the HBA referenced by *HbaHandle* does not support target mapping.<br/>                      |
| <dl> <dt>**HBA\_STATUS\_ERROR**</dt> </dl>                 | Returned if an unspecified error occurred that prevented the retrieval of the mapping information. <br/> |



 

## Remarks

The difference between the **HBA\_GetFcpTargetMappingV2** routine and the [**HBA\_GetFcpTargetMapping**](hba-getfcptargetmapping.md) routine is that the mappings returned by **HBA\_GetFcpTargetMappingV2** include a logical unit ID descriptor (LUID) for each logical unit. If the vital product data for a logical unit provides more than one LUID, then the LUID that **HBA\_GetFcpTargetMappingV2** returns depends on the types of LUIDs provided. For a complete explanation of how the LUID is chosen when more than one LUID is available, see the T11 committee's *Fibre Channel HBA API* specification.

## Requirements



|                            |                                                                                                        |
|----------------------------|--------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                     |
| Header<br/>          | <dl> <dt>Hbaapi.h (include Hbaapi.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Hbaapi.lib</dt> </dl>                  |
| DLL<br/>             | <dl> <dt>Hbaapi.dll</dt> </dl>                  |



## See also

<dl> <dt>

[**HBA\_FCPTargetMappingV2**](hba-fcptargetmappingv2.md)
</dt> <dt>

[**HBA\_GetFcpTargetMapping**](hba-getfcptargetmapping.md)
</dt> <dt>

[**HBA\_OpenAdapter**](hba-openadapter.md)
</dt> <dt>

[HBA\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff557233)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HBA_GetFcpTargetMappingV2%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






