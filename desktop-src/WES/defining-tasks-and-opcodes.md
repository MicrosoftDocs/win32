---
title: Defining Tasks and Opcodes
description: Providers use tasks and opcodes to logically group events. Grouping events helps consumers query for only those events that contain specific task and opcode combinations.
ms.assetid: 6a872517-14de-423e-a7ff-7edb9a29b22d
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Defining Tasks and Opcodes

Providers use tasks and opcodes to logically group events. Grouping events helps consumers query for only those events that contain specific task and opcode combinations. Typically, you use tasks to identify a major component of the provider such as the networking or database component. You could then use opcodes to identify the operations that the component performs, such as the send and receive operations for a networking component. If you had only one component, you could use task to reflect a major operation in the component, such as connect or disconnect, and use opcode to reflect an activity within the operation such as reading the registry. You could also use opcode without specifying a task. How you use task and opcodes to group events for the consumer is completely up to you.

To define a task, use the **task** element. To define an opcode, use the **opcode** element. You can define the opcodes at the provider level (known as global opcodes) or locally at the task level (known as task-specific opcodes). If your provider will define more than 228 operations, you must define task-specific opcodes or a combination of task-specific and global opcodes. You can specify up to 228 global opcodes and up to 228 task-specific opcodes for each task that you define. The opcodes must be in the range from 11 through 239. The Winmeta.xml file defines common operations that you can use instead of defining your own.

The following example shows how to define a task, a task with task-specific opcodes, and several global opcodes.


```XML
<instrumentationManifest
    xmlns="http://schemas.microsoft.com/win/2004/08/events" 
    xmlns:win="http://manifests.microsoft.com/win/2004/08/windows/events"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"    
    >

    <instrumentation>
        <events>
            <provider name="Microsoft-Windows-SampleProvider" 
                guid="{1db28f2e-8f80-4027-8c5a-a11f7f10f62d}" 
                symbol="PROVIDER_GUID" 
                resourceFileName="<path to the exe or dll that contains the metadata resources>" 
                messageFileName="<path to the exe or dll that contains the string resources>"
                message="$(string.Provider.Name)">

                . . .

                <tasks>
                    <task name="Disconnect" 
                          symbol="TASK_DISCONNECT"
                          value="0" 
                          message="$(string.Task.Disconnect)"/>
 
                    <task name="Connect" 
                          symbol="TASK_CONNECT"
                          value="1" 
                          message="$(string.Task.Connect)">

                        <opcodes>
                            <opcode name="ReadRegistry" 
                                    symbol="OPCODE_READ_REGISTRY" 
                                    value="11"
                                    message="$(string.Task.Connect.ReadRegistry)"/>
                        </opcodes>
                    </task>

                    <task name="Validate" 
                          symbol="TASK_VALIDATE"
                          value="2" 
                          message="$(string.Task.Validate)">

                        <opcodes>
                            <opcode name="GetRules" 
                                    symbol="OPCODE_GET_RULES" 
                                    value="11"
                                    message="$(string.Task.Validate.GetRules)"/>
                        </opcodes>
                    </task>
                </tasks>

                <opcodes>
                    <opcode name="Initialize" 
                            symbol="OPCODE_INITIALIZE" 
                            value="12"
                            message="$(string.Opcode.Initialize)"/>

                    <opcode name="Cleanup" 
                            symbol="OPCODE_CLEANUP" 
                            value="13"
                            message="$(string.Opcode.Cleanup)"/>
                 </opcodes>

                . . .

            </provider>
        </events>
    </instrumentation>

    <localization>
        <resources culture="en-US">
            <stringTable>
                <string id="Provider.Name" value="Sample Provider"/>
                <string id="Task.Disconnect" value="Disconnect"/>
                <string id="Task.Connect" value="Connect"/>
                <string id="Task.Connect.ReadRegistry" value="ReadRegistry"/>
                <string id="Task.Validate" value="Connect"/>
                <string id="Task.Validate.GetRules" value="GetRules"/>
                <string id="Opcode.Initialize" value="Initialize"/>
                <string id="Opcode.Cleanup" value="Cleanup"/>
            </stringTable>
        </resources>
    </localization>

</instrumentationManifest>
```



 

 




