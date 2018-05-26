---
title: How to get associated objects
description: This topic shows how to get objects that are associated with a given object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 536AB0AC-32A3-437B-A4EE-1E3C5D9B3558
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# How to get associated objects

This topic shows how to get objects that are associated with a given object.

> \[!Important\]  
> The object being used is the example Win32\_Process object defined in the [CIM Class Overview](cim-class-overview.md) topic.

 

In this example, we want to get a list of processes that are using a given file. In CIM, the relationship between Process and File is represented through an association class called CIM\_ProcessExecutable.

``` syntax
Get-Win32Process –ProcessFile <CimInstance#CIM_DataFile>
```

Here we want to find the list of processes for a given logon session (instance of Win32\_LogonSession class). The Name and Id parameters have been removed to keep the example simple.


```mof
<PowerShellMetadata xmlns="http://schemas.microsoft.com/cmdlets-over-objects/2009/11">
  <Class ClassName="root\cimv2\Win32_Process">
    <Version>2.0.0.0</Version>
    <DefaultNoun>Win32Process</DefaultNoun>
    <InstanceCmdlets>
      <GetCmdletParameters/>
       <GetCmdlet>
        <CmdletMetadata Verb="Get" HelpUri="http://link.to.online.help"/>
         <GetCmdletParameters DefaultCmdletParameterSet="ByName">
          <QueryableAssociations>
           <Association Association="CIM_ProcessExecutable" ResultRole="Dependent" SourceRole="Antecedent">
            <AssociatedInstance>
              <Type PSType="Microsoft.Management.Infrastructure.CimInstance"    ETSType="Microsoft.Management.Infrastructure.CimInstance#root\cimv2\CIM_DataFile"/>
              <CmdletParameterMetadata PSName="ProcessFile" ValueFromPipeline="true" CmdletParameterSets="ByName ByLiteralName"/>
            </AssociatedInstance>
          </Association>
        </QueryableAssociations>
        </GetCmdletParameters>
      </GetCmdlet>           
     </InstanceCmdlets>
  </Class>
</PowerShellMetadata>
```



Here is how you would use the sample CDXML in PowerShell.


```mof
#Save the sample file as CDXML (for example, Win32Process.cdxml)
#Import this file in PS
Import-module .\win32Process.cdxml
#check the imported cmdlets
Get-command –module win32process* -syntax
#run the cmdlet
Get-Win32Process
#Create a local instance of CIM_File class to pass to Get-Win32Process
$file = New-CimInstance -ClassName CIM_DataFile -Namespace root/cimv2 -Property @{Name="C:\Windows\System32\wininet.dll"} -Key Name -ClientOnly 
#NOTE: In most of the cases, there would be another cmdlet to get instances of CIM_DataFile
Get-Win32Process –ProcessFile $file
```



 

 




