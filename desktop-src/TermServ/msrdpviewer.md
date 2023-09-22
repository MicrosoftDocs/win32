---
title: MsRdpViewer class
description: Interacts with the remote desktop viewer control to enable Windows Desktop Sharing scenarios.
ms.assetid: 9D0F2312-0D85-402D-874D-9FA477435210
ms.tgt_platform: multiple
keywords:
- RDPViewer class Remote Desktop Services
- RDPViewer class Remote Desktop Services , described
topic_type:
- apiref
api_name:
- RDPViewer
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 09/12/2023
---

# RDPViewer class

Interacts with the remote desktop viewer control to enable Windows Desktop Sharing scenarios.

This class implements the following interfaces.

- [**IRDPSRAPIViewer interface**](/windows/win32/api/rdpencomapi/nn-rdpencomapi-irdpsrapiviewer)
- [**_IRDPSessionEvents interface**](/windows/win32/api/rdpencomapi/nn-rdpencomapi-_irdpsessionevents)
- [**IRDPSRAPIDebug interface**](/windows/win32/api/rdpencomapi/nn-rdpencomapi-irdpsrapidebug)
- [**IOleObject  interface**](/windows/win32/api/oleidl/nn-oleidl-ioleobject)
- [**IOleInPlaceActiveObject  interface**](/windows/win32/api/oleidl/nn-oleidl-ioleobject)
- [**IOleInPlaceObject interface  interface**](/windows/win32/api/oleidl/nn-oleidl-ioleinplaceobject)
- [**IConnectionPointContainer interface**](/windows/win32/api/ocidl/nn-ocidl-iconnectionpointcontainer)

A pointer to each of these interfaces can be obtained by calling [IUnknown::QueryInterface](/windows/win32/api/unknwn/nf-unknwn-iunknown-queryinterface(refiid_void))

## Remarks

To initialize an instance of **RDPViewer**, call [CoCreateInstance](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance), specifying **CLSID_RDPViewer** for the *rclsid* parameter and **CLSCTX_INPROC_SERVER** for the *dwClsContext* parameter.

The following list describes example uses of the **RDPViewer** class for Windows Desktop Sharing scenarios.

- Configure the viewer control's display location by calling [IOleObject::SetClientSite](/windows/win32/api/oleidl/nf-oleidl-ioleobject-setclientsite).
- Display the viewer control by calling [IOleObject::DoVerb](/windows/win32/api/oleidl/nf-oleidl-ioleobject-doverb) and specifying **OLEIVERB_PRIMARY** for the *iVerb* parameter.
- Connect the viewer control by calling [IRDPSRAPIViewer::Connect](/windows/win32/api/rdpencomapi/nf-rdpencomapi-irdpsrapiviewer-connect).
- Get the **HWND** of the viewer control by calling [GetWindow](/windows/win32/api/oleidl/nf-oleidl-iolewindow-getwindow) on a pointer to its [IOleInPlaceActiveObject](/windows/win32/api/oleidl/nn-oleidl-ioleinplaceactiveobject) interface.
- Notify the viewer control of the activation of the application window by calling [IOleInPlaceActiveObject::OnFrameWindowActivate](/windows/win32/api/oleidl/nf-oleidl-ioleinplaceactiveobject-onframewindowactivate)
- Receive the notifications for [_IRDPSessionEvents](/windows/win32/api/rdpencomapi/nn-rdpencomapi-_irdpsessionevents) events from the viewer control by calling [IConnectionPointContainer::FindConnectionPoint](/windows/win32/api/ocidl/nf-ocidl-iconnectionpointcontainer-findconnectionpoint), specifying `__uuidof(_IRDPSessionEvents)` for the *riid* parameter, and then calling [IConnectionPoint::Advise](/windows/win32/api/ocidl/nf-ocidl-iconnectionpoint-advise) with an application-defined implementation of **_IRDPSessionEvents**. The application is responsible for implementing the dispatching of those events to its **_IRDPSessionEvents** interface from its implementation of [IDispatch::Invoke](/windows/win32/api/oaidl/nf-oaidl-idispatch-invoke).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                         |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |
| CLSID<br/>                    | CLSID\_RdpViewer is defined as C0EFA91A-EEB7-41C7-97FA-F0ED645EFB24<br/>     |



## See also

<dl> <dt>

[Remote Desktop ActiveX control classes](remote-desktop-activex-control-classes.md)
</dt> </dl>

