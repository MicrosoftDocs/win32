---
description: The following C# and Visual Basic Scripting Edition (VBScript) samples retrieve the DNS name of the virtual machine.
ms.assetid: 1E1F7E6F-5CF6-475F-8351-6A5F56B4FC8E
title: Getting the virtual machine DNS name
ms.topic: article
ms.date: 05/31/2018
---

# Getting the virtual machine DNS name

The following C# and Visual Basic Scripting Edition (VBScript) samples retrieve the DNS name of the virtual machine.

To run this sample code, you must install the client integration services and the client operating system must be running.


```CSharp
using System;
using System.IO;
using System.Xml.XPath;
using System.Management;


// exchangeDataItem xml document sample instance
//
//<INSTANCE CLASSNAME="Msvm_KvpExchangeDataItem">
//      <PROPERTY NAME="Caption" PROPAGATED="true" TYPE="string"></PROPERTY>
//      <PROPERTY NAME="Data" TYPE="string">
//         <VALUE>AUTOBVT-4OVYXAB</VALUE>
//      </PROPERTY>
//      <PROPERTY NAME="Description" PROPAGATED="true" TYPE="string"></PROPERTY>
//      <PROPERTY NAME="ElementName" PROPAGATED="true" TYPE="string"></PROPERTY>
//      <PROPERTY NAME="Name" TYPE="string">
//         <VALUE>FullyQualifiedDomainName</VALUE>
//      </PROPERTY>
//      <PROPERTY NAME="Source" TYPE="uint16">
//          <VALUE>2</VALUE>
//      </PROPERTY>
//</INSTANCE>        



namespace HyperVSamples
{
    class GetVirtualMachineDNSName
    {
        static bool VMRunning(ManagementObject vm)
        {
            const int Enabled = 2;

            bool running = false;

            foreach (UInt16 operationStatus in (UInt16[])vm["OperationalStatus"])
            {
                if (operationStatus == Enabled)
                {
                    running = true;
                    break;
                }
            }

            return running;
        }

        static void GetVirtualSystemDNS(string vmName)
        {
            ManagementScope scope = new ManagementScope(@"root\virtualization\v2", null);

            string query = String.Format("select * from Msvm_ComputerSystem where ElementName = '{0}'", vmName);

            ManagementObjectSearcher searcher = new ManagementObjectSearcher(scope, new ObjectQuery(query));

            ManagementObjectCollection vms = searcher.Get();

            foreach (ManagementObject vm in vms)
            {
                if (VMRunning(vm))
                {
                    ManagementObjectCollection kvpExchangeComponents = vm.GetRelated("Msvm_KvpExchangeComponent");
                    if (kvpExchangeComponents.Count != 1)
                    {
                        throw new Exception(String.Format("{0} instance of Msvm_KvpExchangeComponent was found", kvpExchangeComponents.Count));
                    }

                    foreach (ManagementObject kvpExchangeComponent in kvpExchangeComponents)
                    {
                        foreach (string exchangeDataItem in (string[])kvpExchangeComponent["GuestIntrinsicExchangeItems"])
                        {
                            XPathDocument xpathDoc = new XPathDocument(new StringReader(exchangeDataItem));
                            XPathNavigator navigator = xpathDoc.CreateNavigator();
                            navigator = navigator.SelectSingleNode("/INSTANCE/PROPERTY[@NAME='Name']/VALUE[child::text() = 'FullyQualifiedDomainName']");
                            if (navigator != null)
                            {
                                navigator = navigator.SelectSingleNode("/INSTANCE/PROPERTY[@NAME='Data']/VALUE/child::text()");
                                Console.WriteLine("Virtual machine {0} DNS name is: {1}", vmName, navigator.Value);
                                break;
                            }
                        }
                    }
                }
                else
                {
                    Console.WriteLine("Unable to retrieve virtual machine DNS name. VM {0} is not in running state", vmName);
                }
            }
        }

        static void Main(string[] args)
        {
            if (args != null && args.Length != 1)
            {
                Console.WriteLine("Usage: GetVirtualMachineDNSName vmName");
                return;
            }
            GetVirtualSystemDNS(args[0]);
        }
    }
}
```


