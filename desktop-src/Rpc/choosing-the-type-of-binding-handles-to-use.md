---
title: Choosing the Type of Binding Handles to Use
description: Choosing the Type of Binding Handles to Use
ms.assetid: b0c2c71d-c6c9-4a58-83f9-10ac9b6b214b
ms.topic: article
ms.date: 05/31/2018
---

# Choosing the Type of Binding Handles to Use

**Best practice:** If you know which server the application will use, use explicit handles. If you don't, use explicit handles construct every time, or use generic handles with **\_bind** and **\_unbind** routines.

Do not use implicit handles or auto handles. Implicit handles are not thread safe, and even though thread safety may seem unnecessary, it could become necessary later. Auto handles have large overhead and require a lot of setup to work properly. Their search capabilities have been superseded by Active Directory services.

Explicit handles are highly efficient, and many attractive capabilities are available only for explicit handles. For example, if several RPC calls will be going to the same server, you can construct the binding handle once and make all calls with it. This approach is much more efficient than any other method. If the server to which the call will go is unknown, construct an explicit binding handle for every call, or use generic binding handles.

In Microsoft™ Windows XP, the RPC run time is quite efficient in re-using and caching calls, so if the *n*+1st call ends up on the same server as the *n*th call, RPC re-uses the resources allocated for the *n*th call, circumventing the need to cache binding handles to improve performance.

 

 




