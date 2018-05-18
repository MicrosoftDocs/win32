---
title: CPROV.CPP
description: In the example provider component, a code example used to implement the ADs provider object is found in cprov.cpp. Supported methods are listed in the following table.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '606d3539-0d87-4706-a4d1-e71fa25156c1'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
---

# CPROV.CPP

In the example provider component, a code example used to implement the ADs provider object is found in cprov.cpp. Supported methods are listed in the following table.



| Item                                      | Description                                         |
|-------------------------------------------|-----------------------------------------------------|
| **CSampleDSProvider::CSampleDSProvider**  | Standard creator.                                   |
| **CSampleDSProvider::~CSampleDSProvider** | Standard destructor.                                |
| **CSampleDSProvider::Create**             | Create the object.                                  |
| **CSampleDSProvider::QueryInterface**     | Check for supported interfaces.                     |
| **CSampleDSProvider::ParseDisplayName**   | Resolve the path.                                   |
| **CSampleDSProvider::ResolvePathName**    | Get the object and create a pointer moniker for it. |



 

 

 




