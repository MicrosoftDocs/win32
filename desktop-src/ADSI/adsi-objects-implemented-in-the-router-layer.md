---
title: ADSI Objects Implemented in the Router Layer
description: The following table presents a brief description of the COM objects implemented in the ADSI router.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: bd446e05-a15d-4354-9204-1df4e360497c
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ADSI Objects Implemented in the Router Layer

The following table presents a brief description of the COM objects implemented in the ADSI router.



| ADSI Object            | Description                                                         | Supported Interfaces                                                                                                                                                                                                                                                                      |
|------------------------|---------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **AccessControlEntry** | An ADSI object that represents an access control entry (ACE).       | [**IADsAccessControlEntry**](/windows/win32/Iads/nn-iads-iadsaccesscontrolentry?branch=master)                                                                                                                                                                                                                                  |
| **AccessControlList**  | An ADSI object that represents an access control list (ACL).        | [**IADsAccessControlList**](/windows/win32/Iads/nn-iads-iadsaccesscontrollist?branch=master)                                                                                                                                                                                                                                    |
| **ADsNamespaces**      | An ADSI object that represents the container of various namespaces. | <dl> <dt>[**IADs**](/windows/win32/Iads/nn-iads-iads?branch=master)</dt> <dt>[**IADsContainer**](/windows/win32/Iads/nn-iads-iadscontainer?branch=master)</dt> <dt>[**IADsNamespaces**](/windows/win32/Iads/nn-iads-iadsnamespaces?branch=master)</dt> </dl> |
| **LargeInteger**       | An ADSI object that represents a large integer.                     | [**IADsLargeInteger**](/windows/win32/Iads/nn-iads-iadslargeinteger?branch=master)                                                                                                                                                                                                                                              |
| **PropertyEntry**      | An ADSI object that represents a property entry.                    | [**IADsPropertyEntry**](/windows/win32/Iads/nn-iads-iadspropertyentry?branch=master)                                                                                                                                                                                                                                            |
| **PropertyValue**      | An ADSI object that represents a property value.                    | [**IADsPropertyValue**](/windows/win32/Iads/nn-iads-iadspropertyvalue?branch=master)                                                                                                                                                                                                                                            |
| **PropertyValue2**     | An ADSI object that represents a property value.                    | [**IADsPropertyValue2**](/windows/win32/Iads/nn-iads-iadspropertyvalue2?branch=master)                                                                                                                                                                                                                                          |
| **SecurityDescriptor** | An ADSI object that represents a security descriptor.               | [**IADsSecurityDescriptor**](/windows/win32/Iads/nn-iads-iadssecuritydescriptor?branch=master)                                                                                                                                                                                                                                  |



 

 

 




