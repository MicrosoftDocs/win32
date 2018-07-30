---
Description: Windows provides applications with a complete set of functions that allow printing to various devices, such as laser printers, vector plotters, raster printers, and fax machines.
ms.assetid: e5c115b0-9c1e-46e7-8fb5-eddbc2c75298
title: Printing
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Printing

Windows provides applications with a complete set of functions that allow printing to various devices, such as laser printers, vector plotters, raster printers, and fax machines.

## Desktop App Printing

Windows programmers can select from several different technologies to print from their application.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Technology</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[Print Document Package API](https://msdn.microsoft.com/en-us/library/Hh448418(v=VS.85).aspx)<br/></td>
<td>Provides an interface that allows an application to access and manage the print document package. This API is available with Windows 8 and later versions of Windows.<br/></td>
</tr>
<tr class="even">
<td>[Print Spooler API](print-spooler-api.md)<br/></td>
<td>Provides an interface to the print spooler so that applications can manage printers and print jobs.<br/> Applications use the [Print Spooler API](print-spooler-api.md) to start, stop, control, and configure print jobs managed by the print spooler whether they use the [Print Document Package API](https://msdn.microsoft.com/en-us/library/Hh448418(v=VS.85).aspx) or the [GDI Print API](gdi-printing.md) to print the content.<br/></td>
</tr>
<tr class="odd">
<td>[Print Ticket API](print-ticket-api.md)<br/></td>
<td>Provides applications with functions to manage and convert print tickets.<br/></td>
</tr>
<tr class="even">
<td>[GDI Print API](gdi-printing.md)<br/></td>
<td>Provides applications with a device-independent printing interface. <br/>
<blockquote>
[!Note]<br />
Developers who are writing applications for Windows Vista and later versions of Windows should consider using the [XPS Document API](https://msdn.microsoft.com/en-us/library/Dd316976(v=VS.85).aspx) in their application.
</blockquote>
<br/> The [GDI Print API](gdi-printing.md) is suitable for applications that must run on Windows XP and earlier versions of Windows.<br/></td>
</tr>
</tbody>
</table>



 

The following illustration provides a high-level view of how the different printing APIs are related.

![a diagram that shows how a native windows application can use the print apis](../images/print-apis.png)

 

The [Print Document Package API](https://msdn.microsoft.com/en-us/library/Hh448418(v=VS.85).aspx)s in this section describe the print document package and print preview interfaces that you can use with Windows 8 and later versions of Windows desktop.

For more info about printing from Windows Store apps that are written in JavaScript and HTML, see [Printing (Windows Store apps using JavaScript and HTML)](https://msdn.microsoft.com/library/windows/apps/hh465225). For more info about printing from Windows Store apps that are written in C#, Microsoft Visual Basic, or C++ and XAML, see [Printing (Windows Store apps using C)](https://msdn.microsoft.com/library/windows/apps/xaml/hh465196).

> [!Note]  
> See [Win32 and COM for Windows Store apps (printing and documents)](https://msdn.microsoft.com/library/windows/apps/br205760) for the list of the Desktop App Printing APIs that can also be used in Windows Store apps.

 

## Related topics

<dl> <dt>

[XPS Document API](https://msdn.microsoft.com/en-us/library/Dd316976(v=VS.85).aspx)
</dt> <dt>

[Bidirectional printer communications (Hardware Dev Center)](http://go.microsoft.com/fwlink/p/?LinkId=613189  )
</dt> </dl>

 

 




