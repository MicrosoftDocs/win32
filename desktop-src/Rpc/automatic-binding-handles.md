---
title: Automatic Binding Handles
description: Automatic binding handles are useful when the application does not require a specific server and when it does not need to maintain any state information between the client and server.
ms.assetid: ba049369-6c8b-4313-a266-e0364a30056e
ms.topic: article
ms.date: 05/31/2018
---

# Automatic Binding Handles

Automatic binding handles are useful when the application does not require a specific server and when it does not need to maintain any state information between the client and server. When you use an automatic binding handle, you do not have to write any client application code to deal with binding and handles—you simply specify the use of the automatic binding handle in the application configuration file (ACF). The stub then defines the handle and manages the binding.

For example, a time-stamp operation can be implemented using an auto handle. It makes no difference to the client application which server provides it with the time stamp because it can accept the time from any available server.

> [!Note]  
> Auto handles are not supported for the Macintosh platform.

 

You specify the use of auto handles by including the \[[**auto\_handle**](/windows/desktop/Midl/auto-handle)\] attribute in the ACF. The time-stamp example uses the following ACF:

``` syntax
/* ACF file */
[
  auto_handle
]
interface autoh
{
}
```

When the ACF does not include any other handle attribute, and when the remote procedures do not use explicit handles, the MIDL compiler uses automatic handles by default. It also uses automatic handles as the default when the ACF is not present.

The remote procedures are specified in the IDL file. The auto handle must not appear as an argument to the remote procedure. For example:

``` syntax
/* IDL file */
[ 
  uuid (6B29FC40-CA47-1067-B31D-00DD010662DA),
  version(1.0),
  pointer_default(unique)
]
interface autoh
{
  void GetTime([out] long * time);
  void Shutdown(void);
}
```

The benefit of the auto handle is that the developer does not have to write any code to manage the handle; the stubs manage the binding automatically. This is significantly different from the [Hello, World example](tutorial.md), where the client manages the implicit primitive handle defined in the ACF and must call several run-time functions to establish the binding handle.

 

 