---
title: GetPersistentBinding2\_OUT structure
description: The GetBindingSupport\_OUT structure is used to report the output parameter data of the GetPersistentBinding2 WMI method to the WMI client.
ms.assetid: '883a7a56-ecb9-428f-a15a-ba428a626bed'
keywords: ["GetPersistentBinding2_OUT structure Storage Devices", "PGetPersistentBinding2_OUT structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- GetPersistentBinding2_OUT
api_location:
- hbapiwmi.h
api_type:
- HeaderDef
---

# GetPersistentBinding2\_OUT structure

The GetBindingSupport\_OUT structure is used to report the output parameter data of the [**GetPersistentBinding2**](https://msdn.microsoft.com/library/windows/hardware/ff554959) WMI method to the WMI client.

## Syntax


```C++
typedef struct _GetPersistentBinding2_OUT {
  ULONG               HBAStatus;
  ULONG               TotalEntryCount;
  ULONG               OutEntryCount;
  HBAFCPBindingEntry2 Bindings[1];
} GetPersistentBinding2_OUT, *PGetPersistentBinding2_OUT;
```



## Members

<dl> <dt>

**HBAStatus**
</dt> <dd>

Contains the status of the operation. For a list of allowed values and their descriptions, see [HBA\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff557233).

</dd> <dt>

**TotalEntryCount**
</dt> <dd>

Indicates the number of binding entries that the WMI provider can report.

</dd> <dt>

**OutEntryCount**
</dt> <dd>

Indicates the total number of persistent bindings retrieved by the GetPersistentBinding2 method.

</dd> <dt>

**Bindings**
</dt> <dd>

Contains an array of structures of type [**HBAFCPBindingEntry2**](hbafcpbindingentry2.md) that describe an HBA's bindings between operating system and fibre channel protocol (FCP) identifiers.

</dd> </dl>

## Remarks

The WMI tool suite generates a declaration of the GetPersistentBinding2\_OUT structure in *Hbapiwmi.h* when it compiles the [MSFC\_HBAFCPInfo WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff562509).

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbapiwmi.h (include Hbapiwmi.h)</dt> </dl> |



## See also

<dl> <dt>

[**GetPersistentBinding2**](https://msdn.microsoft.com/library/windows/hardware/ff554959)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20GetPersistentBinding2_OUT%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






