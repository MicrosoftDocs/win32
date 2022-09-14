---
description: Describes how to create a new WMI script using either the PowerShell or VBScript scripting languages.
ms.assetid: 90e71e17-c2e7-42ad-a72e-2b475e6163fe
ms.tgt_platform: multiple
title: Creating a WMI Script
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Creating a WMI Script

You can view or manipulate any information made available through WMI using scripts. Scripts can be written in any scripting language that supports Microsoft ActiveX script hosting, including Visual Basic Scripting Edition (VBScript), PowerShell, and Perl. Windows Script Host (WSH), Active Server Pages, and Internet Explorer can all host WMI scripts.

> [!Note]
>
> The primary scripting language currently supported by WMI is PowerShell. However, WMI also contains a robust body of scripting support for VBScript and other languages that access the [Scripting API for WMI](scripting-api-for-wmi.md).

 

## WMI Scripting Languages

The two main languages supported by WMI are PowerShell and VBScript (through the Windows Script Host, or WSH).

-   **PowerShell** was designed with tight integration with WMI in mind. As such, much of the underlying elements of WMI are built into the WMI cmdlets: [Get-WmiObject](/powershell/module/microsoft.powershell.management/get-wmiobject), [Set-WmiInstance](/powershell/module/microsoft.powershell.management/set-wmiinstance), [Invoke-WmiMethod](/powershell/module/microsoft.powershell.management/invoke-wmimethod), and [Remove-WmiObject](/powershell/module/microsoft.powershell.management/remove-wmiobject). The following table describes the general processes used for accessing WMI information. Note that while most of these examples use Get-WMIObject, many of the PowerShell WMI cmdlets have the same parameters, such as *-Class* or *-Credentials*. Therefore, many of these processes also work for other objects. For a more in-depth discussion of PowerShell and WMI, see [Using the Get-WMiObject Cmdlet](/previous-versions/windows/it-pro/windows-powershell-1.0/ee176860(v=technet.10)) and [Windows PowerShell - the WMI Connection](/previous-versions/technet-magazine/cc162365(v=msdn.10)).

-   **VBScript**, in contrast, explicitly makes calls to the [Scripting API for WMI](scripting-api-for-wmi.md), as mentioned above. Other languages, such as Perl, can also use the scripting API for WMI. However, for the purposes of this documentation, most samples that demonstrate the scripting API for WMI will use VBScript. When a programming technique is specific to VBScript, however, it will be called out.

    VBScript has essentially two separate ways of accessing WMI. The first is using an [**SWbemLocator**](swbemlocator.md) object to connect to WMI. Alternately, you can use [**GetObject**](/windows/desktop/api/Provider/nf-provider-provider-getobject(cinstance_long_cframeworkquery_)) and a moniker. A moniker is a string that can describe a number of elements: your credentials, impersonation settings, what computer you want to connect to, the WMI [*namespace*](gloss-n.md) (ie, the general location where WMI stores groups of objects), and what WMI object you want to retrieve. Many of the examples below describe both techniques. For more information, see [Constructing a Moniker String](constructing-a-moniker-string.md) and [Describing the Location of a WMI Object](describing-the-location-of-a-wmi-object.md).

    Regardless of what technique you use to connect to WMI, you will likely retrieve one or more objects from the Scripting API. The most common is [**SWbemObject**](swbemobject.md), which WMI uses to describe a WMI object. Alternately, you may use an [**SWbemServices**](swbemservices.md) object to describe the WMI service itself, or an [**SWbemObjectPath**](swbemobjectpath.md) object to describe the location of a WMI object. For more information, see [Scripting with SWbemObject](scripting-with-swbemobject.md) and [Scripting Helper Objects](scripting-helper-objects.md).

## Using WMI and a Scripting Language, How Do I...

<dl> <dt>

<span id="...connect_to_WMI_"></span><span id="...connect_to_wmi_"></span><span id="...CONNECT_TO_WMI_"></span>...connect to WMI?
</dt> <dd>

For VBScript and the Scripting API for WMI, retrieve an [**SWbemServices**](swbemservices.md) object with a moniker and a call to [**GetObject**](/windows/desktop/api/Provider/nf-provider-provider-getobject(cinstance_long_cframeworkquery_)). Alternately, you can connect to the server with a call to [**SWbemLocator.ConnectServer**](/windows/desktop/api/Wbemcli/nf-wbemcli-iwbemlocator-connectserver). You can then use the object to access a specific WMI namespace or WMI class instance.

