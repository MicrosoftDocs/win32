---
Description: Represents the set of all fax accounts on the server. It provides methods for adding, removing, and retrieving fax accounts.
ms.assetid: ae298925-c428-420e-a0a2-ce3f72c5cff4
title: FaxAccountSet object
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# FaxAccountSet object

Represents the set of all fax accounts on the server. It provides methods for adding, removing, and retrieving fax accounts.

## Members

The **FaxAccountSet** object has these types of members:

-   [Methods](#methods)

### Methods

The **FaxAccountSet** object has these methods.



| Method                                                        | Description                                                                                                                        |
|:--------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------|
| [**AddAccount**](-mfax-faxaccountset-addaccount-vb.md)       | Adds a fax account to the fax server and returns the new [**IFaxAccount**](-mfax-faxaccount-cpp.md) object.<br/>            |
| [**GetAccount**](-mfax-faxaccountset-getaccount-vb.md)       | Returns an [**IFaxAccount**](-mfax-faxaccount-cpp.md) object by using the account name.<br/>                                |
| [**GetAccounts**](-mfax-faxaccountset-getaccounts-vb.md)     | Returns an [**IFaxAccounts**](-mfax-faxaccounts-cpp.md) object that represents all the fax accounts on the fax server.<br/> |
| [**RemoveAccount**](-mfax-faxaccountset-removeaccount-vb.md) | Removes a fax account from the fax server.<br/>                                                                              |



 

## Remarks

![faxserver2, faxaccountset, and faxaccount](images/faxaccountset.png)

To create a **FaxAccountSet** object in Microsoft Visual Basic, call the [**FaxAccountSet**](-mfax-faxserver2-faxaccountset-vb.md) property of the [**IFaxServer2**](-mfax-faxserver2-cpp.md) interface.

To create a **FaxAccountSet** object in C++, call the [**FaxAccountSet**](-mfax-faxserver2-faxaccountset-vb.md) method.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Faxcomex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |
| IID<br/>                      | CLSID\_FaxAccountSet<br/>                                                         |



## See also

<dl> <dt>

[**IFaxAccountSet**](-mfax-faxaccountset-cpp.md)
</dt> </dl>

 

 




