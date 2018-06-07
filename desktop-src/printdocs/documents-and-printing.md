---
Description: These topics describe the documents and printing features of Windows that enable applications to save, view, and print.
ms.assetid: 20e56af6-9598-4d6a-a2bf-454cef8a3368
title: Documents and Printing
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Documents and Printing

These topics describe the documents and printing features of Windows that enable applications to save, view, and print.

## In this section



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Topic</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[What's New for Printing](https://www.bing.com/search?q=What's+New+for+Printing)<br/></td>
<td>Windows 8 supports [printing for Windows Store apps using JavaScript and HTML](https://msdn.microsoft.com/library/windows/apps/hh465225) and [printing for Windows Store apps using C#/VB/C++ and XAML](https://msdn.microsoft.com/library/windows/apps/xaml/hh465196).<br/> Windows 8 also includes a new COM-based API that provides full support for Open XPS and access to portions of the new printer drivers that Windows 8 supports. For more information about the new API, see [Print Document Package API](https://www.bing.com/search?q=Print+Document+Package+API).<br/> The Windows Print Driver Inbox Program makes sure that Windows 8 includes support for a high percentage of the popular printers.<br/></td>
</tr>
<tr class="even">
<td>[XPS Documents](https://www.bing.com/search?q=XPS+Documents)<br/></td>
<td>Information about the XPS Document API an XPS Digital Signatures.<br/>
<ul>
<li>[XPS Document API](https://www.bing.com/search?q=XPS+Document+API)<br/> The XPS Document API is a native Windows API that supports the XPS OM. The XPS Document API was introduced in Windows 7 and can be used in user-mode programs and XPSDrv printer drivers.<br/></li>
<li>[XPS Digital Signature API](https://www.bing.com/search?q=XPS+Digital+Signature+API)<br/> XPS Digital Signatures enable document signing, verification of the signer's identity, and indication of whether an XPS document has changed since it was signed.<br/></li>
</ul></td>
</tr>
<tr class="odd">
<td>[Printing](printdocs-printing.md)<br/></td>
<td>Information about the printing features supported by Windows. These features include:<br/>
<ul>
<li>[Print Document Package API](https://www.bing.com/search?q=Print+Document+Package+API)<br/> Provides apps with an interface that allows the management of the <strong>PrintDocument</strong> package.<br/></li>
<li>[Print Spooler API](print-spooler-api.md)<br/> Provides an interface to the print spooler so that applications can manage printers and print jobs.<br/></li>
<li>[Print Ticket API](print-ticket-api.md)<br/> Provides applications with functions to manage and convert print tickets.<br/></li>
<li>[GDI Print API](gdi-printing.md)<br/> Provides applications with a device-independent printing interface. <br/></li>
<li><p>[XPS Print API](xps-printing.md)<br/> Provides an interface to the print spooler that applications can use to send XPS documents to a printer.</p>
<blockquote>
[!Note]<br />
The XPS Print API is not supported and may be altered or unavailable in the future. Client applications should use the [Print Document Package API](https://www.bing.com/search?q=Print+Document+Package+API) instead.
</blockquote>
<p><br/> <br/></p></li>
</ul></td>
</tr>
<tr class="even">
<td>[Print Schema](https://www.bing.com/search?q=Print+Schema)<br/></td>
<td>The Print Schema and related technologies describe a printer's features and specify the printing preferences of a document to printers and viewing applications. The [Print Schema Specification](http://go.microsoft.com/?linkid=7141496) is a downloadable document that contains information about the Print Schema and how to use it in documents and printing. The online information that is found in this section is provided for your information only and might not accurately reflect the current version of the [Print Schema Specification](http://go.microsoft.com/?linkid=7141496).<br/> Refer to the [Print Schema Specification](http://go.microsoft.com/?linkid=7141496) for the most current design information.<br/></td>
</tr>
</tbody>
</table>



 

## Additional resources

The [Print Sample sample app](http://go.microsoft.com/fwlink/p/?linkid=242999) demonstrates how to print from a Windows Store app starting with Windows 8.

The features described in this section are for native Windows programming. To use similar features in .NET (managed) programming, see [Windows Presentation Foundation Documents](https://msdn.microsoft.com/windows/desktop/7bf37ccb-5d09-4eae-9661-929582aeb259).

XPS documents are built on the [Packaging](https://msdn.microsoft.com/library/windows/desktop/dd371623) API. See the Packaging API, for lower level access to the contents of an XPS document.

## Related topics

<dl> <dt>

[Bidirectional printer communications (Hardware Dev Center)](http://go.microsoft.com/fwlink/p/?LinkId=613189  )
</dt> </dl>

 

 




