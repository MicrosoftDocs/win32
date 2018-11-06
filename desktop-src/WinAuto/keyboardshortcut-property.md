---
title: KeyboardShortcut Property
description: The KeyboardShortcut property describes a key or key combination that activates a specified accessible object.
ms.assetid: 42587468-f069-4ef1-868e-ac6a285e1715
ms.topic: article
ms.date: 05/31/2018
---

# KeyboardShortcut Property

The **KeyboardShortcut** property describes a key or key combination that activates a specified accessible object.

The **KeyboardShortcut** property is retrieved by calling [**IAccessible::get\_accKeyboardShortcut**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_acckeyboardshortcut).

The retrieved string describes a *shortcut key* (also called a *keyboard accelerator*) or an *access key* (also called a *mnemonic*). An access key is an underlined character in the text of a menu, menu item, or label of a control such as a push button.

The retrieved string must contain the name of the key along with the modifier key or keys. The string must be in the following format so that clients can easily parse it: \[\[modifier key\]+\[...\]+\] key name.

Examples include ALT+F, CTRL+ALT+4, WIN+F1, CTRL+ALT+SHIFT+BACKSPACE, or simply BACKSPACE.

The following table lists modifier keys.



| Modifier key | Description                        |
|--------------|------------------------------------|
| ALT          | Alternate modifier key             |
| CTRL         | Control modifier key               |
| SHIFT        | Shift modifier key                 |
| WIN          | Windows logo key                   |
| FN           | Function key on portable computers |



 

Do not localize keyboard shortcut strings.

## Handling Objects That Have Both Key Types

If an object has both a shortcut key and an access key, the **KeyboardShortcut** property returns the access key. The access key is the one a user would press when the object or the object's parent has the keyboard focus. For example, the **Print** menu item might have both a shortcut key (CTRL+P) and an access key (P). If a user presses CTRL+P while the menu is active, nothing happens. But if a user presses P while the menu is active, it invokes the application's **Print** dialog box. In this case, the **KeyboardShortcut** property is "P" to reflect what the user must press when the menu has the keyboard focus.

 

 




