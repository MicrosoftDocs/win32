---
title: Schema Management
description: The ADSI example provider component defines the schema classes \ 0034;Organizational Unit \ 0034; and \ 0034;User \ 0034; and manages these schema classes in the following way.
ms.assetid: c3e07846-a11e-46d4-9863-a89810896ad7
ms.tgt_platform: multiple
keywords:
- Schema Management ADSI
- schema management ADSI
- managing schemas ADSI
- schemas, managing ADSI
- managing a schema ADSI
ms.topic: article
ms.date: 05/31/2018
---

# Schema Management

The ADSI example provider component defines the schema classes "Organizational Unit" and "User" and manages these schema classes in the following way.

The "Organizational Unit" schema class is represented by an ADs container object and can contain other "Organizational Units" and "Users". The container object supports the interfaces [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown), [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch), [**IADs**](/windows/desktop/api/Iads/nn-iads-iads), and [**IADsContainer**](/windows/desktop/api/Iads/nn-iads-iadscontainer). The "User" schema class is represented by a generic Active Directory object and does not contain other types of objects. In the example provider component, the User object is implemented as a generic Active Directory object that supports the interfaces **IUnknown**, **IDispatch**, and **IADs**. Be aware that the User object, in this case, does not support the [**IADsUser**](/windows/desktop/api/Iads/nn-iads-iadsuser) interface.

The example provider component must also implement the ADs namespace object, which supports the interfaces [**IUnknown**](/windows/win32/api/unknwn/nn-unknwn-iunknown), [**IADs**](/windows/desktop/api/Iads/nn-iads-iads), [**IADsContainer**](/windows/desktop/api/Iads/nn-iads-iadscontainer), [**IADsOpenDSObject**](/windows/desktop/api/Iads/nn-iads-iadsopendsobject), and [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch).

The following figure shows the details of the schema that represents the two example provider component schema classes.

![adsi example provider component schema](images/dssmsch.png)

Be aware that in the preceding figure the "Organizational Unit" schema class defines three properties: "Description," "Headcounts," and "ID." The "User" schema class defines four properties: "ID," "Name," "PhoneNumber," and "Title." The "ID" property is shared by both schema classes. Each property is defined by either the "String" or the "Integer" syntax object.

> [!Note]  
> Syntax objects are not present in the first release of the example provider component. However, in most Microsoft ADSI schema implementations, the syntax objects are included in the schema container object, just as the schema class and property objects are. For this reason, they are shown here.

 

This provider component makes schema data accessible to the ADSI client application in the form of ADs class objects, ADs property objects, and ADs syntax objects, all within a schema class container object, so that schema data can be retrieved at run time.

The ADsPaths for the schema class container objects defined for the example provider component are "Sample://Seattle/schema" and "Sample://Toronto/schema". In this example, the contents of the schemas are identical.

 

 