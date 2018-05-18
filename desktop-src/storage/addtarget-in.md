---
title: AddTarget\_IN structure
description: The AddPort\_IN structure is used by a WMI client to deliver the input parameter data of the AddTarget WMI method to the HBA miniport driver.
ms.assetid: '7c6a7ca8-83aa-41fe-92f5-6598464d9803'
keywords: ["AddTarget_IN structure Storage Devices", "PAddTarget_IN structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- AddTarget_IN
api_location:
- hbapiwmi.h
api_type:
- HeaderDef
---

# AddTarget\_IN structure

The AddPort\_IN structure is used by a WMI client to deliver the input parameter data of the [**AddTarget**](https://msdn.microsoft.com/library/windows/hardware/ff550136) WMI method to the HBA miniport driver.

## Syntax


```C++
typedef struct _AddTarget_IN {
  UCHAR HbaPortWWN[8];
  UCHAR DiscoveredPortWWN[8];
  ULONG AllTargets;
} AddTarget_IN, *PAddTarget_IN;
```



## Members

<dl> <dt>

**HbaPortWWN**
</dt> <dd>

Contains the worldwide name of the local port whose events the WMI client will receive.

</dd> <dt>

**DiscoveredPortWWN**
</dt> <dd>

Contains a worldwide name that specifies the discovered target whose events the WMI client will receive.

</dd> <dt>

**AllTargets**
</dt> <dd>

Indicates the scope of the target events to report. If this member is zero, the WMI client will receive events associated with the port that is indicated by *DiscoveredPortWWN*. If this member is nonzero, the WMI client will all events associated with all currently discovered targets as well as targets that are discovered in the future.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbapiwmi.h (include Hbapiwmi.h)</dt> </dl> |



## See also

<dl> <dt>

[**AddTarget**](https://msdn.microsoft.com/library/windows/hardware/ff550136)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20AddTarget_IN%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






