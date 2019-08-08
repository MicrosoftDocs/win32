---
UID: NE:dxcore_interface.DXCoreNotificationType
title: DXCoreNotificationType
description: TBD
author: windows-sdk-content
tech.root: dxcore
ms.author: windowssdkdev
ms.date: 06/11/2019
ms.keywords: DXCoreNotificationType enumeration, dxcore_interface.dxcorenotificationtype
ms.localizationpriority: low
ms.topic: enumeration
targetos: Windows
product: Windows
req.assembly: 
req.construct-type: enumeration
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
 - HeaderDef
api_location:
 - dxcore.dll
api_name:
 - DXCoreNotificationType
---

# DXCoreNotificationType enum

> [!NOTE]
> **Some information relates to pre-released product, which may be substantially modified before it's commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

> [!IMPORTANT]
> The feature described in this topic is available in pre-release versions of the [Windows 10 Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK).

## Description

Defines constants that specify types of notifications raised by [IDXCoreAdapter](/windows/desktop/dxcore/dxcore_interface/nn-dxcore_interface-idxcoreadapter) or [IDXCoreAdapterList](/windows/desktop/dxcore/dxcore_interface/nn-dxcore_interface-idxcoreadapterlist) objects.

You can register and unregister for these notifications by calling [IDXCoreAdapterFactory::RegisterEventNotification](/windows/desktop/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapterfactory-registereventnotification) and [IDXCoreAdapterFactory::UnregisterEventNotification](/windows/desktop/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapterfactory-unregistereventnotification), respectively.

## Enum fields

### AdapterListStale

This notification is raised by an <a href="/windows/desktop/dxcore/dxcore_interface/nn-dxcore_interface-idxcoreadapterlist">IDXCoreAdapterList</a> object when the adapter list becomes stale. The fresh-to-stale transition is one-way, and one-time, so this notification is raised at most one time.

### AdapterNoLongerValid

This notification is raised by an <a href="/windows/desktop/dxcore/dxcore_interface/nn-dxcore_interface-idxcoreadapter">IDXCoreAdapter</a> object when the adapter becomes no longer valid. The valid-to-invalid transition is one-way, and one-time, so this notification is raised at most one time.

### AdapterBudgetChange

This notification is raised by an <a href="/windows/desktop/dxcore/dxcore_interface/nn-dxcore_interface-idxcoreadapter">IDXCoreAdapter</a> object when an adapter budget change occurs. This notification can occur many times. Using this notification is functionally similar to <a href="/windows/desktop/api/dxgi1_4/nf-dxgi1_4-idxgiadapter3-registervideomemorybudgetchangenotificationevent">IDXGIAdapter3::RegisterVideoMemoryBudgetChangeNotificationEvent</a>. In response to this event, you should call [IDXCoreAdapter::QueryState](/windows/desktop/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapter-querystate) (with [DXCoreAdapterState::AdapterMemoryBudget](/windows/desktop/dxcore/dxcore_interface/ne-dxcore_interface-dxcoreadapterstate)) to evaluate the current memory budget state.

### AdapterHardwareContentProtectionTeardown

This notification is raised by an <a href="/windows/desktop/dxcore/dxcore_interface/nn-dxcore_interface-idxcoreadapter">IDXCoreAdapter</a> object to notify of an adapter's hardware content protection teardown. This notification can occur many times. It is functionally similar to <a href="/windows/desktop/api/dxgi1_4/nf-dxgi1_4-idxgiadapter3-registerhardwarecontentprotectionteardownstatusevent">IDXGIAdapter3::RegisterHardwareContentProtectionTeardownStatusEvent</a>. In response to this event, you should re-evaluate the current crypto session status; for example, by calling [ID3D11VideoContext1::CheckCryptoSessionStatus](/windows/desktop/api/d3d11_1/nf-d3d11_1-id3d11videocontext1-checkcryptosessionstatus) to determine the impact of the hardware teardown for a specific [ID3D11CryptoSession](/windows/desktop/api/d3d11/nn-d3d11-id3d11cryptosession) interface.

## See also

[IDXCoreAdapterFactory::RegisterEventNotification](/windows/desktop/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapterfactory-registereventnotification), [IDXCoreAdapterFactory::UnregisterEventNotification](/windows/desktop/dxcore/dxcore_interface/nf-dxcore_interface-idxcoreadapterfactory-unregistereventnotification), [IDXCoreAdapter](/windows/desktop/dxcore/dxcore_interface/nn-dxcore_interface-idxcoreadapter), [IDXCoreAdapterList](/windows/desktop/dxcore/dxcore_interface/nn-dxcore_interface-idxcoreadapterlist), [DXCore Reference](/windows/desktop/dxcore/dxcore-reference), [Using DXCore to enumerate adapters](/windows/desktop/dxcore/dxcore-enum-adapters)
