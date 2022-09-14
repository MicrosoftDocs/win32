---
title: Licensing
description: Licensing
ms.assetid: a77c0141-62b4-4032-a734-5a55da6a50e0
ms.topic: article
ms.date: 05/31/2018
---

# Licensing

In order to embed licensed controls successfully, ActiveX control containers must use [**IClassFactory2**](/windows/desktop/api/OCIdl/nn-ocidl-iclassfactory2) instead of [**IClassFactory**](/windows/win32/api/unknwn/nn-unknwn-iclassfactory). Several OLE creation and loading helper functions ([**OleLoad**](/windows/desktop/api/Ole2/nf-ole2-oleload) and [**CoCreateInstance**](/windows/desktop/api/combaseapi/nf-combaseapi-cocreateinstance)) explicitly call **IClassFactory** and not **IClassFactory2**, and therefore cannot be used to create or load licensed ActiveX controls. ActiveX control containers should explicitly create and load ActiveX Controls using **IClassFactory2**.

 

 