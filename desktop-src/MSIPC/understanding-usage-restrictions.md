---
title: Understanding usage restrictions
description: All RMS enabled applications must enforce usage restrictions.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: E388B16C-ECDA-4696-A040-D457D3C96766
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Understanding usage restrictions

All RMS enabled applications must enforce usage restrictions. A usage restriction is a condition that results when a user tries to take an action (ex. printing a document), but the RMS policy for that document does not grant them permission or right to perform that action (ex. the PRINT right).

A user's permissions for a document can be queried by using the [**IpcAccessCheck**](ipcaccesscheck.md) function.

## Understanding usage restrictions

-   Familiarize yourself with standard RMS rights

    For the full set of RMS rights your application may enforce, see [Usage restriction reference](usage-restriction-reference.md).

    Note that application defined rights specific to your situation and that go beyond the standard RMS rights may be created.

-   Identify usage restriction enforcement points

    A *usage restriction enforcement point* is a place in your application's control flow where you need to enforce a usage restriction. The [Usage restriction reference](usage-restriction-reference.md) topic gives several examples of common enforcement points.

    Evaluate your own application to determine which usage restriction enforcement points apply.

    Your application may not need all enforcement points described in [Usage restriction reference](usage-restriction-reference.md). For example, if your application does not allow users to print content, it does not need to check for the **IPC\_GENERIC\_PRINT** right.

-   Update your code to perform an access check at each enforcement point

    For guidance about how to enforce specific rights, see [Usage restriction reference](usage-restriction-reference.md).

## Related topics

<dl> <dt>

[**IpcAccessCheck**](ipcaccesscheck.md)
</dt> <dt>

[Usage restriction reference](usage-restriction-reference.md)
</dt> </dl>

 

 




