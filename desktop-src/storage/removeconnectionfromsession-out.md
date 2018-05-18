---
title: RemoveConnectionFromSession\_OUT structure
description: The RemoveConnectionFromSession\_OUT structure holds the output data for the RemoveConnectionFromSession method, which is used to remove a connection from a session.
ms.assetid: '00c6c94e-06a8-40ec-8ddd-4a4191fa1ec6'
keywords: ["RemoveConnectionFromSession_OUT structure Storage Devices", "PRemoveConnectionFromSession_OUT structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- RemoveConnectionFromSession_OUT
api_location:
- iscsiop.h
api_type:
- HeaderDef
---

# RemoveConnectionFromSession\_OUT structure

The RemoveConnectionFromSession\_OUT structure holds the output data for the [RemoveConnectionFromSession](https://msdn.microsoft.com/library/windows/hardware/ff563973) method, which is used to remove a connection from a session.

## Syntax


```C++
typedef struct _RemoveConnectionFromSession_OUT {
  ULONG Status;
} RemoveConnectionFromSession_OUT, *PRemoveConnectionFromSession_OUT;
```



## Members

<dl> <dt>

**Status**
</dt> <dd>

This specifies the status of the [RemoveConnectionFromSession](https://msdn.microsoft.com/library/windows/hardware/ff563973) operation. For a list of status qualifiers, see [ISCSI\_STATUS\_QUALIFIERS](https://msdn.microsoft.com/library/windows/hardware/ff561568).

</dd> </dl>

## Remarks

You must implement this class.

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsiop.h (include Iscsiop.h)</dt> </dl> |



## See also

<dl> <dt>

[RemoveConnectionFromSession](https://msdn.microsoft.com/library/windows/hardware/ff563973)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20RemoveConnectionFromSession_OUT%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