For PowerShell, connecting to WMI is generally done directly in the cmdlet call; as such, no additional steps are necessary.

For more information, see [Describing the Location of a WMI Object](describing-the-location-of-a-wmi-object.md), [Constructing a Moniker String](constructing-a-moniker-string.md), and [Connecting to WMI with VBScript](connecting-to-wmi-with-vbscript.md).


```VB
Set objLocator = CreateObject("WbemScripting.SWbemLocator")
Set objService = objLocator.ConnectServer(".", "root\cimv2")

' Second example: implicitly uses the local compuer (.) and default namespace ("root\cimv2")
Set objWMIService = GetObject("winmgmts:")
```


```PowerShell

#Already has all the defaults set
get-WmiObject Win32_LogicalDisk

#Or, to be explicit,
get-WmiObject -class Win32_LogicalDisk -Computer &quot;.&quot; -Namespace &quot;root\cimv2&quot; -Impersonation Impersonate
```





</dd> <dt>

<span id="...retrieve_information_from_WMI_"></span><span id="...retrieve_information_from_wmi_"></span><span id="...RETRIEVE_INFORMATION_FROM_WMI_"></span>...retrieve information from WMI?
</dt> <dd>

For VBScript and the Scripting API for WMI, use a retrieval function, such as [**WbemServices.Get**](swbemservices-get.md) or [**WbemServices.InstancesOf**](swbemservices-instancesof.md). You may also place the class name of the object to retrieve in a moniker, which may be more efficient.

For PowerShell, use the *-Class* parameter. Note that -Class is the default parameter; as such, you don't need to explicitly state it.

For more information, see [Retrieving WMI Class or Instance Data](retrieving-class-or-instance-data.md).


```VB
Set objLocator = CreateObject("WbemScripting.SWbemLocator")
Set objService = objLocator.ConnectServer(".", "root\cimv2")
Set colScheduledJobs = objService.InstancesOf("Win32_ScheduledJob")

' Second example
SSet Service = GetObject("WinMgmts:{impersonationLevel=impersonate}!Win32_Service=""ALERTER""")
```


```PowerShell

#default - you don't actually need to use the -Class parameter
Get-WMIObject Win32_WmiSetting

#but you can if you want to
Get-WMIObject -Class Win32_WmiSetting
```





</dd> <dt>

<span id="...create_a_WMI_query_"></span><span id="...create_a_wmi_query_"></span><span id="...CREATE_A_WMI_QUERY_"></span>...create a WMI query?
</dt> <dd>

For VBScript and the Scripting API for WMI, use the [**SWbemServices.ExecQuery**](swbemservices-execquery.md) method.

For PowerShell, use the *-Query* parameter. You can also filter using the *-Filter* parameter.

For more information, see [Querying WMI](querying-wmi.md).


```VB
strComputer = "."
Set objWMIService = GetObject("winmgmts:{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2")
Set colScheduledJobs = objWMIService.ExecQuery("Select * from Win32_ScheduledJob")
For Each objJob in colScheduledJobs
    Wscript.Echo "Job ID: " & objJob.JobId & "Command: " & objJob.Command & VBNewLine
```


```PowerShell

Get-WmiObject -query &quot;SELECT * FROM Win32_logicalDisk WHERE DeviceID = 'C:'&quot;

#or

get-wmiObject -Class Win32_LogicalDisk -Filter &quot;DeviceID = &#39;C:&#39;&quot;
```





</dd> <dt>

<span id="...enumerate_through_a_list_of_WMI_objects_"></span><span id="...enumerate_through_a_list_of_wmi_objects_"></span><span id="...ENUMERATE_THROUGH_A_LIST_OF_WMI_OBJECTS_"></span>...enumerate through a list of WMI objects?
</dt> <dd>

For VBScript and the Scripting API for WMI, use the [**SWbemObjectSet**](swbemobjectset.md) container object, which is treated in script as a collection that can be enumerated. You can retrieve an **SWbemObjectSet** from a call from [**SWbemServices.InstancesOf**](swbemservices-instancesof.md) or [**SWbemServices.ExecQuery**](swbemservices-execquery.md).

PowerShell is able to retrieve and handle enumerations as it would any other object; there is nothing particularly unique to WMI.

