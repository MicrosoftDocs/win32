---
title: The Request Object
description: The Request Object
ms.assetid: d8b37164-6855-48c0-bcf8-a86c0f8b3a59
ms.topic: article
ms.date: 05/31/2018
---

# The Request Object

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

The server processes some methods asynchronously. This enables your application code to continue while the method is completing. When a client application calls one of these methods, the control creates and returns a [**Request**](/windows/desktop/lwef/the-request-object) object for the request. You can use the **Request** object to track the status of the method by assigning an object variable to the method. In Visual Basic, first declare an object variable:


```
   Dim MyRequest as Object
```



In VBScript, you don't include the variable type in your declaration:


```
   Dim MyRequest
```



And use Visual Basic's Set statement to assign the variable to the method call:


```
   Set MyRequest = <i>agent</i>.Characters("<i>CharacterID</i>").<i>method</i> (<i>parameter</i>[s])
```



This adds a reference to the [**Request**](/windows/desktop/lwef/the-request-object) object. The **Request** object will be destroyed when there are no more references to it. Where you declare the **Request** object and how you use it determines its lifetime. If the object is declared local to a subroutine or function, it will be destroyed when it goes out of scope; that is, when the subroutine or function ends. If the object is declared globally, it will not be destroyed until either the program terminates or a new value (or a value set to "empty") is assigned to the object.

The [**Request**](/windows/desktop/lwef/the-request-object) object provides several properties you can query. For example, the [**Status**](status-property.md) property returns the current status of the request. You can use this property to check the status of your request:


```
   Dim MyRequest
   
   Set MyRequest = Agent1.Characters.Load ("Genie", "https://agent.microsoft.com/characters/v2/genie/genie.acf")

   If (MyRequest.Status = 2) then
      'do something

   Else If (MyRequest.Status = 0) then
      'do something right away

   End If
```



The [**Status**](status-property.md) property returns the status of a [**Request**](/windows/desktop/lwef/the-request-object) object as a Long integer value.



| Status | Definition                                        |
|--------|---------------------------------------------------|
| 0      | Request successfully completed.                   |
| 1      | Request failed.                                   |
| 2      | Request pending (in the queue, but not complete). |
| 3      | Request interrupted.                              |
| 4      | Request in progress.                              |



 

The [**Request**](/windows/desktop/lwef/the-request-object) object also includes a Long integer value in the [**Number**](https://www.bing.com/search?q=**Number**) property that returns the error or cause of the [**Status**](status-property.md) code. If none, this value is zero (0). The [**Description**](description-property.md) property contains a string value that corresponds to the error number. If the string doesn't exist, **Description** contains "Application-defined or object-defined error".

For the values and meaning returned by the [**Number**](https://www.bing.com/search?q=**Number**) property, see [Error Codes](microsoft-agent-error-codes.md).

The server places animation requests in the specified character's queue. This enables the server to play the animation on a separate thread, and your application's code can continue while animations play. If you create a [**Request**](/windows/desktop/lwef/the-request-object) object reference, the server automatically notifies you when an animation request has started or completed through the [**RequestStart**](https://www.bing.com/search?q=**RequestStart**) and [**RequestComplete**](https://www.bing.com/search?q=**RequestComplete**) events. Because methods that return **Request** objects are asynchronous and may not complete during the scope of the calling function, declare your reference to the **Request** object globally.

The following methods can be used to return a [**Request**](/windows/desktop/lwef/the-request-object) object: [**GestureAt**](gestureat-method.md), [**Get**](get-method.md), [**Hide**](hide-method.md), [**Interrupt**](interrupt-method.md), [**Load**](load-method.md), [**MoveTo**](moveto-method.md), [**Play**](play-method.md), [**Show**](show-method.md), [**Speak**](speak-method.md), and [**Wait**](https://www.bing.com/search?q=**Wait**).

 

 