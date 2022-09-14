---
description: Transient subscriptions cannot be set by using the Component Services administration tool. You must use the COM+ administrative interfaces to create or update a transient subscription.
ms.assetid: 28d48d59-abb2-4682-ab54-60b6aa7b31b1
title: Registering a Transient Subscription
ms.topic: article
ms.date: 05/31/2018
---

# Registering a Transient Subscription

Transient subscriptions request an event for a specific subscriber object that already exists. Transient subscriptions are stored in the COM+ catalog, but the subscription is deleted if the event system or operating system is stopped. Unlike persistent subscriptions, transient subscriptions are tied to a particular object and are stored only in the event system. If there is a problem with the event system or operating system, the subscription disappears. Transient subscriptions can be more efficient than persistent subscriptions, but you must manage their object life cycles.

Transient subscriptions cannot be set by using the Component Services administration tool. You must use the COM+ administrative interfaces to create or update a transient subscription.

## Visual Basic

The following procedure describes how to create a transient subscription using Microsoft Visual Basic:

1.  Specify a subscription as transient by adding a new entry to the [**TransientSubscriptions**](transientsubscriptions.md) collection and setting the SubscriberInterface property to the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface of the subscriber object. COM+ Events does not create a new instance of the subscriber object when firing an event but instead uses the instance you specify. COM+ Events holds a reference count for the subscriber object until the subscription is removed from the system.
2.  Create a COM+ server application (an .exe, a .dll, or an .ocx file) with an object that implements the interfaces or methods you want to subscribe to.
3.  Create your transient subscription using the following code, by passing in the CLSID of the [event class](the-com--event-class-object.md) object and the instance of the subscriber object. Using the Component Services administrative tool, you can get the EventCLSID property by right-clicking the COM+ component, selecting **Properties**, and selecting the **General** tab.

    ``` syntax
    Public Function CreateTransientSubscription( _
      ByVal clsid As String, ByVal objref As Object) As String 
        Dim oCOMAdminCatalog As COMAdmin.COMAdminCatalog
        Dim oTSCol As COMAdminCatalogCollection
        Dim oSubscription As ICatalogObject
        Dim objvar As Variant
        On Error GoTo CreateTransientSubscriptionError
        Set oCOMAdminCatalog = CreateObject("COMAdmin.COMAdminCatalog")
        'Gets the TransientSubscriptions collection
        Set oTSCol = oCOMAdminCatalog.GetCollection( _
          "TransientSubscriptions")
        Set oSubscription = oTSCol.Add
        Set objvar = objref
        oSubscription.Value("SubscriberInterface") = objref
        oSubscription.Value("EventCLSID") = clsid
        oSubscription.Value("Name") = "TransientSubscription"
        oTSCol.SaveChanges
        CreateTransientSubscription = oSubscription.Value("ID")
        Set oSubscription = Nothing
        Set oTSCol = Nothing
        Set oCOMAdminCatalog = Nothing
        Set objvar = Nothing
        Exit Function
    CreateTransientSubscriptionError:
        CreateTransientSubscription = ""
        Err.Raise Err.Number, "[CreateTransientSubscription]" & _
          Err.Source, Err.Description
    End Function
    ```

The following example illustrates how to call the CreateTransientSubscription function to subscribe to an interface called IStockTicker, which has a method called UpdateStock.

1.  Create an event class that supports the interface IStockTicker, which has one method, UpdateStock.
2.  In your subscriber project, add a class that implements the IStockTicker interface.
3.  When you want to subscribe execute the following code:

    ``` syntax
    Dim oMyTicker As Object
    Dim sSubscriptionID As String
    Set oMyTicker = CreateObject("TheProject.CMyTicker")
    sSubscriptionID = CreateTransientSubscription( _
      "{..CLSID for the Event Class..}", oMyTicker)
    ```

The CreateTransientSubscription function returns a string, which is a GUID that can be used as a handle or a cookie to revoke the subscription later. To remove the subscription, call the [**Remove**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-remove) method of [**COMAdminCatalogCollection**](comadmincatalogcollection.md) on the [**TransientSubscriptions**](transientsubscriptions.md) collection, passing in the index corresponding to the subscription with the GUID previously received.

## Related topics

<dl> <dt>

[Registering a Subscription](registering-a-subscription.md)
</dt> </dl>

 

 
