---
title: ADSI Objects Implemented in the Router Layer
description: The following table presents a brief description of the COM objects implemented in the ADSI router.
ms.assetid: bd446e05-a15d-4354-9204-1df4e360497c
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# ADSI Objects Implemented in the Router Layer

The following table presents a brief description of the COM objects implemented in the ADSI router.



| ADSI Object            | Description                                                         | Supported Interfaces                                                                                                                                                                                                                                                                      |
|------------------------|---------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **AccessControlEntry** | An ADSI object that represents an access control entry (ACE).       | [**IADsAccessControlEntry**](/windows/desktop/api/Iads/nn-iads-iadsaccesscontrolentry)                                                                                                                                                                                                                                  |
| **AccessControlList**  | An ADSI object that represents an access control list (ACL).        | [**IADsAccessControlList**](/windows/desktop/api/Iads/nn-iads-iadsaccesscontrollist)                                                                                                                                                                                                                                    |
| **ADsNamespaces**      | An ADSI object that represents the container of various namespaces. | <dl> <dt>[**IADs**](/windows/desktop/api/Iads/nn-iads-iads)</dt> <dt>[**IADsContainer**](/windows/desktop/api/Iads/nn-iads-iadscontainer)</dt> <dt>[**IADsNamespaces**](/windows/desktop/api/Iads/nn-iads-iadsnamespaces)</dt> </dl> |
| **LargeInteger**       | An ADSI object that represents a large integer.                     | [**IADsLargeInteger**](/windows/desktop/api/Iads/nn-iads-iadslargeinteger)                                                                                                                                                                                                                                              |
| **PropertyEntry**      | An ADSI object that represents a property entry.                    | [**IADsPropertyEntry**](/windows/desktop/api/Iads/nn-iads-iadspropertyentry)                                                                                                                                                                                                                                            |
| **PropertyValue**      | An ADSI object that represents a property value.                    | [**IADsPropertyValue**](/windows/desktop/api/Iads/nn-iads-iadspropertyvalue)                                                                                                                                                                                                                                            |
| **PropertyValue2**     | An ADSI object that represents a property value.                    | [**IADsPropertyValue2**](/windows/desktop/api/Iads/nn-iads-iadspropertyvalue2)                                                                                                                                                                                                                                          |
| **SecurityDescriptor** | An ADSI object that represents a security descriptor.               | [**IADsSecurityDescriptor**](/windows/desktop/api/Iads/nn-iads-iadssecuritydescriptor)                                                                                                                                                                                                                                  |



 

 

 




