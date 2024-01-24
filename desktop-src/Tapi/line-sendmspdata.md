---
description: The TSPI LINE\_SENDMSPDATA message is sent when the telephony service provider (TSP) wants to pass information to the media service provider (MSP).
ms.assetid: 982f40b3-7758-493c-9d04-6480e3c9e86d
title: LINE_SENDMSPDATA message (Tspi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# LINE\_SENDMSPDATA message

The TSPI **LINE\_SENDMSPDATA** message is sent when the telephony service provider (TSP) wants to pass information to the media service provider (MSP).


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

The value LINE\_SENDMSPDATA.

</dd> <dt>

*dwParam1* 
</dt> <dd>

Identifies the MSP that should receive the message. If 0, the message will be sent to all MSPs. This is the handle that is passed to the [**TSPI\_LineCreateMSPInstance**](/windows/win32/api/tspi/nf-tspi-tspi_linecreatemspinstance) function.

</dd> <dt>

*dwParam2* 
</dt> <dd>

The buffer to pass to the MSP. The buffer is not interpreted by TAPI.

</dd> <dt>

*dwParam3* 
</dt> <dd>

The size, in bytes, of the buffer in *dwParam2*.

</dd> </dl>

## Remarks

The service provider must negotiate a TAPI version 3.0 or later for this message to operate.

## Requirements



| Requirement | Value |
|-------------------------|-----------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 2.2<br/>                                                      |
| Header<br/>       | <dl> <dt>Tspi.h</dt> </dl> |



## See also

<dl> <dt>

[About The Media Service Provider (MSP)](./about-the-media-service-provider-msp-.md)
</dt> <dt>

[**TSPI\_lineMSPIdentify**](/windows/win32/api/tspi/nf-tspi-tspi_linemspidentify)
</dt> <dt>

[**TSPI\_LineCreateMSPInstance**](/windows/win32/api/tspi/nf-tspi-tspi_linecreatemspinstance)
</dt> <dt>

[**TSPI\_lineCloseMSPInstance**](/windows/win32/api/tspi/nf-tspi-tspi_lineclosemspinstance)
</dt> <dt>

[**TSPI\_lineRecieveMSPData**](/windows/win32/api/tspi/nf-tspi-tspi_linereceivemspdata)
</dt> <dt>

[**LINEDEVCAPS**](/windows/win32/api/tapi/ns-tapi-linedevcaps)
</dt> </dl>

 

