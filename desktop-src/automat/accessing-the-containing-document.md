---
title: Accessing the Containing Document
description: Describes how to access the programmability interface of a container.
ms.assetid: 39eebc21-b5ae-4bd9-9a5b-b64772182d4d
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Accessing the Containing Document

Objects that are embedded in a container often require access to that container's programmability interface (for example, its **IDispatch** implementation). The container should implement its document-level programmabity interface (for example, the Document object) that matches the one used by **IOleContainer** (either VTBL or [**IDispatch**](/windows/previous-versions/oaidl/nn-oaidl-idispatch?branch=master)). To access the containing document, an object can call **IOleClientSite::GetContainer**, which returns a pointer to **IOleContainer**, and can then call **QueryInterface** for the appropriate interface (usually **IID\_IDispatch**).

Embedded objects can also access type information by using VTBL binding to dual interfaces, calling **QueryInterface** to **IOleContainer** for **IProvideClassInfo**.

 

 




