---
UID: NC:dxcore_interface.PFN_DXCORE_NOTIFICATION_CALLBACK
title: PFN_DXCORE_NOTIFICATION_CALLBACK
description: A callback function (implemented by your application), which is called by a DXCore object for notification events.
author: windows-sdk-content
tech.root: dxcore
ms.author: windowssdkdev
ms.date: 06/10/2019
ms.keywords: PFN_DXCORE_NOTIFICATION_CALLBACK, dxcore_interface.pfn_dxcore_notification_callback
ms.localizationpriority: low
ms.topic: callback
targetos: Windows
product: Windows
req.assembly: 
req.construct-type: callback
req.ddi-compliance: 
req.dll: dxcore.dll
req.header: dxcore_interface.h
req.idl: 
req.include-header: dxcore.h
req.irql: 
req.kmdf-ver: 
req.lib: dxcore.lib
req.max-support: 
req.namespace: 
req.redist: 
req.target-min-winverclnt: Windows 10 (Build 18936)
req.target-min-winversvr: 
req.target-type: Windows
req.type-library: 
req.umdf-ver: 
req.unicode-ansi: 
topic_type:
 - apiref
 - kbsyntax
api_type:
 - LibDef
api_location:
 - dxcore.dll
api_name:
 - PFN_DXCORE_NOTIFICATION_CALLBACK
---

# PFN_DXCORE_NOTIFICATION_CALLBACK callback

> [!NOTE]
> **Some information relates to pre-released product, which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

> [!IMPORTANT]
> The feature described in this topic is available in pre-release versions of the [Windows 10 Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK).

## Description

A callback function (implemented by your application), which is called by a DXCore object for notification events.

## Parameters

### notificationType

Type: **[DXCoreNotificationType](/windows/desktop/dxcore/dxcore_interface/ne-dxcore_interface-dxcorenotificationtype)**

The type of notification representing this invocation. See the table in [DXCoreNotificationType](/windows/desktop/dxcore/dxcore_interface/ne-dxcore_interface-dxcorenotificationtype) for info about what types are valid with which kinds of objects.

### object

Type: **[IUnknown](/windows/desktop/api/unknwn/nn-unknwn-iunknown)\***

The [IDXCoreAdapter](/windows/desktop/dxcore/dxcore_interface/nn-dxcore_interface-idxcoreadapter) or [IDXCoreAdapterList](/windows/desktop/dxcore/dxcore_interface/nn-dxcore_interface-idxcoreadapterlist) object raising the notification.

### context [in]

Type: **void\***

A pointer, which may be `nullptr`, to an object containing context info.

## See also

[IDXCoreAdapter](/windows/desktop/dxcore/dxcore_interface/nn-dxcore_interface-idxcoreadapter), [IDXCoreAdapterList](/windows/desktop/dxcore/dxcore_interface/nn-dxcore_interface-idxcoreadapterlist), [DXCore Reference](/windows/desktop/dxcore/dxcore-reference), [Using DXCore to enumerate adapters](/windows/desktop/dxcore/dxcore-enum-adapters)
