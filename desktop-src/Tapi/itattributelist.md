---
description: The ITAttributeList interface supplies methods for getting and setting of uninterpreted attributes.
ms.assetid: 12806c2e-615c-4d78-a4bb-5cc35ea21175
title: ITAttributeList interface (Sdpblb.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ITAttributeList interface

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **ITAttributeList** interface supplies methods for getting and setting of uninterpreted attributes. Regarding the position of the attribute strings in a Session Descriptor Protocol (SDP, see RFC 2327) packet, the methods assume that all attribute strings exist just before the media attributes are specified and after all the common attributes. The **ITAttributeList** interface is created by calling **QueryInterface** on [**ITDirectoryObject**](/windows/desktop/api/Rend/nn-rend-itdirectoryobject).

## Members

The **ITAttributeList** interface inherits from the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface. **ITAttributeList** also has these types of members:

-   [Methods](#methods)

### Methods

The **ITAttributeList** interface has these methods.



| Method                                                          | Description                                             |
|:----------------------------------------------------------------|:--------------------------------------------------------|
| [**Add**](itattributelist-add.md)                              | Adds the attribute at the specified index.<br/>   |
| [**Delete**](itattributelist-delete.md)                        | Deletes the attribute at the specified index<br/> |
| [**get\_AttributeList**](itattributelist-get-attributelist.md) | Gets the list of attributes.<br/>                 |
| [**get\_Count**](itattributelist-get-count.md)                 | Gets the number of attributes.<br/>               |
| [**get\_Item**](itattributelist-get-item.md)                   | Gets the attribute specified by the index.<br/>   |
| [**put\_AttributeList**](itattributelist-put-attributelist.md) | Sets the list of attributes.<br/>                 |



 

## Requirements



| Requirement | Value |
|-------------------------|---------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                 |
| Header<br/>       | <dl> <dt>Sdpblb.h</dt> </dl>   |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>   |
| DLL<br/>          | <dl> <dt>Sdpblb.dll</dt> </dl> |



 

