---
description: The service providers which support the out-of-band data (OOB) abstraction for the stream-style sockets must adhere to the semantics in this section.
ms.assetid: 83ed881f-8474-445e-8fb5-9635138a63dd
title: Out-of-Band Data in the SPI
ms.topic: article
ms.date: 05/31/2018
---

# Out-of-Band Data in the SPI

The service providers which support the out-of-band data (OOB) abstraction for the stream-style sockets must adhere to the semantics in this section. We will describe OOB data handling in a protocol-independent manner. Please refer to the [Winsock Annexes](winsock-annexes.md) for a discussion of OOB data implemented using urgent data in TCP/IP service providers. In the following, the use of [**WSPRecv**](/previous-versions/windows/hardware/network/ff566309(v=vs.85)) also applies to [**WSPRecvFrom**](/previous-versions/windows/desktop/legacy/ms742287(v=vs.85)).

 

 
