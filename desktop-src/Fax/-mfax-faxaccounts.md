---
Description: Represents the collection of fax accounts on the fax server. It provides a default implementation of the IFaxAccounts interface.
ms.assetid: bf26e82e-af97-43a1-81be-1bcb61b6cf98
title: FaxAccounts object
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# FaxAccounts object

Represents the collection of fax accounts on the fax server. It provides a default implementation of the [**IFaxAccounts**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxaccounts?branch=master) interface.

## Members

The **FaxAccounts** object has these types of members:

-   [Properties](#properties)

### Properties

The **FaxAccounts** object has these properties.



| Property                                                   | Access type          | Description                                                                                                                          |
|:-----------------------------------------------------------|:---------------------|:-------------------------------------------------------------------------------------------------------------------------------------|
| [**Count**](-mfax-faxaccounts-count-vb.md)<br/>     | Read-only<br/> | Holds the number of items in the [**IFaxAccounts**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxaccounts?branch=master) collection. <br/>                               |
| [**Item**](-mfax-faxaccounts-item.md)<br/>          | Read-only<br/> | Returns a [**FaxAccount**](-mfax-faxaccount.md) object from a [**IFaxAccounts**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxaccounts?branch=master) collection. <br/> |
| [**NewEnum**](-mfax-faxaccounts-newenum-vb.md)<br/> | Read-only<br/> | Holds the enumerator for the [**IFaxAccounts**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxaccounts?branch=master) object. <br/>                                       |



 

## Remarks

![faxaccountset, faxaccounts, and faxaccount](images/faxaccounts.png)

To create a **FaxAccounts** object in Microsoft Visual Basic or C++, call the [**GetAccounts**](-mfax-faxaccountset-getaccounts-vb.md) method of the [**FaxAccountSet**](-mfax-faxaccountset.md) object.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Faxcomex.h</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>Fxscomex.dll</dt> </dl> |
| IID<br/>                      | CLSID\_FaxAccounts<br/>                                                           |



## See also

<dl> <dt>

[**IFaxAccounts**](/windows/previous-versions/FaxComex/nn-faxcomex-ifaxaccounts?branch=master)
</dt> </dl>

 

 




