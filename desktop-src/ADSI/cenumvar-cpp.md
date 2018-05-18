---
title: CENUMVAR.CPP
description: In the example provider component, the base implementation for xxxEnumVariant derived classes can be found in cenumvar.cpp. Associated methods are listed in the following table.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '6b38bc99-25d4-40af-863a-9cc37f786d9b'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
---

# CENUMVAR.CPP

In the example provider component, the base implementation for xxxEnumVariant derived classes can be found in cenumvar.cpp. Associated methods are listed in the following table.



| Method                                          | Description                                                                           |
|-------------------------------------------------|---------------------------------------------------------------------------------------|
| **CSampleDSEnumVariant::CSampleDSEnumVariant**  | Standard constructor.                                                                 |
| **CSampleDSEnumVariant::~CSampleDSEnumVariant** | Standard destructor.                                                                  |
| **CSampleDSEnumVariant::QueryInterface**        | Standard [**IUnknown::QueryInterface**](_com_iunknown_queryinterface) implementation. |
| **CSampleDSEnumVariant::AddRef**                | Standard [**IUnknown::AddRef**](_com_iunknown_addref) implementation.                 |
| **CSampleDSEnumVariant::Release**               | Standard [**IUnknown::Release**](_com_iunknown_release) implementation.               |
| **CSampleDSEnumVariant::Skip**                  | Standard **IEnumXXXX::Skip** implementation.                                          |
| **CSampleDSEnumVariant::Reset**                 | Standard **IEnumXXXX::Reset** implementation.                                         |
| **CSampleDSEnumVariant::Clone**                 | Standard **IEnumXXXX::Clone** implementation.                                         |



 

 

 