For more information, see [Accessing a Collection](accessing-a-collection.md).


```VB
For Each Disk In GetObject("winmgmts:").InstancesOf ("CIM_LogicalDevice")
```


```PowerShell

$logicalDevices = Get-WmiObject CIM_LogicalDevice
foreach ($device in $logicalDevices)
{
    $device.name
}

#or, to be more compact

Get-WmiObject cim_logicalDevice | ForEach-Object { $_.name }

```





</dd> <dt>

<span id="...access_a_different_WMI_namespace_"></span><span id="...access_a_different_wmi_namespace_"></span><span id="...ACCESS_A_DIFFERENT_WMI_NAMESPACE_"></span>...access a different WMI namespace?
</dt> <dd>

For VBScript and the Scripting API for WMI, state the namespace in the moniker, or else you can explicitly state the namespace in the call to [**SwbemLocator.ConnectServer**](/windows/desktop/api/Wbemcli/nf-wbemcli-iwbemlocator-connectserver).

For PowerShell, use the *-Namespace* parameter. The default namespace is "root\\cimV2"; however, many older classes are stored in "root\\default".

To find the location of a given WMI class, look at the reference page. Alternately, you can manually explore a namespace using get-WmiObject.


```VB
Set objLocator = CreateObject("WbemScripting.SWbemLocator")
Set objService = objLocator.ConnectServer(".", "root\cimv2")

' Second example
Set objWMIService = GetObject("winmgmts:{impersonationLevel=impersonate}!\\" & "." & "\root\cimv2")
```


```PowerShell

Get-WmiObject -list * -Namespace root\default

#or, to retrieve all namespaces,
Get-WmiObject -Namespace root -Class __Namespace
```





</dd> <dt>

<span id="...retrieve_all_child_instances_of_a_class_"></span><span id="...RETRIEVE_ALL_CHILD_INSTANCES_OF_A_CLASS_"></span>...retrieve all child instances of a class?
</dt> <dd>

For languages that directly use the Scripting API for WMI and PowerShell, WMI supports retrieving the child classes of a base class. As such, in order to retrieve the child instances, you need to only search for the parent class. The following example searches for [**CIM\_LogicalDisk**](/windows/desktop/CIMWin32Prov/cim-logicaldisk), which is a preinstalled WMI class that represents logical disks on a Windows-based computer system. As such, searching for this parent class also returns instances of [**Win32\_LogicalDisk**](/windows/desktop/CIMWin32Prov/win32-logicaldisk), which is what Windows uses to describe hard drives. For more information, see [Common Information Model](common-information-model.md). WMI supplies an entire schema of such preinstalled classes that allow you to access and control managed objects. For more information, see [Win32 Classes](/windows/desktop/CIMWin32Prov/win32-provider) and [WMI Classes](wmi-classes.md)..


```VB
For Each Disk In GetObject("winmgmts:").InstancesOf ("CIM_LogicalDisk")
  WScript.Echo "Instance:", Disk.Name
```




```PowerShell
Get-WmiObject CIM_LogicalDisk | ForEach-Object { "Instance: " + $_.Name  }
```



</dd> <dt>

<span id="...locate_a_WMI_object_"></span><span id="...locate_a_wmi_object_"></span><span id="...LOCATE_A_WMI_OBJECT_"></span>...locate a WMI object?
</dt> <dd>

For both the Scripting API for WMI and PowerShell, WMI uses a combination of namespace, class name, and key properties to uniquely identify a given WMI instance. Together, this is known as the WMI object path. For VBScript, the [**SWbemObject.Path\_**](swbemobject-path-.md) property describes the path for any given object returned by the scripting API. For PowerShell, every WMI object will have a \_\_PATH property. For more information, see [Describing the Location of a WMI Object](describing-the-location-of-a-wmi-object.md)

In addition to namespace and class name, a WMI object will also have a key property, which uniquely identifies that instance compared to other instances on your machine. For example, the **DeviceID** property is the key property for the [**Win32\_LogicalDisk**](/windows/desktop/CIMWin32Prov/win32-logicaldisk) class. For more information, see [Managed Object Format (MOF)](managed-object-format--mof-.md).

Finally, the Relative path is simply a shortened form of the path, and includes the class name and key value. In the examples below, the path may be "\\\\computerName\\root\\cimv2:Win32\_LogicalDisk.DeviceID="D:"", while the relative path would be ""Win32LogicalDisk.DeviceID="D""".


