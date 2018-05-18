---
title: CSCHOBJ.CPP
description: In the example provider component, a code example, that manages the lifetime of the schema objects, is in cschobj.cpp. Supported methods are listed in the following table.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 'ed8cc113-2ada-4522-87b9-32c922e89819'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
---

# CSCHOBJ.CPP

In the example provider component, a code example, that manages the lifetime of the schema objects, is in cschobj.cpp. Supported methods are listed in the following table.



| Method                                                   | Description                                    |
|----------------------------------------------------------|------------------------------------------------|
| **CSampleDSSchema::CreateSchema**                        | Standard constructor.                          |
| **CSampleDSSchema::~CSampleDSSchema**                    | Standard destructor.                           |
| Standard [**IADs**](iads.md) methods.                   |                                                |
| Standard [**IADsContainer**](iadscontainer.md) methods. |                                                |
| **CSampleDSSchema::QueryInterface**                      | Verify the given interface ID on this object.  |
| **CSampleDSSchema::AllocateSchema**                      | Create a schema object and load its type data. |



 

 

 




