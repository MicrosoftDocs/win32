---
title: HBA\_OpenAdapterByWWN routine
description: The HBA\_OpenAdapterByWWN routine opens the HBA that is associated with either a node or a port that has the indicated name.
ms.assetid: 62492c9b-ace0-48be-ae8b-bb681dbca8b7
keywords:
- HBA_OpenAdapterByWWN routine Storage Devices
topic_type:
- apiref
api_name:
- HBA_OpenAdapterByWWN
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

# HBA\_OpenAdapterByWWN routine

The **HBA\_OpenAdapterByWWN** routine opens the HBA that is associated with either a node or a port that has the indicated name.

## Syntax


```C++
HBA_STATUS HBA_API HBA_OpenAdapterByWWN(
  _Out_ HBA_HANDLE *HbaHandle,
  _In_  HBA_WWN    Wwn
);
```



## Parameters

<dl> <dt>

*HbaHandle* \[out\]
</dt> <dd>

Contains, on output, a handle that identifies the HBA.

</dd> <dt>

*Wwn* \[in\]
</dt> <dd>

Contains a 64-bit worldwide name (WWN) that must either match the name of the node on which the HBA is located, or must match the name of a port on the HBA. For a discussion of worldwide names, see the T11 committee's *Fibre Channel HBA API* specification.

</dd> </dl>

## Return value

The **HBA\_OpenAdapterByWWN** routine returns a value of type [HBA\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff557233) that indicates the status of the HBA. In particular, **HBA\_OpenAdapterByWWN** returns one of the following qualifiers.



| Return code                                                                                                       | Description                                                                                                                                                                       |
|-------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**HBA\_STATUS\_OK**</dt> </dl>                    | Returned if **HBA\_OpenAdapterByWWN** successfully returns a valid handle. <br/>                                                                                            |
| <dl> <dt>**HBA\_STATUS\_ERROR\_ILLEGAL\_WWN**</dt> </dl>   | Returned if there is no HBA that has a port name or node name that matches *Wwn*.<br/>                                                                                      |
| <dl> <dt>**HBA\_STATUS\_ERROR\_AMBIGUOUS\_WWN**</dt> </dl> | Returned if multiple adapters have associated port or node names that match *Wwn*. This can occur if two or more adapters are associated with nodes of the same name. <br/> |
| <dl> <dt>**HBA\_STATUS\_ERROR**</dt> </dl>                 | Returned if an unspecified error occurred that prevented the opening of the adapter. <br/>                                                                                  |



 

## Requirements



|                            |                                                                                                        |
|----------------------------|--------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                     |
| Header<br/>          | <dl> <dt>Hbaapi.h (include Hbaapi.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Hbaapi.lib</dt> </dl>                  |
| DLL<br/>             | <dl> <dt>Hbaapi.dll</dt> </dl>                  |



## See also

<dl> <dt>

[HBA\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff557233)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HBA_OpenAdapterByWWN%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






