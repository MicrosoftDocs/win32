---
title: Releasing OLE and Objects
description: To release OLE and the exposed objects, use the RevokeActiveObject, CoRevokeClassObject, and OLEUninitialize functions.
ms.assetid: 6e84a44b-e961-43c7-bb76-071376ec8e2b
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Releasing OLE and Objects

To release OLE and the exposed objects, use the following functions:

-   [**RevokeActiveObject**](/windows/previous-versions/OleAuto/nf-oleauto-revokeactiveobject?branch=master) — Ends an object's status as the active object.

-   [**CoRevokeClassObject**](https://msdn.microsoft.com/library/windows/desktop/ms688650) — Informs OLE that a class factory is no longer available for use by other applications.

-   [OLEUninitialize](https://msdn.microsoft.com/library/windows/desktop/ms691326) — Releases OLE.

For more information on **OleUninitialize** and **CoRevokeClassObject**, see the *COM Programmers Reference*.

 

 




