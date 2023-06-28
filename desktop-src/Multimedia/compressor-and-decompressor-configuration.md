---
title: Compressor and Decompressor Configuration
description: Compressor and Decompressor Configuration
ms.assetid: 677241d2-3ddd-423a-a1e7-b5fa3ce0a4eb
keywords:
- video compression manager (VCM),configuring compressors
- VCM (video compression manager),configuring compressors
- ICM_CONFIGURE message
- ICQueryConfigure macro
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Compressor and Decompressor Configuration

\[The feature associated with this page, [Video Compression Manager](/windows/win32/multimedia/video-compression-manager), is a legacy feature. Microsoft strongly recommends that new code does not use this feature.\]

Your application can configure the compressor or decompressor automatically, or it can allow the user to configure them. If it is practical, allow the user to configure the compressor or decompressor; this frees you from considering all the options for the compressor or decompressor.

The user can configure the compressor or decompressor by using a configuration dialog box. You can send the [**ICM\_CONFIGURE**](icm-configure.md) message to VCM (or use the [**ICQueryConfigure**](/windows/desktop/api/Vfw/nf-vfw-icqueryconfigure) macro) to determine if a compressor or decompressor can display a configuration dialog box. If so, send the ICM\_CONFIGURE message (or use the [**ICConfigure**](/windows/desktop/api/Vfw/nf-vfw-icconfigure) macro) to display it.

Your application can send the [**ICM\_GETSTATE**](icm-getstate.md) and [**ICM\_SETSTATE**](icm-setstate.md) messages (or use the [**ICGetStateSize**](/windows/desktop/api/Vfw/nf-vfw-icgetstatesize), [**ICGetState**](/windows/desktop/api/Vfw/nf-vfw-icgetstate), and [**ICSetState**](/windows/desktop/api/Vfw/nf-vfw-icsetstate) macros) to get and set the status for a compressor or decompressor. If your application creates or modifies the status, it must obtain the layout of the compressor or decompressor data before restoring its status. Alternatively, if your application obtains the status from a compressor or decompressor and uses it to restore the status in a subsequent session, it must ensure that it restores only status information obtained from the compressor or decompressor it is currently using.

 

 




