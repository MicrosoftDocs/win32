---
title: ReportDiscoveredTargets\_OUT structure
description: The ReportDiscoveredTargets\_OUT structure holds the output data for the ReportDiscoveredTargets method.
ms.assetid: 'cecef33a-a192-41f4-8006-b5d8b8c73e8d'
keywords: ["ReportDiscoveredTargets_OUT structure Storage Devices", "PReportDiscoveredTargets_OUT structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- ReportDiscoveredTargets_OUT
api_location:
- iscsifnd.h
api_type:
- HeaderDef
---

# ReportDiscoveredTargets\_OUT structure

The ReportDiscoveredTargets\_OUT structure holds the output data for the [ReportDiscoveredTargets](https://msdn.microsoft.com/library/windows/hardware/ff564046) method.

## Syntax


```C++
typedef struct _ReportDiscoveredTargets_OUT {
  ULONG                  Status;
  ULONG                  TargetCount;
  ISCSI_DiscoveredTarget Targets[1];
} ReportDiscoveredTargets_OUT, *PReportDiscoveredTargets_OUT;
```



## Members

<dl> <dt>

**Status**
</dt> <dd>

On output, the status of the **ReportDiscoveredTargets** operation. For a list of status qualifiers, see [ISCSI\_STATUS\_QUALIFIERS](https://msdn.microsoft.com/library/windows/hardware/ff561568).

</dd> <dt>

**TargetCount**
</dt> <dd>

On output, the number of targets that are discovered.

</dd> <dt>

**Targets**
</dt> <dd>

On output, an array of [**ISCSI\_DiscoveredTarget**](iscsi-discoveredtarget.md) structures, which provide information that is related to discovered targets.

</dd> </dl>

## Remarks

You must implement this method.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsifnd.h (include Iscsifnd.h)</dt> </dl> |



## See also

<dl> <dt>

[**ISCSI\_DiscoveredTarget**](iscsi-discoveredtarget.md)
</dt> <dt>

[ISCSI\_STATUS\_QUALIFIERS](https://msdn.microsoft.com/library/windows/hardware/ff561568)
</dt> <dt>

[ReportDiscoveredTargets](https://msdn.microsoft.com/library/windows/hardware/ff564046)
</dt> <dt>

[**ReportDiscoveredTargets2\_OUT**](reportdiscoveredtargets2-out.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ReportDiscoveredTargets_OUT%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






