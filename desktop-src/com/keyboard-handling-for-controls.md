---
title: Keyboard Handling for Controls
description: A control responds to keyboard accelerators so the end-user can initiate actions performed by the control.
ms.assetid: 59aca5cb-f109-49ee-897d-43610501f7f8
ms.topic: article
ms.date: 05/31/2018
---

# Keyboard Handling for Controls

A control responds to keyboard accelerators so the end-user can initiate actions performed by the control. The container manages keyboard activity for all its embedded controls. With compound documents, keyboard accelerators apply only to the currently active object. With controls, a mechanism has been added so that a control can respond to its keyboard mnemonics even if it is not currently UI-active.

The [**IOleControl::GetControlInfo**](/windows/desktop/api/OCIdl/nf-ocidl-iolecontrol-getcontrolinfo) and [**IOleControl::OnMnemonic**](/windows/desktop/api/OCIdl/nf-ocidl-iolecontrol-onmnemonic) methods and the [**IOleControlSite::OnControlInfoChanged**](/windows/desktop/api/OCIdl/nf-ocidl-iolecontrolsite-oncontrolinfochanged) method handle a control's keyboard mnemonics. A [**CONTROLINFO**](/windows/win32/api/ocidl/ns-ocidl-controlinfo) structure describes a control's mnemonic accelerators, and the flags passed back with it through the **GetControlInfo** method describe the controls behavior with the Enter and Esc keys. When a control changes its mnemonics, it calls **OnControlInfoChanged** so the container can reload the structure if necessary.

When a control is UI active, it is also the control with the focus. As controls are activated and deactivated between the in-place active and the UI active states, the control calls [**IOleControlSite::OnFocus**](/windows/desktop/api/OCIdl/nf-ocidl-iolecontrolsite-onfocus) to tell the container of such changes.

In addition, when a control is UI active, it will have first chance to process any keystrokes. To give a container the opportunity to process the keystroke before the control, the control calls [**IOleControlSite::TranslateAccelerator**](/windows/desktop/api/OCIdl/nf-ocidl-iolecontrolsite-translateaccelerator). If the container does not handle the keystroke, the control then processes it.

## Related topics

<dl> <dt>

[ActiveX Controls](activex-controls.md)
</dt> </dl>

 

 




