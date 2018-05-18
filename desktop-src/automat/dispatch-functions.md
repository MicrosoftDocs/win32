---
title: Dispatch Functions
description: These functions simplify the creation of IDispatch interfaces. The dispatch functions are summarized in the following table.
ms.assetid: '2c66b04e-9d96-45e9-8105-82d58a5a4085'
---

# Dispatch Functions

These functions simplify the creation of [**IDispatch**](idispatch.md) interfaces. The dispatch functions are summarized in the following table.

## In this section



| Topic                                                       | Description                                                                                                                                                                       |
|-------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateDispTypeInfo**](createdisptypeinfo.md)<br/> | Creates simplified type information for use in an implementation of [**IDispatch**](idispatch.md).<br/>                                                                    |
| [**CreateStdDispatch**](createstddispatch.md)<br/>   | Creates a standard implementation of the [**IDispatch**](idispatch.md) interface through a single function call. This simplifies exposing objects through Automation.<br/> |
| [**DispCallFunc**](dispcallfunc.md)<br/>             | Low-level helper for [**Invoke**](idispatch-invoke.md) that provides machine independence for customized **Invoke**.<br/>                                                  |
| [**DispGetIDsOfNames**](dispgetidsofnames.md)<br/>   | Low-level helper for [**Invoke**](idispatch-invoke.md) that provides machine independence for customized **Invoke**. <br/>                                                 |
| [**DispGetParam**](dispgetparam.md)<br/>             | Retrieves a parameter from the DISPPARAMS structure, checking both named parameters and positional parameters, and coerces the parameter to the specified type.<br/>        |
| [**DispInvoke**](dispinvoke.md)<br/>                 | Automatically calls member functions on an interface, given the type information for the interface.<br/>                                                                    |



 

## Related topics

<dl> <dt>

[Dispatch Interface and Automation Functions](dispatch-interfaces.md)
</dt> <dt>

[Automation Programming Reference](automation-programming-reference.md)
</dt> </dl>

 

 





