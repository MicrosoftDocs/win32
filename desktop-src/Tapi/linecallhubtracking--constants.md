---
description: The LINECALLHUBTRACKING\_ bit-flag constants describe the type of call hub tracking provided.
ms.assetid: ad3c8d2e-f074-4db0-bb72-fb2181cbf687
title: LINECALLHUBTRACKING_ Constants (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINECALLHUBTRACKING\_ Constants

The **LINECALLHUBTRACKING\_** bit-flag constants describe the type of call hub tracking provided.

<dl> <dt>

<span id="LINECALLHUBTRACKING_ALLCALLS"></span><span id="linecallhubtracking_allcalls"></span>**LINECALLHUBTRACKING\_ALLCALLS**
</dt> <dd> <dl> <dt>



Call hub tracking is provided at the call level.


</dt> </dl> </dd> <dt>

<span id="LINECALLHUBTRACKING_NONE"></span><span id="linecallhubtracking_none"></span>**LINECALLHUBTRACKING\_NONE**
</dt> <dd> <dl> <dt>



No call hub tracking is provided.


</dt> </dl> </dd> <dt>

<span id="LINECALLHUBTRACKING_PROVIDERLEVEL"></span><span id="linecallhubtracking_providerlevel"></span>**LINECALLHUBTRACKING\_PROVIDERLEVEL**
</dt> <dd> <dl> <dt>



Call hubs are tracked at the service provider level. Call by call changes are not reported.


</dt> </dl> </dd> </dl>

## Remarks

No extensibility. All 32 bits are reserved.

When changes occur in this data structure, a [**LINE\_CALLINFO**](line-callinfo.md) message is sent to the application. The parameters to this message are a handle to the call and an indication of the information item that has changed. The [**LINECALLHUBTRACKINGINFO**](/windows/desktop/api/Tapi/ns-tapi-linecallhubtrackinginfo) data structure indicates which tracking type is provided.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.2<br/>                                                      |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



## See also

<dl> <dt>

[**LINE\_CALLINFO**](line-callinfo.md)
</dt> <dt>

[**LINECALLHUBTRACKINGINFO**](/windows/desktop/api/Tapi/ns-tapi-linecallhubtrackinginfo)
</dt> <dt>

[**LINECALLINFO**](/windows/desktop/api/Tapi/ns-tapi-linecallinfo)
</dt> </dl>

 

 




