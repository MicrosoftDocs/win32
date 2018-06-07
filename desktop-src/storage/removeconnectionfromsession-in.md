---
title: RemoveConnectionFromSession\_IN structure
description: The RemoveConnectionFromSession\_IN structure holds the input data for the RemoveConnectionFromSession method, which is used to remove a connection from a session.
ms.assetid: dd5fd1f2-7040-40ee-bf9c-42e77c9738da
keywords:
- RemoveConnectionFromSession_IN structure Storage Devices
- PRemoveConnectionFromSession_IN structure pointer Storage Devices
topic_type:
- apiref
api_name:
- RemoveConnectionFromSession_IN
api_location:
- iscsiop.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# RemoveConnectionFromSession\_IN structure

The RemoveConnectionFromSession\_IN structure holds the input data for the [RemoveConnectionFromSession](https://msdn.microsoft.com/library/windows/hardware/ff563973) method, which is used to remove a connection from a session.

## Syntax


```C++
typedef struct _RemoveConnectionFromSession_IN {
  ULONGLONG UniqueSessionId;
  ULONGLONG UniqueConnectionId;
} RemoveConnectionFromSession_IN, *PRemoveConnectionFromSession_IN;
```



## Members

<dl> <dt>

**UniqueSessionId**
</dt> <dd>

A 64-bit integer that uniquely identifies the session. The [LoginToTarget](https://msdn.microsoft.com/library/windows/hardware/ff561599) and [AddConnectionToSession](https://msdn.microsoft.com/library/windows/hardware/ff550121) methods both return this value in their *UniqueSessionId* parameter. Do not confuse this value with the values in the ISID and TSID members.

</dd> <dt>

**UniqueConnectionId**
</dt> <dd>

A 64-bit integer that uniquely identifies the connection. Do not confuse this value with the connection ID (CID).

</dd> </dl>

## Remarks

You must implement this class.

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsiop.h (include Iscsiop.h)</dt> </dl> |



## See also

<dl> <dt>

[AddConnectionToSession](https://msdn.microsoft.com/library/windows/hardware/ff550121)
</dt> <dt>

[LoginToTarget](https://msdn.microsoft.com/library/windows/hardware/ff561599)
</dt> <dt>

[RemoveConnectionFromSession](https://msdn.microsoft.com/library/windows/hardware/ff563973)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20RemoveConnectionFromSession_IN%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






