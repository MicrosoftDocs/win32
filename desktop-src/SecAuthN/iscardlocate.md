---
description: The ISCardLocate interface provides services for locating a smart card by its name.
ms.assetid: add00705-69d5-4562-a74f-94c6864f6bd8
title: ISCardLocate interface (Scardmgr.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCardLocate
- ISCardLocate.ConfigureCardGuidSearch
api_type: 
- COM
api_location: 
- Scardssp.dll
---

# ISCardLocate interface

\[The **ISCardLocate** interface is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [Smart Card Modules](/previous-versions/windows/desktop/secsmart/smart-card-modules) provide similar functionality.\]

The **ISCardLocate** interface provides services for locating a [*smart card*](../secgloss/s-gly.md) by its name.

This interface can display the smart card [*user interface*](../secgloss/u-gly.md) if it is required.

The following scenario shows a typical use of the **ISCardLocate** interface. The **ISCardLocate** interface is used to build an [*application protocol data unit*](../secgloss/a-gly.md) (APDU).

**To locate a specific card using its name**

1.  Create an **ISCardLocate** interface.
2.  Call [**ConfigureCardNameSearch**](iscardlocate-configurecardnamesearch.md) to search for a smart card name.
3.  Call [**FindCard**](iscardlocate-findcard.md) to search for the smart card.
4.  Interpret the results.
5.  Release the **ISCardLocate** interface.

## Members

The **ISCardLocate** interface inherits from the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface. **ISCardLocate** also has these types of members:

-   [Methods](#methods)

### Methods

The **ISCardLocate** interface has these methods.



| Method                                                                  | Description                                                                |
|:------------------------------------------------------------------------|:---------------------------------------------------------------------------|
| **ConfigureCardGuidSearch**                                             | Reserved for future use.<br/>                                        |
| [**ConfigureCardNameSearch**](iscardlocate-configurecardnamesearch.md) | Specifies the card name to be used in the search.<br/>               |
| [**FindCard**](iscardlocate-findcard.md)                               | Searches for the smart card and opens a valid connection to it.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| End of client support<br/>    | Windows XP<br/>                                                                   |
| End of server support<br/>    | Windows Server 2003<br/>                                                          |
| Header<br/>                   | <dl> <dt>Scardmgr.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Scardmgr.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Scardssp.dll</dt> </dl> |
| IID<br/>                      | IID\_ISCardLocate is defined as 1461AACD-6810-11D0-918F-00AA00C18068<br/>         |



 

 
