---
title: Win32\_Product class
description: Epresents products as they are installed by Windows Installer. A product generally correlates to one installation package.
ms.assetid: b2c60a2b-6aaf-43e3-9cb8-9cb49027a8bb
keywords:
- Win32_Product class
- Win32_Product class, described
topic_type:
- apiref
api_name:
- Win32_Product
- Win32_Product.AssignmentType
- Win32_Product.Caption
- Win32_Product.Description
- Win32_Product.IdentifyingNumber
- Win32_Product.InstallDate
- Win32_Product.InstallDate2
- Win32_Product.InstallLocation
- Win32_Product.InstallState
- Win32_Product.HelpLink
- Win32_Product.HelpTelephone
- Win32_Product.InstallSource
- Win32_Product.Language
- Win32_Product.LocalPackage
- Win32_Product.Name
- Win32_Product.PackageCache
- Win32_Product.PackageCode
- Win32_Product.PackageName
- Win32_Product.ProductID
- Win32_Product.RegOwner
- Win32_Product.RegCompany
- Win32_Product.SKUNumber
- Win32_Product.Transforms
- Win32_Product.URLInfoAbout
- Win32_Product.URLUpdateInfo
- Win32_Product.Vendor
- Win32_Product.WordCount
- Win32_Product.Version
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

# Win32\_Product class

