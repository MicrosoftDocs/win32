---
title: Connected Property
description: Connected Property
ms.assetid: 61b7f550-d8d6-4719-a0d4-0bf3a8cf096c
ms.topic: article
ms.date: 05/31/2018
---

# Connected Property

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Returns or sets whether the current control is connected to the Microsoft Agent server.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent.***Connected** \[ = *boolean*\]



| Part      | Description                                                                                                     |
|-----------|-----------------------------------------------------------------------------------------------------------------|
| *boolean* | A Boolean expression specifying whether the control is connected. **True** The control is connected.<br/> |



 

</dd> </dl>

## Remarks

In many situations, specifying the control automatically creates a connection with the Microsoft Agent server. For example, specifying the Microsoft Agent control's CLSID in the &lt;OBJECT&gt; tag in a webpage automatically opens a server connection and exiting the page closes the connection. Similarly, for Visual Basic or other languages that enable you to drop a control on a form, running the program automatically opens a connection and exiting the program closes the connection. If the server isn't currently running, it automatically starts.

However, if you want to create an Agent control at run time, you may also need to explicitly open a new connection to the server using the **Connected** property. For example, in Visual Basic you can create an ActiveX object at run time using the Set statement with the **New** keyword (or CreateObject function). While this creates the object, it may not create the connection to the server. You can use the **Connected** property before any code that calls into Microsoft Agent's programming interface, as shown in the following example:


```
   ' Declare a global variable for the control
   Dim MyAgent as Agent

   ' Create an instance of the control using New
   Set MyAgent = New Agent

   ' Open a connection to the server
   MyAgent.Connected = True

   ' Load a character
   MyAgent.Characters.Load "Genie", " Genie.acs"

   ' Display the character
   MyAgent.Characters("Genie").Show
```



Creating a control using this technique does not expose the Agent control's events. In Visual Basic 5.0 (and later), you can access the control's events by including the control in your project's references, and use the **WithEvents** keyword in your variable declaration:


```
   Dim WithEvents MyAgent as Agent

   ' Create an instance of the control using New
   Set MyAgent = New Agent
```



Using **WithEvents** to create an instance of the Agent control at run time automatically opens the connection with the Microsoft Agent server. Therefore, you don't need to include a **Connected** statement.

You can close your connection to the server by releasing all references you created to Agent objects, such as IAgentCtlCharacterEx and IAgentCtlCommandEx. You must also release your reference to the Agent control itself. In Visual Basic, you can release a reference to an object by setting its variable to **Nothing**. If you have loaded characters, unload them before releasing the character object.


```
   Dim WithEvents MyAgent as Agent
   Dim Genie as IAgentCtlCharacterEx
   
   Sub Form_Load

   ' Create an instance of the control using New
   Set MyAgent = New Agent

   ' Open a connection to the server
   MyAgent.Connected = True

   ' Load the character into the Characters collection
   MyAgent.Characters.Load "Genie", " Genie.acs"

   ' Create a reference to the character
   Set Genie = MyAgent.Characters("Genie")

   End Sub

   Sub CloseConnection

   ' Unload the character
   MyAgent.Characters.Unload "Genie"

   ' Release the reference to the character object
   Set Genie = Nothing

   ' Release the reference to the Agent control
   Set MyAgent = Nothing
   End Sub
```



> [!Note]  
> You cannot close your connection to the server by releasing references where the component has been added. For example, you cannot close your connection to the server on webpages where you use the &lt;OBJECT&gt; tag to declare the control or in a Visual Basic application where you drop the control on a form. While releasing all Agent references will reduce Agent's working set, the connection remains until you navigate to the next page or exit the application.

 

 

 





