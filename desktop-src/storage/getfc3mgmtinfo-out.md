---
title: GetFC3MgmtInfo\_OUT structure
description: The GetFC3MgmtInfo\_OUT structure is used to report the output parameter data of the GetFC3MgmtInfo WMI method to the WMI client.
ms.assetid: '5cce25e7-582b-49b3-9f10-be59471e377f'
keywords: ["GetFC3MgmtInfo_OUT structure Storage Devices", "PGetFC3MgmtInfo_OUT structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- GetFC3MgmtInfo_OUT
api_location:
- hbapiwmi.h
api_type:
- HeaderDef
---

# GetFC3MgmtInfo\_OUT structure

The GetFC3MgmtInfo\_OUT structure is used to report the output parameter data of the [**GetFC3MgmtInfo**](https://msdn.microsoft.com/library/windows/hardware/ff553939) WMI method to the WMI client.

## Syntax


```C++
typedef struct _GetFC3MgmtInfo_OUT {
  ULONG          HBAStatus;
  HBAFC3MgmtInfo MgmtInfo;
} GetFC3MgmtInfo_OUT, *PGetFC3MgmtInfo_OUT;
```



## Members

<dl> <dt>

**HBAStatus**
</dt> <dd>

Contains a value associated with the WMI class qualifier [HBA\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff557233) that indicates the result of an HBA query operation.

</dd> <dt>

**MgmtInfo**
</dt> <dd>

Contains a structure of type [**HBAFC3MgmtInfo**](hbafc3mgmtinfo.md) that reports FC3 management information.

</dd> </dl>

## Remarks

The [**GetFC3MgmtInfo**](https://msdn.microsoft.com/library/windows/hardware/ff553939) method reports fibre channel-3 management information.

The WMI tool suite generates a declaration of the GetEventBuffer\_OUT structure in *Hbapiwmi.h* when it compiles the [MSFC\_HBAAdapterMethods WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff562506).

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbapiwmi.h (include Hbapiwmi.h)</dt> </dl> |



## See also

<dl> <dt>

[**GetFC3MgmtInfo**](https://msdn.microsoft.com/library/windows/hardware/ff553939)
</dt> <dt>

[HBA\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff557233)
</dt> <dt>

[**HBAFC3MgmtInfo**](hbafc3mgmtinfo.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20GetFC3MgmtInfo_OUT%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






