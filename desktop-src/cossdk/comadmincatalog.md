---
description: Accesses the data that is stored in the COM+ catalog.
ms.assetid: d77123f6-9821-4c80-860c-5f1feaca7987
title: COMAdminCatalog class (ComAdmin.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- COMAdminCatalog
api_type: 
- COM
api_location: 
- ComAdmin.Idl
---

# COMAdminCatalog class

Accesses the data that is stored in the COM+ catalog.

## When to implement

This class is implemented by COM+.



| Requirement | Value |
|------------|-------------------------------------------------------------------------------------------------------------------|
| CLSID      | CLSID\_COMAdminCatalog                                                                                            |
| ProgID     | L"COMAdmin.COMAdminCatalog"                                                                                       |
| Interfaces | [**ICOMAdminCatalog**](/windows/desktop/api/ComAdmin/nn-comadmin-icomadmincatalog)<br/> [**ICOMAdminCatalog2**](/windows/desktop/api/ComAdmin/nn-comadmin-icomadmincatalog2)<br/> |



 

## When to use

You use objects created from the **COMAdminCatalog** class to begin programmatic access to COM+ configuration data stored in the COM+ catalog. This information underlies the folders and items in the console tree of the Component Services administration tool. The **COMAdminCatalog** class enables you to access collections in the catalog, install COM+ applications and components, start and stop services, and connect to and administer remote servers.

Folders in the Component Services administration tool correspond to collections in the catalog, which you can represent by using objects created from the [**COMAdminCatalogCollection**](comadmincatalogcollection.md) class. Items in the folders correspond to items in the collections, which you can represent by using objects created from the [**COMAdminCatalogObject**](comadmincatalogobject.md) class.

Not all of the collections and items exposed through [**COMAdminCatalogCollection**](comadmincatalogcollection.md) and [**COMAdminCatalogObject**](comadmincatalogobject.md) are available in the Component Services administration tool.

For information regarding specific collections and their properties, see [COM+ Administration Collections](com--administration-collections.md).

For an introduction to programmatic administration of COM+, see [Automating COM+ Administration](automating-com--administration.md).

## Remarks

To create this object, call [**CoCreateInstance**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstance).

To use this class from Microsoft Visual Basic, add a reference to the COM+ Admin Type Library. A COMAdminCatalog object can be declared using "COMAdmin.COMAdminCatalog" as the class name.

In COM+ 1.5, released with Windows XP, the **COMAdminCatalog** class implements the [**ICOMAdminCatalog2**](/windows/desktop/api/ComAdmin/nn-comadmin-icomadmincatalog2) interface. However, in COM+ 1.0, released with Windows 2000, the **COMAdminCatalog** class implements only the [**ICOMAdminCatalog**](/windows/desktop/api/ComAdmin/nn-comadmin-icomadmincatalog) interface.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>ComAdmin.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>ComAdmin.Idl</dt> </dl> |



## See also

<dl> <dt>

[**COMAdminCatalogCollection**](comadmincatalogcollection.md)
</dt> <dt>

[**COMAdminCatalogObject**](comadmincatalogobject.md)
</dt> <dt>

[**ICOMAdminCatalog**](/windows/desktop/api/ComAdmin/nn-comadmin-icomadmincatalog)
</dt> <dt>

[**ICOMAdminCatalog2**](/windows/desktop/api/ComAdmin/nn-comadmin-icomadmincatalog2)
</dt> </dl>

 

