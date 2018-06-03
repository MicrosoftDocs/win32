---
title: GetVirtualHardDiskInfo method of the Msvm\_ImageManagementService class
description: Retrieves information about the virtual hard disk files.
ms.assetid: 0c45468c-e8ce-40ee-bef8-69b33760783e
keywords:
- GetVirtualHardDiskInfo method Hyper-V
- GetVirtualHardDiskInfo method Hyper-V , Msvm_ImageManagementService class
- Msvm_ImageManagementService class Hyper-V , GetVirtualHardDiskInfo method
topic_type:
- apiref
api_name:
- Msvm_ImageManagementService.GetVirtualHardDiskInfo
api_location:
- Root\Virtualization
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetVirtualHardDiskInfo method of the Msvm\_ImageManagementService class

Retrieves information about the virtual hard disk files.

## Syntax


```mof
uint32 GetVirtualHardDiskInfo(
  [in]  string              Path,
  [out] string              Info,
  [out] CIM_ConcreteJob REF Job
);
```



## Parameters

<dl> <dt>

*Path* \[in\]
</dt> <dd>

Type: **string**

A fully qualified path that specifies the location of the disk image file.

</dd> <dt>

*Info* \[out\]
</dt> <dd>

Type: **string**

If successful, this object contains the information for the requested virtual hard disk. This is an embedded instance of [**Msvm\_VirtualHardDiskInfo**](msvm-virtualharddiskinfo.md).

</dd> <dt>

*Job* \[out\]
</dt> <dd>