The **Win32\_Product** [WMI class](https://msdn.microsoft.com/library/aa393244) represents products as they are installed by Windows Installer. A product generally correlates to one installation package.

> [!Note]  
> For more information about support or requirements for installation of a specific operating system, see [Operating System Availability of WMI Components](https://msdn.microsoft.com/library/aa392726#windows-installer-provider).

 

The following syntax is simplified from Managed Object Format (MOF) code and includes all inherited properties. Properties and methods are in alphabetic order, not MOF order.

## Syntax

``` syntax
[Provider("MSIProv"), Dynamic]
class Win32_Product : CIM_Product
{
  uint16   AssignmentType;
  string   Caption;
  string   Description;
  string   IdentifyingNumber;
  string   InstallDate;
  datetime InstallDate2;
  string   InstallLocation;
  sint16   InstallState;
  string   HelpLink;
  string   HelpTelephone;
  string   InstallSource;
  string   Language;
  string   LocalPackage;
  string   Name;
  string   PackageCache;
  string   PackageCode;
  string   PackageName;
  string   ProductID;
  string   RegOwner;
  string   RegCompany;
  string   SKUNumber;
  string   Transforms;
  string   URLInfoAbout;
  string   URLUpdateInfo;
  string   Vendor;
  uint32   WordCount;
  string   Version;
};
```

## Members

The **Win32\_Product** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Win32\_Product** class has these methods.



| Method                                                       | Description                                                                                                                                                                                                   |
|:-------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Admin**](admin-method-in-class-win32-product.md)         | Performs an administrative install of an associated **Win32\_Product** instance using the installation package provided through *PackageLocation*, and any command line options that are supplied.<br/> |
| [**Advertise**](advertise-method-in-class-win32-product.md) | Advertises an associated **Win32\_Product** instance using the installation package provided through *PackageLocation* and any command line options that are supplied.<br/>                             |
| [**Configure**](configure-method-in-class-win32-product.md) | Configures the associated instance of **Win32\_Product** to the specified install state and level.<br/>                                                                                                 |
| [**Install**](install-method-in-class-win32-product.md)     | Installs an associated **Win32\_Product** instance using the installation package provided through *PackageLocation* and any command line options that are supplied.<br/>                               |
| [**Reinstall**](reinstall-method-in-class-win32-product.md) | Reinstalls the associated instance of **Win32\_Product** using the specified reinstallation mode.<br/>                                                                                                  |
| [**Uninstall**](uninstall-method-in-class-win32-product.md) | Uninstalls the associated instance of **Win32\_Product**.<br/>                                                                                                                                          |
| [**Upgrade**](upgrade-method-in-class-win32-product.md)     | Upgrades the associated **Win32\_Product** instance using the upgrade package provided through *PackageLocation* and any command line options that are supplied.<br/>                                   |



 

### Properties

The **Win32\_Product** class has these properties.

<dl> <dt>

**AssignmentType**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Assignment type of the product.

**Windows Server 2003:** This property is not available.

Possible values are



| Value                                                                        | Meaning                                         |
|------------------------------------------------------------------------------|-------------------------------------------------|
| <dl> <dt>0</dt> </dl> | The product is assigned by user.<br/>     |
| <dl> <dt>1</dt> </dl> | The product is assigned by computer.<br/> |



 

</dd> <dt>

**Caption**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Short textual description for the product a one-line string.

</dd> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Description of the product.

</dd> <dt>

**HelpLink**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The support link for the product.

**Windows Server 2003:** This property is not available.

</dd> <dt>

**HelpTelephone**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The support telephone for the product.

**Windows Server 2003:** This property is not available.

</dd> <dt>

**IdentifyingNumber**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Product identification such as a serial number on software, or a die number on a hardware chip.

</dd> <dt>

**InstallDate**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

This property is no longer supported for **Win32\_Product**. Instead, use the **InstallDate2** property, which is in the WMI [CIM\_DATETIME](https://msdn.microsoft.com/library/aa387237) format.

</dd> <dt>

**InstallDate2**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Date that this product was installed on the system. This property does not require a value to indicate that the object is installed. For more information about WMI dates and times, see [Date and Time Format](https://msdn.microsoft.com/library/aa389802).

</dd> <dt>

**InstallLocation**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Location of the installed product.

</dd> <dt>

**InstallSource**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The installation source directory of the product.

**Windows Server 2003:** This property is not available.

</dd> <dt>

**InstallState**
</dt> <dd> <dl> <dt>

Data type: **sint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Installed state of the product.



| Value                                                                                                  | Meaning                      |
|--------------------------------------------------------------------------------------------------------|------------------------------|
| <span id="-6"></span><dl> <dt>**-6**</dt> </dl> | Bad Configuration<br/> |
| <span id="-2"></span><dl> <dt>**-2**</dt> </dl> | Invalid Argument<br/>  |
| <span id="-1"></span><dl> <dt>**-1**</dt> </dl> | Unknown Package<br/>   |
| <span id="1"></span><dl> <dt>**1**</dt> </dl>   | Advertised<br/>        |
| <span id="2"></span><dl> <dt>**2**</dt> </dl>   | Absent<br/>            |
| <span id="5"></span><dl> <dt>**5**</dt> </dl>   | Installed<br/>         |



 

</dd> <dt>

**Language**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The language of the product.

**Windows Server 2003:** This property is not available.

</dd> <dt>

**LocalPackage**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The location of the locally cached package for this product.

**Windows Server 2003:** This property is not available.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, [**Dynamic**](https://msdn.microsoft.com/library/aa393651)
</dt> </dl>

Commonly used product name.

</dd> <dt>

**PackageCache**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Location of the locally cached package for this product.

</dd> <dt>

**PackageCode**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The identifier for the package from which this product was installed.

**Windows Server 2003:** This property is not available.

</dd> <dt>

**PackageName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The original package name for the product.

**Windows Server 2003:** This property is not available.

</dd> <dt>

**ProductID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The product ID.

**Windows Server 2003:** This property is not available.

</dd> <dt>

**RegCompany**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The company registered to use the product.

**Windows Server 2003:** This property is not available.

</dd> <dt>

**RegOwner**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The owner registered to use the product.

**Windows Server 2003:** This property is not available.

</dd> <dt>

**SKUNumber**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Product SKU (stock-keeping unit) information.

</dd> <dt>

**Transforms**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The transforms of the product.

**Windows Server 2003:** This property is not available.

</dd> <dt>

**URLInfoAbout**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The URL information for the product.

**Windows Server 2003:** This property is not available.

</dd> <dt>

**URLUpdateInfo**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The URL update information the product.

**Windows Server 2003:** This property is not available.

</dd> <dt>

**Vendor**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Name of the product supplier. Corresponds to the **Vendor** property in the product object in the Desktop Management Task Force (DMTF) Solution Exchange Standard.

</dd> <dt>

**Version**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Product version information. Corresponds to the **Version** property in the product object in the DMTF Solution Exchange Standard.

</dd> <dt>

**WordCount**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Number of words in the summary information for the product.

**Windows Server 2003:** This property is not available.

</dd> </dl>

## Remarks

The **Win32\_Product** class is derived from [**CIM\_Product**](https://msdn.microsoft.com/library/aa387980).

Knowing the software packages that have been installed on a computer is useful for many reasons. Among other things, this knowledge helps you:

-   Gain insight into what the computer is used for. A computer that does not have a word processor installed is probably not used for writing memos or other documents.
-   Ensuring that only licensed software, and only approved software, is in use in your organization. If your organization has decided to standardize on Microsoft Excel, it is very useful, for both support and legal reasons, to know whether anyone has installed a different spreadsheet program on a computer.
-   Tracking the progress of software deployment projects (for example, the number of people who have installed this new application and the number of people who have not).
-   Planning for future software needs.

These activities cannot be carried out using Group Policy because the Software Installation and Maintenance component does not provide information on the software installed on a computer; it only makes that software available for installation. For example, although the Software Installation and Maintenance component can publish a software package, it provides no way to track which users install that package. This makes it difficult to analyze actual software use or to make projections for future software needs.

The **Win32\_Product** class enables you to enumerate the software installed on a computer, provided the software was installed by using the Windows Installer.

> \[!Warning\]  
> **Win32\_Product** is not query optimized. Queries such as "select \* from Win32\_Product where (name like 'Sniffer%')" require WMI to use the MSI provider to enumerate all of the installed products and then parse the full list sequentially to handle the  where  clause. This process also initiates a consistency check of packages installed, verifying and repairing the install. With an account with only user privileges, as the user account may not have access to quite a few locations, may cause delay in application launch and an event 11708 stating an installation failure. For more information, see [KB Article 794524](http://support.microsoft.com/kb/974524).

 

## Examples

The [Powershell Remote PC Info Script](http://gallery.technet.microsoft.com/2a8a008c-ee30-4b50-a81a-1b7545ef3436) PowerShell code sample uses a number of hardware and software classes, including Win32\_Product, to find various information about a remote PC using WMI and the remote registry.

The [List Information About the Binary Files Used by an Application](http://gallery.technet.microsoft.com/bd9f6682-050e-4ff1-97d5-1d5105610c92) VBScript returns the name and product code of binary information (such as bitmaps, icons, executable files, and so on) used by a Windows Installer application.

The following code example shows how to generate an inventory list of installed software on a local computer. The script generates a text file with a list of the software and versions installed on a local computer.


```VB
strComputer = "."

Set objWMIService = GetObject("winmgmts:" & _
    "{impersonationLevel=impersonate}!\\" & _
    strComputer & _
    "\root\cimv2")

Set colSoftware = objWMIService.ExecQuery _
    ("SELECT * FROM Win32_Product")   

If colSoftware.Count > 0 Then

    Set objFSO = CreateObject("Scripting.FileSystemObject")
    Set objTextFile = objFSO.CreateTextFile( _
        "c:\SoftwareList.txt", True)

    For Each objSoftware in colSoftware
        objTextFile.WriteLine objSoftware.Caption & vbtab & _
        objSoftware.Version
    Next

    objTextFile.Close

Else
    WScript.Echo "Cannot retrieve software from this computer."

End If
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

[WMI Tasks: Computer Software](https://msdn.microsoft.com/library/aa394588)
</dt> <dt>

[**Win32\_SoftwareFeature**](win32-softwarefeature.md)
</dt> </dl>

 

 





