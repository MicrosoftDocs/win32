---
description: Provides COM-standard methods to manage protected storage data items.
ms.assetid: 6a4200ed-c3cf-4d6c-8936-22261e670087
title: IPStore interface (Pstore.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IPStore
api_type: 
- COM
api_location: 
- Pstorec.dll
---

# IPStore interface

\[Protected Storage (Pstore) is available for use in Windows Server 2003 and Windows XP. It is only available for read-only operations in Windows Server 2008 and Windows Vista, but may be unavailable in subsequent versions. Pstore uses an older implementation of data protection. Developers are strongly encouraged to take advantage of the stronger data protection provided by the [**CryptProtectData**](/windows/win32/api/dpapi/nf-dpapi-cryptprotectdata) and [**CryptUnprotectData**](/windows/win32/api/dpapi/nf-dpapi-cryptunprotectdata) functions.\]

\[This interface may be altered or unavailable in future versions of Windows.\]

Provides COM-standard methods to manage protected storage data items. The [**PStoreCreateInstance**](pstorecreateinstance.md) method returns a pointer to this interface.

## Members

The **IPStore** interface inherits from the [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface. **IPStore** also has these types of members:

-   [Methods](#methods)

### Methods

The **IPStore** interface has these methods.



| Method                                                   | Description                                                                                                           |
|:---------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------|
| [**CloseItem**](ipstore-closeitem.md)                   | Closes a specified data item from protected storage.<br/>                                                       |
| [**CreateSubtype**](ipstore-createsubtype.md)           | Creates the specified subtype within the specified type.<br/>                                                   |
| [**CreateType**](ipstore-createtype.md)                 | Creates the specified type with the specified name.<br/>                                                        |
| [**DeleteItem**](ipstore-deleteitem.md)                 | Deletes the specified item from the protected storage.<br/>                                                     |
| [**DeleteSubtype**](ipstore-deletesubtype.md)           | Deletes the specified item subtype from the protected storage.<br/>                                             |
| [**DeleteType**](ipstore-deletetype.md)                 | Deletes the specified type from the protected storage.<br/>                                                     |
| [**EnumItems**](ipstore-enumitems.md)                   | Returns the interface pointer of a subtype for enumerating items in the protected storage database.<br/>        |
| [**EnumSubtypes**](ipstore-enumsubtypes.md)             | Returns an interface for enumerating subtypes of the types currently registered in the protected database.<br/> |
| [**EnumTypes**](ipstore-enumtypes.md)                   | Returns an interface for enumerating the types currently registered in the protected database.<br/>             |
| [**GetInfo**](ipstore-getinfo.md)                       | Retrieves information about the storage provider.<br/>                                                          |
| [**GetProvParam**](ipstore-getprovparam.md)             | Not implemented.<br/>                                                                                           |
| [**GetSubtypeInfo**](ipstore-getsubtypeinfo.md)         | Retrieves information associated with a subtype.<br/>                                                           |
| [**GetTypeInfo**](ipstore-gettypeinfo.md)               | Retrieves information associated with a type.<br/>                                                              |
| [**OpenItem**](ipstore-openitem.md)                     | Opens an item for multiple accesses.<br/>                                                                       |
| [**ReadAccessRuleSet**](ipstore-readaccessruleset.md)   | Not implemented.<br/>                                                                                           |
| [**ReadItem**](ipstore-readitem.md)                     | Reads the specified data item from protected storage.<br/>                                                      |
| [**SetProvParam**](ipstore-setprovparam.md)             | Sets the specified parameter information.<br/>                                                                  |
| [**WriteAccessRuleset**](ipstore-writeaccessruleset.md) | Not implemented.<br/>                                                                                           |
| [**WriteItem**](ipstore-writeitem.md)                   | Writes a data item to protected storage.<br/>                                                                   |



 

## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Pstore.h</dt> </dl>    |
| DLL<br/>    | <dl> <dt>Pstorec.dll</dt> </dl> |



 

 
