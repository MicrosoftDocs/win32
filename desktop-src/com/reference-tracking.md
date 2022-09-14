---
title: Reference Tracking
description: Reference Tracking
ms.assetid: 1e2cf555-3b96-42d5-a0bb-abb720c93520
ms.topic: article
ms.date: 05/31/2018
---

# Reference Tracking

Reference tracking can prevent the unintentional or malicious early release of objects.

When you enable reference tracking, you are requesting that distributed [**AddRef**](/windows/win32/api/unknwn/nf-unknwn-iunknown-addref) and [**Release**](/windows/win32/api/unknwn/nf-unknwn-iunknown-release) calls be authenticated by COM. When reference tracking is enabled, COM keeps track of per-user reference counts so that a user can call **Release** only on objects that the user previously called **AddRef** on. Although reference tracking can decrease performance, it ensures that no matter how many times a given user calls **Release**, the objects and stubs will still exist if someone else has a reference to them.

The client can set reference tracking for a process by passing the EOAC\_SECURE\_REFS capability flag in a call to [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity). You can also enable or disable reference tracking for all applications on a computer by using Dcomcnfg.exe.

If reference tracking is enabled, [**IUnknown**](/windows/desktop/api/Unknwn/nn-unknwn-iunknown) always uses default security settings. In this case, calls to [**CoSetProxyBlanket**](/windows/desktop/api/combaseapi/nf-combaseapi-cosetproxyblanket) on **IUnknown** will fail.

 

 