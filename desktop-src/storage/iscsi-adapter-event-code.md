---
title: ISCSI\_ADAPTER\_EVENT\_CODE enumeration
description: The ISCSI\_ADAPTER\_EVENT\_CODE enumeration indicates the type of adapter event.
ms.assetid: '65fa2307-8d71-4c83-86b3-a965bd7f3da8'
keywords: ["ISCSI_ADAPTER_EVENT_CODE enumeration Storage Devices", "PISCSI_ADAPTER_EVENT_CODE enumeration pointer Storage Devices"]
topic_type:
- apiref
api_name:
- ISCSI_ADAPTER_EVENT_CODE
api_location:
- iscsiop.h
api_type:
- HeaderDef
---

# ISCSI\_ADAPTER\_EVENT\_CODE enumeration

The ISCSI\_ADAPTER\_EVENT\_CODE enumeration indicates the type of adapter event.

## Syntax


```C++
typedef enum  { 
  ISCSI_ADAPTER_TARGETS_CHANGED  = 3
} ISCSI_ADAPTER_EVENT_CODE, *PISCSI_ADAPTER_EVENT_CODE;
```



## Constants

<dl> <dt>

<span id="ISCSI_ADAPTER_TARGETS_CHANGED"></span><span id="iscsi_adapter_targets_changed"></span>**ISCSI\_ADAPTER\_TARGETS\_CHANGED**
</dt> <dd>

An adapter discovered that its list of targets changed.

</dd> </dl>

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsiop.h (include Iscsiop.h)</dt> </dl> |



## See also

<dl> <dt>

[MSiSCSI\_AdapterEvent WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff562971)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ISCSI_ADAPTER_EVENT_CODE%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






