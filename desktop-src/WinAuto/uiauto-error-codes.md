---
title: Error Codes (UIAutomationCoreApi.h)
description: This topic describes the error codes exposed by Microsoft UI Automation.
ms.assetid: f7820aa3-908e-426e-851c-84397019d735
topic_type:
- apiref
api_name:
- UIA_E_ELEMENTNOTAVAILABLE
- UIA_E_ELEMENTNOTENABLED
- UIA_E_INVALIDOPERATION
- UIA_E_NOCLICKABLEPOINT
- UIA_E_NOTSUPPORTED
- UIA_E_PROXYASSEMBLYNOTLOADED
- UIA_E_TIMEOUT
api_location:
- UIAutomationCoreApi.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Error Codes (UIAutomationCoreApi.h)

This topic describes the error codes exposed by Microsoft UI Automation. The list is sorted alphabetically by name.



| Constant/value                                                                                                                                                                                                                                                              | Description                                                                                                                                                                                                                                              |
|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="UIA_E_ELEMENTNOTAVAILABLE"></span><span id="uia_e_elementnotavailable"></span><dl> <dt>**UIA\_E\_ELEMENTNOTAVAILABLE**</dt> <dt>0x80040201</dt> </dl>          | Indicates that a method was called on a virtualized element, or on an element that no longer exists, usually because it has been destroyed. <br/>                                                                                                  |
| <span id="UIA_E_ELEMENTNOTENABLED"></span><span id="uia_e_elementnotenabled"></span><dl> <dt>**UIA\_E\_ELEMENTNOTENABLED**</dt> <dt>0x80040200</dt> </dl>                | Indicates that a method that requires an enabled element, such as [**Select**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-iselectionitemprovider-select) or [**Expand**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-iexpandcollapseprovider-expand), was called on an element that was disabled. <br/>             |
| <span id="UIA_E_INVALIDOPERATION"></span><span id="uia_e_invalidoperation"></span><dl> <dt>**UIA\_E\_INVALIDOPERATION**</dt> <dt>0x80131509</dt> </dl>                   | Indicates that the method attempted an operation that was not valid.<br/>                                                                                                                                                                          |
| <span id="UIA_E_NOCLICKABLEPOINT"></span><span id="uia_e_noclickablepoint"></span><dl> <dt>**UIA\_E\_NOCLICKABLEPOINT**</dt> <dt>0x80040202</dt> </dl>                   | Indicates that the [**GetClickablePoint**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-getclickablepoint) method was called on an element that has no clickable point.<br/>                                                                                    |
| <span id="UIA_E_NOTSUPPORTED"></span><span id="uia_e_notsupported"></span><dl> <dt>**UIA\_E\_NOTSUPPORTED**</dt> <dt>0x80040204</dt> </dl>                               | Indicates that the provider explicitly does not support the specified property or control pattern. UI Automation will return this error code to the caller without attempting to provide a default value or falling back to another provider.<br/> |
| <span id="UIA_E_PROXYASSEMBLYNOTLOADED"></span><span id="uia_e_proxyassemblynotloaded"></span><dl> <dt>**UIA\_E\_PROXYASSEMBLYNOTLOADED**</dt> <dt>0x80040203</dt> </dl> | Indicates that a problem occurred when loading an assembly that contains a client-side (proxy) provider.<br/>                                                                                                                                      |
| <span id="UIA_E_TIMEOUT"></span><span id="uia_e_timeout"></span><dl> <dt>**UIA\_E\_TIMEOUT**</dt> <dt>0x80131505</dt> </dl>                                                      | Indicates that the time allotted for a process or operation has expired.<br/>                                                                                                                                                                      |



## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                      |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                             |
| Header<br/>                   | <dl> <dt>UIAutomationCoreApi.h</dt> </dl> |



 

 





