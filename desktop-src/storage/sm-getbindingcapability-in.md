---
title: SM\_GetBindingCapability\_IN structure
description: The SM\_GetBindingCapability\_IN structure is used to provide input parameters to the SM\_GetBindingCapability method.
ms.assetid: 9b2d471a-649e-4289-a27a-b78893d8477b
keywords:
- SM_GetBindingCapability_IN structure Storage Devices
- PSM_GetBindingCapability_IN structure pointer Storage Devices
topic_type:
- apiref
api_name:
- SM_GetBindingCapability_IN
api_location:
- hbapiwmi.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# SM\_GetBindingCapability\_IN structure

The SM\_GetBindingCapability\_IN structure is used to provide input parameters to the SM\_GetBindingCapability method.

## Syntax


```C++
typedef struct _SM_GetBindingCapability_IN {
  UCHAR HbaPortWWN[8];
  UCHAR DomainPortWWN[8];
} SM_GetBindingCapability_IN, *PSM_GetBindingCapability_IN;
```



## Members

<dl> <dt>

**HbaPortWWN**
</dt> <dd>

The worldwide name (WWN) of the local port whose events the WMI client will receive.

</dd> <dt>

**DomainPortWWN**
</dt> <dd>

A worldwide name (WWN) that specifies the SAS domain worldwide name of the local port.

</dd> </dl>

## Remarks

The WMI tool suite generates a declaration of the SM\_GetBindingCapability\_IN structure in *Hbapiwmi.h* when it compiles the SM\_TargetInformationMethod WMI class.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbapiwmi.h (include Hbapiwmi.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20SM_GetBindingCapability_IN%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





