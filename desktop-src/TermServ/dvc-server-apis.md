---
title: DVC Server APIs
description: The dynamic virtual channel (DVC) server APIs are implemented by the Remote Desktop Connection (RDC) server of the connection.
ms.assetid: 9743ce32-9262-4af3-b013-668e834e279c
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# DVC Server APIs

The dynamic virtual channel (DVC) server APIs are implemented by the Remote Desktop Connection (RDC) server of the connection.

## In this section

<dl> <dt>

[**IWTSServerChannel**](iwtsserverchannel.md)
</dt> <dd>

This interface is not supported.

</dd> <dt>

[**IWTSServerChannelManager**](iwtsserverchannelmanager.md)
</dt> <dd>

This interface is not supported.

</dd> <dt>

[**TPriority**](tpriority.md)
</dt> <dd>

This enumeration is not used.

</dd> </dl>

## Changes in Behavior for Other Server APIs

-   The server API has been extended with an additional call which opens a dynamic virtual channel (DVC). The additional call is made using the [**WTSVirtualChannelOpenEx**](/windows/desktop/api/Wtsapi32/nf-wtsapi32-wtsvirtualchannelopenex) function.
-   [**WTSVirtualChannelRead**](/windows/desktop/api/Wtsapi32/nf-wtsapi32-wtsvirtualchannelread)

    When using this API with DVC, it will always prepend the data read with [**CHANNEL\_PDU\_HEADER**](/windows/win32/api/pchannel/ns-pchannel-channel_pdu_header). This means that any read must be done with at least the **CHANNEL\_PDU\_LENGTH** data block passed as the input buffer.

-   [**ReadFile**](/windows/desktop/api/fileapi/nf-fileapi-readfile)

    If the file handle to the DVC is retrieved by calling [**WTSVirtualChannelQuery**](/windows/desktop/api/Wtsapi32/nf-wtsapi32-wtsvirtualchannelquery) with parameter *WTSVirtualFileHandle*, the same rule will apply. All reads will include the [**CHANNEL\_PDU\_HEADER**](/windows/win32/api/pchannel/ns-pchannel-channel_pdu_header), and the read buffer has to be at least **CHANNEL\_PDU\_LENGTH** size.

 

 