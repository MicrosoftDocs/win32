---
description: The TAPI LINE\_CALLHUBCLOSE message is sent when a call hub has been closed.
ms.assetid: 738dcb20-99b5-44fe-8ad9-b14b8d977f53
title: LINE_CALLHUBCLOSE message (Tapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINE\_CALLHUBCLOSE message

The TAPI **LINE\_CALLHUBCLOSE** message is sent when a call hub has been closed.


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

Reserved. Set to 0.

</dd> <dt>

*dwParam2* 
</dt> <dd>

Reserved. Set to 0.

</dd> <dt>

*dwParam3* 
</dt> <dd>

Reserved. Set to 0.

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



 

 




