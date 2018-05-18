---
title: Revisiting COM Aggregation Rules with ADSI Extensions
description: The following is a brief review of COM aggregation and ADSI extension rules.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '3efcdfcf-4965-4436-90b2-dc0f627c71b4'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-domain-services'
ms.tgt_platform: multiple
keywords: ["Extensions ADSI , COM Aggregation Rules", "COM Aggregation ADSI", "Revisiting COM Aggregation Rules with ADSI Extensions ADSI"]
---

# Revisiting COM Aggregation Rules with ADSI Extensions

The following is a brief review of COM aggregation and ADSI extension rules.

-   The **CreateInstance** method returns a pointer to an [**IUnknown**](_com_iunknown) interface, as follows, that does not delegate any function calls to the aggregator.

    The [**IUnknown::QueryInterface**](_com_iunknown_queryinterface) method returns pointers to the interfaces that it supports, and errors for interfaces it does not support.

    The [**IUnknown::AddRef**](_com_iunknown_addref) method increments the reference count on the aggregated extension object itself.

    The [**IUnkown::Release**](_com_iunknown_release) method decrements the reference count on the aggregated extension object itself and destroys itself when the reference count is 0.

-   The extension object should store the [**IUnknown**](_com_iunknown) pointer of the aggregator, such as m\_pOuterUnknown, during the implementation of the **CreateInstance** method.
-   All interfaces that the extension object supports, including [**IADsExtension**](iadsextension.md), should inherit from [**IUnknown**](_com_iunknown), which delegates all function calls back to the aggregator.
    -   [**IUnknown::QueryInterface**](_com_iunknown_queryinterface) calls "m\_pOuterUnknown-&gt;QueryInterface"
    -   [**IUnknown::AddRef**](_com_iunknown_addref) calls "m\_pOuterUnknown-&gt;AddRef"
    -   [**IUnkown::Release**](_com_iunknown_release) calls "m\_pOuterUnknown-&gt;Release"

Extension writers can choose any internal implementation they prefer as long as they obey standard COM aggregation rules. Be aware that an extension object does not have to work as a standalone object. Extensions are designed to work as aggregates. However, an extension can be written to work as both a standalone object and as an aggregate.

In addition to standard COM aggregation support, an extension object may support [**IADsExtension**](iadsextension.md) for more advanced features. If late binding is supported, the extension should:

-   Delegate functions for [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) back to the aggregator.
-   Implement the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface in [**IADsExtension**](iadsextension.md).

 

 