```VB
For Each Disk In GetObject("winmgmts:").InstancesOf ("CIM_LogicalDisk")
  WScript.Echo "Instance:", Disk.Path_.Relpath

'or to get the path
For Each Disk In GetObject("winmgmts:").InstancesOf ("CIM_LogicalDisk")
  WScript.Echo "Instance:", Disk.Path_
```




```PowerShell
#retrieving the path
Get-WmiObject CIM_LogicalDisk | ForEach-Object { "Instance: " + $_.__PATH  }

#retrieving the relative path
Get-WmiObject CIM_LogicalDisk | ForEach-Object { "Instance: " + $_.__RELPATH  }
```



</dd> <dt>

<span id="...set_information_in_WMI_"></span><span id="...set_information_in_wmi_"></span><span id="...SET_INFORMATION_IN_WMI_"></span>...set information in WMI?
</dt> <dd>

For VBScript and the Scripting API for WMI, use the [**SWbemObject.Put\_**](swbemobject-put-.md) method.

For PowerShell, you can either use the Put method, or else [Set-WmiInstance](/powershell/module/microsoft.powershell.management/set-wmiinstance?view=powershell-5.1&preserve-view=true).

For more information, see [Modifying an Instance Property](modifying-an-instance-property.md).


```VB
wbemCimtypeString = 8
Set objSWbemService = GetObject("Winmgmts:root\default")
Set objClass = objSWbemService.Get()
objClass.Path_.Class = "NewClass"

' Add a property
' String property
objClass.Properties_.add "PropertyName", wbemCimtypeString  
' Make the property a key property 
objClass.Properties_("PropertyName").Qualifiers_.add "key", true

' Write the new class to the root\default namespace in the repository
Set objClassPath = objClass.Put_
WScript.Echo objClassPath.Path

'Create an instance of the new class using SWbemObject.SpawnInstance
Set objNewInst = GetObject("Winmgmts:root\default:NewClass").Spawninstance_

objNewInst.PropertyName = "My Instance"

' Write the instance into the repository
Set objInstancePath = objNewInst.Put_
WScript.Echo objInstancePath.Path
```


```PowerShell

$mySettings = get-WMIObject Win32_WmiSetting
$mySettings.LoggingLevel = 1
$mySettings.Put()

#or

Set-WMIInstance -class Win32_WMISetting -argument @{LoggingLevel=1}
```





</dd> <dt>

<span id="...use_different_credentials_"></span><span id="...USE_DIFFERENT_CREDENTIALS_"></span>...use different credentials?
</dt> <dd>

For VBScript and the Scripting API for WMI, use the *UserName* and *Password* parameters in the [**SWbemLocator.ConnectServer**](swbemlocator-connectserver.md) method.

For PowerShell, use the *-Credential* parameter.

Note that you can only use alternate credentials on a remote system. For more information, see [Securing Scripting Clients](securing-scripting-clients.md).


```VB
strComputer = "remoteComputerName" 
strDomain = "DOMAIN" 
Wscript.StdOut.Write "Please enter your user name:"
strUser = Wscript.StdIn.ReadLine 
Set objPassword = CreateObject("ScriptPW.Password")
Wscript.StdOut.Write "Please enter your password:"
strPassword = objPassword.GetPassword()
 
Set objSWbemLocator = CreateObject("WbemScripting.SWbemLocator")
Set objSWbemServices = objSWbemLocator.ConnectServer(strComputer, _
                                                     "Root\CIMv2", _
                                                     strUser, _
                                                     strPassword, _
                                                     "MS_409", _
                                                     "ntlmdomain:" + strDomain)
Set colSwbemObjectSet = objSWbemServices.ExecQuery("Select * From Win32_Process")
For Each objProcess in colSWbemObjectSet
    Wscript.Echo "Process Name: " & objProcess.Name 
Next
```


