---
description: The LINE\_QUEUESTATUS message is sent when the status of an ACD queue changes on an agent handler for which the application currently has an open line. This message is generated using the lineProxyMessage function.
ms.assetid: 9baacfc5-f26c-41c7-a1f8-f48ec8aa844c
title: LINE_QUEUESTATUS message (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINE\_QUEUESTATUS message

The **LINE\_QUEUESTATUS** message is sent when the status of an ACD queue changes on an agent handler for which the application currently has an open line. This message is generated using the [**lineProxyMessage**](/windows/desktop/api/Tapi/nf-tapi-lineproxymessage) function.


```C++
        
```



## Parameters

<dl> <dt>

*dwDevice* 
</dt> <dd>

The application's handle to the line device. This relates to the agent handler.

</dd> <dt>

*dwCallbackInstance* 
</dt> <dd>

The callback instance supplied when opening the line.

</dd> <dt>

*dwParam1* 
</dt> <dd>

The identifier of the queue whose status has changed.

</dd> <dt>

*dwParam2* 
</dt> <dd>

Specifies the queue status that has changed. Can be one or more of the [**LINEQUEUESTATUS\_ constants**](linequeuestatus--constants.md).

</dd> <dt>

*dwParam3* 
</dt> <dd>

Reserved. Set to zero.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.2<br/>                                                      |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



## See also

<dl> <dt>

[**lineProxyMessage**](/windows/desktop/api/Tapi/nf-tapi-lineproxymessage)
</dt> </dl>

 

 




