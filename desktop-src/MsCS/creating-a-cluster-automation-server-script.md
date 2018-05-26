---
title: Creating a Failover Cluster Automation Server Script
description: The following example illustrates a basic Windows Script Host shell in which a script can be inserted. For more information on Windows Script Host, see the Scripting reference in the Microsoft Windows Software Development Kit (SDK).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2ca508c9-c34a-4af5-a6c0-3d710171f3df
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Cluster Automation Server Failover Cluster ,scripts
- Failover Cluster Automation Server Failover Cluster ,scripts
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Creating a Failover Cluster Automation Server Script

\[The [Failover Cluster Automation Server](https://msdn.microsoft.com/library/aa372940) is available for use in Windows Server 2008. It may be altered or unavailable in subsequent versions.\]

The following example illustrates a basic Windows Script Host shell in which a script can be inserted. For more information on Windows Script Host, see the Scripting reference in the Microsoft Windows Software Development Kit (SDK).

``` syntax
<?xml version="1.0" encoding="US-ASCII"?>
<!--==================================================================
;  Wshell.wsf
; 
;  Generic Windows Script Host shell in which to insert
;  VBScript and JScript code.
;  
;  To use this file,
;  1. Save it under a new name (File - Save As - filename)
;     using the "wsf" extension.
;  2. Rename the package and job ID's as needed.
;  3. For each job:
;     a.  Load type library information as needed.
;     b.  Include or insert script code as needed.
;  4. Run the script by calling Windows Script Host from
;     the command prompt according to the following syntax:
;        wscript <filename> [/<options>] [<arguments>]
;        cscript <filename> [/<options>] [<arguments>]
;   
;  For more information, see the Scripting reference in the
;  Platform Software Development Kit (SDK).
===================================================================-->

<package id="Main">

 <job id="Job1">

  <!--==============================================================
  ; The following line references the MSCLUS type library, which 
  ; makes the library-defined constants and enums available to your 
  ; scripts. The reference is job-specific. Each job must include
  ; this line in order to use the type library definitions.
  ===============================================================-->
  <reference guid="{F2E606E0-2631-11D1-89F1-00A0C90D061E}" version="1.0"/>

  <!--==============================================================
  ; To "include" external script files, use the following syntax:
  ;   <script language="VBScript" src="c:\path\filename.vbs"/>
  ;   <script language="JScript" src="c:\path\filename.js"/>
  ; Otherwise you can embed your script as shown below.
  ; The CDATA wrapper is necessary for the file to be valid XML.
  ===============================================================-->
  <script language="VBScript">

   <![CDATA[

    'Add VBScript code here.

   ]]>

  </script>

  <script language="JScript">

   <![CDATA[

    //  Add JScript code here.                        

   ]]>

  </script>

 </job>

 <job id="Job2">
 </job>
</package>
```

 

 




