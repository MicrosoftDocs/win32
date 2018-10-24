---
title: CENUMVAR.CPP
description: In the example provider component, the base implementation for xxxEnumVariant derived classes can be found in cenumvar.cpp. Associated methods are listed in the following table.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 6b38bc99-25d4-40af-863a-9cc37f786d9b
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CENUMVAR.CPP

In the example provider component, the base implementation for xxxEnumVariant derived classes can be found in cenumvar.cpp. Associated methods are listed in the following table.



| Method                                          | Description                                                                           |
|-------------------------------------------------|---------------------------------------------------------------------------------------|
| **CSampleDSEnumVariant::CSampleDSEnumVariant**  | Standard constructor.                                                                 |
| **CSampleDSEnumVariant::~CSampleDSEnumVariant** | Standard destructor.                                                                  |
| **CSampleDSEnumVariant::QueryInterface**        | Standard [**IUnknown::QueryInterface**](https://msdn.microsoft.com/en-us/library/ms682521(v=VS.85).aspx) implementation. |
| **CSampleDSEnumVariant::AddRef**                | Standard [**IUnknown::AddRef**](https://msdn.microsoft.com/en-us/library/ms691379(v=VS.85).aspx) implementation.                 |
| **CSampleDSEnumVariant::Release**               | Standard [**IUnknown::Release**](https://msdn.microsoft.com/en-us/library/ms682317(v=VS.85).aspx) implementation.               |
| **CSampleDSEnumVariant::Skip**                  | Standard **IEnumXXXX::Skip** implementation.                                          |
| **CSampleDSEnumVariant::Reset**                 | Standard **IEnumXXXX::Reset** implementation.                                         |
| **CSampleDSEnumVariant::Clone**                 | Standard **IEnumXXXX::Clone** implementation.                                         |



 

 

 




