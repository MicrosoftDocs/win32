---
Description: 'Use the EventWriteTransfer function when several components want to relate their events in an end-to-end tracing scenario.'
ms.assetid: '715e3161-d85a-45c0-84df-c6c360b266a1'
title: 'Writing Related Events in a Manifest-based Provider'
---

# Writing Related Events in a Manifest-based Provider

Use the [**EventWriteTransfer**](eventwritetransfer-func.md) function when several components want to relate their events in an end-to-end tracing scenario. For example, components A, B and C perform work on a related activity and want to link all the events related to that activity.

ETW uses thread local storage to make the previous component's activity identifier available to the next component. The component retrieves the previous component's identifier from the local storage and sets the related activity identifier to it. The consumer can then use the related activity identifier to walk the chain of the events from one component to the next.

 

 



