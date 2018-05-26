---
title: Windows Event Collector Data Types
description: The data types for the Windows Event Collector are used as event subscription object variable types, function parameter types, and function return types.
audience: developer
ms.assetid: b78bdaf8-e034-40fe-acf8-632313e4fd94
ms.prod: windows-server-dev
ms.technology: windows-event-collector
ms.tgt_platform: multiple
keywords:
- EC_HANDLE
- EC_OBJECT_ARRAY_PROPERTY_HANDLE
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Windows Event Collector Data Types

The data types for the Windows Event Collector are used as event subscription object variable types, function parameter types, and function return types.


```C++
typedef HANDLE EC_HANDLE;
typedef HANDLE EC_OBJECT_ARRAY_PROPERTY_HANDLE;
```



<dl> <dt>

**EC\_HANDLE**
</dt> <dd>

Handle to a subscription object. Used to represent an event collector subscription.

</dd> <dt>

**EC\_OBJECT\_ARRAY\_PROPERTY\_HANDLE**
</dt> <dd>

Handle to an array of property values for the event sources of a subscription. The array handle is returned by the [**EcGetSubscriptionProperty**](/windows/win32/Evcoll/nf-evcoll-ecgetsubscriptionproperty?branch=master) method when the **EcSubscriptionEventSources** value is passed into the *PropertyId* parameter.

</dd> </dl>

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                      |
| Header<br/>                   | <dl> <dt>Evcoll.h</dt> </dl> |



 

 





