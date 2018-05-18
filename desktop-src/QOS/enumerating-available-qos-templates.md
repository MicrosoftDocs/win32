---
title: Enumerating Available QOS Templates
description: In order to discover which templates are available on a given system, an application can enumerate the available QOS templates, using the WSAGetQOSByName function.
ms.assetid: '19d2d4ac-d809-4325-ab77-cabe5e720165'
---

# Enumerating Available QOS Templates

In order to discover which templates are available on a given system, an application can enumerate the available QOS templates, using the [**WSAGetQOSByName**](https://msdn.microsoft.com/library/windows/desktop/ms741587) function.

The process of using the [**WSAGetQOSByName**](https://msdn.microsoft.com/library/windows/desktop/ms741587) to enumerate available QOS templates follows a set of steps, as outlined in the following list.

1.  The application calls the [**WSAGetQOSByName**](https://msdn.microsoft.com/library/windows/desktop/ms741587) function with the *lpQOS* parameter set to **NULL**, and a pointer to a structure of type [**WSABUF**](https://msdn.microsoft.com/library/windows/desktop/ms741542) provided for the *lpQOSName* parameter.
2.  A list of available QOS template names is returned in the [**WSABUF**](https://msdn.microsoft.com/library/windows/desktop/ms741542) structure pointed to by *lpQOSName*.
3.  The application peruses the available templates, and selects an appropriate template, based on the template's name (codec), to service the application's required QOS parameters.

Once the list of available QOS templates is obtained, the application may apply a QOS template to a requested connection. The process of applying a QOS template is explained in the section called [Applying a QOS Template](applying-a-qos-template.md).

 

 




