---
description: A provider is not required to support any partial-instance operations. However, a provider must either support all the semantics of a partial-instance operation, process a complete instance, or return WBEM\_E\_UNSUPPORTED\_PARAMETER.
ms.assetid: bc498655-ad6d-44f5-912d-9b7ee95825ec
ms.tgt_platform: multiple
title: Supporting Partial-Instance Operations
ms.topic: article
ms.date: 05/31/2018
---

# Supporting Partial-Instance Operations

A provider is not required to support any partial-instance operations. However, a provider must either support all the semantics of a partial-instance operation, process a complete instance, or return **WBEM\_E\_UNSUPPORTED\_PARAMETER**.

When creating a provider that supports partial-instance operations, you must observe the following rules:

-   Reuse the same context object that WMI sends to the provider. WMI uses the "\_\_GET\_EXT\_CLIENT\_REQUEST" named value to prevent deadlocks and removes this client before forwarding the context object to a provider.
-   For reentrant calls back into WMI that do not require a partial-instance operation, ensure to pass back the same context object without any modifications. WMI receives the context object without the "\_\_GET\_EXT\_CLIENT\_REQUEST" named value set and deletes all named values associated with partial-instance operations from the context object before passing it to other providers. Not changing the context object blocks other providers from receiving partial-instance retrieval operations intended for a different, unrelated object.
-   To perform a reentrant partial-instance operation while carrying out a request, set the missing "\_\_GET\_EXT\_CLIENT\_REQUEST" named value and property clear. Optionally, you can modify the properties in the "\_\_GET\_EXT\_PROPERTIES" named value before sending the context object back into WMI with the reentrant call.
-   Do not access the context object after you return it to WMI during a reentrant call; other providers may modify the property lists or other values during reentrancy. You can examine or modify the context object only for the duration of the [**IWbemServices**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemservices) call that you implement.

 

 



