---
description: Represents any collection in the COM+ catalog. Use it to enumerate, add, remove, and retrieve items in a collection and to access related collections.
ms.assetid: 2530e44f-c428-4baa-88e1-8d01eaf234cc
title: COMAdminCatalogCollection class (ComAdmin.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- COMAdminCatalogCollection
api_type: 
- COM
api_location: 
- ComAdmin.Idl
---

# COMAdminCatalogCollection class

Represents any collection in the COM+ catalog. Use it to enumerate, add, remove, and retrieve items in a collection and to access related collections.

## When to implement

This class is implemented by COM+.



| Requirement | Value |
|------------|--------------------------------------------------|
| Interfaces | [**ICatalogCollection**](/windows/desktop/api/ComAdmin/nn-comadmin-icatalogcollection) |



 

## When to use

Use objects created from the **COMAdminCatalogCollection** class when you want to programmatically manipulate a collection in the COM+ catalog. These collections correspond to folders in the Component Services administration tool. Items inside the folders correspond to items in collections, which you can represent by using objects created from the [**COMAdminCatalogObject**](comadmincatalogobject.md) class.

For information regarding the collections on the catalog and their properties, see [COM+ Administration Collections](com--administration-collections.md).

For an introduction to programmatic administration of COM+, see [Automating COM+ Administration](automating-com--administration.md).

## Remarks

You cannot directly create a **COMAdminCatalogCollection** object. To use the methods this object, you must create a [**COMAdminCatalog**](comadmincatalog.md) object, obtain a reference to [**ICOMAdminCatalog**](/windows/desktop/api/ComAdmin/nn-comadmin-icomadmincatalog), and then use [**ICOMAdminCatalog::GetCollection**](/windows/desktop/api/ComAdmin/nf-comadmin-icomadmincatalog-getcollection) to get a reference to an [**ICatalogCollection**](/windows/desktop/api/ComAdmin/nn-comadmin-icatalogcollection) interface that represents a top-level collection. This is shown in the following example, where "TopCollection" must be replaced by the name of one of the top-level COM+ administration collections.


```C++
    HRESULT hr = CoCreateInstance(CLSID_COMAdminCatalog, NULL, 
      CLSCTX_INPROC_SERVER, IID_IUnknown, (void**)&pUnknown);
    if (FAILED (hr)) exit(0);  // Replace with specific error handling.
    hr = pUnknown->QueryInterface(IID_ICOMAdminCatalog, 
      (void**)&pCatalog); 
    if (FAILED (hr)) exit(0);  // Replace with specific error handling.
    hr = pCatalog->GetCollection(L"TopCollection", 
      (IDispatch**)&pTopColl);
    if (FAILED (hr)) exit(0);  // Replace with specific error handling.
```



To use this class from Microsoft Visual Basic, add a reference to the COM+ Admin Type Library. A COMAdminCatalogCollection object can be created by calling [**GetCollection**](/windows/desktop/api/ComAdmin/nf-comadmin-icomadmincatalog-getcollection) on a [**COMAdminCatalog**](comadmincatalog.md) object. This is shown in the following example, where "TopCollection" must be replaced by the name of one of the top-level COM+ administration collections.


```VB
Dim objCatalog As COMAdmin.COMAdminCatalog
Set objCatalog = CreateObject("COMAdmin.COMAdminCatalog")
Dim objTopCollection As COMAdmin.COMAdminCatalogCollection
Set objTopCollection = objCatalog.GetCollection("TopCollection")

```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>ComAdmin.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>ComAdmin.Idl</dt> </dl> |



## See also

<dl> <dt>

[**COMAdminCatalog**](comadmincatalog.md)
</dt> <dt>

[**COMAdminCatalogObject**](comadmincatalogobject.md)
</dt> <dt>

[**ICatalogCollection**](/windows/desktop/api/ComAdmin/nn-comadmin-icatalogcollection)
</dt> </dl>

 

 




