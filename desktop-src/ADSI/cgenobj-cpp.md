---
title: CGENOBJ.CPP
description: In the example provider component, generic Active Directory object methods, supported in cgenobj.cpp, are listed in the following table.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 72ccdc6e-1f3e-4633-92b3-500309433337
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CGENOBJ.CPP

In the example provider component, generic Active Directory object methods, supported in cgenobj.cpp, are listed in the following table.



| Method                                                                                  | Description                                                                                                                                                                                                                                                                                                                 |
|-----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **CSampleDSGenObject::CSampleDSGenObject**                                              | Standard constructor.                                                                                                                                                                                                                                                                                                       |
| **CSampleDSGenObject::~CSampleDSGenObject**                                             | Standard destructor.                                                                                                                                                                                                                                                                                                        |
| **CSampleDSGenObject::CreateGenericObject**                                             | Create an ADS generic object. Initialize as appropriate.                                                                                                                                                                                                                                                                    |
| **CSampleDSGenObject::SampleDSCreateObject**                                            | Create this object in its parent container.                                                                                                                                                                                                                                                                                 |
| **CSampleDSGenObject::SampleDSSetObject**                                               | Save the properties of this object (clear the cache).                                                                                                                                                                                                                                                                       |
| **CSampleDSGenObject::AllocateGenObject**                                               | Create a generic object and load its type data.                                                                                                                                                                                                                                                                             |
| **CSampleDSGenObject::QueryInterface**                                                  | Return the requested interface pointer, if available.                                                                                                                                                                                                                                                                       |
| Standard [**IADs**](/windows/win32/Iads/nn-iads-iads?branch=master) methods, including implementations for:                   | [**Get**](/windows/win32/Iads/nf-iads-iads-get?branch=master) (including mapping from native data type to VARIANT type) [**Put**](/windows/win32/Iads/nf-iads-iads-put?branch=master) (including mapping from VARIANT type to native data type)<br/> [**GetInfo**](/windows/win32/Iads/nf-iads-iads-getinfo?branch=master) (refresh the property cache)<br/> [**SetInfo**](/windows/win32/Iads/nf-iads-iads-setinfo?branch=master) (save the property cache)<br/> |
| Standard [**IADsContainer**](/windows/win32/Iads/nn-iads-iadscontainer?branch=master) methods, including implementations for: | [**GetObject**](/windows/win32/Iads/nf-iads-iadscontainer-getobject?branch=master)[**get\_\_NewEnum**](/windows/win32/Iads/nf-iads-iadscontainer-get__newenum?branch=master)<br/> [**get\_Filter**](iadscontainer-property-methods.md)<br/> [**Create**](/windows/win32/Iads/nf-iads-iadscontainer-create?branch=master)<br/> [**Delete**](/windows/win32/Iads/nf-iads-iadscontainer-delete?branch=master)<br/>                                            |
| **ConvertSafeArrayToVariantArray**                                                      | Utility routine.                                                                                                                                                                                                                                                                                                            |



 

 

 





