---
title: Dispatch Functions
description: These functions simplify the creation of IDispatch interfaces. The dispatch functions are summarized in the following table.
ms.assetid: 2c66b04e-9d96-45e9-8105-82d58a5a4085
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Dispatch Functions

These functions simplify the creation of [**IDispatch**](/windows/previous-versions/oaidl/nn-oaidl-idispatch?branch=master) interfaces. The dispatch functions are summarized in the following table.

## In this section



| Topic                                                       | Description                                                                                                                                                                       |
|-------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateDispTypeInfo**](/windows/previous-versions/OleAuto/nf-oleauto-createdisptypeinfo?branch=master)<br/> | Creates simplified type information for use in an implementation of [**IDispatch**](/windows/previous-versions/oaidl/nn-oaidl-idispatch?branch=master).<br/>                                                                    |
| [**CreateStdDispatch**](/windows/previous-versions/OleAuto/nf-oleauto-createstddispatch?branch=master)<br/>   | Creates a standard implementation of the [**IDispatch**](/windows/previous-versions/oaidl/nn-oaidl-idispatch?branch=master) interface through a single function call. This simplifies exposing objects through Automation.<br/> |
| [**DispCallFunc**](/windows/previous-versions/OleAuto/nf-oleauto-dispcallfunc?branch=master)<br/>             | Low-level helper for [**Invoke**](/windows/previous-versions/oaidl/nf-oaidl-idispatch-invoke?branch=master) that provides machine independence for customized **Invoke**.<br/>                                                  |
| [**DispGetIDsOfNames**](/windows/previous-versions/OleAuto/nf-oleauto-dispgetidsofnames?branch=master)<br/>   | Low-level helper for [**Invoke**](/windows/previous-versions/oaidl/nf-oaidl-idispatch-invoke?branch=master) that provides machine independence for customized **Invoke**. <br/>                                                 |
| [**DispGetParam**](/windows/previous-versions/OleAuto/nf-oleauto-dispgetparam?branch=master)<br/>             | Retrieves a parameter from the DISPPARAMS structure, checking both named parameters and positional parameters, and coerces the parameter to the specified type.<br/>        |
| [**DispInvoke**](/windows/previous-versions/OleAuto/nf-oleauto-dispinvoke?branch=master)<br/>                 | Automatically calls member functions on an interface, given the type information for the interface.<br/>                                                                    |



 

## Related topics

<dl> <dt>

[Dispatch Interface and Automation Functions](dispatch-interfaces.md)
</dt> <dt>

[Automation Programming Reference](automation-programming-reference.md)
</dt> </dl>

 

 





