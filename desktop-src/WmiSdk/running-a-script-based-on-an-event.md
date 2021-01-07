---
description: The standard consumer that is implemented by the ActiveScriptEventConsumer class allows a computer to run a script and take action when important events occur to ensure that a computer can detect and resolve problems automatically.
ms.assetid: 0d2ac139-3e2b-4089-ae9c-289d376e27a2
ms.tgt_platform: multiple
title: Running a Script Based on an Event
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Running a Script Based on an Event

The standard consumer that is implemented by the [**ActiveScriptEventConsumer**](activescripteventconsumer.md) class allows a computer to run a script and take action when important events occur to ensure that a computer can detect and resolve problems automatically.

This consumer is loaded by default in the **root\\subscription** namespace.

You can configure the performance of all instances of [**ActiveScriptEventConsumer**](activescripteventconsumer.md) on a system by setting the values of the **Timeout** or **MaximumScripts** property in a single instance of [**ScriptingStandardConsumerSetting**](scriptingstandardconsumersetting.md).

The basic procedure for using standard consumers is always the same, and is located in [Monitoring and Responding to Events with Standard Consumers](monitoring-and-responding-to-events-with-standard-consumers.md). The following procedure that adds to the basic procedure, is specific to the [**ActiveScriptEventConsumer**](activescripteventconsumer.md) class, and describes how to create an event consumer that runs a script.

> [!Caution]  
> The [**ActiveScriptEventConsumer**](activescripteventconsumer.md) class has special security constraints. This standard consumer must be configured by a local member of the Administrators group on the local computer. If you use a domain account to create the subscription, the LocalSystem account must have the necessary permissions on the domain to verify that the creator is a member of the local Administrators group.

 

The following procedure describes how to create an event consumer that executes a script.

**To create an event consumer that executes a script**

1.  Write the script to run when an event takes place.

    You can write the script in any language, but ensure that a scripting engine for the language that you choose is installed on your machine. The script does not have to use WMI scripting objects.

    Only an administrator can set up a script consumer, and the script runs under LocalSystem credentials, which gives broad capabilities to the consumer except for network access. However, the script does not have access to specific user logon data, for example, environment variables and network shares.

2.  In the Managed Object Format (MOF) file, create an instance of [**ActiveScriptEventConsumer**](activescripteventconsumer.md) to receive the events you request in the query.

    You can put the text of the script in **ScriptText**, or you can specify the path and filename of the script in **ScriptFileName**. For more information, see [Designing Managed Object Format (MOF) Classes](designing-managed-object-format--mof--classes.md).

3.  Create an instance of [**\_\_EventFilter**](--eventfilter.md), name it, and then create a query to specify the type of event, which triggers executing the script.

    For more information see, [Querying with WQL](querying-with-wql.md).

4.  Create an instance of [**\_\_FilterToConsumerBinding**](--filtertoconsumerbinding.md) to associate the filter with the instance of [**ActiveScriptEventConsumer**](activescripteventconsumer.md).
5.  Compile the MOF file by using [**Mofcomp.exe**](mofcomp.md).

The examples in the following section show two ways to implement an event-driven script. The first example uses a script that is defined in an external file, and the second example uses a script that is built into the MOF code. The examples are in MOF code, but you can create the instances programmatically by using either the [Scripting API for WMI](scripting-api-for-wmi.md) or the [COM API for WMI](com-api-for-wmi.md).

## Example Using an External Script

The following procedure describes how to use the external script example.

**To use the external script example**

1.  Create a file named c:\\Asec.vbs, and then copy the script in this example into it.
2.  Copy the MOF list into a text file and save it with a .mof extension.
3.  In a command prompt window, compile the MOF file by using the following command.

    **Mofcomp** *filename***.mof**

4.  Run the Calculator, which creates a calc.exe process. Wait for more than five seconds, close the Calculator window, and then look in the C:\\ directory for a file named ASEC.log.

    The following text is similar to the text that will be contained in the ASEC.log file.

    ``` syntax
    Time: 12/31/2002 2:56:33 PM; Entry made by: ASEC
    Application closed. UserModeTime:  1562500; 
    KernelModeTime: 3125000 [hundreds of nanoseconds]
    ```

