---
title: Dispatch Functions
description: These functions simplify the creation of IDispatch interfaces. The dispatch functions are summarized in the following table.
ms.assetid: 2c66b04e-9d96-45e9-8105-82d58a5a4085
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Dispatch Functions

These functions simplify the creation of [**IDispatch**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-idispatch) interfaces. The dispatch functions are summarized in the following table.

## In this section



| Topic                                                       | Description                                                                                                                                                                       |
|-------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateDispTypeInfo**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-createdisptypeinfo)<br/> | Creates simplified type information for use in an implementation of [**IDispatch**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-idispatch).<br/>                                                                    |
| [**CreateStdDispatch**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-createstddispatch)<br/>   | Creates a standard implementation of the [**IDispatch**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-idispatch) interface through a single function call. This simplifies exposing objects through Automation.<br/> |
| [**DispCallFunc**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-dispcallfunc)<br/>             | Low-level helper for [**Invoke**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-idispatch-invoke) that provides machine independence for customized **Invoke**.<br/>                                                  |
| [**DispGetIDsOfNames**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-dispgetidsofnames)<br/>   | Low-level helper for [**Invoke**](/previous-versions/windows/desktop/api/oaidl/nf-oaidl-idispatch-invoke) that provides machine independence for customized **Invoke**. <br/>                                                 |
| [**DispGetParam**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-dispgetparam)<br/>             | Retrieves a parameter from the DISPPARAMS structure, checking both named parameters and positional parameters, and coerces the parameter to the specified type.<br/>        |
| [**DispInvoke**](/previous-versions/windows/desktop/api/OleAuto/nf-oleauto-dispinvoke)<br/>                 | Automatically calls member functions on an interface, given the type information for the interface.<br/>                                                                    |



 

## Related topics

<dl> <dt>

[Dispatch Interface and Automation Functions](dispatch-interfaces.md)
</dt> <dt>

[Automation Programming Reference](automation-programming-reference.md)
</dt> </dl>

 

 





