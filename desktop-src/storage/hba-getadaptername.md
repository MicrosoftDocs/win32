---
title: HBA\_GetAdapterName routine
description: The HBA\_GetAdapterName routine retrieves the text string that identifies the HBA name that corresponds to the indicated adapter index.
ms.assetid: 'ec17efca-2cb9-4ab4-b98f-7319f6145e4e'
keywords: ["HBA_GetAdapterName routine Storage Devices"]
topic_type:
- apiref
api_name:
- HBA_GetAdapterName
api_location:
- Hbaapi.dll
api_type:
- DllExport
---

# HBA\_GetAdapterName routine

The **HBA\_GetAdapterName** routine retrieves the text string that identifies the HBA name that corresponds to the indicated adapter index.

## Syntax


```C++
HBA_STATUS HBA_API HBA_GetAdapterName(
  _In_    HBA_UINT32 AdapterIndex,
  _Inout_ PCHAR      AdapterName
);
```



## Parameters

<dl> <dt>

*AdapterIndex* \[in\]
</dt> <dd>

Indicates the index of the HBA for which the name will be returned.

</dd> <dt>

*AdapterName* \[in, out\]
</dt> <dd>

Pointer to memory area in which the HBA name will be returned. The HBA name will be a string of the form


```
mfgdomain-model-adapterindex
```



where **mfgdomain** is derived from the domain name owned by the manufacturer of the HBA, **model** is a vendor-specific identifier of the HBA product model, and **adapterindex** is a decimal representation of the HBA index in *AdapterIndex.* For example:


```
com.HotBiscuitsAdapters-HBA1040A-1
```



For a description of the formatting of the adapter name, see the *Fibre Channel HBA API* specification published by the T11 committee.

</dd> </dl>

## Return value

The **HBA\_GetAdapterName** routine returns a value of type [HBA\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff557233) that indicates the status of the HBA.

## Requirements



|                            |                                                                                                        |
|----------------------------|--------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                     |
| Header<br/>          | <dl> <dt>Hbaapi.h (include Hbaapi.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Hbaapi.lib</dt> </dl>                  |
| DLL<br/>             | <dl> <dt>Hbaapi.dll</dt> </dl>                  |



## See also

<dl> <dt>

[**HBA\_AdapterAttributes**](hba-adapterattributes.md)
</dt> <dt>

[**HBA\_OpenAdapter**](hba-openadapter.md)
</dt> <dt>

[HBA\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff557233)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HBA_GetAdapterName%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






