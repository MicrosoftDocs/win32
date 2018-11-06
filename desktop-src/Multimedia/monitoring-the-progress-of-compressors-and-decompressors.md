---
title: Monitoring the Progress of Compressors and Decompressors
description: Monitoring the Progress of Compressors and Decompressors
ms.assetid: 6507be44-1916-46b2-bae3-c4fe633cdc5a
keywords:
- video compression manager (VCM),monitoring
- VCM (video compression manager),monitoring
- ICSetStatusProc function
ms.topic: article
ms.date: 05/31/2018
---

# Monitoring the Progress of Compressors and Decompressors

Your application can monitor the progress of a lengthy operation performed by a compressor or decompressor by sending it the address of a callback function. You can use the [**ICSetStatusProc**](/windows/desktop/api/Vfw/nf-vfw-icsetstatusproc) function to send the address to the compressor or decompressor. When the compressor or decompressor receives this address, it sends status messages to the function. These messages indicate whether the operation is starting, stopping, yielding, or proceeding.

 

 




