---
title: Creating a Binding Handle
description: The client program of a distributed application needs to create a binding handle that tells the RPC run time which server should be contacted, and how the server should be contacted.
ms.assetid: 52c5d0bd-f9b4-4d3f-ac7f-f9b4fb919846
keywords:
- Remote Procedure Call RPC , tasks, creating a binding handle
ms.topic: article
ms.date: 05/31/2018
---

# Creating a Binding Handle

The client program of a distributed application needs to create a binding handle that tells the RPC run time which server should be contacted, and how the server should be contacted.

The following code fragment demonstrates a common approach to creating a binding handle:


```C++
RPC_STATUS status;
unsigned short *StringBinding;
RPC_BINDING_HANDLE BindingHandle;
status = RpcStringBindingCompose(NULL,  // Object UUID
             L"ncacn_ip_tcp",           // Protocol sequence to use
             L"MyServer.MyCompany.com", // Server DNS or Netbios Name
             NULL,
             NULL,
             &StringBinding);
// Error checking ommitted. If no error, we proceed below
status = RpcBindingFromStringBinding(StringBinding, &BindingHandle);

// free string regardless of errors from RpcBindingFromStringBinding
RpcStringFree(&StringBinding);

// Error checking ommitted. If no error, we have a valid binding handle
```



 

 




