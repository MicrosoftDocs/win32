---
title: Win32\_SoftwareFeature class
description: The Win32\_SoftwareFeature WMI class represents a distinct subset of a product that consists of one or more software elements.
ms.assetid: fc1248db-b2a1-42bc-a99f-f3c4970b38c8
keywords:
- Win32_SoftwareFeature class
- Win32_SoftwareFeature class, described
topic_type:
- apiref
api_name:
- Win32_SoftwareFeature
- Win32_SoftwareFeature.Accesses
- Win32_SoftwareFeature.Attributes
- Win32_SoftwareFeature.Caption
- Win32_SoftwareFeature.Description
- Win32_SoftwareFeature.IdentifyingNumber
- Win32_SoftwareFeature.InstallDate
- Win32_SoftwareFeature.InstallState
- Win32_SoftwareFeature.LastUse
- Win32_SoftwareFeature.Name
- Win32_SoftwareFeature.ProductName
- Win32_SoftwareFeature.Status
- Win32_SoftwareFeature.Vendor
- Win32_SoftwareFeature.Version
api_location:
- Msiprov.dll
api_type:
- DllExport
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Win32\_SoftwareFeature class

The **Win32\_SoftwareFeature** [WMI class](https://msdn.microsoft.com/library/aa393244) represents a distinct subset of a product that consists of one or more software elements. Each software element is defined in a [**Win32\_SoftwareElement**](win32-softwareelement.md) instance, and the association between a feature and its **Win32\_SoftwareFeature** instance is defined in the [**Win32\_SoftwareFeatureSoftwareElements**](win32-softwarefeaturesoftwareelements.md) association class.

> [!Note]  
> For more information about support or requirements for installation on a specific operating system, see [Operating System Availability of WMI Components](https://msdn.microsoft.com/library/aa392726#windows-installer-provider).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Provider("MSIProv"), Dynamic]
class Win32_SoftwareFeature : CIM_SoftwareFeature
{
  uint16   Accesses;
  uint16   Attributes;
  string   Caption;
  string   Description;
  string   IdentifyingNumber;
  datetime InstallDate;
  sint16   InstallState;
  datetime LastUse;
  string   Name;
  string   ProductName;
  string   Status;
  string   Vendor;
  string   Version;
};
```

## Members

The **Win32\_SoftwareFeature** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Win32\_SoftwareFeature** class has these methods.



| Method                                                               | Description                                                                                                             |
|:---------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------|
| [**Configure**](configure-method-in-class-win32-softwarefeature.md) | Configures the associated instance of **Win32\_SoftwareFeature** to the specified install state.<br/>             |
| [**Reinstall**](reinstall-method-in-class-win32-softwarefeature.md) | Reinstalls the associated instance of **Win32\_SoftwareFeature** by using the specified reinstallation mode.<br/> |



 

### Properties

The **Win32\_SoftwareFeature** class has these properties.

<dl> <dt>

**Accesses**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of times the software feature has been used.

</dd> <dt>

**Attributes**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Remote execution option.



| Value                                                                                                | Meaning                                                                                        |
|------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| <span id="0"></span><dl> <dt>**0**</dt> </dl> | ifrsFavorLocal - Install components locally, if possible.<br/>                           |
| <span id="1"></span><dl> <dt>**1**</dt> </dl> | ifrsFavorSource - Install components to run from the source CD/server, if possible.<br/> |
| <span id="2"></span><dl> <dt>**2**</dt> </dl> | ifrsFollowParent - Follow the remote execution option of the parent feature.<br/>        |



 

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Short textual description of the object a one-line string.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Textual description of the object.

</dd> <dt>

**IdentifyingNumber**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Product identification, such as a serial number on software or a die number on a hardware chip.

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Object was installed. This property does not need a value to indicate that the object is installed.

</dd> <dt>

**InstallState**
</dt> <dd> <dl> <dt>

Data type: **sint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Installed state of the software feature.



| Value                                                                                                  | Meaning                      |
|--------------------------------------------------------------------------------------------------------|------------------------------|
| <span id="-6"></span><dl> <dt>**-6**</dt> </dl> | Bad Configuration<br/> |
| <span id="-2"></span><dl> <dt>**-2**</dt> </dl> | Invalid Argument<br/>  |
| <span id="-1"></span><dl> <dt>**-1**</dt> </dl> | Unknown Package<br/>   |
| <span id="1"></span><dl> <dt>**1**</dt> </dl>   | Advertised<br/>        |
| <span id="2"></span><dl> <dt>**2**</dt> </dl>   | Absent<br/>            |
| <span id="3"></span><dl> <dt>**3**</dt> </dl>   | Local<br/>             |
| <span id="4"></span><dl> <dt>**4**</dt> </dl>   | Source<br/>            |



 

</dd> <dt>

**LastUse**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Software feature was last used.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Label by which the object is known to the world outside the data processing system. This label is a human-readable name that uniquely identifies the element in the context of the element's namespace.

</dd> <dt>

**ProductName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Commonly used product name.

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Current status of the object. Various operational and non-operational statuses can be defined. Operational statuses include: "OK", "Degraded", and "Pred Fail". An element, such as a SMART-enabled hard disk drive, can function properly but predict a failure in the near future. Nonoperational statuses include: "Error", "Starting", "Stopping", and "Service". The latter, "Service", can apply during mirror-resilvering of a disk, reload of a user permissions list, or other administrative work. Not all such work is online, yet the managed element is neither "OK" nor in one of the other states.

Values are the following:

<dl><span id="_OK_"></span><span id="_ok_"></span><dt>

**"OK"**
</dt><span id="_Error_"></span><span id="_error_"></span><span id="_ERROR_"></span><dt>

**"Error"**
</dt><span id="_Degraded_"></span><span id="_degraded_"></span><span id="_DEGRADED_"></span><dt>

**"Degraded"**
</dt><span id="_Unknown_"></span><span id="_unknown_"></span><span id="_UNKNOWN_"></span><dt>

**"Unknown"**
</dt><span id="_Pred_Fail_"></span><span id="_pred_fail_"></span><span id="_PRED_FAIL_"></span><dt>

**"Pred Fail"**
</dt><span id="_Starting_"></span><span id="_starting_"></span><span id="_STARTING_"></span><dt>

**"Starting"**
</dt><span id="_Stopping_"></span><span id="_stopping_"></span><span id="_STOPPING_"></span><dt>

**"Stopping"**
</dt><span id="_Service_"></span><span id="_service_"></span><span id="_SERVICE_"></span><dt>

**"Service"**
</dt><span id="_Stressed_"></span><span id="_stressed_"></span><span id="_STRESSED_"></span><dt>

**"Stressed"**
</dt><span id="_NonRecover_"></span><span id="_nonrecover_"></span><span id="_NONRECOVER_"></span><dt>

**"NonRecover"**
</dt><span id="_No_Contact_"></span><span id="_no_contact_"></span><span id="_NO_CONTACT_"></span><dt>

**"No Contact"**
</dt><span id="_Lost_Comm_"></span><span id="_lost_comm_"></span><span id="_LOST_COMM_"></span><dt>

**"Lost Comm"**
</dt> </dl>

</dd> <dt>

**Vendor**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the product supplier. Corresponds to the **Vendor** property in the product object in the Distributed Management Task Force (DMTF) Solution Exchange Standard.

</dd> <dt>

**Version**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Product version information. Corresponds to the **Version** property in the product object in the DMTF Solution Exchange Standard.

</dd> </dl>

## Remarks

Because much of the software developed today allows the user to choose which features to install, enumerating only the software packages might not provide a complete picture of the software installed on that computer. To obtain more detailed information about the software installed on a computer, you might need to enumerate the installed features of each software package, including such things as a dictionary, clip art, and design templates. You can retrieve a list of software features by using the **Win32\_SoftwareFeature** class.

Any component can be shared between two or more **Win32\_SoftwareFeature** instances. If two or more features reference the same component, that component is selected for installation if any of these features are selected.

The **Win32\_SoftwareFeature** class is derived from [**CIM\_SoftwareFeature**](https://msdn.microsoft.com/library/aa388473).

## Examples

The following VBScript code sample enumerates the software features installed on a computer.


```VB
strComputer = "."
Set objWMIService = GetObject("winmgmts:{impersonationLevel=impersonate}!\\" & strComputer & "\root\cimv2")
Set colFeatures = objWMIService.ExecQuery("SELECT * FROM Win32_SoftwareFeature")
For each objFeature in colFeatures
 Wscript.Echo "Accesses: " & objFeature.Accesses
 Wscript.Echo "Attributes: " & objFeature.Attributes
 Wscript.Echo "Caption: " & objFeature.Caption
 Wscript.Echo "Description: " & objFeature.Description
 Wscript.Echo "Identifying Number: " & objFeature.IdentifyingNumber
 Wscript.Echo "Install Date: " & objFeature.InstallDate
 Wscript.Echo "Install State: " & objFeature.InstallState
 Wscript.Echo "Last Use: " & objFeature.LastUse
 Wscript.Echo "Name: " & objFeature.Name
 Wscript.Echo "Product Name: " & objFeature.ProductName
 Wscript.Echo "Vendor: " & objFeature.Vendor
 Wscript.Echo "Version: " & objFeature.Version
Next
```



## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                         |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                 |
| MOF<br/>                      | <dl> <dt>Msi.mof</dt> </dl>     |
| DLL<br/>                      | <dl> <dt>Msiprov.dll</dt> </dl> |



## See also

<dl> <dt>

[Installed Applications Classes](https://msdn.microsoft.com/library/aa390887)
</dt> <dt>

[**Win32\_Product**](win32-product.md)
</dt> </dl>

 

 





