---
description: A method provider should implement IWbemServices as the primary interface. However, a pure method provider requires only that you implement the IWbemServices::ExecMethodAsync method.
ms.assetid: 39466513-48f3-4bf6-a3ab-e9d2c387480c
ms.tgt_platform: multiple
title: Implementing the Primary Interface for a Method Provider
ms.topic: article
ms.date: 05/31/2018
---

# Implementing the Primary Interface for a Method Provider

A method provider should implement [**IWbemServices**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemservices) as the primary interface. However, a pure method provider requires only that you implement the [**IWbemServices::ExecMethodAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-execmethodasync) method.

Because other providers use [**IWbemServices**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemservices), the interface contains many methods that are irrelevant to a pure method provider. Your pure method provider should supply a stub implementation that returns WBEM\_E\_PROVIDER\_NOT\_CAPABLE for all of other **IWbemServices** methods besides [**ExecMethodAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-execmethodasync). However, many method providers also serve as instance or class providers. Combination method and instance providers must support more of the **IWbemServices** methods.

 

 



