---
description: The LINE\_GROUPSTATUS message is sent when the status of an ACD group changes on an agent handler for which the application currently has an open line. This message is generated using the lineProxyMessage function.
ms.assetid: 1f3210fe-a7c8-4cfa-8e36-3a88e93d68bb
title: LINE_GROUPSTATUS message (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINE\_GROUPSTATUS message

The **LINE\_GROUPSTATUS** message is sent when the status of an ACD group changes on an agent handler for which the application currently has an open line. This message is generated using the [**lineProxyMessage**](/windows/desktop/api/Tapi/nf-tapi-lineproxymessage) function.


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

Reserved. Set to zero.

</dd> <dt>

*dwParam2* 
</dt> <dd>

Specifies the group status that has changed. The application can invoke [**lineGetGroupList**](/windows/desktop/api/Tapi/nf-tapi-linegetgrouplista) to determine the changes in available groups. The *dwParam2* parameter is one or more of the [**LINEGROUPSTATUS\_ constants**](linegroupstatus--constants.md).

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

[**lineGetGroupList**](/windows/desktop/api/Tapi/nf-tapi-linegetgrouplista)
</dt> </dl>

 

 




