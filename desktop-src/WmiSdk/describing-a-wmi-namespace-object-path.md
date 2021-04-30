---
description: A namespace object path describes the location of a particular namespace on a server. A namespace object path contains server and namespace elements, and is formatted using either forward or backward slashes.
ms.assetid: 6d8da19e-0914-4267-870e-c203176b895e
ms.tgt_platform: multiple
title: Describing a WMI Namespace Object Path
ms.topic: article
ms.date: 05/31/2018
---

# Describing a WMI Namespace Object Path

A namespace object path describes the location of a particular namespace on a server. A namespace object path contains server and namespace elements, and is formatted using either forward or backward slashes.

The server element specifies the network name of the computer that is hosting the namespace, as shown in the following example.

``` syntax
\\Server\Namespace
```

\- or -

``` syntax
//Server/Namespace
```

If the server is the local computer, use a single dot instead of the server name, as shown in the following example.

``` syntax
\\.\Namespace
```

The namespace element specifies any valid namespace. A namespace is represented with a hierarchical string containing elements delimited by single backslashes, such as root\\cimv2. You cannot use forward slashes within namespace names.

 

 



