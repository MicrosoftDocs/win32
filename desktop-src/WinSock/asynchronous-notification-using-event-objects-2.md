---
Description: 'The WSAEventSelect and WSAEnumNetworkEvents functions are provided to accommodate applications such as daemons and services that have no user interface (and hence do not use Windows handles).'
ms.assetid: '4254937c-7ee6-49a3-9f30-09aebaf2265b'
title: Asynchronous Notification Using Event Objects
---

# Asynchronous Notification Using Event Objects

The [**WSAEventSelect**](wsaeventselect-2.md) and [**WSAEnumNetworkEvents**](wsaenumnetworkevents-2.md) functions are provided to accommodate applications such as daemons and services that have no user interface (and hence do not use Windows handles). The **WSAEventSelect** function behaves exactly like the [**WSAAsyncSelect**](wsaasyncselect-2.md) function. However, instead of causing a Windows message to be sent on the occurrence of an FD\_XXX network event (for example, FD\_READ and FD\_WRITE), an application-designated event object is set.

Also, the fact that a particular FD\_XXX network event has occurred is remembered by the service provider. The application can call [**WSAEnumNetworkEvents**](wsaeventselect-2.md) to have the current contents of the network event memory copied to an application-supplied buffer and to have the network event memory automatically cleared. If needed, the application can also designate a particular event object that is cleared along with the network event memory.

 

 



