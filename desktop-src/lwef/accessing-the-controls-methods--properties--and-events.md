---
title: Accessing the Controls Methods, Properties, and Events
description: Accessing the Controls Methods, Properties, and Events
ms.assetid: 70a3b011-0290-4df4-9b66-23b27bcb14e9
ms.topic: article
ms.date: 05/31/2018
---

# Accessing the Controls Methods, Properties, and Events

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

Using Microsoft Agent's control with Visual Basic is very similar to using the control with VBScript, except that events in Visual Basic must include the data type of passed parameters. Adding the Microsoft Agent control to a form will automatically include Microsoft Agent's events with their appropriate parameters. It will also automatically create a connection to the Agent server when the application runs.

You may also be able to use your programming language's object's creation syntax to create an instance of the control at runtime. For example, in Visual Basic (5.0 or later), if you include the Microsoft Agent 2.0 Control in your project's references, you can use a [**With Events**](https://www.bing.com/search?q=**With+Events**)..[**New**](https://www.bing.com/search?q=**New**) declaration. If you do not include the reference, VB raises an error indicating that Microsoft Agent was unable to start (error code 80042502).

``` syntax
   ' Declare a global variable for the control
   Dim WithEvents MyAgent as Agent

   ' Create an instance of the control using New
   Set MyAgent = New Agent

' Load a character
   MyAgent.Characters.Load "Genie", " Genie.acs"

   ' Display the character
   MyAgent.Characters("Genie").Show
```

For versions of VB prior to 5.0, you can use the VB [**New**](https://www.bing.com/search?q=**New**) keyword without [**WithEvents**](https://www.bing.com/search?q=**WithEvents**) declaration or the VB [**CreateObject**](https://msdn.microsoft.com/library/Bb545141(v=VS.85).aspx) function, but these conventions will not expose the Agent control's events. You also need to use the [**Connected**](https://www.bing.com/search?q=**Connected**) property before you reference any Agent methods or properties. If this is not done, VB will raise an error indicating that Microsoft Agent was unable to start (error code 80042502).

Similarly for other programming languages, you may have to use the [**Connected**](https://www.bing.com/search?q=**Connected**) property to establish a connection to the Agent Component Object Model (COM) server before your code can call any of the Agent control's methods or properties. In addition, for some programming languages, Agent's methods and properties may not be directly exposed unless you declare the Agent control using its type. For example, in Microsoft Access 97, you will need to declare the object as type Agent to see the methods and properties display in the Auto List Members drop-down box when you type.

Most programming languages that support ActiveX controls follow conventions similar to Visual Basic. For programming languages that do not support object collections, you can use the [**Character**](https://www.bing.com/search?q=**Character**) method and [**Command**](https://www.bing.com/search?q=**Command**) method to access methods and properties of items in the collection.

Programming languages like Visual Basic, that provide access to the object types exposed by the Agent control, enable you to use these in your object declarations. For example, instead of declaring an object as a generic type:

``` syntax
   Dim Genie as Object
```

You can declare an object as a specific type:

``` syntax
   Dim Genie as IAgentCtlCharacterEx
```

This may improve the overall performance of your application.

For some object types, you may find two types that are the same except for the "Ex" suffix. Where both exist, use the "Ex" type because this provides the full functionality of Agent. The non-"Ex" counterparts are included only for backward compatibility.

 

 




