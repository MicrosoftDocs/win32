---
title: ADSI Objects Implemented in the Router Layer
description: The following table presents a brief description of the COM objects implemented in the ADSI router.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 'bd446e05-a15d-4354-9204-1df4e360497c'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
---

# ADSI Objects Implemented in the Router Layer

The following table presents a brief description of the COM objects implemented in the ADSI router.



| ADSI Object            | Description                                                         | Supported Interfaces                                                                                                                                                                                                                                                                      |
|------------------------|---------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **AccessControlEntry** | An ADSI object that represents an access control entry (ACE).       | [**IADsAccessControlEntry**](iadsaccesscontrolentry.md)                                                                                                                                                                                                                                  |
| **AccessControlList**  | An ADSI object that represents an access control list (ACL).        | [**IADsAccessControlList**](iadsaccesscontrollist.md)                                                                                                                                                                                                                                    |
| **ADsNamespaces**      | An ADSI object that represents the container of various namespaces. | <dl> <dt>[**IADs**](iads.md)</dt> <dt>[**IADsContainer**](iadscontainer.md)</dt> <dt>[**IADsNamespaces**](iadsnamespaces.md)</dt> </dl> |
| **LargeInteger**       | An ADSI object that represents a large integer.                     | [**IADsLargeInteger**](iadslargeinteger.md)                                                                                                                                                                                                                                              |
| **PropertyEntry**      | An ADSI object that represents a property entry.                    | [**IADsPropertyEntry**](iadspropertyentry.md)                                                                                                                                                                                                                                            |
| **PropertyValue**      | An ADSI object that represents a property value.                    | [**IADsPropertyValue**](iadspropertyvalue.md)                                                                                                                                                                                                                                            |
| **PropertyValue2**     | An ADSI object that represents a property value.                    | [**IADsPropertyValue2**](iadspropertyvalue2.md)                                                                                                                                                                                                                                          |
| **SecurityDescriptor** | An ADSI object that represents a security descriptor.               | [**IADsSecurityDescriptor**](iadssecuritydescriptor.md)                                                                                                                                                                                                                                  |



 

 

 




