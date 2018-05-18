---
title: HBA\_GetFcpTargetMapping routine
description: The HBA\_GetFcpTargetMapping routine retrieves the mappings between operating system and fibre channel protocol (FCP) identifiers for a set of targets that the HBA can enumerate.
ms.assetid: 'd1064f97-e640-49b6-be8c-19662e5de9bb'
keywords: ["HBA_GetFcpTargetMapping routine Storage Devices"]
topic_type:
- apiref
api_name:
- HBA_GetFcpTargetMapping
api_location:
- Hbaapi.dll
api_type:
- DllExport
---

# HBA\_GetFcpTargetMapping routine

The **HBA\_GetFcpTargetMapping** routine retrieves the mappings between operating system and fibre channel protocol (FCP) identifiers for a set of targets that the HBA can enumerate.

## Syntax


```C++
HBA_STATUS HBA_API HBA_GetFcpTargetMapping(
  _In_    HBA_HANDLE            HbaHandle,
  _Inout_ PHBA_FCPTARGETMAPPING Mapping
);
```



## Parameters

<dl> <dt>

*HbaHandle* \[in\]
</dt> <dd>

Contains a value returned by the routine [**HBA\_OpenAdapter**](hba-openadapter.md) that identifies the HBA to query for the target mappings. The HBA returns mappings for the targets that it can enumerate.

</dd> <dt>

*Mapping* \[in, out\]
</dt> <dd>

Pointer to a structure of type [**HBA\_FCPTargetMapping**](hba-fcptargetmapping.md) that contains an array of bindings between operating system and FCP identifiers for a set of target devices. These mappings are maintained by the HBA referenced by *HbaHandle*. On input, the **NumberOfEntries** member of HBA\_FCPTargetMapping should contain a number of mappings that fit in the output buffer. On output, the **NumberOfEntries** contains the number of mappings requested, or the full set of mappings, whichever is smaller. The value in **NumberOfEntries** contains the number of mappings returned even when an error occurred due to insufficient buffer space.

</dd> </dl>

## Return value

The **HBA\_GetFcpTargetMapping** routine returns a value of type [HBA\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff557233) that indicates the status of the HBA. In particular, **HBA\_GetFcpTargetMapping** returns one of the following qualifiers.



| Return code                                                                                                   | Description                                                                                                |
|---------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**HBA\_STATUS\_OK**</dt> </dl>                | Returned if all the mapping entries were retrieved. <br/>                                            |
| <dl> <dt>**HBA\_STATUS\_ERROR\_MORE\_DATA**</dt> </dl> | Returned if there was insufficient buffer space to retrieve all of the target mappings. <br/>        |
| <dl> <dt>**HBA\_STATUS\_ERROR**</dt> </dl>             | Returned if an unspecified error occurred that prevented the retrieval of the target mappings. <br/> |



 

## Requirements



|                            |                                                                                                        |
|----------------------------|--------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                     |
| Header<br/>          | <dl> <dt>Hbaapi.h (include Hbaapi.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Hbaapi.lib</dt> </dl>                  |
| DLL<br/>             | <dl> <dt>Hbaapi.dll</dt> </dl>                  |



## See also

<dl> <dt>

[**HBA\_FCPTargetMapping**](hba-fcptargetmapping.md)
</dt> <dt>

[**HBA\_OpenAdapter**](hba-openadapter.md)
</dt> <dt>

[HBA\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff557233)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HBA_GetFcpTargetMapping%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






