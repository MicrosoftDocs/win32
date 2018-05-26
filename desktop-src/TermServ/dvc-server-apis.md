---
title: DVC Server APIs
description: The dynamic virtual channel (DVC) server APIs are implemented by the Remote Desktop Connection (RDC) server of the connection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9743ce32-9262-4af3-b013-668e834e279c
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
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

-   The server API has been extended with an additional call which opens a dynamic virtual channel (DVC). The additional call is made using the [**WTSVirtualChannelOpenEx**](/windows/win32/Wtsapi32/nf-wtsapi32-wtsvirtualchannelopenex?branch=master) function.
-   [**WTSVirtualChannelRead**](/windows/win32/Wtsapi32/nf-wtsapi32-wtsvirtualchannelread?branch=master)

    When using this API with DVC, it will always prepend the data read with [**CHANNEL\_PDU\_HEADER**](/windows/win32/Pchannel/ns-pchannel-tagchannel_pdu_header?branch=master). This means that any read must be done with at least the **CHANNEL\_PDU\_LENGTH** data block passed as the input buffer.

-   [**ReadFile**](https://msdn.microsoft.com/library/windows/desktop/aa365467)

    If the file handle to the DVC is retrieved by calling [**WTSVirtualChannelQuery**](/windows/win32/Wtsapi32/nf-wtsapi32-wtsvirtualchannelquery?branch=master) with parameter *WTSVirtualFileHandle*, the same rule will apply. All reads will include the [**CHANNEL\_PDU\_HEADER**](/windows/win32/Pchannel/ns-pchannel-tagchannel_pdu_header?branch=master), and the read buffer has to be at least **CHANNEL\_PDU\_LENGTH** size.

 

 




