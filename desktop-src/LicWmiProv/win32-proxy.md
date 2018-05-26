---
Description: The Win32\_Proxy&\#8194;WMI class contains properties and methods to query and configure an Internet connection related to Windows Product Activation (WPA).
ms.assetid: 431fb980-6518-4b9b-8ca3-6e6d5471abf5
title: Win32\_Proxy class
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Win32\_Proxy class

The **Win32\_Proxy** [WMI class](https://msdn.microsoft.com/library/aa393244) contains properties and methods to query and configure an Internet connection related to Windows Product Activation (WPA).

The following syntax is simplified from MOF code and includes all of the inherited properties, but excludes methods. For reference information about methods, see the table of methods later in this topic.

## Syntax

``` syntax
class Win32_Proxy : CIM_Setting
{
  string Caption;
  string Description;
  string ProxyPortNumber;
  string ProxyServer;
  string ServerName;
  string SettingID;
};
```

## Members

The **Win32\_Proxy** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Win32\_Proxy** class has these methods.



| Method                                                                 | Description                                                                                            |
|:-----------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------|
| [**SetProxySetting**](setproxysetting-method-in-class-win32-proxy.md) | Creates a persistent Internet connection for WPA using a specified address and port number.<br/> |



 

### Properties

The **Win32\_Proxy** class has these properties.

<dl> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (64)
</dt> </dl>

Short textual description of the [**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461) object. This property is inherited from **CIM\_Setting**.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Textual description of the [**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461) object. This property is inherited from **CIM\_Setting**.

</dd> <dt>

**ProxyPortNumber**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (1024)
</dt> </dl>

Port number configured on the computer for access to the proxy server specified by the **ProxyServer** property.

</dd> <dt>

**ProxyServer**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (1024)
</dt> </dl>

Name of the proxy server configured for the user.

</dd> <dt>

**ServerName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (1024)
</dt> </dl>

Name of the computer whose proxy settings are to be accessed.

</dd> <dt>

**SettingID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](https://msdn.microsoft.com/library/aa393650) (256)
</dt> </dl>

Identifier by which the [**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461) object is known. This property is inherited from **CIM\_Setting**.

</dd> </dl>

## Remarks

The **Win32\_Proxy** class is derived from [**CIM\_Setting**](https://msdn.microsoft.com/library/aa388461).

> [!Note]  
> Windows Product Activation is not available on the Itanium-based versions of the Windows operating system.

 

## Examples

The following VBScript code sample displays the property information from a **Win32\_Proxy** object.


```VB
On Error Resume Next

Const wbemFlagReturnImmediately = &amp;h10
Const wbemFlagForwardOnly = &amp;h20

arrComputers = Array("\localhost")
For Each strComputer In arrComputers
   WScript.Echo
   WScript.Echo "=========================================="
   WScript.Echo "Computer: " & strComputer
   WScript.Echo "=========================================="

   Set objWMIService = GetObject("winmgmts:\\" & strComputer & "\root\CIMV2")
   Set colItems = objWMIService.ExecQuery("SELECT * FROM Win32_Proxy", "WQL", _
                                          wbemFlagReturnImmediately + wbemFlagForwardOnly)

   For Each objItem In colItems
      WScript.Echo "Caption: " & objItem.Caption
      WScript.Echo "Description: " & objItem.Description
      WScript.Echo "ProxyPortNumber: " & objItem.ProxyPortNumber
      WScript.Echo "ProxyServer: " & objItem.ProxyServer
      WScript.Echo "ServerName: " & objItem.ServerName
      WScript.Echo "SettingID: " & objItem.SettingID
      WScript.Echo
   Next
Next
```



## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                        |
| End of client support<br/>    | Windows XP<br/>                                                                 |
| End of server support<br/>    | Windows Server 2003 R2<br/>                                                     |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                |
| MOF<br/>                      | <dl> <dt>Licwmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Licwmi.dll</dt> </dl> |



## See also

<dl> <dt>

[Windows Product Activation Provider](windows-product-activation-provider.md)
</dt> <dt>

[**Win32\_WindowsProductActivation**](win32-windowsproductactivation.md)
</dt> <dt>

[**Win32\_ComputerSystemWindowsProductActivationSetting**](win32-computersystemwindowsproductactivationsetting.md)
</dt> </dl>

 

 




