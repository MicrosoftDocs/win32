---
Description: Explains the differences between SSP/APs and SSPs.
ms.assetid: 0ed4291b-6562-440f-b892-4e6e5b4b49c8
title: SSP/APs vs. SSPs
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SSP/APs vs. SSPs

[*Security packages*](https://www.bing.com/search?q=*Security packages*) are deployed in one of the following types of dynamic-link libraries (DLLs):

-   [SSP/APs](#sspaps-vs-ssps)
-   [SSPs](#sspaps-vs-ssps)

Whether a security package is in a security support provider/[*authentication package*](https://www.bing.com/search?q=*authentication package*) (SSP/AP) or a [*security support provider*](https://www.bing.com/search?q=*security support provider*) (SSP) DLL is determined by the types of security services it provides and the extent to which it requires integration with the [*Local Security Authority*](https://www.bing.com/search?q=*Local Security Authority*) (LSA). These differences also determine the API implemented in a custom security package.

## SSP/APs

An SSP/AP is a DLL that contains one or more [*security packages*](https://www.bing.com/search?q=*security packages*) and can function as an SSP for client/server applications and as an [authentication package](authentication-packages.md) for logon applications. To function in both of these roles, SSP/APs are loaded into the LSA process space at system startup and can be loaded into client/server application processes as well.

Custom SSP/AP security packages must implement both the [Functions Implemented by User-mode SSP/APs](https://www.bing.com/search?q=Functions Implemented by User-mode SSP/APs), and [Functions Implemented by SSP/APs](https://www.bing.com/search?q=Functions Implemented by SSP/APs). These function implementations can make use of LSA support functions to offer advanced security features such as token creation, [*supplemental credentials*](https://www.bing.com/search?q=*supplemental credentials*) support, and pass-through authentication.

If a custom SSP/AP security package provides the full range of message [*integrity*](https://www.bing.com/search?q=*integrity*) and privacy functions, it will also implement the [Functions Implemented by User-mode SSP/APs](https://www.bing.com/search?q=Functions Implemented by User-mode SSP/APs).

## SSPs

An SSP is a DLL that contains one or more security packages that provide authenticated connection, message integrity, and message encryption services to client/server applications. SSPs implement [Security Support Provider Interface](sspi.md) (SSPI) functions. Applications can access the security packages in an SSP by calling the SSPI functions directly. SSPs are loaded into the client and server processes; they are not integrated with the LSA.

 

 



