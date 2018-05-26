---
Description: A method provider should implement IWbemServices as the primary interface. However, a pure method provider requires only that you implement the IWbemServicesExecMethodAsync method.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 39466513-48f3-4bf6-a3ab-e9d2c387480c
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: Implementing the Primary Interface for a Method Provider
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Implementing the Primary Interface for a Method Provider

A method provider should implement [**IWbemServices**](/windows/win32/WbemCli/nn-wbemcli-iwbemservices?branch=master) as the primary interface. However, a pure method provider requires only that you implement the [**IWbemServices::ExecMethodAsync**](/windows/win32/WbemCli/nf-wbemcli-iwbemservices-execmethodasync?branch=master) method.

Because other providers use [**IWbemServices**](/windows/win32/WbemCli/nn-wbemcli-iwbemservices?branch=master), the interface contains many methods that are irrelevant to a pure method provider. Your pure method provider should supply a stub implementation that returns WBEM\_E\_PROVIDER\_NOT\_CAPABLE for all of other **IWbemServices** methods besides [**ExecMethodAsync**](/windows/win32/WbemCli/nf-wbemcli-iwbemservices-execmethodasync?branch=master). However, many method providers also serve as instance or class providers. Combination method and instance providers must support more of the **IWbemServices** methods.

 

 



