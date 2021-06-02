---
description: You can use the registry to define one or more extended verbs. The associated commands will be displayed only when the user right-clicks an object while pressing the SHIFT key.
ms.assetid: C6E51716-1D4F-454F-9AF4-8D0E486CB885
title: How to Define Extended Verbs
ms.topic: article
ms.date: 05/31/2018
---

# How to Define Extended Verbs

You can use the registry to define one or more extended verbs. The associated commands will be displayed only when the user right-clicks an object while pressing the SHIFT key.

## Instructions


To define a verb as extended, simply add an "extended" **REG\_SZ** value to the verb's subkey. The value should not have any data associated with it. The following sample registry entry shows the example from the previous section, with "doit" defined as an extended verb.

```
HKEY_CLASSES_ROOT
   .myp
      (Default) = MyProgram.1
   MyProgram.1
      (Default) = MyProgram Application
      Shell
         (Default) = doit
         open
            command
               (Default) = C:\MyDir\MyProgram.exe "%1"
         doit
            (Default) = &Do It
            extended
            command
               (Default) = C:\MyDir\MyProgram.exe /d "%1"
         print
            command
               (Default) = C:\MyDir\MyProgram.exe /p "%1"
         printto
            command
               (Default) = C:\MyDir\MyProgram.exe /p "%1" "%2" %3 %4
```

 

 



