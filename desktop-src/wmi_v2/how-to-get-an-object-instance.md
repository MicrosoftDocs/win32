---
title: How to get an object instance
description: This topic illustrates how to define a simple cmdlet to get instances of an object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2F2F07A5-7A43-4114-855C-7EEDEF93AF2E
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# How to get an object instance

This topic illustrates how to define a simple cmdlet to get instances of an object.

> \[!Important\]  
> The object being used is the example Win32\_Process object defined in the [CIM Class Overview](cim-class-overview.md) topic.

 

The syntax for the Win32\_Process cmdlet is as follows.

``` syntax
Get-Win32Process [[-Name] <string[]>] 
Get-Win32Process -ProcessId <UInt32[]> 
```

For the cmdlet signature, or syntax, above, we have the following information.

-   The noun for the cmdlet is Win32Process
-   The cmdlet is query only for instances (as it's a Get cmdlet).
-   The Get is a regular query expression where Win32\_Process instances that match a specified ID or Name are returned.
-   The Name parameter is an optional parameter of type string that accepts wildcards.
-   The default ParameterSet is ByName.

The following CDXML defines the cmdlet.


```mof
<PowerShellMetadata xmlns="http://schemas.microsoft.com/cmdlets-over-objects/2009/11">
<!--
ClassName attribute defines the CIM Class in namespace/class format.
In this example, root/cimv2 is the namespace and Win32_process is the WMI class.
-->
<Class ClassName="root/cimv2/Win32_Process">
    <Version>2.0.0.0</Version>    <DefaultNoun>Win32Process</DefaultNoun>
    <InstanceCmdlets>
<!--
Global definition for query parameters. Not used in this example because we have a single cmdlet only.
-->

     <GetCmdletParameters/>

<!--
Definition of Get-Process cmdlet
-->
      
      <GetCmdlet>
        <CmdletMetadata Verb="Get" HelpUri="http://link.to.online.help"/>
        <GetCmdletParameters DefaultCmdletParameterSet="ByName">
        <QueryableProperties>
          <Property PropertyName="Name">
            <Type PSType="string"/>
            <RegularQuery AllowGlobbing="true">
              <CmdletParameterMetadata IsMandatory="false" Position="0"
                  ValueFromPipelineByPropertyName="true" CmdletParameterSets="ByName"/>
            </RegularQuery>
          </Property>
          <Property PropertyName="ProcessId">
            <Type PSType="uint32"/>
            <RegularQuery>
              <CmdletParameterMetadata IsMandatory="true" Aliases="ID PID"
                 CmdletParameterSets="ById"/>
            </RegularQuery>
          </Property>
        </QueryableProperties>
       </GetCmdletParameters>
      </GetCmdlet>      
    </InstanceCmdlets
  </Class>
</PowerShellMetadata>
```



Here is how you would use the sample CDXML in PowerShell.


```mof
#Save the sample file as CDXML (for example, Win32Process.cdxml)#Import this file in PS
Import-module .\win32Process.cdxml
#check the imported cmdlets
Get-command –module winprocess* -syntax
#run the cmdlet
Get-Win32Process
Get-Win32Process –id 0
Get-Win32Process –id 0,10,11
Get-Win32Process –Name c*
Get-Win32Process –Name a*,csrss.exe
```



 

 




