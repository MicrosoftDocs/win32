---
Description: 'This topic describes the hierarchy of the Fax Service Extended COM.'
ms.assetid: '45752ea8-c11f-45d5-939e-7d699aef05de'
title: Fax Service Extended COM Object Model
---

# Fax Service Extended COM Object Model

Most of the objects in the Fax Service Extended Component Object Model (COM) are organized in a hierarchical manner. The diagram that follows illustrates this hierarchy. Note that if multiple objects can exist, this is indicated in the diagram by a "stack" of objects; for example, multiple [**FaxOutboundRoutingRule**](-mfax-faxoutboundroutingrule.md) and [**FaxInboundRoutingMethod**](-mfax-faxinboundroutingmethod.md) objects can exist.

The client application must call the [**Connect**](-mfax-faxserver-cpp-mfax-faxserver-connect-cpp.md) method of the [**FaxServer**](-mfax-faxserver.md) object to establish a connection with a fax server before accessing other interfaces in the fax extended COM API or other fax client objects.

Note also that an application can call the [CoCreateInstance](http://msdn.microsoft.com/en-us/library/ms686615.aspx) function or the Microsoft Visual Basic [**CreateObject**](ec11fd03-b420-412f-b25a-057f877cefbc) function to create only two of the objects in the model: the [**FaxServer**](-mfax-faxserver.md) and the [**FaxDocument**](-mfax-faxdocument.md) objects. (This is indicated by shading in the diagram.) All of the other objects, with the exception of notification objects, can be accessed only through existing objects.

For a list and brief description of all of the objects, see [Fax Service Extended COM Objects](-mfax-fax-service-extended-com-objects.md).

The extended COM supports notifications for fax service events. For more information, see [Registering for Event Notifications](-mfax-registering-for-event-notifications.md).

![fax service extended com object model hierarchy](images/faxcomobject.png)

 

 



