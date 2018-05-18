---
title: DeleteInitiatorNodeName\_IN structure
description: The DeleteInitiatorNodeName\_IN structure holds the input data for the DeleteInitiatorNodeName method, which is used to delete an initiator node name.
ms.assetid: '10b6660c-7f48-4717-89d4-d6a5eb6594c8'
keywords: ["DeleteInitiatorNodeName_IN structure Storage Devices", "PDeleteInitiatorNodeName_IN structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- DeleteInitiatorNodeName_IN
api_location:
- iscsiop.h
api_type:
- HeaderDef
---

# DeleteInitiatorNodeName\_IN structure

The DeleteInitiatorNodeName\_IN structure holds the input data for the [DeleteInitiatorNodeName](https://msdn.microsoft.com/library/windows/hardware/ff552500) method, which is used to delete an initiator node name.

## Syntax


```C++
typedef struct _DeleteInitiatorNodeName_IN {
  WCHAR DeletedInitiatorName[223 + 1];
} DeleteInitiatorNodeName_IN, *PDeleteInitiatorNodeName_IN;
```



## Members

<dl> <dt>

**DeletedInitiatorName**
</dt> <dd>

The iSCSI initiator node name that is to be deleted.

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

[**DeleteInitiatorNodeName\_OUT**](deleteinitiatornodename-out.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20DeleteInitiatorNodeName_IN%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






