---
title: Compiling Ribbon Markup
description: For the Windows Ribbon framework to consume the Ribbon markup file, the markup file must be compiled into a binary format resource file.
ms.assetid: ef9fea92-8c67-461d-9d74-2e259e407fb0
keywords:
- Windows Ribbon,compiling markup
- Ribbon,compiling markup
- Windows Ribbon,compiler workflow
- Ribbon,compiler workflow
- Windows Ribbon,UI Command Compiler (UICC.exe)
- Ribbon,UI Command Compiler (UICC.exe)
- UI Command Compiler (UICC.exe)
- UICC.exe (UI Command Compiler)
- compiling Windows Ribbon markup
ms.topic: article
ms.date: 05/31/2018
---

# Compiling Ribbon Markup

For the Windows Ribbon framework to consume the [Ribbon markup](windowsribbon-schema.md) file, the markup file must be compiled into a binary format resource file. A dedicated markup compiler, the UI Command Compiler (UICC), is included with the Windows Software Development Kit (SDK) (7.0 or later) for this purpose. In addition to compiling the binary version of the markup, the UICC generates an ID definition header (.h) file that exposes all markup elements to the Ribbon host application and a resource (.rc) file that is used to link image and string resources to the host application at build time.

-   [Compiler Workflow](#compiler-workflow)
-   [Command-Line Syntax](#command-line-syntax)
    -   [Arguments and Options](#arguments-and-options)
    -   [Example](#example)
-   [Related topics](#related-topics)

## Compiler Workflow

The workflow of the Ribbon markup compiler is illustrated in the following diagram.

![diagram showing the ribbon markup compiler workflow.](images/overviews/overviews-intentcl.png)

## Command-Line Syntax

The command-line syntax for the Ribbon markup compiler is shown in the following example.


```
UICC <ribbonFile> <binaryFile> [options]
```



### Arguments and Options

The arguments and options for this tool are described in the following table.

> [!Note]  
> The command-line options listed must be specified in the order given.

 



<table>
<colgroup>
<col  />
<col  />
</colgroup>
<thead>
<tr class="header">
<th>Option</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>/header:&lt;headerFile&gt;</td>
<td>Generate a header file called &lt;headerFile&gt; that contains the markup Command ID resource symbols. If omitted, a header file is not generated.</td>
</tr>
<tr class="even">
<td>/res:&lt;resourceFile&gt;</td>
<td>Generate a resource file called &lt;resourceFile&gt; that links all image and string resources, the binary markup file, and the header file to the host application at build time. If omitted, a resource file is not generated.</td>
</tr>
<tr class="odd">
<td>/name:&lt;ribbonName&gt;</td>
<td>The resource name for the binary markup file that is logged in the &lt;resourceFile&gt;. The default is APPLICATION_RIBBON.</td>
</tr>
<tr class="even">
<td>/W{0\1\2}</td>
<td>Filter the event messages based on severity. 
<table>
<tbody>
<tr class="odd">
<td>0<br/></td>
<td>Error messages only.<br/></td>
</tr>
<tr class="even">
<td>1<br/></td>
<td>Error and Warning messages only.<br/></td>
</tr>
<tr class="odd">
<td><strong>2</strong><br/></td>
<td>Default. <br/> Error, Warning, and Informational messages.<br/></td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
</tbody>
</table>



 

### Example

The following example demonstrates how to use the Ribbon markup compiler to generate a typical set of resource files for a Ribbon application.

`UICC.exe RibbonMarkup.xml RibbonMarkup.bml /header:RibbonIds.h /res:RibbonUI.rc`

## Related topics

<dl> <dt>

[Declaring Commands and Controls with Ribbon Markup](windowsribbon-schema.md)
</dt> <dt>

[Creating a Ribbon Application](windowsribbon-stepbystep.md)
</dt> </dl>

 

 





