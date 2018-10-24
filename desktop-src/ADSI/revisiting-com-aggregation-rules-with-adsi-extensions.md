---
title: Revisiting COM Aggregation Rules with ADSI Extensions
description: The following is a brief review of COM aggregation and ADSI extension rules.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 3efcdfcf-4965-4436-90b2-dc0f627c71b4
ms.tgt_platform: multiple
keywords:
- Extensions ADSI , COM Aggregation Rules
- COM Aggregation ADSI
- Revisiting COM Aggregation Rules with ADSI Extensions ADSI
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Revisiting COM Aggregation Rules with ADSI Extensions

The following is a brief review of COM aggregation and ADSI extension rules.

-   The **CreateInstance** method returns a pointer to an [**IUnknown**](https://msdn.microsoft.com/en-us/library/ms680509(v=VS.85).aspx) interface, as follows, that does not delegate any function calls to the aggregator.

    The [**IUnknown::QueryInterface**](https://msdn.microsoft.com/en-us/library/ms682521(v=VS.85).aspx) method returns pointers to the interfaces that it supports, and errors for interfaces it does not support.

    The [**IUnknown::AddRef**](https://msdn.microsoft.com/en-us/library/ms691379(v=VS.85).aspx) method increments the reference count on the aggregated extension object itself.

    The [**IUnkown::Release**](https://msdn.microsoft.com/en-us/library/ms682317(v=VS.85).aspx) method decrements the reference count on the aggregated extension object itself and destroys itself when the reference count is 0.

-   The extension object should store the [**IUnknown**](https://msdn.microsoft.com/en-us/library/ms680509(v=VS.85).aspx) pointer of the aggregator, such as m\_pOuterUnknown, during the implementation of the **CreateInstance** method.
-   All interfaces that the extension object supports, including [**IADsExtension**](/windows/desktop/api/Iads/nn-iads-iadsextension), should inherit from [**IUnknown**](https://msdn.microsoft.com/en-us/library/ms680509(v=VS.85).aspx), which delegates all function calls back to the aggregator.
    -   [**IUnknown::QueryInterface**](https://msdn.microsoft.com/en-us/library/ms682521(v=VS.85).aspx) calls "m\_pOuterUnknown->QueryInterface"
    -   [**IUnknown::AddRef**](https://msdn.microsoft.com/en-us/library/ms691379(v=VS.85).aspx) calls "m\_pOuterUnknown->AddRef"
    -   [**IUnkown::Release**](https://msdn.microsoft.com/en-us/library/ms682317(v=VS.85).aspx) calls "m\_pOuterUnknown->Release"

Extension writers can choose any internal implementation they prefer as long as they obey standard COM aggregation rules. Be aware that an extension object does not have to work as a standalone object. Extensions are designed to work as aggregates. However, an extension can be written to work as both a standalone object and as an aggregate.

In addition to standard COM aggregation support, an extension object may support [**IADsExtension**](/windows/desktop/api/Iads/nn-iads-iadsextension) for more advanced features. If late binding is supported, the extension should:

-   Delegate functions for [**IDispatch**](https://msdn.microsoft.com/en-us/library/ms221608(v=VS.71).aspx) back to the aggregator.
-   Implement the [**IDispatch**](https://msdn.microsoft.com/en-us/library/ms221608(v=VS.71).aspx) interface in [**IADsExtension**](/windows/desktop/api/Iads/nn-iads-iadsextension).

 

 




