---
description: A logical consumer is an instance of a permanent event consumer class.
ms.assetid: fd984de8-0fe6-4b32-8e8c-4e2db84b4cc0
ms.tgt_platform: multiple
title: Creating a Logical Consumer
ms.topic: article
ms.date: 05/31/2018
---

# Creating a Logical Consumer

A logical consumer is an instance of a permanent event consumer class. The main purpose of a logical consumer is to provide the physical consumer with the parameters for the activities the physical consumer performs. For more information, see [Creating a New Permanent Event Consumer Class](creating-a-new-permanent-event-consumer-class.md). The permanent consumer must have the same [**CreatorSID**](--eventconsumer.md) in the consumer, filter, and binding instances. For more information, see [Receiving Events Securely](receiving-events-securely.md). For an example of using a logical consumer, see [Running a Script Based on an Event](running-a-script-based-on-an-event.md), which shows the use of the standard consumer class [**ActiveScriptEventConsumer**](activescripteventconsumer.md) to configure a permanent consumer.

The following procedure describes how to create a logical consumer.

**To create a logical consumer**

1.  Create an instance of your permanent consumer class.
2.  Fill the properties of the instance with the parameters of the action you want the physical consumer to perform.

The following MOF code example describes a logical consumer that contains a script.

``` syntax
#pragma namespace("\\\\.\\root\\subscription")

instance of ActiveScriptEventConsumer as $CONSUMER
{
    Name = "MyConsumerName";
    ScriptingEngine = "VBScript";
    ScriptText = 

        "Set objFS = CreateObject(\"Scripting.FileSystemObject\")\n"
        "Set objFile = objFS.OpenTextFile(\"C:\\\\ASEC.log\", 8, true);\n"
        "objFile.WriteLine \"Time: \" + new Date() + \";\n"
        "objFile.WriteLine \"Entry made by: \\\"ActiveScript\\\"\";\n"
        "objFile.Close\n";
    
    // this is the Administrators SID in array of bytes format
    CreatorSID = {1,2,0,0,0,0,0,5,32,0,0,0,32,2,0,0}; 
};
```

After you create the logical consumer, you must then link each filter to an event filter to assign the action to a particular event. For more information, see [Creating an Event Filter](creating-an-event-filter.md).

 

 



