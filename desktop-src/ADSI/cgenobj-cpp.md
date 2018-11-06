---
title: CGENOBJ.CPP
description: In the example provider component, generic Active Directory object methods, supported in cgenobj.cpp, are listed in the following table.
ms.assetid: 72ccdc6e-1f3e-4633-92b3-500309433337
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
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
| Standard [**IADs**](/windows/desktop/api/Iads/nn-iads-iads) methods, including implementations for:                   | [**Get**](/windows/desktop/api/Iads/nf-iads-iads-get) (including mapping from native data type to VARIANT type) [**Put**](/windows/desktop/api/Iads/nf-iads-iads-put) (including mapping from VARIANT type to native data type)<br/> [**GetInfo**](/windows/desktop/api/Iads/nf-iads-iads-getinfo) (refresh the property cache)<br/> [**SetInfo**](/windows/desktop/api/Iads/nf-iads-iads-setinfo) (save the property cache)<br/> |
| Standard [**IADsContainer**](/windows/desktop/api/Iads/nn-iads-iadscontainer) methods, including implementations for: | [**GetObject**](/windows/desktop/api/Iads/nf-iads-iadscontainer-getobject)[**get\_\_NewEnum**](/windows/desktop/api/Iads/nf-iads-iadscontainer-get__newenum)<br/> [**get\_Filter**](iadscontainer-property-methods.md)<br/> [**Create**](/windows/desktop/api/Iads/nf-iads-iadscontainer-create)<br/> [**Delete**](/windows/desktop/api/Iads/nf-iads-iadscontainer-delete)<br/>                                            |
| **ConvertSafeArrayToVariantArray**                                                      | Utility routine.                                                                                                                                                                                                                                                                                                            |



 

 

 





