---
title: How to Expose ActiveX Objects
description: To expose ActiveX objects, you write code to initialize the objects, implement the objects, and then release OLE when the application terminates.
ms.assetid: '8520200a-4bdf-4f57-a3c1-24439a51ab18'
---

# How to: Expose ActiveX Objects

To expose ActiveX objects, you write code to initialize the objects, implement the objects, and then release OLE when the application terminates.

**To initialize exposed objects**

1.  Initialize OLE.

2.  Register the class factories of the exposed objects.

3.  Register the active object.

**To implement exposed objects**

1.  Implement the **IUnknown**, [**IDispatch**](idispatch.md), and virtual function table (VTBL) interfaces for the objects.

2.  Implement the properties and methods of the objects.

**To release OLE when the application terminates**

1.  Revoke the registration of the class factories and revoke the active object.

2.  Uninitialize OLE.

**To retrieve active objects for use by others**

1.  Use the Object Description Language (ODL) to create an .odl file, or use the Interface Definition Language (IDL) to create a library section in an .idl file that describes the properties and methods of the exposed objects. Use the Microsoft Interface Definition Language (MIDL) compiler to compile both the .idl file and .odl file.

2.  Create a registration (.reg) file for the application.

## In this section



| Topic                                                                             | Description                                                                                                                                                                                                                                                                              |
|-----------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Initializing Exposed Objects](initializing-exposed-objects.md)<br/>       | To initialize OLE and exposed objects, use [**OleInitialize**](https://msdn.microsoft.com/library/windows/desktop/ms690134), [**CoRegisterClassObject**](https://msdn.microsoft.com/library/windows/desktop/ms693407), and [**RegisterActiveObject**](registeractiveobject.md).<br/>                                                                          |
| [Implementing Exposed Objects](implementing-exposed-objects.md)<br/>       | To expose ActiveX objects, you must implement certain interfaces.<br/>                                                                                                                                                                                                             |
| [Implementing a Class Factory](implementing-a-class-factory.md)<br/>       | This topics describes what you must do to expose objects for Automation.<br/>                                                                                                                                                                                                      |
| [Exposing the Application Object](exposing-the-application-object.md)<br/> | The Application object identifies the application and provides a way for ActiveX clients to bind to and navigate the application's exposed objects. All other exposed objects are subordinate to the Application object; it is the root-level object in the object hierarchy.<br/> |
| [Creating a Registration File](creating-a-registration-file.md)<br/>       | Before an application can use OLE and Automation, the OLE objects must be registered with the user's system registration database.<br/>                                                                                                                                            |
| [Releasing OLE and Objects](releasing-ole-and-objects.md)<br/>             | To release OLE and the exposed objects, use the [**RevokeActiveObject**](revokeactiveobject.md), [**CoRevokeClassObject**](https://msdn.microsoft.com/library/windows/desktop/ms688650), and [OLEUninitialize](B2A8233F-7E1B-4C54-9363-7478C40C3830) functions.<br/>                                                  |
| [Retrieving Objects](retrieving-objects.md)<br/>                           | Automation provides several functions to identify and retrieve the active instance of an object or application, so you can make the object available to others.<br/>                                                                                                               |
| [Returning Objects](returning-objects.md)<br/>                             | To return an object from a property or method, the application should return a pointer to the object's implementation of the [**IDispatch**](idispatch.md) interface.<br/>                                                                                                        |
| [Shutting Down Objects](shutting-down-objects.md)<br/>                     | Describes how to shut down an ActiveX object.<br/>                                                                                                                                                                                                                                 |



 

 

 





