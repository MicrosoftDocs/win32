---
title: Compressor and Decompressor Configuration
description: Compressor and Decompressor Configuration
ms.assetid: 677241d2-3ddd-423a-a1e7-b5fa3ce0a4eb
keywords:
- video compression manager (VCM),configuring compressors
- VCM (video compression manager),configuring compressors
- ICM_CONFIGURE message
- ICQueryConfigure macro
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Compressor and Decompressor Configuration

Your application can configure the compressor or decompressor automatically, or it can allow the user to configure them. If it is practical, allow the user to configure the compressor or decompressor; this frees you from considering all the options for the compressor or decompressor.

The user can configure the compressor or decompressor by using a configuration dialog box. You can send the [**ICM\_CONFIGURE**](icm-configure.md) message to VCM (or use the [**ICQueryConfigure**](/windows/win32/Vfw/nf-vfw-icqueryconfigure?branch=master) macro) to determine if a compressor or decompressor can display a configuration dialog box. If so, send the ICM\_CONFIGURE message (or use the [**ICConfigure**](/windows/win32/Vfw/nf-vfw-icconfigure?branch=master) macro) to display it.

Your application can send the [**ICM\_GETSTATE**](icm-getstate.md) and [**ICM\_SETSTATE**](icm-setstate.md) messages (or use the [**ICGetStateSize**](/windows/win32/Vfw/nf-vfw-icgetstatesize?branch=master), [**ICGetState**](/windows/win32/Vfw/nf-vfw-icgetstate?branch=master), and [**ICSetState**](/windows/win32/Vfw/nf-vfw-icsetstate?branch=master) macros) to get and set the status for a compressor or decompressor. If your application creates or modifies the status, it must obtain the layout of the compressor or decompressor data before restoring its status. Alternatively, if your application obtains the status from a compressor or decompressor and uses it to restore the status in a subsequent session, it must ensure that it restores only status information obtained from the compressor or decompressor it is currently using.

 

 




