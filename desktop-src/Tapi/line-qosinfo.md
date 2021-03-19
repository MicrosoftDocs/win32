---
description: The TSPI LINE\_QOSINFO message causes TAPI to fire a QOS event. See ITQOSEvent for additional information.
ms.assetid: b2844d12-c524-42ab-aeb9-8daf4e07a436
title: LINE_QOSINFO message (Tspi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINE\_QOSINFO message

The TSPI **LINE\_QOSINFO** message causes TAPI to fire a QOS event. See [**ITQOSEvent**](/windows/win32/api/tapi3if/nn-tapi3if-itqosevent) for additional information.


```C++
        
```



## Parameters

<dl> <dt>

*htLine* 
</dt> <dd>

The TAPI handle for the line.

</dd> <dt>

*htCall* 
</dt> <dd>

The TAPI handle for the call.

</dd> <dt>

*dwMsg* 
</dt> <dd>

The value LINE\_QOSINFO.

</dd> <dt>

*dwParam1* 
</dt> <dd>

A member of the [**QOS\_EVENT**](/windows/win32/api/tapi3if/ne-tapi3if-qos_event) enumerator that identifies the type of event.

</dd> <dt>

*dwParam2* 
</dt> <dd>

A [media type](./tapiprotocol--constants.md) constant that identifies the media of the call associated with this event.

</dd> <dt>

*dwParam3* 
</dt> <dd>

Unused.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.2<br/>                                                      |
| Header<br/>       | <dl> <dt>Tspi.h</dt> </dl> |



## See also

<dl> <dt>

[**QOS\_EVENT**](/windows/win32/api/tapi3if/ne-tapi3if-qos_event)
</dt> <dt>

[**ITQOSEvent**](/windows/win32/api/tapi3if/nn-tapi3if-itqosevent)
</dt> </dl>

 

