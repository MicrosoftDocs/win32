---
title: CENUMVAR.CPP
description: In the example provider component, the base implementation for xxxEnumVariant derived classes can be found in cenumvar.cpp. Associated methods are listed in the following table.
ms.assetid: 6b38bc99-25d4-40af-863a-9cc37f786d9b
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# CENUMVAR.CPP

In the example provider component, the base implementation for xxxEnumVariant derived classes can be found in cenumvar.cpp. Associated methods are listed in the following table.



| Method                                          | Description                                                                           |
|-------------------------------------------------|---------------------------------------------------------------------------------------|
| **CSampleDSEnumVariant::CSampleDSEnumVariant**  | Standard constructor.                                                                 |
| **CSampleDSEnumVariant::~CSampleDSEnumVariant** | Standard destructor.                                                                  |
| **CSampleDSEnumVariant::QueryInterface**        | Standard [**IUnknown::QueryInterface**](/windows/win32/api/unknwn/nf-unknwn-iunknown-queryinterface(q)) implementation. |
| **CSampleDSEnumVariant::AddRef**                | Standard [**IUnknown::AddRef**](/windows/win32/api/unknwn/nf-unknwn-iunknown-addref) implementation.                 |
| **CSampleDSEnumVariant::Release**               | Standard [**IUnknown::Release**](/windows/win32/api/unknwn/nf-unknwn-iunknown-release) implementation.               |
| **CSampleDSEnumVariant::Skip**                  | Standard **IEnumXXXX::Skip** implementation.                                          |
| **CSampleDSEnumVariant::Reset**                 | Standard **IEnumXXXX::Reset** implementation.                                         |
| **CSampleDSEnumVariant::Clone**                 | Standard **IEnumXXXX::Clone** implementation.                                         |



 

 

 