```PowerShell

$Computer = &quot;atl-dc-01&quot;

Get-WmiObject -Namespace &quot;root\cimv2&quot; -Class Win32_Process -Credential FABRIKAM\administrator  `
-ComputerName $Computer
```





</dd> <dt>

<span id="...access_a_remote_computer_"></span><span id="...ACCESS_A_REMOTE_COMPUTER_"></span>...access a remote computer?
</dt> <dd>

For VBScript and the Scripting API for WMI, explicitly state the name of the computer in either the moniker, or else in the call to [**SWbemLocator.ConnectServer**](swbemlocator-connectserver.md). For more information, see [Connecting to WMI Remotely with VBScript](connecting-to-wmi-remotely-with-vbscript.md).

For PowerShell, use the *-ComputerName* parameter. For more information, see [Connecting to WMI Remotely with PowerShell](connecting-to-wmi-on-a-remote-computer-by-using-powershell.md).


```VB
Set objLocator = CreateObject("WbemScripting.SWbemLocator")
Set objService = objLocator.ConnectServer("myRemoteServerName", "root\cimv2")
Set colScheduledJobs = objService.ExecQuery("SELECT * FROM Win32_ScheduledJob")
For Each objJob in colScheduledJobs
    Wscript.Echo "Job ID: " & objJob.JobId & "Command: " & objJob.Command & VBNewLine

'example 2

strComputer = "myRemoteServerName"
Set objWMIService = GetObject("winmgmts:{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2")
Set colScheduledJobs = objWMIService.ExecQuery("Select * from Win32_ScheduledJob")
For Each objJob in colScheduledJobs
    Wscript.Echo "Job ID: " & objJob.JobId & "Command: " & objJob.Command & VBNewLine
```


```PowerShell

$Computer = &quot;atl-dc-01&quot;

Get-WmiObject -Namespace &quot;root\cimv2&quot; -Class Win32_logicalDisk -ComputerName $Computer
```





</dd> <dt>

<span id="...set_the_Authentication_and_Impersonation_levels_"></span><span id="...set_the_authentication_and_impersonation_levels_"></span><span id="...SET_THE_AUTHENTICATION_AND_IMPERSONATION_LEVELS_"></span>...set the Authentication and Impersonation levels?
</dt> <dd>

For VBScript and the Scripting API for WMI, use the [**SWbemServices.Security\_**](swbemlocator-security-.md) property on the returned server object, or else set the relevant values in the moniker.

For PowerShell, use the *-Authentication* and *-Impersonation* parameters, respectively. For more information, see [Securing Scripting Clients](securing-scripting-clients.md).

For more information, see [Securing Scripting Clients](securing-scripting-clients.md).


```VB
' First example
Set Service = GetObject("WinMgmts:{impersonationLevel=impersonate}!Win32_Service=""ALERTER""")

' Second example
Set Locator = CreateObject("WbemScripting.SWbemLocator")
Set Service = Locator.ConnectServer       
service.Security_.ImpersonationLevel = wbemImpersonationLevelImpersonate  
Set objinstance = Service.Get("Win32_Service=""ALERTER""")
```


```PowerShell

$Computer = &quot;atl-dc-01&quot;

Get-WmiObject -Namespace &quot;root\cimv2&quot; -Class Win32_Process -Impersonation Impersonate `
 -Authentication PacketIntegrity -Credential FABRIKAM\administrator -ComputerName $Computer
```





</dd> <dt>

<span id="...handle_errors_in_WMI_"></span><span id="...handle_errors_in_wmi_"></span><span id="...HANDLE_ERRORS_IN_WMI_"></span>...handle errors in WMI?
</dt> <dd>

For the Scripting API for WMI, the provider may supply an [**SWbemLastError**](swbemlasterror.md) object to give further information on an error.

In VBScript in particular, error handling is also supported using the native **Err** object. You may also access the [**SWbemLastError**](swbemlasterror.md)object, as described above. For more information, see [Retrieving an Error Code](retrieving-an-error-code.md).

For PowerShell, you can use the standard PowerShell error handling techniques. For more information, see [An Introduction to Error Handling in PowerShell](/archive/blogs/kebab/an-introduction-to-error-handling-in-powershell).


```VB
'using Err
On Error Resume Next
Set objProcess = GetObject("winmgmts:root\cimv2:Win32_Process.Handle='one'")
Wscript.Echo Err.Number

'using SWbemLastError

On Error Resume Next
Set obj = GetObject("winmgmts:root\cimv2:Win32_Process.Handle='one'")
Set LastError = createobject("wbemscripting.swbemlasterror")
Wscript.Echo "Operation = " & LastError.operation & VBCRLF & "ParameterInfo = " _
            & LastError.ParameterInfo & VBCRLF & "ProviderName = " & LastError.ProviderName
```



</dd> </dl>

 

 
