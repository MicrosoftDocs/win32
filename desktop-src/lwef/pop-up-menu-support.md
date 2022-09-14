---
title: Pop-up Menu Support
description: Pop-up Menu Support
ms.assetid: a8a1cf91-c18a-497f-89a7-b47536eaca0a
ms.topic: article
ms.date: 05/31/2018
---

# Pop-up Menu Support

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

Microsoft Agent includes a pop-up menu (also known as a contextual menu) for each character. The server displays this pop-up menu automatically when a user right-clicks the character. You can add commands for your client application to the menu by defining a [**Commands**](/windows/desktop/lwef/the-commands-collection-object) collection. For each command in the collection that you define, you can specify [**Caption**](caption-property.md) and [**Visible**](visible-property.md) properties. The **Caption** is the text that appears in the menu when the **Visible** property is set to **True**. You can also use the [**Enabled**](enabled-property.md) property to display the command in the menu as disabled and the [**HelpContextID**](helpcontextid-property.md) to support Help support for the property. Define the access key for the menu text by including an ampersand (&) before the text character of the **Caption** text setting.

The server automatically adds to the menu commands for opening the Voice Commands Window and hiding the character as well as the [**Commands**](/windows/desktop/lwef/the-commands-collection-object) captions of other clients of the character to enable users to switch between clients. The server automatically adds a separator to the menu between its menu entries and those defined by the client. Separators appear only when there are items in the menu to separate.

To remove commands from a menu, use the [**Remove**](remove-method.md) method. Note that menu entries do not change while the menu displays. If you add or remove commands or change their properties, the menu displays the changes when the user redisplays the menu.

If you prefer to provide your own pop-up menu services for a character, you can use the [**AutoPopupMenu**](autopopupmenu-property.md) property to turn off server handling of the right-click action. You can then use the [**Click**](click-event.md) event notification to create your own menu handling behavior.

When the user selects a command from a character's pop-up menu or the Voice Commands Window, the server triggers the [**Command**](command-event.md) event of the associated client and passes back the parameters of the input using the [**UserInput**](/windows/desktop/lwef/iagentuserinput) object.

The server also provides a pop-up menu for the character's taskbar icon. When the character is visible, right-clicking this menu displays the same commands as those displayed by right-clicking the character. However, when the character is hidden, only the server-supplied commands are included.

 

 