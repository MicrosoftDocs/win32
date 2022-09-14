---
title: MIDL Binding Handles
description: Binding handles are data objects that represent the binding between the client and the server.
ms.assetid: 178f4838-3deb-43d4-804f-ad6404b377bd
keywords:
- data types MIDL , binding handles
ms.topic: article
ms.date: 05/31/2018
---

# MIDL Binding Handles

Binding handles are data objects that represent the binding between the client and the server.

MIDL supports the base type [**handle\_t**](handle-t.md). Handles of this type are known as "primitive handles."

You can define your own handle types using the **\[handle\]** attribute. Handles defined in this way are known as "user-defined" or "customized" or "generic" handles.

You can also define a handle that maintains state information using the **\[**[**context\_handle**](context-handle.md)**\]** attribute. Handles defined in this way are known as "context" handles.

If no state information is needed and you do not choose to call the RPC run-time libraries to manage the handle, you can request that the run-time libraries provide automatic binding. This is done by using the ACF keyword **\[**[**auto\_handle**](auto-handle.md)**\]**.

You can specify a global variable as the binding handle by using the ACF keyword **\[**[**implicit\_handle**](implicit-handle.md)**\]**. The **\[explicit\_handle\]** keyword is used to state that each remote function has an explicitly specified handle.

For more information, see [Binding and Handles](/windows/desktop/Rpc/binding-and-handles).

 

 