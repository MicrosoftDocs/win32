---
title: Applying a QOS Template
description: When an application knows the name of the QOS template it wants to use, the process of applying the QOS template is implemented through the WSAGetQOSByName function.
ms.assetid: 73c04cf7-5060-4a94-aba6-832b76117654
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Applying a QOS Template

When an application knows the name of the QOS template it wants to use, the process of applying the QOS template is implemented through the [**WSAGetQOSByName**](https://msdn.microsoft.com/library/windows/desktop/ms741587) function.

**To apply a QOS template**

1.  The application then implements a QOS template by making a call to [**WSAGetQOSByName**](https://msdn.microsoft.com/library/windows/desktop/ms741587). In the function call, the application passes the template name in the *lpQOSName* parameter, and provides a pointer to a [**QOS**](/windows/desktop/api/Winsock2/ns-winsock2-_qualityofservice) structure to be filled with the template's settings in the *lpQOS* parameter with a **NULL** string.
2.  The RSVP SP fills the [**QOS**](/windows/desktop/api/Winsock2/ns-winsock2-_qualityofservice) structure pointed to in *lpQOS* with the parameters from the selected QOS template.
3.  The application then sets members of its **SendingFlowspec** and **ReceivingFlowspec** members of the [**QOS**](/windows/desktop/api/Winsock2/ns-winsock2-_qualityofservice) structure with values that correspond to the values of the associated template. (**SendingFlowspec** and **ReceivingFlowspec** are members of the **QOS** structure, and both are of type [**FLOWSPEC**](/previous-versions/windows/desktop/api/Qos/ns-qos-_flowspec).) When using a QOS template, you should ensure that your application conforms to the transmission characteristics specified by the template being used.
4.  The application may then make a QOS-enabled connection request, and by using the [**QOS**](/windows/desktop/api/Winsock2/ns-winsock2-_qualityofservice) structure filled in Step 2, implement the QOS template's QOS parameters as part of the request.

For applications that do not know the name of the QOS template they want to use, or want to enumerate the available QOS templates, the process outlined in [Enumerating Available QOS Templates](enumerating-available-qos-templates.md) should be followed.

 

 




