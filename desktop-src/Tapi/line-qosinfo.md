---
Description: The TSPI LINE\_QOSINFO message causes TAPI to fire a QOS event. See ITQOSEvent for additional information.
ms.assetid: b2844d12-c524-42ab-aeb9-8daf4e07a436
title: LINE\_QOSINFO message
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# LINE\_QOSINFO message

The TSPI **LINE\_QOSINFO** message causes TAPI to fire a QOS event. See [**ITQOSEvent**](https://msdn.microsoft.com/en-us/library/ms731442(v=VS.85).aspx) for additional information.


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

A member of the [**QOS\_EVENT**](https://msdn.microsoft.com/en-us/library/ms734166(v=VS.85).aspx) enumerator that identifies the type of event.

</dd> <dt>

*dwParam2* 
</dt> <dd>

A [media type](https://msdn.microsoft.com/en-us/library/ms734212(v=VS.85).aspx) constant that identifies the media of the call associated with this event.

</dd> <dt>

*dwParam3* 
</dt> <dd>

Unused.

</dd> </dl>

## Requirements



|                         |                                                                                   |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.2<br/>                                                      |
| Header<br/>       | <dl> <dt>Tspi.h</dt> </dl> |



## See also

<dl> <dt>

[**QOS\_EVENT**](https://msdn.microsoft.com/en-us/library/ms734166(v=VS.85).aspx)
</dt> <dt>

[**ITQOSEvent**](https://msdn.microsoft.com/en-us/library/ms731442(v=VS.85).aspx)
</dt> </dl>

 

 




