---
title: How to perform operations on an instance
description: This topic shows how to invoke an instance method using CDXML.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 821E602C-C5CB-42FF-B5E6-77F74E65BDB7
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# How to perform operations on an instance

This topic shows how to invoke an instance method using CDXML.

> \[!Important\]  
> The object being used is the example Win32\_Process object defined in the [CIM Class Overview](cim-class-overview.md) topic.

 

The following shows the syntax for various Win32 process cmdlets.

``` syntax
Get-Win32Process [[-Name] <string[]>] 

Get-Win32Process -ProcessId <UInt32[]> 


Stop-Win32Process [-Name] <string[]> [[-Reason] <UInt32>] [-WhatIf] [-Confirm] 


Stop-Win32Process -ProcessId <UInt32[]> [[-Reason] <UInt32>] [-WhatIf] [-Confirm] 


Stop-Win32Process -InputObject <CimInstance#Win32_Process[]>[[-Reason] <UInt32>] [-WhatIf] [-Confirm] 


Debug-Win32Process [-Name] <string[]>

Debug-Win32Process -ProcessId <UInt32[]> 

Debug-Win32Process -InputObject 
```

The key points to mention when looking at the above syntax are the following.

-   The Name and ProcessId parameters are used for filtering the instances of Win32\_Process objects.
-   There is a slight difference in the usage of the Name parameter. It is optional in the Get-Win32Process cmdlet, but mandatory in the Stop-Win32Process and Debug-Win32Process cmdlets.
-   The Stop-Win32Process cmdlet supports both the WhatIf and Confirm since, per Windows PowerShell guidelines, any cmdlet that changes the state of the system should support these semantics. Because the Win32\_Process WMI class does not natively support ShouldProcess, WhatIf and Confirm must be handled on the client.

As a general Windows PowerShell convention, there should not be any mandatory parameters in the default parameter set for a Get cmdlet. However, we want to make it mandatory in other cmdlets . It's common to have a set of cmdlets follow a similar pattern for query parameters. For example, the Windows PowerShell Get-Service , Set-Service, Start-Service, and Stop-Service cmdlets all have the same parameters. To minimize duplication of common parameters, CDXML allows you to define a global set of Query Parameters that is shared by all instance cmdlets. Individual cmdlets can define their own query parameters that override the global definition. It is very likely that a Get cmdlet would have slightly different parameter attributes because its default parameter set may not have any required parameters.

The following sample CDXML shows how to define the cmdlets.


```mof
<PowerShellMetadata xmlns="http://schemas.microsoft.com/cmdlets-over-objects/2009/11">
  <Class ClassName="root\cimv2\Win32_Process">
    <Version>2.0.0.0</Version>
    <DefaultNoun>Win32Process</DefaultNoun>
    <InstanceCmdlets>
      <!--
Global definition for query parameters used by Stop-win32Process and Get-Win32ProcessOwner cmdlets
-->
      <GetCmdletParameters DefaultCmdletParameterSet="ByName">
        <QueryableProperties>
          <Property PropertyName="Name">
            <Type PSType="string"/>
            <RegularQuery AllowGlobbing="true">
              <CmdletParameterMetadata IsMandatory="true" Position="0" ValueFromPipelineByPropertyName="true" CmdletParameterSets="ByName"/>
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

      <GetCmdlet>
        <CmdletMetadata Verb="Get"/>
        <!--
        Definition of query parameters used by Get-win32Process 
        It does not use the global definition because the Get cmdlet should not have mandatory parameters in the default parameter set
        -->
        <GetCmdletParameters DefaultCmdletParameterSet="ByName">
          <QueryableProperties>
            <Property PropertyName="Name">
              <Type PSType="string"/>
              <RegularQuery AllowGlobbing="true">
                <CmdletParameterMetadata IsMandatory="false" Position="0" ValueFromPipelineByPropertyName="true" CmdletParameterSets="ByName"/>
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
      <Cmdlet>
        <CmdletMetadata Verb="Stop" ConfirmImpact="Medium"/>
        <Method MethodName="Terminate">
          <Parameters>
            <Parameter ParameterName="Reason">
              <Type PSType="Uint32"/>
              <CmdletParameterMetadata IsMandatory="false" Position="1"/>
            </Parameter>
          </Parameters>
        </Method>
      </Cmdlet>
     <Cmdlet>
        <CmdletMetadata Verb="Debug"/>
        <Method MethodName="AttachDebugger">
          <ReturnValue>
            <Type PSType="int"/>
            <CmdletOutputMetadata>
              <ErrorCode/>
            </CmdletOutputMetadata>
          </ReturnValue>
        </Method>
      </Cmdlet>

      
    </InstanceCmdlets>
  <CmdletAdapterPrivateData>
      <Data Name="ClientSideShouldProcess"/>
  </CmdletAdapterPrivateData>

  </Class>
</PowerShellMetadata>
```



 

 




