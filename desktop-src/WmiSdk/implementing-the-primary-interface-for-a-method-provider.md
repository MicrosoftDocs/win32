---
Description: 'A method provider should implement IWbemServices as the primary interface. However, a pure method provider requires only that you implement the IWbemServices::ExecMethodAsync method.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: '39466513-48f3-4bf6-a3ab-e9d2c387480c'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: Implementing the Primary Interface for a Method Provider
---

# Implementing the Primary Interface for a Method Provider

A method provider should implement [**IWbemServices**](iwbemservices.md) as the primary interface. However, a pure method provider requires only that you implement the [**IWbemServices::ExecMethodAsync**](iwbemservices-execmethodasync.md) method.

Because other providers use [**IWbemServices**](iwbemservices.md), the interface contains many methods that are irrelevant to a pure method provider. Your pure method provider should supply a stub implementation that returns WBEM\_E\_PROVIDER\_NOT\_CAPABLE for all of other **IWbemServices** methods besides [**ExecMethodAsync**](iwbemservices-execmethodasync.md). However, many method providers also serve as instance or class providers. Combination method and instance providers must support more of the **IWbemServices** methods.

 

 



