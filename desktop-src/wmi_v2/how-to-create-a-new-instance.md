---
title: How to create a new instance
description: This topic shows how to create a new instance using the CreateInstance intrinsic method.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'CFB678FE-7E14-483B-960D-0EB48C8F929D'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
---

# How to create a new instance

This topic shows how to create a new instance using the CreateInstance intrinsic method.

> \[!Important\]  
> This example uses the Win32\_Environment class, defined in the root\\cimv2 namespace, because it implements the CreateInstance method.

 

``` syntax
New-EnvironmentVariable -Name <string> -UserName <string> -VariableValue <string> 
```

The following sample CDXML shows how to markup a CDXML file to use the CreateInstance method to create a new instance of an object.


```mof
<PowerShellMetadata xmlns="http://schemas.microsoft.com/cmdlets-over-objects/2009/11">
  <Class ClassName="ROOT\cimv2\Win32_Environment">
    <Version>1.0.0.0</Version>
    <DefaultNoun>EnvironmentVariable</DefaultNoun>
    <StaticCmdlets>
      <Cmdlet>
        <CmdletMetadata Verb="New"/>
        <Method MethodName="cim:CreateInstance">
          <Parameters>
            <Parameter ParameterName="Name">
              <Type PSType="System.String"/>
              <CmdletParameterMetadata IsMandatory="true"/>
            </Parameter>
            <Parameter ParameterName="UserName">
              <Type PSType="System.String"/>
              <CmdletParameterMetadata IsMandatory="true"/>
            </Parameter>
            <Parameter ParameterName="VariableValue">
              <Type PSType="System.String"/>
              <CmdletParameterMetadata IsMandatory="true"/>
            </Parameter>
          </Parameters>
        </Method>
      </Cmdlet>
    </StaticCmdlets>
  </Class>
</PowerShellMetadata>
```



 

 




