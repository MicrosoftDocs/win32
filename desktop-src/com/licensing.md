---
title: Licensing
description: Licensing
ms.assetid: a77c0141-62b4-4032-a734-5a55da6a50e0
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Licensing

In order to embed licensed controls successfully, ActiveX control containers must use [**IClassFactory2**](/windows/win32/OCIdl/nn-ocidl-iclassfactory2?branch=master) instead of [**IClassFactory**](/windows/win32/unknwnbase/nn-unknwn-iclassfactory?branch=master). Several OLE creation and loading helper functions ([**OleLoad**](/windows/win32/Ole2/nf-ole2-oleload?branch=master) and [**CoCreateInstance**](/windows/win32/combaseapi/nf-combaseapi-cocreateinstance?branch=master)) explicitly call **IClassFactory** and not **IClassFactory2**, and therefore cannot be used to create or load licensed ActiveX controls. ActiveX control containers should explicitly create and load ActiveX Controls using **IClassFactory2**.

 

 




