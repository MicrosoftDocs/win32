---
Description: A credential manager is similar to a network provider in that it provides entry points that are called by the Multiple Provider Router (MPR). In fact, some network providers are also credential managers.
ms.assetid: a1105754-a57f-4a0d-9797-bec22b99900c
title: Credential Manager
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Credential Manager

A credential manager is similar to a network provider in that it provides entry points that are called by the [*Multiple Provider Router*](https://msdn.microsoft.com/library/windows/desktop/ms721594#-security-multiple-provider-router-gly) (MPR). In fact, some network providers are also credential managers.

Whether you implement the credential management functions in the same DLL as the network provider functions depends on the requirements of your application. Credential managers receive notifications when authentication information changes. For example, credential managers are notified when a user logs on or an account password changes. When a logon process, such as [*Winlogon*](https://msdn.microsoft.com/library/windows/desktop/ms721635#-security-winlogon-gly), is in the process of logging on or changing the password for an account, it calls the appropriate MPR Windows Networking (WNet) function. The MPR then calls the appropriate entry point for each credential manager. These credential management functions will always be called in the system context, LocalSystem, rather than the user context. For more information about WNet functions, see [Windows Networking](https://msdn.microsoft.com/library/windows/desktop/aa385406). For more information about the interface that credential managers must implement, see [**Credential Management API**](credential-management-api.md).

 

 



