---
title: Properties and Methods
description: Like any OLE object, a control provides much of its functionality through a set of incoming interfaces with properties and methods.
ms.assetid: 5a0cdb5d-7e27-40e9-94db-cfda853879c6
ms.topic: reference
ms.date: 05/31/2018
---

# Properties and Methods

Like any OLE object, a control provides much of its functionality through a set of incoming interfaces with properties and methods.

A control exposes properties and methods through OLE automation so that containers can access them under the control of a container-supplied programming language.

To support access to properties through a user interface, a control provides property pages, support for OLEIVERB\_PROPERTIES, per property browsing, and data binding through property change notfications.

-   Through property pages a control can display its properties, independent of its container, if necessary.
-   By supporting OLEIVERB\_PROPERTIES, the Properties item is displayed on the container's menu. Then, the end user can select the **Properties** item to view the control's property pages and modify the properties.
-   Per property browsing supports a container that can display the control's properties as part of a larger property sheet that may include properties from several controls in the container.
-   Through property change notification, a control can notify a client that its properties have change, allowing the client to take any necessary actions as a result.

For more information, see the following topics:

-   [Control Properties](control-properties.md)
-   [Control Methods](control-methods.md)

## Related topics

<dl> <dt>

[ActiveX Controls](activex-controls.md)
</dt> <dt>

[Property Pages and Property Sheets](property-pages-and-property-sheets.md)
</dt> </dl>

 

 




