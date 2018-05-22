---
title: How to get an object instance with different query types
description: This topic illustrates how to define a simple cmdlet to get instances of an object with different query types.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'C6D01287-E860-4A60-B086-664D866B1172'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
---

# How to get an object instance with different query types

This topic illustrates how to define a simple cmdlet to get instances of an object with different query types.

> \[!Important\]  
> The object being used is the example Win32\_Process object defined in the [CIM Class Overview](cim-class-overview.md) topic.

 

The syntax for the Win32\_Process cmdlet is as follows.

``` syntax
Get-Win32Process [[-Name] <string[]>] [-ExcludeName <string[]>] [-MinWorkingSet <UInt64>] [-MaxWorkingSet <UInt64>] 

Get-Win32Process -ProcessId <UInt32[]> 
```

The following CDXML defines the cmdlet.


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
          <QueryableProperties>
            <Property PropertyName="Name">
              <Type PSType="string"/>
              <RegularQuery AllowGlobbing="true">
                <CmdletParameterMetadata IsMandatory="false" Position="0" ValueFromPipelineByPropertyName="true" CmdletParameterSets="ByName"/>
              </RegularQuery>
              <ExcludeQuery AllowGlobbing="true">
                <CmdletParameterMetadata PSName="ExcludeName" CmdletParameterSets="ByName"/>
              </ExcludeQuery>
            </Property>
            <Property PropertyName="ProcessId">
              <Type PSType="uint32"/>
              <RegularQuery>
                <CmdletParameterMetadata IsMandatory="true" Aliases="ID PID"
                   CmdletParameterSets="ById"/>
              </RegularQuery>
            </Property>
            <Property PropertyName="WorkingSetSize">
             <Type PSType="Uint64"/>
             <MinValueQuery>
               <CmdletParameterMetadata PSName="MinWorkingSet" CmdletParameterSets="ByName"/>
             </MinValueQuery>
             <MaxValueQuery>
               <CmdletParameterMetadata PSName="MaxWorkingSet" CmdletParameterSets="ByName"/>
             </MaxValueQuery>
            </Property>           
          </QueryableProperties>
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
Get-command –module winprocess* -syntax
#run the cmdlet
Get-Win32Process
Get-Win32Process –id 0
Get-Win32Process –id 0,10,11
Get-Win32Process –Name c*
Get-Win32Process –Name a*,csrss.exe
Get-Win32Process –Name c* -ExcludeName csrss* 
Get-Win32Process -MinWorkingSet 2MB -MaxWorkingSet 5MB 
```



 

 