```VB

option explicit 

dim objWMIService
dim fileSystem

const Enabled = 2


Main()

'-----------------------------------------------------------------
' Main routine
'-----------------------------------------------------------------
Sub Main()

    dim computer, objArgs, computerSystem, vmName
    
    set fileSystem = Wscript.CreateObject("Scripting.FileSystemObject")

    computer = "."
    set objWMIService = GetObject("winmgmts:\\" & computer & "\root\virtualization\v2")

    set objArgs = WScript.Arguments
    if WScript.Arguments.Count = 1 then
       vmName= objArgs.Unnamed.Item(0)
    else
       WScript.Echo "usage: cscript GetVirtualMachineDNSName.vbs vmName"
       WScript.Quit
    end if
    
    if GetVirtualSystemDNS(vmName) then
        WriteLog "Done"
        WScript.Quit(0)
    else
        WriteLog "GetVirtualMachineDNSName failed"
        WScript.Quit(1)
    end if

End Sub

'-----------------------------------------------------------------
' Check if virtual machine is running
'-----------------------------------------------------------------
Function VMRunning(computerSystem)
    dim operationStatus

    VMRunning = false
    
    for each operationStatus in computerSystem.OperationalStatus
        if operationStatus = Enabled then
            VMRunning = true
            exit function
        end if
    next

End Function

'-----------------------------------------------------------------
' GetVirtualSystemDNS
'
' exchangeDataItem xml document sample instance
'
' <INSTANCE CLASSNAME="Msvm_KvpExchangeDataItem">
'      <PROPERTY NAME="Caption" PROPAGATED="true" TYPE="string"></PROPERTY>
'      <PROPERTY NAME="Data" TYPE="string">
'         <VALUE>AUTOBVT-4OVYXAB</VALUE>
'      </PROPERTY>
'      <PROPERTY NAME="Description" PROPAGATED="true" TYPE="string"></PROPERTY>
'      <PROPERTY NAME="ElementName" PROPAGATED="true" TYPE="string"></PROPERTY>
'      <PROPERTY NAME="Name" TYPE="string">
'         <VALUE>FullyQualifiedDomainName</VALUE>
'      </PROPERTY>
'      <PROPERTY NAME="Source" TYPE="uint16">
'          <VALUE>2</VALUE>
'      </PROPERTY>
' </INSTANCE>           
'-----------------------------------------------------------------
Function GetVirtualSystemDNS(vmName)
    dim objXMLDoc, query , kvpExchangeComponents, kvpExchangeComponent, vm, vms
    dim exchangeDataItem, xpath, node
    GetVirtualSystemDNS = false
    set objXMLDoc = CreateObject("Microsoft.XMLDOM") 
    objXMLDoc.async = False 

    query = Format1("select * from Msvm_ComputerSystem where ElementName = '{0}'", vmName)
    set vms = objWMIService.ExecQuery(query)
    for each vm in vms
        if VMRunning(vm) then
            query = Format1("ASSOCIATORS OF {{0}} WHERE resultClass = Msvm_KvpExchangeComponent", vm.Path_.Path)
            set kvpExchangeComponents = objWMIService.ExecQuery(query)
            if kvpExchangeComponents.Count <> 1 then
                WriteLog Format1("{0} instance of Msvm_KvpExchangeComponent was found", kvpExchangeComponents.Count)
                WScript.Quit(1)
            end if
            
            set kvpExchangeComponent = kvpExchangeComponents.ItemIndex(0)
            for each exchangeDataItem in kvpExchangeComponent.GuestIntrinsicExchangeItems
                objXMLDoc.loadXML(exchangeDataItem) 
                xpath = "/INSTANCE/PROPERTY[@NAME='Name']/VALUE[child:text() = 'FullyQualifiedDomainName']"
                set node = objXMLDoc.selectSingleNode(xpath) 
                if Not (node Is Nothing) then
                    xpath = "/INSTANCE/PROPERTY[@NAME='Data']/VALUE/child:text()"
                    set node = objXMLDoc.selectSingleNode(xpath) 
                    WriteLog Format2("Virtual machine {0} DNS name is: {1}", vmName, node.Text)
                end if
            next
        else
            WriteLog Format1("Unable to retrieve virtual machine DNS name. VM {0} is not in running state", vmName)
            WScript.Quit(1)
        end if
    next 
    
    GetVirtualSystemDNS = true

End Function

'-----------------------------------------------------------------
' Create the console log files.
'-----------------------------------------------------------------
Sub WriteLog(line)
    dim fileStream
    set fileStream = fileSystem.OpenTextFile(".\GetVirtualSystemDNSName.log", 8, true)
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

## Related topics

[Common utilities for the virtualization samples (V2)](common-utilities-for-the-virtualization-samples-v2.md)

[**Msvm\_ComputerSystem**](msvm-computersystem.md)

[**Msvm\_KvpExchangeComponent**](msvm-kvpexchangecomponent.md)
