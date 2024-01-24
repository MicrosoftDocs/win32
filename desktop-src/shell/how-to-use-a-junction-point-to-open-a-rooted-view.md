---
description: You can use the registry to specify that browsing into a junction point will open a rooted view rather than the default view of the contents of the associated extension.
title: How to Open a Rooted View of a Junction Point Through the Registry
ms.topic: article
ms.date: 05/31/2018
---

# How to Open a Rooted View of a Junction Point Through the Registry

You can use the registry to specify that browsing into a junction point will open a rooted view rather than the default view of the contents of the associated extension.

## Instructions


To specify that browsing into a junction point should open a rooted view, add **Open**\\**Command** and **Explore**\\**Command** subkeys to your extension's **CLSID** subkey, with their default values assigned to the command lines shown here:

```
HKEY_CLASSES_ROOT
   CLSID
      {Extension CLSID}
         Shell
            Open
               Command
                  (Default) = %SYSTEMROOT%\explorer.exe/e,/root,"%1"
            Explore
               Command
                  (Default) = %SYSTEMROOT%\explorer.exe/e,/root,"%1"
```

Once you've added those values, an instance of Explorer.exe is launched to display the contents of the extension as a rooted view when the user selects the junction point.

## Related topics

<dl> <dt>

[Specifying a Namespace Extension's Location](nse-junction.md)
</dt> <dt>

[How to Open a Rooted View of a Junction Point Through a Shortcut File](how-to-use-a-shortcut-file-to-open-a-rooted-view.md)
</dt> </dl>

 

 



