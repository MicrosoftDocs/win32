---
description: Occasionally, you may want to update only part of an instance.
ms.assetid: c92bf8f9-9cac-4cf0-a45d-f60aee5a9ec2
ms.tgt_platform: multiple
title: Updating Part of an Instance
ms.topic: article
ms.date: 05/31/2018
---

# Updating Part of an Instance

Occasionally, you may want to update only part of an instance. For example, some instances have a large number of properties. If you had to update a large number of these instances, you may reduce system performance. Therefore, you can choose to update only part of the instance, and thus reduce the amount of information you must send and retrieve to and from WMI. However, WMI does not directly support partial-instance operations, nor do most providers. Therefore, if you write an application that uses partial-instance operations, be prepared for your calls to fail with either the **WBEM\_E\_PROVIDER\_NOT\_CAPABLE** or **WBEM\_E\_NOT\_SUPPORTED** error code in C++. In scripting languages the error codes are either **wbemErrProviderNotCapable** or **wbemErrNotSupported**.

In scripting, this operation is only necessary to aid performance when updating one or two writeable properties in a very large number of objects over an enterprise. Otherwise, the normal VBScript calls to [**SWbemObject.Put\_**](swbemobject-put-.md) or [**SWbemObject.PutAsync\_**](swbemobject-putasync-.md), while seeming to write the entire object, are actually only updating the properties which the provider has write-enabled.

The following procedure describes how to request a partial-instance update using PowerShell.

**To request a partial-instance update using PowerShell**

1.  Retrieve the path of the object you wish to update.

    You can describe the path either manually, or else query the object and then retrieve the **\_\_Path** property.

    ```PowerShell
    $myWMIDrivePath = (get-wmiObject Win32_LogicalDisk -filter "Name = 'C:'").__Path
    #or
    $myWmiDrivePath = \\myComputer\root\cimv2:Win32_LogicalDisk.DeviceID="C:"
    ```

    

2.  Set up a hash table listing the names of the properties to be updated, and use this hash table in a call to [Set-WmiInstance](/powershell/module/microsoft.powershell.management/set-wmiinstance?view=powershell-5.1&preserve-view=true).

    ```PowerShell
    $newDriveName = @{VolumeName = "OSDisk"}
    Set-WmiInstance -Path $myWMIDrivePath -Arguments $newDriveName
    ```

    

The following procedure describes how to request a partial-instance update using C#.

> [!Note]  
> **System.Management** was the original .NET namespace used to access WMI; however, the APIs in this namespace generally are slower and do not scale as well relative to their more modern **Microsoft.Management.Infrastructure** counterparts.

 

**To request a partial-instance update using C#**

1.  Create a new [ManagementObject](/dotnet/api/system.management.managementobject) object that represents the specific instance to update.

    ```PowerShell
    using System.Management;
    ...
    ManagementObject myDisk = new ManagementObject("Win32_LogicalDisk.DeviceID='C:'");
    ```

    

