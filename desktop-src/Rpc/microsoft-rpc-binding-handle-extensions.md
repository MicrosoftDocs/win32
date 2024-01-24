---
title: Microsoft RPC Binding-Handle Extensions
description: The Microsoft extensions to the IDL language support multiple handle parameters that appear in positions other than the first, leftmost, parameter.
ms.assetid: 084b0d8e-0c8a-43b9-b3ae-4f69cab3a2c2
ms.topic: article
ms.date: 05/31/2018
---

# Microsoft RPC Binding-Handle Extensions

The Microsoft extensions to the IDL language support multiple handle parameters that appear in positions other than the first, leftmost, parameter. The following steps describe the sequence that the MIDL compiler goes through to resolve the binding-handle parameter in DCE-compatibility mode (/**osf**), and in default (Microsoft-extended) mode.

## DCE-compatibility mode

-   Binding handle that appears in first position.
-   Leftmost \[[**in**](/windows/desktop/Midl/in), [**context\_handle**](/windows/desktop/Midl/context-handle)\] parameter.
-   Implicit binding handle specified by \[[**implicit\_handle**](/windows/desktop/Midl/implicit-handle)\] or \[[**auto\_handle**](/windows/desktop/Midl/auto-handle)\].
-   If no ACF present, default to use of \[**auto\_handle**\].

## Default mode

-   Leftmost explicit binding handle.
-   Implicit binding handle specified by \[[**implicit\_handle**](/windows/desktop/Midl/implicit-handle)\] or \[[**auto\_handle**](/windows/desktop/Midl/auto-handle)\].
-   If no ACF present, default to use of \[[**auto\_handle**](/windows/desktop/Midl/auto-handle)\].

DCE IDL compilers look for an explicit binding handle as the first parameter. When the first parameter is not a binding handle and one or more context handles are specified, the leftmost context handle is used as the binding handle. When the first parameter is not a handle and there are no context handles, the procedure uses implicit binding using the ACF attribute \[[**implicit\_handle**](/windows/desktop/Midl/implicit-handle)\] or \[[**auto\_handle**](/windows/desktop/Midl/auto-handle)\].

The Microsoft extensions to the IDL allow the binding handle to be in a position other than the first parameter. The leftmost \[[**in**](/windows/desktop/Midl/in)\] explicit-handle parameter–whether it is a primitive, programmer-defined, or context handle–is the binding handle. When there are no handle parameters, the procedure uses implicit binding using the ACF attribute \[[**implicit\_handle**](/windows/desktop/Midl/implicit-handle)\] or \[[**auto\_handle**](/windows/desktop/Midl/auto-handle)\].

The following rules apply to both DCE-compatibility (/osf) mode and default mode:

-   Auto-handle binding is used when no ACF is present.
-   Explicit \[[**in**](/windows/desktop/Midl/in)\] or \[**in**, [**out**](/windows/desktop/Midl/out-idl)\] handles for an individual function preempt any implicit binding specified for the interface.
-   Multiple \[[**in**](/windows/desktop/Midl/in)\] or \[**in**, out\] primitive handles are not supported.
-   Multiple \[[**in**](/windows/desktop/Midl/in)\] or \[**in**, out\] explicit context handles are allowed.
-   All programmer-defined handle parameters except the binding-handle parameter are treated as transmissible data.

The following table contains examples and describes how binding handles are assigned in each compiler mode.




| Example | Description | 
|---------|-------------|
| <pre class="syntax" data-space="preserve"><code>void proc1( void );</code></pre> | No explicit handle is specified. The implicit binding handle, specified by [ <a href="/windows/desktop/Midl/implicit-handle">implicit_handle</a>] or [ <a href="/windows/desktop/Midl/auto-handle">auto_handle</a>], is used. When no ACF is present, an auto handle is used. | 
| <pre class="syntax" data-space="preserve"><code>void proc2([in] handle_t H,           [in] short s );</code></pre> | An explicit handle of type handle_t is specified. The parameter <em>H</em> is the binding handle for the procedure. | 
| <pre class="syntax" data-space="preserve"><code>void proc3([in] short s,           [in] handle_t H );</code></pre> | The first parameter is not a handle. In default mode, the leftmost handle parameter, <em>H</em>, is the binding handle. In /osf mode, implicit binding is used. An error is reported because the second parameter is expected to be transmissible, and handle_t cannot be transmitted. | 
| <pre class="syntax" data-space="preserve"><code>typedef [handle] short * MY_HDL;void proc1([in] short s,           [in] MY_HDL H );</code></pre> | The first parameter is not a handle. In default mode, the leftmost handle parameter, <em>H</em>, is the binding handle. The stubs call the user-supplied routines MY_HDL_bind and MY_HDL_unbind. In/osf mode, implicit binding is used. The programmer-defined handle parameter <em>H</em> is treated as transmissible data. | 
| <pre class="syntax" data-space="preserve"><code>Typedef [handle] short * MY_HDL;void proc1([in] MY_HDL H,            [in] MY_HDL p );</code></pre> | The first parameter is a binding handle. The parameter <em>H</em> is the binding-handle parameter. The second programmer-defined handle parameter is treated as transmissible data. | 
| <pre class="syntax" data-space="preserve"><code>Typedef [context_handle] void * CTXT_HDL;void proc1([in] short s,           [in] long l,           [in] CTXT_HDL H ,           [in] char c);</code></pre> | The binding handle is a context handle. The parameter <em>H</em> is the binding handle. | 




 

 

 
