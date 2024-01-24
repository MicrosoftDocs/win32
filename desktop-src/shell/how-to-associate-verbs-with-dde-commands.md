---
description: Illustrates invoking a DDE command using a Shell verb.
ms.assetid: 65DDD992-5E96-447E-9151-2CCA740822A1
title: How to Associate Verbs with DDE Commands
ms.topic: article
ms.date: 05/31/2018
---

# How to Associate Verbs with DDE Commands

Invoking a verb ordinarily launches the application that is specified by the verb's command subkey. However, if your application supports Dynamic Data Exchange (DDE), you can instead have the Shell initiate a DDE conversation.

To specify that invoking a verb should initiate a DDE conversation, follow these steps.

## Instructions

### Step 1:

Add a **ddeexec** subkey to the verb's key.

### Step 2:

Set the default value of **ddeexec** to the DDE command string.

## Remarks

The **ddeexec** key has three optional subkeys that provide some control over the DDE process:

-   **application**. Set the default value of this subkey to the application name to be used to establish the DDE conversation. If there is no **application** subkey, the default value of the verb's **command** subkey is used as the application name.
-   **topic**. Set the default value of this subkey to the topic name of the DDE conversation. If there is no **topic** subkey, System is used as the topic name.
-   **ifexec**. Set the default value of this subkey to the DDE command to be used if DDE conversation cannot be initiated. When initiation fails, the application that is specified by the default value of the verb's **command** subkey is launched. If an **ifexec** key exists, its default value will then be used as the DDE command. If there is no **ifexec** subkey, the default value of the **ddeexec** key will be used again as the DDE command.

The following example specifies that invoking the open verb for MyProgram.1 initiates a DDE conversation with a DDE command of Open("%1") and an application name of MyProgram.

```
HKEY_CLASSES_ROOT
   MyProgram.1
      (Default) = MyProgram Application
      Shell
         (Default) = doit
         open
            command
               (Default) = C:\MyDir\MyProgram.exe "%1"
            ddeexec
               (Default) = Open("%1")
               application
                  (Default) = MyProgram
```

 

 