2.  Set the property value with a call to [ManagementObject.SetPropertyValue](/dotnet/api/system.management.managementbaseobject.setpropertyvalue#System_Management_ManagementBaseObject_SetPropertyValue_System_String_System_Object_).

    ```CSharp
    myDisk.SetPropertyValue("VolumeName", "OSDisk");
    ```

    

The following procedure describes how to request a partial-instance update using VBScript.

**To request a partial-instance update using VBScript**

1.  Create an [**SWbemNamedValueSet**](swbemnamedvalueset.md) context object.

    ```VB
    Set objwbemNamedValueSet = CreateObject ("WbemScripting.SWbemNamedValueSet")
    ```

    

2.  Add the Put extension values "\_\_PUT\_EXTENSIONS" and "\_\_PUT\_EXT\_CLIENT\_REQUEST" to the context object using the [**SWbemNamedValueSet.Add**](swbemnamedvalueset-add.md) method.

    ```VB
    objwbemNamedValueSet.Add "__PUT_EXTENSIONS", True
    objwbemNamedValueSet.Add "__PUT_EXT_CLIENT_REQUEST", True
    ```

    

3.  Set up an array listing the names of the properties to be updated and add this array to the [**SWbemNamedValueSet**](swbemnamedvalueset.md) context object with the Put extension value "\_\_PUT\_EXT\_PROPERTIES".

    ```VB
    arProperties = Array("propertyname1", "propertyname2") 
    objwbemNamedValueSet.Add "__PUT_EXT_PROPERTIES", arProperties
    ```

    

4.  Set the *iFlags* parameter of the [**SWbemObject.Put\_**](swbemobject-put-.md) call to **wbemChangeFlagUpdateOnly**. Without this flag the call will fail with an invalid context.

5.  Pass your flag and context object to the provider in the *objwbemNamedValueSet* parameter of either [**SWbemObject.Put\_**](swbemobject-put-.md) or [**SWbemObject.PutAsync\_**](swbemobject-putasync-.md).

    ```VB
    call objSystem.put_( wbemChangeFlagUpdateOnly, objwbemNamedValueSet)
    ```

    

The following procedure describes how to request a partial-instance update using C++.

**To request a partial-instance update using C++**

1.  Create an [**IWbemContext**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemcontext) object with a call to [**CoCreateInstance**](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance).

    A context object is an object that WMI uses to pass in more information to a WMI provider. In this case, you are using the [**IWbemContext**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemcontext) object to instruct the provider to accept partial-instance updates.

2.  Add the "\_\_PUT\_EXTENSIONS" and "\_\_PUT\_EXT\_CLIENT\_REQUEST" named values to the [**IWbemContext**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemcontext) object with a call to [**IWbemContext::SetValue**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemcontext-setvalue).

    The following table lists the meaning of "\_\_PUT\_EXTENSIONS" and "\_\_PUT\_EXT\_CLIENT\_REQUEST".

    

    | Named value                     | Description                                                                                                                                                                                                                                             |
    |---------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | "\_\_PUT\_EXTENSIONS"           | **VT\_BOOL** set to **VARIANT\_TRUE**. A value indicating that one or more of the other context values has been specified. This allows a quick check of the context object inside the provider to determine if partial-instance updates are being used. |
    | "\_\_PUT\_EXT\_CLIENT\_REQUEST" | **VT\_BOOL** set to **VARIANT\_TRUE**. Set by the client during the initial request. This value is used to prevent reentrancy errors.                                                                                                                   |

    

     

3.  Add the \_\_PUT\_EXT\_STRICT\_NULLS, \_\_PUT\_EXT\_PROPERTIES, or \_\_PUT\_EXT\_ATOMIC in any combination as needed to the [**IWbemContext**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemcontext) object with another call to [**IWbemContext::SetValue**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemcontext-setvalue).

    The following table lists the meaning of the named values.

    

    | Named value                   | Description                                                                                                                                                                                                                                   |
    |-------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | "\_\_PUT\_EXT\_STRICT\_NULLS" | **VT\_BOOL** set to **VARIANT\_TRUE**. Indicates that the client has intentionally set properties to **VT\_NULL** and expects the write operation to succeed. If the provider cannot set the values to **NULL**, an error should be reported. |
    | "\_\_PUT\_EXT\_PROPERTIES"    | [**SAFEARRAY**](/windows/win32/api/oaidl/ns-oaidl-safearray) of strings containing a list of property names to be updated. May be used alone or in combination with "\_\_PUT\_EXT\_PROPERTIES". The values are in the instance being written.                           |
    | "\_\_PUT\_EXT\_ATOMIC"        | **VT\_BOOL** set to **VARIANT\_TRUE**. Indicates that all updates must succeed simultaneously (atomic semantics) or the provider must revert back. There can be no partial success. May be used alone or in combination with other flags.     |

    

     

4.  Set the *iFlags* parameter to **WBEM\_FLAG\_UPDATE\_ONLY**. Without this flag the call will fail with an invalid context.
5.  Pass the [**IWbemContext**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemcontext) context object into any calls [**IWbemServices::PutInstance**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-putinstance) or [**IWbemServices::PutInstanceAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-putinstanceasync) in the *pCtx* parameter.

    Passing the [**IWbemContext**](/windows/desktop/api/WbemCli/nn-wbemcli-iwbemcontext) object instructs the provider to allow partial-instance updates. In a full-instance update, you would set *pCtx* to **NULL**.

    The provider may write any necessary properties if the context object present in the call does not contain "\_\_PUT\_EXTENSIONS". If "\_\_PUT\_EXTENSIONS" is present in the context object, WMI requires the provider to either obey the semantics of the operation exactly or else fail the call. For more information, see [Handling Access Denied Messages in a Provider](impersonating-a-client.md).

 

 
