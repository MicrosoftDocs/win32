---
title: ActiveX Controls Interfaces
description: ActiveX Controls Interfaces
ms.assetid: 'c4ca5696-c461-4d65-b2a8-c689c056dac8'
---

# ActiveX Controls Interfaces

In addition to other mechanisms for communicating between the control and its client, ActiveX controls technology specifies the [**IOleControl**](iolecontrol.md) and [**IOleControlSite**](iolecontrolsite.md) interfaces for client-control communication. There is also the [**ISimpleFrameSite**](isimpleframesite.md) interface for simple control containers.

These three interfaces are, however, specific to controls and are not generally useful outside the context of controls. These interfaces are defined as follows.

``` syntax
interface IOleControl : IUnknown 
  { 
    HRESULT GetControlInfo([out] CONTROLINFO *pCI); 
    HRESULT OnMnemonic([in] LPMSG pMsg); 
    HRESULT OnAmbientPropertyChange([in] DISPID dispID); 
    HRESULT FreezeEvents([in] BOOL bFreeze); 
  } 
 
interface IOleControlSite : IUnknown 
  { 
    HRESULT OnControlInfoChanged(void); 
    HRESULT LockInPlaceActive([in] BOOL fLock); 
    HRESULT GetExtendedControl([out] IDispatch **ppDisp); 
    HRESULT TransformCoords([in-out] POINTL *pptlHimetric, [in-out] POINTF *pptfContainer, [in] DWORD dwFlags); 
    HRESULT TranslateAccelerator([in] LPMSG pMsg, [in] DWORD grfModifiers); 
    HRESULT OnFocus([in] BOOL fGotFocus); 
    HRESULT ShowPropertyFrame(void); 
  } 
 
interface ISimpleFrameSite : IUnknown 
  { 
    HRESULT PreMessageFilter([in] HWND hWnd, [in] UINT msg, [in] WPARAM wp, [in] LPARAM lp, 
        [out] LRESULT *plResult, [out] DWORD *pdwCookie); 
    HRESULT PostMessageFilter([in] HWND hWnd, [in] UINT msg, [in] WPARAM wp, [in] LPARAM lp, 
        [out] LRESULT *plResult, [in] DWORD dwCookie); 
  } 
 
```

Some controls, like a group box, are merely a simple container of other controls. In such cases, the simple control, called a simple frame, doesn't have to implement all the container requirements. It can delegate most of the interface calls from its contained controls to the container that manages the simple frame. Besides interface calls, the simple frame also has to deal with Windows messages that potentially come from controls within it. For this reason, a container supplies [**ISimpleFrameSite**](isimpleframesite.md) to allow such simple frame controls to pass messages up to the container. [**PreMessageFilter**](isimpleframesite-premessagefilter.md) processes the message first; [**PostMessageFilter**](isimpleframesite-postmessagefilter.md) is called after the simple frame has processed the message itself.

## Related topics

<dl> <dt>

[ActiveX Controls](activex-controls.md)
</dt> </dl>

 

 