Type: **[**CIM\_ConcreteJob**](https://msdn.microsoft.com/library/cc136808)**

A reference to the job (can be **null** if the task is completed).

</dd> </dl>

## Return value

Type: **uint32**

This method can return one of the following values.

<dl> <dt>

**Completed with No Error** (0)
</dt> <dt>

**Method Parameters Checked - Job Started** (4096)
</dt> <dt>

**Failed** (32768)
</dt> <dt>

**Access Denied** (32769)
</dt> <dt>

**Not Supported** (32770)
</dt> <dt>

**Status is unknown** (32771)
</dt> <dt>

**Timeout** (32772)
</dt> <dt>

**Invalid parameter** (32773)
</dt> <dt>

**System is in used** (32774)
</dt> <dt>

**Invalid state for this operation** (32775)
</dt> <dt>

**Incorrect data type** (32776)
</dt> <dt>

**System is not available** (32777)
</dt> <dt>

**Out of memory** (32778)
</dt> <dt>

**File not found** (32779)
</dt> </dl>

## Remarks

Access to the [**Msvm\_ImageManagementService**](msvm-imagemanagementservice.md) class might be restricted by UAC Filtering. For more information, see [User Account Control and WMI](https://msdn.microsoft.com/library/aa826699).

## Examples

The following C# example retrieves information about the virtual hard disk files. The referenced utilities can be found in [Common Utilities for the Virtualization Samples](common-utilities-for-the-virtualization-samples.md).


```CSharp
using System;
using System.Xml;
using System.Management;

namespace HyperVSamples
{

    class GetVirtualHardDiskInfoClass
    {
        static void DisplayPropertyValue(string propertyName, XmlDocument doc)
        {
            string xpath = string.Format(@"//PROPERTY[@NAME = '{0}']/VALUE/child::text()", propertyName);
            XmlNode node = doc.SelectSingleNode(xpath);
            if (node == null)
            {
                if (propertyName != "ParentPath")
                {
                    throw new Exception("GetVirtualHardDiskInfo returned an invalid CIM_XML instance");
                }
            }
            else
            {
                Console.WriteLine("{0}:{1}", propertyName, node.Value);
            }
        }

        static void DisplayVHDProperties(string diskInfo)
        {
            XmlDocument doc = new XmlDocument();
            doc.LoadXml(diskInfo);

            //fileSize
            DisplayPropertyValue("FileSize", doc);

            //MaxInternalSize
            DisplayPropertyValue("MaxInternalSize", doc);

            //disk type
            DisplayPropertyValue("Type", doc);

            //InUse should be false
            DisplayPropertyValue("InUse", doc);

            //InSavedState should be FALSE
            DisplayPropertyValue("InSavedState", doc);

            //ParentPath
            DisplayPropertyValue("ParentPath", doc);
            
        }

        static void GetVirtualHardDiskInfo(string path)
        {
            ManagementScope scope = new ManagementScope(@"root\virtualization", null);
            ManagementObject imageService = Utility.GetServiceObject(scope, "Msvm_ImageManagementService");
            ManagementBaseObject inParams = imageService.GetMethodParameters("GetVirtualHardDiskInfo");
            inParams["Path"] = path;

            ManagementBaseObject outParams = imageService.InvokeMethod("GetVirtualHardDiskInfo", inParams, null);

            if (outParams != null)
            {
                if ((UInt32)outParams["ReturnValue"] == ReturnCode.Completed)
                {
                    //no error
                    string diskInfo = (string)outParams["Info"];
                    DisplayVHDProperties(diskInfo);
                }
                else
                {   // error occurred
                    Console.WriteLine("GetVirtualHardDiskInfo failed. ReturnValue:{0}", (UInt32)outParams["ReturnValue"]);
                }
            }
            else
            {
                Console.WriteLine("WMI failed");
            }

            inParams.Dispose();
            outParams.Dispose();
            imageService.Dispose();
        }

        static void Main(string[] args)
        {
            if (args != null &amp;&amp; args.Length != 1)
            {
                Console.WriteLine("Usage: GetVirtualHardDiskInfo path");
                return;
            }
            GetVirtualHardDiskInfo(args[0]);
        }
    }
}

```



The following VBScript example retrieves information about the virtual hard disk files.


```VB
option explicit

dim objWMIService
dim managementService
dim fileSystem

const wmiSuccessful = 0

Main()

'-----------------------------------------------------------------
' Main
'-----------------------------------------------------------------
Sub Main()

    dim path, objArgs, computer
    
    set fileSystem = Wscript.CreateObject("Scripting.FileSystemObject")

    computer = "."
    set objWMIService = GetObject("winmgmts:\\" & computer & "\root\virtualization")
    set managementService = objWMIService.ExecQuery("Select * from Msvm_ImageManagementService").ItemIndex(0)

    set objArgs = WScript.Arguments
    if WScript.Arguments.Count = 1 then
       path = objArgs.Unnamed.Item(0)
    else
       WScript.Echo "usage: cscript GetVirtualHardDiskInfo.vbs Path"
       WScript.Quit(1)
    end if

    if GetVirtualHardDiskInfo(path) then
        WriteLog "Done"
        WScript.Quit(0)
    else
        WriteLog "GetVirtualHardDiskInfo failed"
        WScript.Quit(1)
    end if

End Sub

'-----------------------------------------------------------------
' Query a filed value from CIM_XML and display it
'-----------------------------------------------------------------
Sub DisplayPropertyValue(propertyName, doc)
   dim xpath, node
   
   xpath = Format1("//PROPERTY[@NAME = '{0}']/VALUE/child:text()", propertyName)
   set node = doc.selectSingleNode(xpath) 
   
   if node Is Nothing then
       if propertyName <> "ParentPath" then
           WriteLog "GetVirtualHardDiskInfo returned an invalid CIM_XML instance"
       end if
   else
       WriteLog Format2("{0}:{1}", propertyName, node.Text)
   end if
End Sub


'-----------------------------------------------------------------
' Display the VHD properties
'-----------------------------------------------------------------
Sub DisplayVHDProperties(diskInfo)

    dim objXMLDoc 
    
    set objXMLDoc = CreateObject("Microsoft.XMLDOM") 
    objXMLDoc.async = False 
    objXMLDoc.loadXML(diskInfo) 
    
    'fileSize
    DisplayPropertyValue "FileSize", objXMLDoc

    'MaxInternalSize
    DisplayPropertyValue "MaxInternalSize", objXMLDoc

    'disk type
    DisplayPropertyValue "Type", objXMLDoc

    'InUse 
    DisplayPropertyValue "InUse", objXMLDoc

    'InSavedState 
    DisplayPropertyValue "InSavedState", objXMLDoc

    'ParentPath
    DisplayPropertyValue "ParentPath", objXMLDoc

End Sub

'-----------------------------------------------------------------
' Execute ExpandVirtualHardDisk
'-----------------------------------------------------------------
Function GetVirtualHardDiskInfo(path)
    
    WriteLog Format1("Sub GetVirtualHardDiskInfo({0})",  path)
    
    dim objInParam, objOutParams

    GetVirtualHardDiskInfo = false

    set objInParam = managementService.Methods_("GetVirtualHardDiskInfo").InParameters.SpawnInstance_()
    objInParam.Path = Path

    set objOutParams = managementService.ExecMethod_("GetVirtualHardDiskInfo", objInParam)

    if (objOutParams.ReturnValue = wmiSuccessful) then
        DisplayVHDProperties objOutParams.Info
        GetVirtualHardDiskInfo = true
    else
        WriteLog Format2("GetVirtualHardDiskInfo {0} failed with error {1}", Path, objOutParams.ReturnValue)
    end if

End Function


'-----------------------------------------------------------------
' Create the console log files.
'-----------------------------------------------------------------
Sub WriteLog(line)
    dim fileStream
    set fileStream = fileSystem.OpenTextFile(".\GetVirtualHardDiskInfo.log", 8, true)
    WScript.Echo line
    fileStream.WriteLine line
    fileStream.Close

End Sub

'------------------------------------------------------------------------------
' The string formatting functions to avoid string concatenation.
'------------------------------------------------------------------------------
Function Format2(myString, arg0, arg1)
    Format2 = Format1(myString, arg0)
    Format2 = Replace(Format2, "{1}", arg1)
End Function

'------------------------------------------------------------------------------
' The string formatting functions to avoid string concatenation.
'------------------------------------------------------------------------------
Function Format1(myString, arg0)
    Format1 = Replace(myString, "{0}", arg0)
End Function
```



## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012<br/>                                                                       |
| Namespace<br/>                | Root\\Virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



## See also

<dl> <dt>

[**GetVirtualHardDiskSettingData (V2)**](https://msdn.microsoft.com/library/windows/desktop/hh850064)
</dt> <dt>

[**CIM\_ConcreteJob**](https://msdn.microsoft.com/library/cc136808)
</dt> <dt>

[**Msvm\_ImageManagementService**](msvm-imagemanagementservice.md)
</dt> </dl>

 

 





