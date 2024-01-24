---
description: WMI scripts can condense many of the steps required in a C++ program.
ms.assetid: 77168079-7253-4DB1-8252-7016F5A58DBA
ms.tgt_platform: multiple
title: Connecting to WMI with VBScript
ms.topic: article
ms.date: 05/31/2018
---

# Connecting to WMI with VBScript

WMI scripts can condense many of the steps required in a C++ program. They can connect to WMI, not only through an [**SWbemLocator**](swbemlocator.md) object, but also through the moniker "winmgmts:". A moniker is a short name that locates a namespace, class, or instance in WMI. The name "winmgmts:" is the WMI moniker that tells the Windows Script Host to use the WMI objects, connects to the default namespace, and obtains an [**SWbemServices**](swbemservices.md) object. Other connection information, such as an impersonation level or a specific class or instance, appears in the string following the moniker name. You can use monikers in calls that either create or get WMI objects. For more information, see [Constructing a Moniker String](constructing-a-moniker-string.md).

The following procedure describes how to connect to WMI using **SWbemLocator**.

**To connect to WMI using SWbemLocator**

1.  Retrieve a locator object with a call to [CreateObject](/previous-versions//xzysf6hc(v=vs.85)).

    ```VB
    Set Locator = CreateObject("WbemScripting.SWbemLocator")
    ```

    

2.  Log on to the namespace using a call to the [**ConnectServer**](swbemlocator-connectserver.md) method.

    ```VB
    Set objLocator = CreateObject("WbemScripting.SWbemLocator")
    Set objService = objLocator.ConnectServer(".", "root\cimv2")
    ```

    

    If you do not specify a computer in the call to [**ConnectServer**](swbemlocator-connectserver.md), then WMI connects to the local computer. If you do not specify a namespace, then WMI connects to the namespace specified in the registry key.

    **HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**\\**Microsoft**\\**WBEM**\\**Scripting**\\**Default Namespace**

    The default namespace is \\root\\cimv2. For more information about namespaces, see [Creating Hierarchies Within WMI](creating-hierarchies-within-wmi.md).

3.  Set the impersonation level with a call to the [**SWbemServices.Security\_**](swbemservices-security-.md) method.

    ```VB
    objService.Security_.ImpersonationLevel = 3 
    ```

    

    For more information, see [Setting the Default Process Security Level Using VBScript](setting-the-default-process-security-level-using-vbscript.md).

4.  Implement the purpose of your script.

    WMI exposes a variety of scripting objects that use to access and manipulate data across your network. For more information, see [Manipulating Class and Instance Information](manipulating-class-and-instance-information.md) and [Scripting API for WMI](scripting-api-for-wmi.md).

    ```VB
    Set objLocator = CreateObject("WbemScripting.SWbemLocator")
    Set objService = objLocator.ConnectServer(".", "root\cimv2")
    objService.Security_.ImpersonationLevel = 3
    Set Jobs = objService.ExecQuery("SELECT * FROM Win32_ScheduledJob")
    i=0
    For each Job in Jobs
        i = i+1   
        WScript.Echo Job.JobId & "  " & Job.Command & VBNewLine
    Next
    If i = 0 Then
        WScript.Echo "No Jobs Scheduled with the AT command were found"
    End If
    ```

    

The following procedure describes how to connect to WMI and retrieve an object using a moniker.

**To connect to WMI and retrieve an object using a moniker**

1.  Call [**GetObject**](https://msdn.microsoft.com/library/ebdktb00(v=VS.71).aspx) with a moniker in the input parameter.

    ```VB
    'the simple version
    Set MyObject = GetObject("winMgmts::Win32_scheduledJob")

    'Or the more complex version
    strComputer = "."
    Set MyObject = GetObject("winMgmts:{impersonationLevel=impersonate}!\\" & strComputer & "\Root\CIMv2:Win32_ScheduledJob")
    ```

    

    The moiniker contains a number of elements that you can use to connect to WMI:

    -   The "winmgmts:" tells WSH to use [Scripting API objects](scripting-api-objects.md). In this particular example, the WSH will know that it should return an SWbemObject that describes the first Win32\_scheduledJob on the system. Other possible objects to return would be an SWbemCollection or an [**SWbemServices**](swbemservices.md) object, depending on what the moniker described.

    -   You can optionally set the security levels for the connection. Note that you cannot set name and password information in a moniker, however. For more information, see [Securing Scripting Clients](securing-scripting-clients.md).

    -   You can optionally define the path to the WMI object. This includes either the local or remote computer, the namespace, as well as the name of the class. For more information about using the VBScript [**GetObject**](https://msdn.microsoft.com/library/ebdktb00(v=VS.71).aspx) in WMI scripts, see [Creating an Instance](creating-an-instance.md) and [Retrieving a WMI Instance](retrieving-an-instance.md).

2.  Instead of retrieving a single item or collection, you can also choose to retrieve the [**SWbemServices**](swbemservices.md) object (as described in the previous example). Afterwards, you can then call additional queries on the returned object.

    ```VB
    strComputer = "."
    Set objWMIService = GetObject("winmgmts:{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2")
    Set colScheduledJobs = objWMIService.ExecQuery("Select * from Win32_ScheduledJob")
    For Each objJob in colScheduledJobs
        Wscript.Echo "Job ID: " & objJob.JobId & "Command: " & objJob.Command & VBNewLine
    Next
    ```

    

    In the previous example, impersonate, or impersonationLevel=3, is the default process security level. In the following example, it is not necessary to specify this process security level unless you need to change the process security to **delegate**. For more information, see [Setting the Default Process Security Level Using VBScript](setting-the-default-process-security-level-using-vbscript.md).

## Related topics

<dl> <dt>

[Scripting in WMI](/windows/desktop/WmiSdk/creating-a-wmi-script)
</dt> </dl>

 

 
