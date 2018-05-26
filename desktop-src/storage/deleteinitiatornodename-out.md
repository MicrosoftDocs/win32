---
title: DeleteInitiatorNodeName\_OUT structure
description: The DeleteInitiatorNodeName\_OUT structure holds the output data for the DeleteInitiatorNodeName method.
ms.assetid: 105f6687-ea0f-45e9-be44-eafdd06156eb
keywords:
- DeleteInitiatorNodeName_OUT structure Storage Devices
- PDeleteInitiatorNodeName_OUT structure pointer Storage Devices
topic_type:
- apiref
api_name:
- DeleteInitiatorNodeName_OUT
api_location:
- iscsiop.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DeleteInitiatorNodeName\_OUT structure

The DeleteInitiatorNodeName\_OUT structure holds the output data for the [DeleteInitiatorNodeName](https://msdn.microsoft.com/library/windows/hardware/ff552500) method.

## Syntax


```C++
typedef struct _DeleteInitiatorNodeName_OUT {
  ULONG Status;
} DeleteInitiatorNodeName_OUT, *PDeleteInitiatorNodeName_OUT;
```



## Members

<dl> <dt>

**Status**
</dt> <dd>

The status of the **DeleteInitiatorNodeName** operation. For a list of status qualifiers, see [ISCSI\_STATUS\_QUALIFIERS](https://msdn.microsoft.com/library/windows/hardware/ff561568).

</dd> </dl>

## Remarks

It is optional that you implement this method.

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsiop.h (include Iscsiop.h)</dt> </dl> |



## See also

<dl> <dt>

[DeleteInitiatorNodeName](https://msdn.microsoft.com/library/windows/hardware/ff552500)
</dt> <dt>

[**DeleteInitiatorNodeName\_IN**](deleteinitiatornodename-in.md)
</dt> <dt>

[ISCSI\_STATUS\_QUALIFIERS](https://msdn.microsoft.com/library/windows/hardware/ff561568)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20DeleteInitiatorNodeName_OUT%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