The following VBScript code example shows the script that is called when an event is received by the permanent consumer. The **TargetEvent** object is an [**\_\_InstanceDeletionEvent**](--instancedeletionevent.md) instance so it has a property named **TargetInstance**, which is a [**Win32\_Process**](/windows/desktop/CIMWin32Prov/win32-process) instance used to fire the event. The **Win32\_Process** class has the **UserModeTime** and **KernelModeTime** properties that are put into the log file created by the script.


```VB
' asec.vbs script
Dim objFS, objFile
Set objFS = CreateObject("Scripting.FileSystemObject")
Set objFile = objFS.OpenTextFile("C:\ASEC.log", 8, true)
objFile.WriteLine "Time: " & Now & "; Entry made by: ASEC"

objFile.WriteLine "Application closed. UserModeTime:  " & _
    TargetEvent.TargetInstance.UserModeTime & _
    "; KernelModeTime: " & _
    TargetEvent.TargetInstance.KernelModeTime & _
    " [hundreds of nanoseconds]"
objFile.Close
```



The following MOF code example calls the script when an event is received. It creates the filter, consumer, and the binding between them in the **root\\subscription** namespace.

``` syntax
#pragma namespace ("\\\\.\\root\\subscription")

instance of ActiveScriptEventConsumer as $Cons
{
    Name = "ASEC";
    ScriptingEngine = "VBScript";
    ScriptFileName = "c:\\asec2.vbs";
};

instance of __EventFilter as $Filt
{
    Name = "EF";
    Query = "SELECT * FROM __InstanceDeletionEvent WITHIN 5 "
        "WHERE TargetInstance ISA \"Win32_Process\" "
        "AND TargetInstance.Name = \"calc.exe\"";
    QueryLanguage = "WQL";
    EventNamespace = "root\\cimv2";
};

instance of __FilterToConsumerBinding
{
    Filter = $Filt;
    Consumer = $Cons;
};
```

## Example Using Inline Script

The following procedure describes how to use the inline script example.

**To use the inline script example**

1.  Copy the MOF list in this section into a text file, and save it with a .mof extension.
2.  In a command prompt window, compile the MOF file by using the following command.

    **Mofcomp** *filename***.mof**

The following MOF code example creates the filter, consumer, and the binding between them and also contains the script inline.

``` syntax
#pragma namespace ("\\\\.\\root\\subscription")

instance of ActiveScriptEventConsumer as $Cons
{
    Name = "ASEC";
    ScriptingEngine = "VBScript";
    
    ScriptText =
        "Dim objFS, objFile\n"
        "Set objFS = CreateObject(\"Scripting.FileSystemObject\")\n"
        "Set objFile = objFS.OpenTextFile(\"C:\\ASEC.log\","
        " 8, true)\nobjFile.WriteLine \"Time: \" & Now & \";"
        " Entry made by: ASEC\"\nobjFile.WriteLine"
        " \"Application closed. UserModeTime:  \" & "
        "TargetEvent.TargetInstance.UserModeTime &_\n"
        "\"; KernelModeTime: \" & "
        "TargetEvent.TargetInstance.KernelModeTime "
        "& \" [hundreds of nanoseconds]\"\n"
        "objFile.Close\n";
};

instance of __EventFilter as $Filt
{
    Name = "EF";
    Query = "SELECT * FROM __InstanceDeletionEvent WITHIN 5 "
        "WHERE TargetInstance ISA \"Win32_Process\" "
        "AND TargetInstance.Name = \"calc.exe\"";
    QueryLanguage = "WQL";
    EventNamespace = "root\\cimv2";
};

instance of __FilterToConsumerBinding
{
    Filter = $Filt;
    Consumer = $Cons;
};
```

## Related topics

<dl> <dt>

[Monitoring and Responding to Events with Standard Consumers](monitoring-and-responding-to-events-with-standard-consumers.md)
</dt> </dl>

 

 
