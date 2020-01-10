---
Description: The ISCardDatabase interface provides the methods for performing the smart card resource manager's database operations.
ms.assetid: 56db3bc0-33c3-4b9c-a4a7-374fc491d8fd
title: ISCardDatabase interface (Scardmgr.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ISCardDatabase
api_type: 
- COM
api_location: 
- Scardssp.dll
---

# ISCardDatabase interface

\[The **ISCardDatabase** interface is available for use in the operating systems specified in the Requirements section. It is not available for use in Windows Server 2003 with Service Pack 1 (SP1) and later, Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The [Smart Card Modules](https://msdn.microsoft.com/library/Dd627652(v=VS.85).aspx) provide similar functionality.\]

The **ISCardDatabase** interface provides the methods for performing the [*smart card*](https://msdn.microsoft.com/library/ms721625(v=VS.85).aspx) [*resource manager's*](https://msdn.microsoft.com/library/ms721604(v=VS.85).aspx) database operations. These operations include listing known smart cards, [*readers*](https://msdn.microsoft.com/library/ms721604(v=VS.85).aspx), and reader groups, plus retrieving the interfaces supported by a smart card and its [*primary service provider*](https://msdn.microsoft.com/library/ms721603(v=VS.85).aspx).

> [!Note]  
> The identifier of the primary service provider is a COM GUID that can be used to instantiate and use the COM objects for a specific card.

 

The following example shows a typical use of the **ISCardDatabase** interface. In this case, the **ISCardDatabase** interface is used to list all the known smart cards.

**To submit a transaction to a specific card**

1.  Create an **ISCardDatabase** interface.
2.  Call [**ListCards**](iscarddatabase-listcards.md) to retrieve all the known smart cards based on an [*ATR string*](https://msdn.microsoft.com/library/ms721532(v=VS.85).aspx) or their supported interfaces.
3.  Release the **ISCardDatabase** interface.

## Members

The **ISCardDatabase** interface inherits from the [**IDispatch**](https://msdn.microsoft.com/library/ms221608(v=VS.71).aspx) interface. **ISCardDatabase** also has these types of members:

-   [Methods](#methods)

### Methods

The **ISCardDatabase** interface has these methods.



| Method                                                          | Description                                                                                                                                                                                      |
|:----------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetProviderCardId**](iscarddatabase-getprovidercardid.md)   | Retrieves the identifier of the [*primary service provider*](https://msdn.microsoft.com/library/ms721603(v=VS.85).aspx) for a specific smart card.<br/> |
| [**ListCardInterfaces**](iscarddatabase-listcardinterfaces.md) | Retrieves the interface identifiers (GUIDs) of all the interfaces supported by a specific smart card.<br/>                                                                                 |
| [**ListCards**](iscarddatabase-listcards.md)                   | Retrieves all the smart card names that match a specific set of interface identifiers (GUIDs) or an [*ATR string*](https://msdn.microsoft.com/library/ms721532(v=VS.85).aspx).<br/> |
| [**ListReaderGroups**](iscarddatabase-listreadergroups.md)     | Retrieves the names of the [*reader groups*](https://msdn.microsoft.com/library/ms721604(v=VS.85).aspx) that the resource manager has knowledge of.<br/>                        |
| [**ListReaders**](iscarddatabase-listreaders.md)               | Retrieve the names of the [*readers*](https://msdn.microsoft.com/library/ms721604(v=VS.85).aspx) of which the resource manager has knowledge.<br/>                                          |



 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| End of client support<br/>    | Windows XP<br/>                                                                   |
| End of server support<br/>    | Windows Server 2003<br/>                                                          |
| Header<br/>                   | <dl> <dt>Scardmgr.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Scardmgr.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Scardssp.dll</dt> </dl> |
| IID<br/>                      | IID\_ISCardDatabase is defined as 1461AAC8-6810-11D0-918F-00AA00C18068<br/>       |



 

 




