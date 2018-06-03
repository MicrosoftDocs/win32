---
title: OnControlLevelChangeResponse event
description: Called in response to a viewer requesting control.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: E190DAEC-776A-4248-8A73-073AB6F2FE8A
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
keywords:
- OnControlLevelChangeResponse event RDP
topic_type:
- apiref
api_name:
- OnControlLevelChangeResponse
api_location:
- RdpEncom.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# OnControlLevelChangeResponse event

Called in response to a viewer requesting control.

## Syntax


```C++
void OnControlLevelChangeResponse(
  [in] IDispatch  *pAttendee,
  [in] CTRL_LEVEL RequestedLevel,
       long       ReasonCode
);
```



## Parameters

<dl> <dt>

*pAttendee* \[in\]
</dt> <dd>

Attendee that requests control. Query the **IDispatch** interface for the [**IRDPSRAPIAttendee**](/windows/desktop/api/RdpEncomAPI/nn-rdpencomapi-irdpsrapiattendee) interface that you use to retrieve information about the attendee.

</dd> <dt>

*RequestedLevel* \[in\]
</dt> <dd>

Level of control requested by the attendee. For possible values, see the [**CTRL\_LEVEL**](/windows/desktop/api/Rdpencomapi/ne-rdpencomapi-__midl___midl_itf_rdpencomapi_0000_0000_0001) enumeration.

</dd> <dt>

*ReasonCode* 
</dt> <dd>

The reason for the request.

</dd> </dl>

## Return value

This event does not return a value.

## Requirements



|                                     |                                                                                            |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                             |
| Header<br/>                   | <dl> <dt>RdpEncomAPI.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>RdpEncomAPI.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>RdpEncomAPI.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RdpEncom.dll</dt> </dl>    |



## See also

<dl> <dt>

[**\_IRDPSessionEvents**](/windows/desktop/api/RdpEncomAPI/)
</dt> <dt>

[**SendControlLevelChangeResponse**](/windows/desktop/api/RdpEncomAPI/nf-rdpencomapi-irdpsrapisharingsession2-sendcontrollevelchangeresponse)
</dt> </dl>

 

 





