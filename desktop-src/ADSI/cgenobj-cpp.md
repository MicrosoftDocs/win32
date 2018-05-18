---
title: CGENOBJ.CPP
description: In the example provider component, generic Active Directory object methods, supported in cgenobj.cpp, are listed in the following table.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '72ccdc6e-1f3e-4633-92b3-500309433337'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
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
| Standard [**IADs**](iads.md) methods, including implementations for:                   | [**Get**](iads-get.md) (including mapping from native data type to VARIANT type) [**Put**](iads-put.md) (including mapping from VARIANT type to native data type)<br/> [**GetInfo**](iads-getinfo.md) (refresh the property cache)<br/> [**SetInfo**](iads-setinfo.md) (save the property cache)<br/> |
| Standard [**IADsContainer**](iadscontainer.md) methods, including implementations for: | [**GetObject**](iadscontainer-getobject.md)[**get\_\_NewEnum**](iadscontainer-get--newenum.md)<br/> [**get\_Filter**](iadscontainer-property-methods.md)<br/> [**Create**](iadscontainer-create.md)<br/> [**Delete**](iadscontainer-delete.md)<br/>                                            |
| **ConvertSafeArrayToVariantArray**                                                      | Utility routine.                                                                                                                                                                                                                                                                                                            |



 

 

 





