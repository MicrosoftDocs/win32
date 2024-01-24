---
description: The TAPI LINE\_APPNEWCALLHUB message is sent to inform an application when a new call hub has been created.
ms.assetid: cf693d95-9abb-4999-81b6-7d2aa06d0f58
title: LINE_APPNEWCALLHUB message (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINE\_APPNEWCALLHUB message

The TAPI **LINE\_APPNEWCALLHUB** message is sent to inform an application when a new call hub has been created.


```C++
            
```



## Parameters

<dl> <dt>

*hDevice* 
</dt> <dd>

A handle to the call.

</dd> <dt>

*dwCallbackInstance* 
</dt> <dd>

The callback instance supplied when opening the call's line.

</dd> <dt>

*dwParam1* 
</dt> <dd>

The tracking level on the new hub, as defined by one of the [**LINECALLHUBTRACKING\_ Constants**](linecallhubtracking--constants.md).

</dd> </dl>

## Return value

No return value.

## Remarks

This message originates with TAPI rather than with a service provider, so there is no corresponding TSPI message.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.2<br/>                                                      |
| Header<br/>       | <dl> <dt>Tapi.h</dt> </dl> |



 

 




