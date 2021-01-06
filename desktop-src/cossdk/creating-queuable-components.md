---
description: A component with at least one queuable interface is a queuable component.
ms.assetid: 8183f640-4bf3-4555-8837-90a26130c618
title: Creating Queuable Components
ms.topic: article
ms.date: 05/31/2018
---

# Creating Queuable Components

A component with at least one queuable interface is a *queuable component*. For a component to be invoked by a queue, the interfaces must be marked as queuable and the component must be installed in a queued application. However, a queuable component can be a component of a non-queued application.

A queuable interface must contain only in parameters—no out parameters and no return values. These characteristics are verified by analyzing the type information during component installation. If the interface is not queuable, the queue of the application containing the component cannot be activated.

To specify a COM+ interface as queuable, use the following steps:

1.  In the console tree of the Component Services administrative tool, under **Component Services**, open the **COM+ Applications** folder associated with the computer you wish to manage.

2.  Open the **Interfaces** folder of the component of the COM+ application that you want to make queuable.

3.  Right-click the interface that you want to mark as queuable, and then click **Properties**.

4.  Select the **Queuing** tab in the properties dialog.

5.  Activate the check box labeled **Queued**.

    > [!Note]  
    > If the **Queued** check box is grayed out, the interface does not satisfy the queuable constraints described above.

     

6.  Click **OK**.

    A queuable component can be identified as such by adding the QUEUEABLE attribute macro to the Interface section of the Interface Definition Language (IDL) source file for all interfaces that are queuable.

    ``` syntax
#include "mtxattr.h"
    [ object, dual, uuid(), helpstring(IShiphip"), QUEUEABLE ]
    interface IShip:IDispatch{
       [propput, id(1)] HRESULT CustomerId ([in] long CustId);
       [propput, id(2)] HRESULT OrderId ([in] long OrderID);
       [id(3)] HRESULT LineItem ([in] long Qty);
       [id(4)] HRESULT Process ();
    }
    ```

## Related topics

<dl> <dt>

[Creating Component Queues](creating-component-queues.md)
</dt> <dt>

[Developing Queued Components](developing-queued-components.md)
</dt> </dl>

 

 



