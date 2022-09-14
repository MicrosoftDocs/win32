---
title: Character Object Properties
description: Character Object Properties
ms.assetid: 86748de2-f5c8-4057-bfa4-79d46cac1e62
ms.topic: article
ms.date: 05/31/2018
---

# Character Object Properties

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

The [**Character**](/windows/desktop/lwef/the-characters-object) object exposes the following properties:

-   [**Active**](active-property.md)
-   [**AutoPopupMenu**](autopopupmenu-property.md)
-   [**Description**](description-property.md)
-   [**ExtraData**](extradata-property.md)
-   [**GUID**](guid-property.md)
-   [**HasOtherClients**](hasotherclients-property.md)
-   [**Height**](height-property.md)
-   [**HelpContextID**](helpcontextid-property-ch.md)
-   [**HelpFile**](helpfile-property.md)
-   [**HelpModeOn**](helpmodeon-property.md)
-   [**IdleOn**](idleon-property.md)
-   [**LanguageID**](languageid-property.md)
-   [**Left**](left-property.md)
-   [**MoveCause**](movecause-property.md)
-   [**Name**](name-property.md)
-   [**OriginalHeight**](originalheight-property.md)
-   [**OriginalWidth**](originalwidth-property.md)
-   [**Pitch**](pitch-property.md)
-   [**SoundEffectsOn**](soundeffectson-property.md)
-   [**Speed**](speed-property.md)
-   [**SRModeID**](srmodeid-property.md)
-   [**SRStatus**](srstatus-property.md)
-   [**Top**](top-property.md)
-   [**TTSModeID**](ttsmodeid-property.md)
-   [**Version**](version-property.md)
-   [**VisibilityCause**](visibilitycause-property.md)
-   [**Visible**](visible-property-cob.md)
-   [**Width**](width-property-co.md)

Note that the [**Height**](height-property.md), [**Left**](left-property.md), [**Top**](top-property.md), and [**Width**](width-property-co.md) properties of a character differ from those that may be supported by the programming environment for the placement of the control. The [**Character**](/windows/desktop/lwef/the-characters-object) properties apply to the visible presentation of a character, not the location of the Microsoft Agent control.

As with [**Character**](/windows/desktop/lwef/the-characters-object) object methods, you can access a character's properties using the [**Characters**](/windows/desktop/lwef/the-characters-object) collection, or simplify your syntax by declaring an object variable and setting it to a character in the collection. In the following example, Test1 and Test2 will be set to the same value:


```
   Dim Genie 
   Dim MyRequest
   
   Sub window_Onload

   Agent.Characters.Load "Genie", "https://agent.microsoft.com/characters/v2/genie/genie.acf"

   Set Genie = Agent.Characters("Genie")

   Genie.MoveTo 15,15
   Set MyRequest = Genie.Show()

   End Sub

   Sub Agent_RequestComplete(ByVal Request)

   If Request = MyRequest Then 
      Test1 = Agent.Characters("Genie").Top
      Test2 = Genie.Top
      MsgBox "Test 1 is " + cstr(Test1) + "and Test 2 is " + cstr(Test2)
   End If

   End Sub
```



Because the server loads a character asynchronously, ensure that the character has been loaded before querying its properties, for example, using the [**RequestComplete**](requestcomplete-event.md) event. Otherwise, the properties may return incorrect values.

 

 