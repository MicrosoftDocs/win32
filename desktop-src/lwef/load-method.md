---
title: Load Method
description: Load Method
ms.assetid: 72a37471-f69b-49a5-a6eb-d65bff970c0f
ms.topic: article
ms.date: 05/31/2018
---

# Load Method

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

<dl> <dt>

<span id="Description"></span><span id="description"></span><span id="DESCRIPTION"></span>**Description**
</dt> <dd>

Loads a character into the [**Characters**](/windows/desktop/lwef/the-characters-object) collection.

</dd> <dt>

<span id="Syntax"></span><span id="syntax"></span><span id="SYNTAX"></span>**Syntax**
</dt> <dd>

*agent***.Characters.Load "***CharacterID***",** *Provider*



| Part          | Description                                                                                                                                                                                                                              |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *CharacterID* | Required. A string value that you will use to refer to the character data to be loaded.                                                                                                                                                  |
| *Provider*    | Required. A variant data type that must be one of the following: **Filespec** The local file location of the specified character's definition file. <br/> **URL** The HTTP address for the character's definition file.<br/> |



 

</dd> </dl>

## Remarks

You can load characters from the Agent subdirectory by specifying a relative path (one that does not include a colon or leading slash character). This prefixes the path with Agent's characters directory (located in the localized Windows\\msagent directory). For example, specifying the following would load Genie.acs from Agent's Chars directory:


```
   Agent.Character.Load "genie", "genie.acs"
```



You can also specify your own directory in Agent's Chars directory.


```
   Agent.Character.Load "genie", "MyCharacters\genie.acs"
```



You can load the character currently set as the current user's default character by not including a path as the second parameter of the **Load** method.


```
   Agent.Character.Load "character"
```



You cannot load the same character (a character having the same GUID) more than once from a single instance of the control. Similarly, you cannot load the default character and other characters at the same time from a single instance of the control because the default character could be the same as the other character. If you attempt to do this, the server raises an error. However, you can create another instance of the Agent control and load the same character.

The Microsoft Agent Data Provider supports loading character data stored either as a single structured file (.ACS) with character data and animation data together or as separate character data (.ACF) and animation (.ACA) files. Use the single structured .ACS file to load a character that is stored on a local disk or network and accessed using a conventional file protocol (such as UNC pathnames). Use the separate .ACF and .ACA files when you want to load the animation files individually from a remote site where they are accessed using the HTTP protocol.

For .ACS files, using the **Load** method provides access to a character's animations. For .ACF files, you also use the [**Get**](get-method.md) method to load animation data. The **Load** method does not support downloading .ACS files from an HTTP site.

Loading a character does not automatically display the character. Use the [**Show**](show-method.md) method first to make the character visible.

If you use the **Load** method to load a character file stored on the local machine and the call fails; for example, because the file is not found, Agent raises an error. You can use the support in your programming language to provide an error handling routine to catch and process the error.


```
   Sub Form_Load
      On Error GoTo ErrorHandler
      Agent1.Characters.Load "mychar", "genie.acs"
      ' Successful load
      . . .
      Exit Sub
      ErrorHandler:
      ' Unsuccessful load
      . . .
      Resume Next
   End Sub
```



You can also handle the error by setting [**RaiseRequestErrors**](https://www.bing.com/search?q=**RaiseRequestErrors**) to **False**, declaring a object, and assigning the **Load** request to it. Then follow the **Load** call with a statement that checks the status of the [**Request**](/windows/desktop/lwef/the-request-object) object.


```
Dim LoadRequest as Object

   Sub Form_Load
      Agent1.RaiseRequestErrors = False
      Set LoadRequest = Agent1.Characters.Load _
         ("mychar", "c:\some directory\some character.acs")
      If LoadRequest.Status Not 0 Then
         ' Unsuccessful load
         . . .
         Exit Sub
      Else 
         ' Successful load
         . . .
   End Sub
```



If you load a character that is not local; for example, using HTTP protocol, you can also check for a **Load** failure by assigning a [**Request**](/windows/desktop/lwef/the-request-object) object to the **Load** method. However, because this method of loading a character is handled asynchronously, check its status in the [**RequestComplete**](requestcomplete-event.md) event. This technique will not work loading a character using the UNC protocol because the **Load** method is processed synchronously.

 

