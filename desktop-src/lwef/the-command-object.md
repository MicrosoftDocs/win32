---
title: The Command Object
description: The Command Object
ms.assetid: a757846a-c2d0-4239-9533-babf5dc8399f
ms.topic: article
ms.date: 05/31/2018
---

# The Command Object

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

A [**Command**](/windows/desktop/lwef/the-command-object) object is an item in a [**Commands**](/windows/desktop/lwef/the-commands-collection-object) collection. The server provides the user access to your **Command** objects when your client application becomes input-active.

-   [Command Object Properties](command-object-properties.md)

To access the property of a [**Command**](/windows/desktop/lwef/the-command-object) object, you reference it in its collection using its [**Name**](name-property.md) property. In VBScript and Visual Basic you can use the **Name** property directly:


```
   <i>agent</i>.Characters("<i>CharacterID</i>").Commands("<i>Name</i>").<i>property</i> [= <i>value</i>]
```



For programming languages that don't support collections, use the [**Command**](command-method.md) method:


```
   <i>agent</i>.Characters("<i>CharacterID</i>").Commands.Command("<i>Name</i>").<i>property</i> [= <i>value</i>]
```



You can also reference a Command object by creating a reference to it. In Visual Basic, declare an object variable and use the Set statement to create the reference:


```
   Dim Cmd1 as Object
   ...
   Set Cmd1 = Agent.Characters("MyCharacterID").Commands("SampleCommand")
   ...
   Cmd1.Enabled = True
```



In Visual Basic 5.0, you can also declare the object as type [**IAgentCtlCommandEx**](https://www.bing.com/search?q=**IAgentCtlCommandEx**) and create the reference. This convention enables early binding, which results in better performance:


```
   Dim Cmd1 as IAgentCtlCommandEx
   ...
   Set Cmd1 = Agent.Characters("MyCharacterID").Commands("SampleCommand")
   ...
   Cmd1.Enabled = True
```



In VBScript, you can declare a reference as a particular type, but you can still declare the variable and set it to the [**Command**](/windows/desktop/lwef/the-command-object) in the collection:


```
   Dim Cmd1
   ...
   Set Cmd1 = Agent.Characters("MyCharacterID").Commands("SampleCommand")
   ...
   Cmd1.Enabled = True
```



A command may appear in either the character's pop-up menu and the Commands Window, or in both. To appear in the pop-up menu it must have a caption and have the [**Visible**](visible-property.md) property set to **True**. In addition, its Commands collection object **Visible** property must also be set to **True**. To appear in the Commands Window, a [**Command**](/windows/desktop/lwef/the-command-object) must have its [**Caption**](caption-property.md) and [**Voice**](voice-property.md) properties set. Note that a character's pop-up menu entries do not change while the menu displays. If you add or remove commands or change their properties while the character's pop-up menu is displayed, the menu displays those changes whenever the user next displays it. However, the Commands Window dynamically reflects any changes you make.

The following table summarizes how the properties of a [**Command**](/windows/desktop/lwef/the-command-object) affect its presentation:



Caption Property

Voice-Caption Property

Voice Property

Visible Property

Enabled Property

Appears in Character's Pop-up Menu

Appears in Commands Window

Yes

Yes

Yes

True

True

Normal, using [**Caption**](caption-property.md)

Yes, using [**VoiceCaption**](voicecaption-property.md)

Yes

Yes

Yes

True

False

Disabled, using [**Caption**](caption-property.md)

No

Yes

Yes

Yes

False

True

Does not appear

Yes, using [**VoiceCaption**](voicecaption-property.md)

Yes

Yes

Yes

False

False

Does not appear

No

Yes

Yes

No 

True

True

Normal, using [**Caption**](caption-property.md)

No

Yes

Yes

No 

True

False

Disabled, using [**Caption**](caption-property.md)

No

Yes

Yes

No 

False

True

Does not appear

No

Yes

Yes

No 

False

False

Does not appear

No

No 

Yes

Yes

True

True

Does not appear

Yes, using [**VoiceCaption**](voicecaption-property.md)

No 

Yes

Yes

True

False

Does not appear

No

No 

Yes

Yes

False

True

Does not appear

Yes, using [**VoiceCaption**](voicecaption-property.md)

No 

Yes

Yes

False

False

Does not appear

No

No 

Yes

No 

True

True

Does not appear

No

No 

Yes

No 

True

False

Does not appear

No

No 

Yes

No 

False

True

Does not appear

No

No 

Yes

No 

False

False

Does not appear

No

Yes

No 

Yes

True

True

Normal, using [**Caption**](caption-property.md)

Yes, using [**Caption**](caption-property.md)

Yes

No 

Yes

True

False

Disabled, using [**Caption**](caption-property.md)

No

Yes

No 

Yes

False

True

Does not appear

Yes, using [**Caption**](caption-property.md)

Yes

No 

Yes

False

False

Does not appear

No

Yes

No 

No 

True

True

Normal, using [**Caption**](caption-property.md)

No

Yes

No 

No 

True

False

Disabled, using [**Caption**](caption-property.md)

No

Yes

No 

No 

False

True

Does not appear

No

Yes

No 

No 

False

False

Does not appear

No

No 

No 

Yes

True

True

Does not appear

No 

No 

No 

Yes

True

False

Does not appear

No

No 

No 

Yes

False

True

Does not appear

No 

No 

No 

Yes

False

False

Does not appear

No

No 

No 

No 

True

True

Does not appear

No

No 

No 

No 

True

False

Does not appear

No

No 

No 

No 

False

True

Does not appear

No

No 

No 

No 

False

False

Does not appear

No

 If the property setting is null. In some programming languages, an empty string may not be interpreted the same as a null string.  The command is still voice-accessible.<br/>



 

When the server receives input for one of your commands, it sends a [**Command**](/windows/desktop/lwef/the-command-object) event, and passes back the name of the **Command** as an attribute of the [**UserInput**](/windows/desktop/lwef/iagentuserinput) object. You can then use conditional statements to match and process the **Command**.

 

