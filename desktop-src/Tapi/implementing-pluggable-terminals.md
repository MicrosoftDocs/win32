---
description: The general requirements for pluggable terminal implementation are listed below.
ms.assetid: 7cee19b1-ceea-494a-b576-4deede759905
title: Implementing Pluggable Terminals
ms.topic: article
ms.date: 05/31/2018
---

# Implementing Pluggable Terminals

The general requirements for pluggable terminal implementation are:

-   A pluggable terminal's underlying streaming code should match the capabilities of the desired MSPs.
-   The terminal must use DirectShow filters to work with most MSPs (this is assumed from here on).
-   Audio terminals must support 8 kHz 16-bit mono linear PCM for most MSPs.
-   The terminal should enable free threaded marshalling by implementing [**IMarshal**](/windows/win32/api/objidlbase/nn-objidlbase-imarshal). The terminal can do this by calling the COM API [**CoCreateFreeThreadedMarshaler**](/windows/win32/api/combaseapi/nf-combaseapi-cocreatefreethreadedmarshaler) and aggregating **IMarshal** to the returned pointer. The terminal object's destructor should call [**IMarshal->Release**](/windows/win32/api/unknwn/nf-unknwn-iunknown-release).
-   The terminal should implement or aggregate any additional terminal-specific interfaces that are appropriate.
-   The terminal implementation must be thread-safe.
-   The terminal implementation must \#include Termmgr.h for the definition of [**ITTerminalControl**](/windows/desktop/api/Termmgr/nn-termmgr-itterminalcontrol). This is in addition to the usual includes and libs that are needed for TAPI 3 or TAPI 3 applications under Windows 2000 SP1.

Interface and method implementation notes:

The terminal must implement [**ITTerminal**](/windows/win32/api/tapi3if/nn-tapi3if-itterminal) (dual interface–vtable + [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch)).

[**ITTerminal::get\_TerminalClass**](/windows/win32/api/tapi3if/nf-tapi3if-itterminal-get_terminalclass)

The terminal must return a **BSTR** representation of a GUID you've picked that identifies your type of terminal. Allocate the **BSTR** via [**SysAllocString**](/windows/win32/api/oleauto/nf-oleauto-sysallocstring). To convert from GUID to **BSTR**, call [**StringFromCLSID**](/windows/win32/api/combaseapi/nf-combaseapi-stringfromclsid), **SysAllocString**, and [**CoTaskMemFree**](/windows/win32/api/combaseapi/nf-combaseapi-cotaskmemfree).

[**ITTerminal::get\_TerminalType**](/windows/win32/api/tapi3if/nf-tapi3if-itterminal-get_terminaltype)

The terminal should generally return TT\_DYNAMIC if an application implements the terminal. Returning TT\_STATIC will also work, and returning this value may be appropriate if the terminal corresponds to a hardware device; however, doing this may be confusing to users because a static terminal will not be present in the MSP's static terminal enumeration.

[**ITTerminal::get\_State**](/windows/win32/api/tapi3if/nf-tapi3if-itterminal-get_state)

If the terminal implementation does not arbitrarily limit the number of streams that the terminal can be concurrently connected to, then the terminal should always return TS\_NOTINUSE.

Otherwise, the terminal implementation arbitrarily limits the number of streams that the terminal can be connected to at a time. In this case, the terminal should keep a count of how many streams it is connected to. The terminal should increment this internal count on a successful [**ITTerminalControl::ConnectTerminal**](/windows/desktop/api/Termmgr/nf-termmgr-itterminalcontrol-connectterminal) call and decrement it on a successful [**ITTerminalControl::DisconnectTerminal**](/windows/desktop/api/Termmgr/nf-termmgr-itterminalcontrol-disconnectterminal) call. In [**ITTerminal::get\_State**](/windows/win32/api/tapi3if/nf-tapi3if-itterminal-get_state), it should return TS\_INUSE if this count is equal to the maximum number of streams that the terminal can be selected on at a time; otherwise, it should return TS\_NOTINUSE. Note that if the limit is one, the count can simply be a Boolean or a TERMINAL\_STATE value.

[**ITTerminal::get\_Name**](/windows/win32/api/tapi3if/nf-tapi3if-itterminal-get_name)

The terminal should return a **BSTR** name of its choice, allocated via [**SysAllocString**](/windows/win32/api/oleauto/nf-oleauto-sysallocstring). This name should be meaningful to the user and should be localized.

[**ITTerminal::get\_MediaType**](/windows/win32/api/tapi3if/nf-tapi3if-itterminal-get_mediatype)

The terminal should return its media type, either TAPIMEDIATYPE\_AUDIO or TAPIMEDIATYPE\_VIDEO.

[**ITTerminal::get\_Direction**](/windows/win32/api/tapi3if/nf-tapi3if-itterminal-get_direction)

The terminal returns the TERMINAL\_DIRECTION enum value indicating the direction of the terminal. If the terminal is bidirectional (for example, a bridge), then it must return TD\_BIDIRECTIONAL.

The terminal must implement [**ITTerminalControl**](/windows/desktop/api/Termmgr/nn-termmgr-itterminalcontrol) (vtable only).

[**ITTerminalControl::get\_AddressHandle**](/windows/desktop/api/Termmgr/nf-termmgr-itterminalcontrol-get_addresshandle)

An application-provided terminal should always return **NULL** as the address handle. This indicates to the MSP that this terminal was not created on a specific MSP address object.

[**ITTerminalControl::ConnectTerminal**](/windows/desktop/api/Termmgr/nf-termmgr-itterminalcontrol-connectterminal)

On this call, the terminal will add its filter(s) to the given graph and connect them to each other, if applicable. Then the terminal should return the pin(s) exposed by the terminal for the stream direction specified.

A terminal that does not support concurrent connection to multiple streams would set an internal variable to TS\_INUSE on successful completion of this method.

The terminal can use the *dwTerminalDirection* parameter from this call to determine the direction of the stream that it is being connected to. This is required for bidirectional terminals.

> [!Note]  
> Typically (in the MSP base classes and in all known MSPs), the MSP stream code will fail the connection if the terminal returns more than one pin from a single [**ConnectTerminal**](/windows/desktop/api/Termmgr/nf-termmgr-itterminalcontrol-connectterminal) call. This is fine, because a terminal that returns more than one pin during connection requires the MSP to have special knowledge of the terminal to make use of the extra pins effectively.

 

[**ITTerminalControl::CompleteConnectTerminal**](/windows/desktop/api/Termmgr/nf-termmgr-itterminalcontrol-completeconnectterminal)

The terminal should just return S\_OK. The terminal may also do post-connection initialization if it needs to.

[**ITTerminalControl::DisconnectTerminal**](/windows/desktop/api/Termmgr/nf-termmgr-itterminalcontrol-disconnectterminal)

The terminal should do whatever is needed to disconnect the terminal from the rest of the graph. Typically this involves removing all the terminals' filters from the graph and setting the terminal state to TS\_NOTINUSE.

[**ITTerminalControl::RunRenderFilter**](/windows/desktop/api/Termmgr/nf-termmgr-itterminalcontrol-runrenderfilter)

The terminal should just return E\_NOTIMPL.

[**ITTerminalControl::StopRenderFilter**](/windows/desktop/api/Termmgr/nf-termmgr-itterminalcontrol-stoprenderfilter)

The terminal should just return E\_NOTIMPL.

 

 
