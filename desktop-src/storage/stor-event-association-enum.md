---
title: STOR\_EVENT\_ASSOCIATION\_ENUM enumeration
description: The STOR\_EVENT\_ASSOCIATION\_ENUM enumerator specifies the type of device that is associated with an event.
ms.assetid: 2e0672b6-e692-43c8-8a20-7947c854c4c9
keywords:
- STOR_EVENT_ASSOCIATION_ENUM enumeration Storage Devices
topic_type:
- apiref
api_name:
- STOR_EVENT_ASSOCIATION_ENUM
api_location:
- storport.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# STOR\_EVENT\_ASSOCIATION\_ENUM enumeration

The STOR\_EVENT\_ASSOCIATION\_ENUM enumerator specifies the type of device that is associated with an event.

## Syntax


```C++
typedef enum _STOR_EVENT_ASSOCIATION_ENUM { 
  StorEventAdapterAssociation  = 0,
  StorEventLunAssociation      = 1,
  StorEventTargetAssociation   = 2,
  StorEventInvalidAssociation  = 3
} STOR_EVENT_ASSOCIATION_ENUM;
```



## Constants

<dl> <dt>

<span id="StorEventAdapterAssociation"></span><span id="storeventadapterassociation"></span><span id="STOREVENTADAPTERASSOCIATION"></span>**StorEventAdapterAssociation**
</dt> <dd>

The event is associated with the adapter.

</dd> <dt>

<span id="StorEventLunAssociation"></span><span id="storeventlunassociation"></span><span id="STOREVENTLUNASSOCIATION"></span>**StorEventLunAssociation**
</dt> <dd>

The event is associated with the LUN.

</dd> <dt>

<span id="StorEventTargetAssociation"></span><span id="storeventtargetassociation"></span><span id="STOREVENTTARGETASSOCIATION"></span>**StorEventTargetAssociation**
</dt> <dd>

The event is associated with the target.

</dd> <dt>

<span id="StorEventInvalidAssociation"></span><span id="storeventinvalidassociation"></span><span id="STOREVENTINVALIDASSOCIATION"></span>**StorEventInvalidAssociation**
</dt> <dd>

Marks end of valid enumeration range

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Storport.h (include Storport.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STOR_EVENT_ASSOCIATION_ENUM%20enumeration%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





