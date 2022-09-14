---
title: CNAMESP.CPP
description: In the example provider component, code that manages the lifetime of the example provider component namespace object is in cnamesp.cpp. Supported methods are listed in the following table.
ms.assetid: 2f570f87-d8c3-42b1-b8b9-758905bf4b86
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# CNAMESP.CPP

In the example provider component, code that manages the lifetime of the example provider component namespace object is in cnamesp.cpp. Supported methods are listed in the following table.



| Method                                                   | Description                                            |
|----------------------------------------------------------|--------------------------------------------------------|
| **CSampleDSNamespace::CSampleDSNamespace**               | Standard constructor.                                  |
| **CSampleDSNamespace::~CSampleDSNamespace**              | Standard destructor.                                   |
| Standard [**IADs**](/windows/desktop/api/Iads/nn-iads-iads) methods.                   |                                                        |
| Standard [**IADsContainer**](/windows/desktop/api/Iads/nn-iads-iadscontainer) methods. |                                                        |
| **CSampleDSNamespace::AllocateNamespaceObject**          | Create a namespace object and load its type data.      |
| **CSampleDSNamespace::CreateNamespace**                  | Allocate, initialize, and validate a namespace object. |
| **CSampleDSNamespace::QueryInterface**                   | Verify the given IID on this object.                   |



 

 

 




