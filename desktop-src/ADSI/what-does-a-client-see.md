---
title: What Does a Client See
description: This topic lists ways that a client views ADSI data.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 238eeea9-1303-4d37-bf09-ad03f1790c1b
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- extensions ADSI ,what does a client see
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# What Does a Client See?

-   A client sees ADSI and all of its extension objects as one object.
-   An ADSI client sees one [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface that handles all the dual and dispatch interfaces in the object, whether the dual or dispatch interface is implemented by the aggregator in the provider or by an extension. Please see [Resolution of Function/Property Name Conflicts in Automation in Extensions](resolution-of-functionproperty-name-conflicts-in-automation-in-extensions.md).
-   ADSI does not expose any type information through the [**IDispatch::GetTypeInfo**](cc1ec9aa-6c40-4e70-819c-a7c6dd6b8c99) or [**IDispatch::GetTypeInfoCount**](da876d53-cb8a-465c-a43e-c0eb272e2a12) methods. ADSI provides type information through the type library.

 

 




