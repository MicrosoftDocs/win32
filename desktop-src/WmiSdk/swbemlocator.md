---
description: You can use the methods of the SWbemLocator object to obtain an SWbemServices object that represents a connection to a namespace on either a local computer or a remote host computer.
ms.assetid: 51ea2c01-04e8-4b1c-bc82-ac96ba8b6eee
ms.tgt_platform: multiple
title: SWbemLocator object (Wbemdisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SWbemLocator
- ISWbemLocator
api_type: 
- COM
api_location: 
- Wbemdisp.dll
---

# SWbemLocator object

You can use the methods of the **SWbemLocator** object to obtain an [**SWbemServices**](swbemservices.md) object that represents a connection to a namespace on either a local computer or a remote host computer. You can then use the methods of the **SWbemServices** object to access WMI. This object can be created by the VBScript **CreateObject** call.

## Members

The **SWbemLocator** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **SWbemLocator** object has these methods.



| Method                                              | Description                                           |
|:----------------------------------------------------|:------------------------------------------------------|
| [**ConnectServer**](swbemlocator-connectserver.md) | Connects to WMI on the specified computer.<br/> |



 

### Properties

The **SWbemLocator** object has these properties.



| Property                                                | Access type          | Description                                              |
|:--------------------------------------------------------|:---------------------|:---------------------------------------------------------|
| [**Security\_**](swbemlocator-security-.md)<br/> | Read-only<br/> | Used to read or change the security settings.<br/> |



 

## Remarks

At the top of the WMI scripting library object model is the SWbemLocator object. SWbemLocator is used to establish an authenticated connection to a WMI namespace, much as the VBScript GetObject function and the WMI moniker "winmgmts:" are used to establish an authenticated connection to WMI. However, SWbemLocator is designed to address two specific scripting scenarios that cannot be performed using GetObject and the WMI moniker. You must use SWbemLocator if you need to:

-   Provide user and password credentials to connect to WMI on a remote computer. The WMI moniker used with the GetObject function does not include a mechanism for specifying credentials. Most WMI activities (including all of those carried out on remote computers) require administrator rights. If you typically log on using a regular user account instead of an administrator account, you will not be able to perform most WMI tasks unless you run the script under alternate credentials.
-   Connect to WMI if you are running a WMI script from within a Web page. You cannot use the GetObject function when running scripts embedded within an HTML page because Internet Explorer disallows the use of GetObject for security reasons.

In addition, you might want to use SWbemLocator to connect to WMI if you find the WMI connection string used with GetObject confusing or difficult.

You use CreateObject rather than GetObject to create a reference to SWbemLocator. To create the reference, you must pass the CreateObject function the SWbemLocator programmatic identifier (ProgID) "WbemScripting.SWbemLocator", as shown on line 2 in the following script sample. After you obtain a reference to an SWbemLocator object, you call the ConnectServer method to connect to WMI and obtain a reference to an SWbemServices object. This is demonstrated on line 3 of the following script.


```VB
strComputer = "."
Set objSWbemLocator = CreateObject("WbemScripting.SWbemLocator")
Set objSWbemServices = objSWbemLocator.ConnectServer(strComputer, "root\cimv2")
Set colSWbemObjectSet = objSWbemServices.InstancesOf("Win32_Service")
For Each objSWbemObject In colSWbemObjectSet
    Wscript.Echo "Name: " & objSWbemObject.Name
Next
```



To run a script under alternate credentials, include the user name and password as additional parameters passed to ConnectServer. For example, this script runs under the credentials of a user named kenmyer, with the password homerj.


```VB
strComputer = "atl-dc-01"
Set objSWbemLocator = CreateObject("WbemScripting.SWbemLocator")
Set objSWbemServices = objSWbemLocator.ConnectServer _
    (strComputer, "root\cimv2", "kenmyer", "homerj")
Set colSWbemObjectSet = objSWbemServices.InstancesOf("Win32_Service")
For Each objSWbemObject In colSWbemObjectSet
    Wscript.Echo "Name: " & objSWbemObject.Name
Next
```



You can also use the Domain\\User Name format to specify a user name. For example:

`" fabrikam\kenmyer"`

## Examples

The following PowerShell example uses **SWbemLocator** to connect to a server.


```PowerShell
$NameSpace = 'root\ccm'
$ComputerName = 'sccm.company.com'
$WbemLocator = New-Object -ComObject "WbemScripting.SWbemLocator"
$WbemServices = $WbemLocator.ConnectServer($ComputerName, $Namespace)
$WbemClasses = $WbemServices.SubclassesOf()
$WbemClasses
```



## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>Wbemdisp.h</dt> </dl>   |
| Type library<br/>             | <dl> <dt>Wbemdisp.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wbemdisp.dll</dt> </dl> |
| CLSID<br/>                    | CLSID\_SWbemLocator<br/>                                                          |
| IID<br/>                      | IID\_ISWbemLocator<br/>                                                           |



## See also

<dl> <dt>

[Scripting API Objects](scripting-api-objects.md)
</dt> </dl>

 

 




