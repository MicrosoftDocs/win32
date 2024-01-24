---
description: Defines methods that handle the ITablet Interface events.
ms.assetid: 9acf32fa-b33f-4b9a-be73-804b7d5434e8
title: ITabletEventSink interface
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ITabletEventSink
api_type: 
- COM
api_location: 
- wisptis.exe
- wisptis.exe.dll
---

# ITabletEventSink interface

Defines methods that handle the [**ITablet Interface**](itablet.md) events.

## Members

The **ITabletEventSink** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **ITabletEventSink** also has these types of members:

-   [Methods](#methods)

### Methods

The **ITabletEventSink** interface has these methods.



| Method                                                        | Description                                                                                      |
|:--------------------------------------------------------------|:-------------------------------------------------------------------------------------------------|
| [**ContextCreate**](itableteventsink-contextcreate.md)       | Occurs when a new tablet context is created.<br/>                                          |
| [**ContextDestroy**](itableteventsink-contextdestroy.md)     | Occurs when a tablet context is being destroyed.<br/>                                      |
| [**CursorDown**](itableteventsink-cursordown.md)             | Occurs when the stylus tip contacts the digitizing tablet surface.<br/>                    |
| [**CursorInRange**](itableteventsink-cursorinrange.md)       | Occurs when a stylus comes within the digitizer's range of detection.<br/>                 |
| [**CursorMove**](itableteventsink-cursormove.md)             | Occurs when the cursor moves over the tablet digitizer.<br/>                               |
| [**CursorNew**](itableteventsink-cursornew.md)               | Occurs when a new stylus is added to the system.<br/>                                      |
| [**CursorOutOfRange**](itableteventsink-cursoroutofrange.md) | Occurs when the stylus leaves the physical detection range (proximity) of the tablet.<br/> |
| [**CursorUp**](itableteventsink-cursorup.md)                 | Occurs when the user has raised the stylus from the tablet digitizer surface.<br/>         |
| [**Packets**](itableteventsink-packets.md)                   | Occurs when the stylus is moving on the digitizer.<br/>                                    |
| [**SystemEvent**](itableteventsink-systemevent.md)           | Occurs when a system event is available.<br/>                                              |



 

## Remarks

Developers should not use this interface.

The following code shows how the **ITabletEventSink** interface is defined.

``` syntax
[
    object,
    uuid(788459C8-26C8-4666-BF57-04AD3A0A5EB5),
    pointer_default(unique)
]
interface ITabletEventSink: IUnknown
{

    HRESULT ContextCreate(
        [in] TABLET_CONTEXT_ID tcid
    );

    HRESULT ContextDestroy(
        [in] TABLET_CONTEXT_ID tcid
    );

    HRESULT CursorNew(
        [in] TABLET_CONTEXT_ID tcid,
        [in] CURSOR_ID cid
    );

    HRESULT CursorInRange(
        [in] TABLET_CONTEXT_ID tcid,
        [in] CURSOR_ID cid
    );

    HRESULT CursorOutOfRange(
        [in] TABLET_CONTEXT_ID tcid,
        [in] CURSOR_ID cid
    );

    HRESULT CursorDown(
        [in] TABLET_CONTEXT_ID tcid,
        [in] CURSOR_ID cid,
        [in] ULONG nSerialNumber,
        [in] ULONG cbPkt,
        [in, size_is(cbPkt)] BYTE *pbPkt
    );

    HRESULT CursorUp(
        [in] TABLET_CONTEXT_ID tcid,
        [in] CURSOR_ID cid,
        [in] ULONG nSerialNumber,
        [in] ULONG cbPkt,
        [in, size_is(cbPkt)] BYTE *pbPkt
    );

    HRESULT Packets(
        [in] TABLET_CONTEXT_ID tcid,
        [in] ULONG cPkts,
        [in] ULONG cbPkts,
        [in, size_is(cbPkts)] BYTE * pbPkts,
        [in, unique, size_is(cPkts)
#ifndef NT_TARGET_XP
         ,disable_consistency_check
#endif
        ] ULONG *pnSerialNumbers,
        [in] CURSOR_ID cid
    );

    HRESULT SystemEvent(
        [in] TABLET_CONTEXT_ID tcid,
        [in] CURSOR_ID cid,
        [in] SYSTEM_EVENT event,
        [in] SYSTEM_EVENT_DATA eventdata
    );
};

     
```

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP Tablet PC Edition \[desktop apps only\]<br/>                          |
| Minimum supported server<br/> | None supported<br/>                                                              |
| Library<br/>                  | <dl> <dt>Wisptis.exe</dt> </dl> |



 

