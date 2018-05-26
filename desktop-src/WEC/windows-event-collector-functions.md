---
title: Windows Event Collector Functions
description: The following list briefly describes the functions that are used in Windows Event Collector.
audience: developer
ms.assetid: 48155df6-ba9c-4abe-ba84-6190cee95878
ms.prod: windows-server-dev
ms.technology: windows-event-collector
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Windows Event Collector Functions

The following list briefly describes the functions that are used in Windows Event Collector.

## In this section

<dl> <dt>

[**EcClose**](/windows/win32/Evcoll/nf-evcoll-ecclose?branch=master)
</dt> <dd>

Closes a handle received from other Event Collector functions.

</dd> <dt>

[**EcDeleteSubscription**](/windows/win32/Evcoll/nf-evcoll-ecdeletesubscription?branch=master)
</dt> <dd>

Deletes an existing subscription.

</dd> <dt>

[**EcEnumNextSubscription**](/windows/win32/Evcoll/nf-evcoll-ecenumnextsubscription?branch=master)
</dt> <dd>

Continues the enumeration of the subscriptions registered on the local machine.

</dd> <dt>

[**EcGetObjectArrayProperty**](/windows/win32/Evcoll/nf-evcoll-ecgetobjectarrayproperty?branch=master)
</dt> <dd>

Retrieves property values for the event sources of a subscription.

</dd> <dt>

[**EcGetObjectArraySize**](/windows/win32/Evcoll/nf-evcoll-ecgetobjectarraysize?branch=master)
</dt> <dd>

Retrieves the number of indexes of the array of property values for the event sources of a subscription.

</dd> <dt>

[**EcGetSubscriptionProperty**](/windows/win32/Evcoll/nf-evcoll-ecgetsubscriptionproperty?branch=master)
</dt> <dd>

Retrieves a property value from a subscription object.

</dd> <dt>

[**EcGetSubscriptionRunTimeStatus**](/windows/win32/Evcoll/nf-evcoll-ecgetsubscriptionruntimestatus?branch=master)
</dt> <dd>

Retrieves the run time status information for an event source of a subscription or the subscription itself.

</dd> <dt>

[**EcInsertObjectArrayElement**](/windows/win32/Evcoll/nf-evcoll-ecinsertobjectarrayelement?branch=master)
</dt> <dd>

Inserts an empty object into an array of property values for the event sources of a subscription.

</dd> <dt>

[**EcOpenSubscriptionEnum**](/windows/win32/Evcoll/nf-evcoll-ecopensubscriptionenum?branch=master)
</dt> <dd>

Creates a subscription enumerator to enumerate all registered subscriptions on the local machine.

</dd> <dt>

[**EcOpenSubscription**](/windows/win32/Evcoll/nf-evcoll-ecopensubscription?branch=master)
</dt> <dd>

Opens an existing subscription or creates a new subscription.

</dd> <dt>

[**EcSaveSubscription**](/windows/win32/Evcoll/nf-evcoll-ecsavesubscription?branch=master)
</dt> <dd>

Saves subscription configuration information.

</dd> <dt>

[**EcSetObjectArrayProperty**](/windows/win32/Evcoll/nf-evcoll-ecsetobjectarrayproperty?branch=master)
</dt> <dd>

Sets a property value in an array of property values for the event sources of a subscription.

</dd> <dt>

[**EcSetSubscriptionProperty**](/windows/win32/Evcoll/nf-evcoll-ecsetsubscriptionproperty?branch=master)
</dt> <dd>

Sets new values or updates existing values of a subscription.

</dd> <dt>

[**EcRemoveObjectArrayElement**](/windows/win32/Evcoll/nf-evcoll-ecremoveobjectarrayelement?branch=master)
</dt> <dd>

Removes an element from an array of objects that contain property values for the event sources of a subscription.

</dd> <dt>

[**EcRetrySubscription**](/windows/win32/Evcoll/nf-evcoll-ecretrysubscription?branch=master)
</dt> <dd>

Retries connecting to the event source of a subscription that is not connected.

</dd> </dl>

 

 




